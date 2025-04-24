from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View

from core.followup.models.membership import MemberFollowUp
from core.followup.models.outreach import FollowUpOutreach

from .forms import FollowUpCheckupForm, FollowUpMembershipForm, FollowUpOutreachForm  # type: ignore


class CheckupView(View):
    success_url = 'followup'
    template_name = 'forms/followup.html'

    def get(self, request, *_args, **kwargs):
        context = {
            'checkup_form': FollowUpCheckupForm(),
            'sunday_form': FollowUpMembershipForm(),
            'outreach_form': FollowUpOutreachForm(),
            'form': {'error': ''},
        }
        return render(request, self.template_name, context)

    def post(self, request, *_args, **kwargs):

        if self.request.POST.get('form_section', None) == 'checkup':
            active_form_class = FollowUpCheckupForm
            selected_form_section = 'form_section_checkup'
            message_text = 'Checkup Form Saved Successfully.'

        elif self.request.POST.get('form_section', None) == 'sunday':
            active_form_class = FollowUpMembershipForm
            if self.request.POST.get('followup_type', None) == 'Firt Timer':
                selected_form_section = 'form_section_sunday_timer'
            else:
                selected_form_section = 'form_section_sunday_convert'
            message_text = 'Follow-Up Form Saved Successfully.'

        else:
            # active form class
            active_form_class = FollowUpOutreachForm
            selected_form_section = 'form_section_outreach'
            message_text = 'Outreach Form Saved Successfully.'

        # copy the request
        form_data = request.POST.copy()

        # use modified request with form class
        form = active_form_class(form_data)

        if form.is_valid():
            # get phone number
            phone_number = self.request.POST.get('phone_number', None)

            if active_form_class == FollowUpOutreachForm:
                cleaned_data = form.cleaned_data

                # remove verification_code and captcha field from form
                cleaned_data.pop('verification_code', None)
                cleaned_data.pop('captcha', None)

                FollowUpOutreach.objects.update_or_create(**cleaned_data)

            else:
                instance = form.save(commit=False)

                # update form instance
                if (
                    active_form_class == FollowUpCheckupForm
                    or active_form_class == FollowUpMembershipForm
                ):
                    instance.user = request.user

                if active_form_class == FollowUpCheckupForm:
                    # get member profile,
                    # no need for checks as it is already
                    # vetted in form clean
                    member_profile = MemberFollowUp.objects.filter(
                        phone_number=phone_number
                    ).first()

                    # update instance
                    instance.member_profile = member_profile

                    # update model instance of  member current welfare check
                    member_profile.current_status = instance.current_status
                    member_profile.save(update_fields=['current_status'])

                # submit form
                instance.save()

            # message
            messages.success(request, message_text)
            return HttpResponsePermanentRedirect(reverse_lazy(self.success_url))

        # message
        messages.error(request, 'Invalid Form Field(s). All fields are required.')

        # render page with form errors
        return render(
            request,
            self.template_name,
            {
                'checkup_form': FollowUpCheckupForm(),
                'sunday_form': FollowUpMembershipForm(),
                'outreach_form': FollowUpOutreachForm(),
                'form': form,
                'form_section': selected_form_section,
            },
        )

    def dispatch(self, request, *args, **kwargs):
        # check if user is authenticated
        if self.request.user.is_anonymous:
            return HttpResponsePermanentRedirect(reverse('account_login'))

        return super().dispatch(request, *args, **kwargs)
