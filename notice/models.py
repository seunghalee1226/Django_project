from datetime import datetime
import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Notice(models.Model):
    user_name = models.CharField(max_length=50)
    # 페이지나 포스트를 설명하는 핵심단어의 집합
    # SlugField : 제목의 단어들을 하이픈으로 연결, URL에서 pk 대신 사용
    title = models.CharField('TITLE', max_length=100, blank=True)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)

    class Meta:
        verbose_name = 'notice'
        verbose_name_plural = 'notices'
        db_table = 'notice_post'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice:notice_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
