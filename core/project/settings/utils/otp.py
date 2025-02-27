from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib import messages
from django_otp.plugins.otp_static.models import StaticToken, StaticDevice

from core.project.settings import ADMIN_PATH


class CustomAdminLoginView(LoginView):
	template_name = 'admin/login.html'

	def form_valid(self, form):
		"""
		Override to enforce OTP or backup code validation.
		"""
		email = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		otp_token = self.request.POST.get('otp_token')

		# authenticate user
		user = authenticate(self.request, username=email, password=password)
		if user is not None:
			# check if OTP device exist
			if TOTPDevice.objects.filter(user=user, confirmed=True).exists():
				device = TOTPDevice.objects.filter(user=user, confirmed=True).first()
				if otp_token:
					# verify otp
					if device.verify_token(otp_token):
						login(self.request, user)
						return redirect(f'/{ADMIN_PATH}/')
					else:
						messages.error(self.request, 'Invalid OTP. Please try again.')
						return render(self.request, self.template_name, {'form': form})
			elif StaticDevice.objects.filter(user__email=email, confirmed=True).exists():
				# verify backup code
				if self.is_valid_backup_code(email, otp_token):
					login(self.request, user)
					return redirect(f'/{ADMIN_PATH}/')
				else:
					messages.error(self.request, 'Invalid OTP. Please try again.')
					return render(self.request, self.template_name, {'form': form})
			else:
				messages.error(self.request, 'No OTP device setup. Please completed setup and try again.')
				return render(self.request, self.template_name, {'form': form})
		else:
			messages.error(self.request, 'Invalid credentials. Please try again.')
			return render(self.request, self.template_name, {'form': form})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['otp_required'] = True
		return context

	def is_valid_backup_code(self, email, backup_code):
		try:
			# Get the backup code associated with the user
			get_device = StaticDevice.objects.get(user__email=email, confirmed=True)
			backup_code_instance = StaticToken.objects.filter(device=get_device, token=backup_code).exists()

			return backup_code_instance
		except StaticToken.DoesNotExist:
			return False
