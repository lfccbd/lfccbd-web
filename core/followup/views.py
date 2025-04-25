from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from core.followup.models.membership import MemberFollowUp
from core.followup.models.outreach import FollowUpOutreach

from .forms import FollowUpCheckupForm, FollowUpMembershipForm, FollowUpOutreachForm, OutreachForm  # type: ignore


class CheckupView(LoginRequiredMixin, View):
    template_name = 'forms/followup.html'
    success_url_name = 'followup'
    login_url = reverse_lazy('account_login')
    redirect_field_name = 'next'

    def _get_context_data(self, **kwargs):
        context = {
            'checkup_form': FollowUpCheckupForm(),
            'sunday_form': FollowUpMembershipForm(),
            'outreach_form': FollowUpOutreachForm(),
        }

        # allow extra context to be passed in
        context.update(kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self._get_context_data())

    def post(self, request, *args, **kwargs):
        form_section = request.POST.get('form_section', None)
        active_form_class = None
        message_text = ''
        form_key = ''

        if form_section == 'checkup':
            active_form_class = FollowUpCheckupForm
            form_key = 'checkup_form'
            message_text = 'Checkup Form Saved Successfully.'
        elif (
            form_section == 'sunday_first_timer' or form_section == 'sunday_new_convert'
        ):
            active_form_class = FollowUpMembershipForm
            form_key = 'sunday_form'
            message_text = 'Follow-Up Form Saved Successfully.'
        elif form_section == 'outreach':
            active_form_class = FollowUpOutreachForm
            form_key = 'outreach_form'
            message_text = 'Outreach Form Saved Successfully.'

        form = active_form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # add user only if the form's model has a user field
            if hasattr(instance, 'user'):
                instance.user = request.user

            if active_form_class == FollowUpCheckupForm:
                phone_number = form.cleaned_data.get('phone_number')
                try:

                    member_profile = MemberFollowUp.objects.filter(
                        phone_number=phone_number
                    ).first()

                    # update indance
                    instance.member_profile = member_profile
                    member_profile.current_status = instance.current_status
                    instance.save(update_fields=['member_profile', 'current_status'])

                except MemberFollowUp.DoesNotExist:
                    messages.error(request, "Could not find matching member profile.")
                    context = self._get_context_data(
                        **{form_key: form, 'form_section': form_section}
                    )
                    return render(request, self.template_name, context)

            instance.save()

            messages.success(request, message_text)
            return redirect(self.success_url_name)

        else:
            messages.error(request, 'Invalid Form Field(s). All fields are required.')
            context = self._get_context_data(
                **{form_key: form, 'form_section': form_section}
            )
            return render(request, self.template_name, context)


class OutreachView(SuccessMessageMixin, CreateView):
    model = FollowUpOutreach
    form_class = OutreachForm
    template_name = 'forms/outreach.html'
    success_url = reverse_lazy('outreach')
    success_message = 'Outreach Form Saved Successfully.'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        # message
        messages.error(self.request, 'Invalid Form Field(s). All fields are required.')
        return super().form_invalid(form)
