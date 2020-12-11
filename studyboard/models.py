from datetime import datetime
import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class Studyboard(models.Model):

    user_name = models.CharField('USER', max_length=50)
    title = models.CharField('TITLE', max_length=100, blank=True)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)
    is_active = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'studyboard'
        verbose_name_plural = 'studyboards'
        db_table = 'studyboard_postlist'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('studyboard:studyboard_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()