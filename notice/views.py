from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from notice.models import Notice


class PostLV(ListView):
    model = Notice
    template_name = 'notice/notice_all.html'
    context_object_name = 'notices'
    paginate_by = 5

class PostDV(DetailView):
    model = Notice

class PostAV(ArchiveIndexView):
    model = Notice
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Notice
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Notice
    date_field = 'modify_dt'
    month_format = '%m'

class PostDAV(DayArchiveView):
    model = Notice
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Notice
    date_field = 'modify_dt'
