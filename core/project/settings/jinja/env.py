from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment

from .filters import date_format, int_comma, media_duration


def JinjaEnvironment(**options):
	env = Environment(**options)  # noqa: S701
	env.globals.update(
		{
			'static': staticfiles_storage.url,
			'url': reverse,
			'get_messages': messages.get_messages,
			'trim_blocks': True,
			'Istrip_blocks': True,
		}
	)
	env.filters.update(
		{
			'int_comma': int_comma,
			'date_format': date_format,
			'media_duration': media_duration,
		}
	)

	return env
