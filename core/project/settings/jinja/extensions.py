from datetime import datetime

from django.template.defaultfilters import date
from django.utils import timezone
from jinja2 import lexer, nodes
from jinja2.ext import Extension

from core.project.settings.base import USE_TZ  # type: ignore


class DjangoNow(Extension):
	tags = set(['now'])

	def _now(self, date_format):
		tzinfo = timezone.get_current_timezone() if USE_TZ else None
		formatted = date(datetime.now(tz=tzinfo), date_format)
		return formatted

	def parse(self, parser):
		lineno = next(parser.stream).lineno
		token = parser.stream.expect(lexer.TOKEN_STRING)
		date_format = nodes.Const(token.value)
		call = self.call_method('_now', [date_format], lineno=lineno)
		token = parser.stream.current
		if token.test('name:as'):
			next(parser.stream)
			as_var = parser.stream.expect(lexer.TOKEN_NAME)
			as_var = nodes.Name(as_var.value, 'store', lineno=as_var.lineno)
			return nodes.Assign(as_var, call, lineno=lineno)
		else:
			return nodes.Output([call], lineno=lineno)
