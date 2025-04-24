from django import forms
from django.contrib import admin
from django.forms import Textarea, TextInput  # noqa: I101
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pgcrypto import (
    EncryptedCharField,
    EncryptedDateTimeField,
    EncryptedEmailField,
    EncryptedIntegerField,
    EncryptedTextField,
)

from .models.__choices import (
    calling,
    convert,
    current_memeber_status,
    in_church_ask,
    in_church_check_sunday,
    in_church_check_wenesday,
    membership,
    title,
)
from .models.checkup import FollowUpCheckup  # type: ignore
from .models.membership import MemberFollowUp  # type: ignore
from .models.outreach import FollowUpOutreach  # type: ignore
from .models.sms import SMSTemplates  # type: ignore
from .models.vercode import OutreachVerficationCode  # type: ignore


class FollowUpResource(resources.ModelResource):
    class Meta:
        model = MemberFollowUp
        skip_unchanged = True
        report_skipped = True
        exclude = ['date_created', 'history']


class FollowUpCheckupAdmin(admin.ModelAdmin):
    list_display = ['id', 'member_profile', 'number_was_called', 'in_church_last_sunday', 'in_church_last_wenesday']
    list_display_links = ['id', 'member_profile']
    list_filter = [
        'number_was_called',
        'in_church_last_sunday',
        'in_church_last_wenesday',
        'church_next_sunday',
        'current_status',
    ]
    readonly_fields = ['id']
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = [
        'member_profile',
        'number_was_called',
        'in_church_last_sunday',
        'in_church_last_wenesday',
        'church_next_sunday',
        'current_status',
        'prayer',
        'last_updated',
        'publish',
    ]
    fieldsets = [
        [
            'Follow Team Assigned',
            {
                'classes': ['wide', 'extrapretty'],
                'fields': ['user'],
            },
        ],
        [
            'Member Info',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['id', 'member_profile'],
            },
        ],
        [
            'Checkup Calls',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': [
                    'number_was_called',
                    ('in_church_last_wenesday', 'in_church_last_sunday'),
                    'church_next_sunday',
                ],
            },
        ],
        [
            'Welfare',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['current_status', 'prayer'],
            },
        ],
        [
            'Record Update',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['publish', 'last_updated'],
            },
        ],
    ]

    # override field display
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, (EncryptedCharField)):
            kwargs['widget'] = TextInput(
                attrs={
                    'size': '10',
                    'class': 'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl',  # noqa: E501
                }
            )

        if (
            db_field.name == 'number_was_called'
            or db_field.name == 'in_church_last_sunday'
            or db_field.name == 'in_church_last_wenesday'
            or db_field.name == 'church_next_sunday'
            or db_field.name == 'current_status'
        ):
            # redeclare label with a class
            label = format_html(
                f'<label class="label-text py-2 px-1 !inline-block relative">{db_field.verbose_name}</label>'  # noqa: E501
            )
            # Override the status field
            kwargs['widget'] = forms.Select(
                attrs={
                    'class': 'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl input w-full focus:outline-0 transition-all input-sm input-bordered focus:outline-offset-0',  # noqa: E501
                    'style': 'height: 35px;',
                }
            )
            if db_field.name == 'number_was_called':
                kwargs['choices'] = calling
            elif db_field.name == 'in_church_check_sunday':
                kwargs['choices'] = in_church_check_sunday
            elif db_field.name == 'in_church_last_wenesday':
                kwargs['choices'] = in_church_check_wenesday
            elif db_field.name == 'church_next_sunday':
                kwargs['choices'] = in_church_ask
            elif db_field.name == 'current_status':
                kwargs['choices'] = current_memeber_status
            kwargs['label'] = label
            kwargs['help_text'] = db_field.help_text
            kwargs['initial'] = ['Mr']

            return forms.ChoiceField(**kwargs)

        elif isinstance(db_field, (EncryptedTextField)):
            kwargs['widget'] = Textarea(
                attrs={
                    'cols': 40,
                    'rows': '10',
                    'class': 'vLargeTextField border bg-white font-medium min-w-20 rounded-md shadow-sm text-font-default-light text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-font-default-dark dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-4xl appearance-none expandable transition transition-height duration-75 ease-in-out',  # noqa: E501
                }
            )
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class FollowUpOutreachAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number']
    list_display_links = ['id', 'full_name', 'phone_number']
    readonly_fields = ['id']
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['id', 'full_name', 'phone_number']
    fields = ['id', 'full_name', 'phone_number', 'publish', 'last_updated']

    # override field display
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, (EncryptedCharField)):
            kwargs['widget'] = TextInput(
                attrs={
                    'size': '10',
                    'class': 'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl',  # noqa: E501
                }
            )
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'template']
    list_display_links = ['id', 'template']
    readonly_fields = ['id']
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['id', 'template']
    fields = ['id', 'template', 'sms_message', 'publish', 'last_updated']


class OutreachVerficationCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']
    list_display_links = ['id', 'code']
    readonly_fields = ['id']
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['id', 'code']
    fields = ['id', 'code', 'usability', 'expiration', 'last_updated']

    # override field display
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, (EncryptedIntegerField)):
            kwargs['widget'] = TextInput(
                attrs={
                    'size': '10',
                    'class': 'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl',  # noqa: E501
                }
            )

        return super().formfield_for_dbfield(db_field, request, **kwargs)


class MemberFollowUpAdmin(ImportExportModelAdmin):
    resource_class = FollowUpResource
    list_display = ['id', 'followup_type', 'title', 'first_name', 'last_name', 'phone_number']
    list_display_links = ['id', 'followup_type', 'title', 'first_name', 'last_name', 'phone_number']
    list_filter = ['followup_type', 'membership']
    readonly_fields = ['id']
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['id', 'followup_type', 'title', 'first_name', 'last_name', 'phone_number']
    fieldsets = [
        [
            'Follow Team Assigned',
            {
                'classes': ['wide', 'extrapretty'],
                'fields': ['user'],
            },
        ],
        [
            'Member Info',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['id', 'title', 'first_name', 'last_name', 'emailbirthday', 'phone_number', 'address'],
            },
        ],
        [
            'Invitation Info',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['invite_process', 'inviter'],
            },
        ],
        [
            'Membership Info',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['membership'],
            },
        ],
        [
            'Prayer Request',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['prayer'],
            },
        ],
        [
            'Welfare',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['current_status'],
            },
        ],
        [
            'Record Update',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['publish', 'last_updated'],
            },
        ],
    ]

    # override field display
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, (EncryptedCharField, EncryptedEmailField, EncryptedDateTimeField)):
            kwargs['widget'] = TextInput(
                attrs={
                    'size': '10',
                    'class': 'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl',  # noqa: E501
                }
            )

        if db_field.name == 'followup_type' or db_field.name == 'membership' or db_field.name == 'title':
            # redeclare label with a class
            label = format_html(
                f'<label class="label-text py-2 px-1 !inline-block relative">{db_field.verbose_name}</label>'  # noqa: E501
            )
            # Override the status field
            kwargs['widget'] = forms.Select(
                attrs={
                    'class': 'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl input w-full focus:outline-0 transition-all input-sm input-bordered focus:outline-offset-0',  # noqa: E501
                    'style': 'height: 35px;',
                }
            )
            if db_field.name == 'followup_type':
                kwargs['choices'] = convert
            elif db_field.name == 'membership':
                kwargs['choices'] = membership
            elif db_field.name == 'title':
                kwargs['choices'] = title
            kwargs['label'] = label
            kwargs['help_text'] = db_field.help_text
            kwargs['initial'] = ['Mr']

            return forms.ChoiceField(**kwargs)

        elif isinstance(db_field, (EncryptedTextField)):
            kwargs['widget'] = Textarea(
                attrs={
                    'cols': 40,
                    'rows': '10',
                    'class': 'vLargeTextField border bg-white font-medium min-w-20 rounded-md shadow-sm text-font-default-light text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-font-default-dark dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-4xl appearance-none expandable transition transition-height duration-75 ease-in-out',  # noqa: E501
                }
            )
        return super().formfield_for_dbfield(db_field, request, **kwargs)


admin.site.register(FollowUpCheckup, FollowUpCheckupAdmin)
admin.site.register(FollowUpOutreach, FollowUpOutreachAdmin)
admin.site.register(MemberFollowUp, MemberFollowUpAdmin)
admin.site.register(SMSTemplates, SMSTemplateAdmin)
admin.site.register(OutreachVerficationCode, OutreachVerficationCodeAdmin)
