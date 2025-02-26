from django.views.generic.base import TemplateView

from core.post.models import UpcomingEvent


class AccountSuspended(TemplateView):
    template_name = 'error-pages/account-suspended.html'


class Home(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = UpcomingEvent.objects.order_by(
            'date_created'
        ).all()[:5]
        return context


class About(TemplateView):
    template_name = 'pages/about.html'


class Giving(TemplateView):
    template_name = 'pages/giving.html'


class Ministries(TemplateView):
    template_name = 'ministries/ministries.html'


class SundayServiceMinistry(TemplateView):
    template_name = 'ministries/sunday_ministry.html'


class WenesdayServiceMinistry(TemplateView):
    template_name = 'ministries/wenesday_ministry.html'


class WOSEMinistry(TemplateView):
    template_name = 'ministries/wose_ministry.html'


class CHOPMinistry(TemplateView):
    template_name = 'ministries/chop_ministry.html'


class WSFMinistry(TemplateView):
    template_name = 'ministries/wsf_ministry.html'


class WOFBIMinistry(TemplateView):
    template_name = 'ministries/wofbi_ministry.html'


class YAFMinistry(TemplateView):
    template_name = 'ministries/yaf_ministry.html'


class ChildrenMinistry(TemplateView):
    template_name = 'ministries/children_ministry.html'


class EvangelismMinistry(TemplateView):
    template_name = 'ministries/evangelism_ministry.html'


class SanctuaryMinistry(TemplateView):
    template_name = 'ministries/sanctuary_ministry.html'


class FollowupMinistry(TemplateView):
    template_name = 'ministries/followup_ministry.html'


class HospitalityMinistry(TemplateView):
    template_name = 'ministries/hospitality_ministry.html'
