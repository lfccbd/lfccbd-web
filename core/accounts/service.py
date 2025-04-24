from defender import utils
from defender.models import AccessAttempt
from defender.utils import get_ip
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

# user model
User = get_user_model()


class AccountService:

    @staticmethod
    def get_user_ip(request):
        client_ip = get_ip(request)
        if client_ip is not None:
            return client_ip
        else:
            raise PermissionDenied

    @staticmethod
    def get_attempt_left(request):
        max_attempts = settings.DEFENDER_LOGIN_FAILURE_LIMIT
        user_ip = AccountService.get_user_ip(request)

        # latest successful login attempt (if any)
        last_successful = (
            AccessAttempt.objects.filter(ip_address=user_ip, login_valid=True)
            .order_by('-attempt_time')
            .first()
        )

        # failed attempts since the last successful login
        if last_successful:
            failed_attempts = AccessAttempt.objects.filter(
                ip_address=user_ip,
                login_valid=False,
                attempt_time__gt=last_successful.attempt_time,
            ).count()
        else:
            failed_attempts = AccessAttempt.objects.filter(
                ip_address=user_ip, login_valid=False
            ).count()

        # remaining attempts
        attempts_left = max(max_attempts - failed_attempts, 0)

        return attempts_left

    @staticmethod
    def defender_block_user(user_ip, email):
        utils.block_ip(ip_address=user_ip)
        utils.block_username(username=email)

    @staticmethod
    def defender_unblock_user(request, user_ip, email):
        utils.reset_failed_attempts(ip_address=user_ip, username=email)
        utils.unblock_username(username=email)
        utils.unblock_ip(ip_address=user_ip)
        utils.add_login_attempt_to_db(request, username=email, login_valid=True)
