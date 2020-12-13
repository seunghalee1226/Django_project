from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from studyboard.models import Studyboard
from django.conf import settings


class PostLV(ListView):
    model = Studyboard
    template_name = 'studyboard/studyboard_all.html'
    context_object_name = 'studyboards'
    paginate_by = 10


class PostDV(DetailView):
    model = Studyboard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f'{settings.DISQUS_SHORTNAME}'
        context['disqus_id'] = f'post-{self.object.id}-{self.object.slug}'
        context['disqus_url'] = f'{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}'
        context['disqus_title'] = f'{self.object.slug}'

        return context

class PostAV(ArchiveIndexView):
    model = Studyboard
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Studyboard
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Studyboard
    date_field = 'modify_dt'
    month_format = '%m'


class PostDAV(DayArchiveView):
    model = Studyboard
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Studyboard
    date_field = 'modify_dt'


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_studyboard_list.html'
    model = Studyboard

    def get_queryset(self):
        return Studyboard.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
