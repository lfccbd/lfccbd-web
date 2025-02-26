from django.urls import path

from .views import (
    About,
    AccountSuspended,
    ChildrenMinistry,
    CHOPMinistry,
    EvangelismMinistry,
    FollowupMinistry,
    Home,
    HospitalityMinistry,
    Ministries,
    SanctuaryMinistry,
    SundayServiceMinistry,
    WenesdayServiceMinistry,
    WOFBIMinistry,
    WOSEMinistry,
    WSFMinistry,
    YAFMinistry,
)

urlpatterns = [
    path('user/suspended/', AccountSuspended.as_view(), name='lockout'),
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('ministries/', Ministries.as_view(), name='ministries'),
    path('ministry/service/sunday/', SundayServiceMinistry.as_view(), name='sunday_ministry'),
    path('ministry/service/wenesday/', WenesdayServiceMinistry.as_view(), name='wenesday_ministry'),
    path('ministry/service/wose/', WOSEMinistry.as_view(), name='wose_ministry'),
    path('ministry/service/chop/', CHOPMinistry.as_view(), name='chop_ministry'),
    path('ministry/service/wsf/', WSFMinistry.as_view(), name='wsf_ministry'),
    path('ministry/service/wofbi/', WOFBIMinistry.as_view(), name='wofbi_ministry'),
    path('ministry/service/yaf/', YAFMinistry.as_view(), name='yaf_ministry'),
    path('ministry/children/department/', ChildrenMinistry.as_view(), name='children_ministry'),
    path('ministry/evangelism/department/', EvangelismMinistry.as_view(), name='evangelism_ministry'),
    path('ministry/sanctuary/department/', SanctuaryMinistry.as_view(), name='sanctuary_ministry'),
    path('ministry/followup/department/', FollowupMinistry.as_view(), name='followup_ministry'),
    path('ministry/hospitality/department/', HospitalityMinistry.as_view(), name='hospitality_ministry'),
]
