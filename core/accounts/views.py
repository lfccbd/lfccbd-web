from defender import utils
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

# import forms
from .forms import UserLoginForm

# import service
from .service import AccountService

# user model
User = get_user_model()


# Account signing
class AccountSignIn(View):
	template_name = 'accounts/login.html'
	success_url = 'followup'

	def __init__(self):
		self.context = {
			'form': UserLoginForm(),
			'login_attempts_left': 0,
		}

	def get(self, request, *args, **kwargs):
		self.context['login_attempts_left'] = AccountService.get_attempt_left(request)
		return render(request, self.template_name, self.context)

	def post(self, request, *args, **kwargs):
		form = UserLoginForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user_ip = AccountService.get_user_ip(request)

			# Check if the user exists
			user = User.objects.filter(email=email).first()

			if not user:
				# user does not exist, check if they are already locked out
				if utils.is_already_locked(request, username=email):
					return redirect('account_logout')

				# failed attempt, update remaining attempts
				utils.add_login_attempt_to_db(request, username=email, login_valid=False)
				self.context['login_attempts_left'] = AccountService.get_attempt_left(request)

				# Block the user if attempts reach zero
				if self.context['login_attempts_left'] == 0:
					AccountService.defender_block_user(user_ip, email)
					return redirect('lockout')

				messages.error(
					request,
					f'Invalid Login Credentials. You have {self.context["login_attempts_left"]} attempt(s) left',
				)

			else:
				# Authenticate user
				user = authenticate(request, email=email, password=password)

				if user:
					# successful login: reset failed attempts and login
					AccountService.defender_unblock_user(request, user_ip, email)
					login(request, user)
					return redirect('followup')

				else:
					# Failed authentication attempt
					utils.add_login_attempt_to_db(request, username=email, login_valid=False)
					self.context['form'] = UserLoginForm(initial={'email': '', 'password': ''})
					self.context['login_attempts_left'] = AccountService.get_attempt_left(request)

					# lockout if necessary
					if utils.is_already_locked(request, username=email) or self.context['login_attempts_left'] == 0:
						AccountService.defender_block_user(user_ip, email)
						return redirect('account_logout')

		# form is invalid, update errors
		self.context['login_attempts_left'] = AccountService.get_attempt_left(request)
		self.context['form'] = form
		return render(request, self.template_name, self.context)


class AccountLogout(View):
	def get(self, request, *args, **kwargs):
		# logout user
		logout(request)
		# flush session
		self.request.session.flush()

		return HttpResponsePermanentRedirect(reverse('home'))


class AccountSuspended(TemplateView):
	template_name = 'error-pages/account-suspended.html'
