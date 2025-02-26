from django.contrib import admin
from django.forms import Textarea, TextInput  # noqa: I101
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pgcrypto import EncryptedCharField, EncryptedDateTimeField, EncryptedEmailField, EncryptedTextField

from .models import Testimony


class TestimonyResource(resources.ModelResource):
	class Meta:
		model = Testimony
		skip_unchanged = True
		report_skipped = True
		exclude = ['id', 'history']


class TestimonyMessageAdmin(ImportExportModelAdmin):
	resource_class = TestimonyResource
	list_display = ['first_name', 'last_name', 'designation', 'date_received']
	list_display_links = ['first_name', 'last_name', 'designation']
	list_filter = ['publish']
	date_hierarchy = 'date_received'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	readonly_fields = ['first_name', 'last_name', 'designation', 'location', 'testimony']
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['first_name', 'last_name', 'designation', 'location', 'testimony', 'date_received']
	fields = ['first_name', 'last_name', 'designation', 'location', 'title', 'testimony', 'publish', 'date_received']

	# override field display
	def formfield_for_dbfield(self, db_field, **kwargs):
		if isinstance(db_field, (EncryptedCharField, EncryptedEmailField, EncryptedDateTimeField)):
			kwargs['widget'] = TextInput(
				attrs={
					'size': '10',
					'class': 'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl',  # noqa: E501
				}
			)
		elif isinstance(db_field, (EncryptedTextField)):
			kwargs['widget'] = Textarea(
				attrs={
					'cols': 40,
					'rows': '10',
					'class': 'vLargeTextField border bg-white font-medium min-w-20 rounded-md shadow-sm text-font-default-light text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-font-default-dark dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-4xl appearance-none expandable transition transition-height duration-75 ease-in-out',  # noqa: E501
				}
			)
		return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Testimony, TestimonyMessageAdmin)
