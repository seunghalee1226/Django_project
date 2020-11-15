from datetime import datetime
import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Notice(models.Model):
    user_name = models.CharField(unique=True, max_length=50)
    # 페이지나 포스트를 설명하는 핵심단어의 집합
    # SlugField : 제목의 단어들을 하이픈으로 연결, URL에서 pk 대신 사용
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)
    title = models.CharField('TITLE', max_length=100, blank=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    secret = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=False)
    create_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True)

    USERNAME_FILE = 'user_name'

    def get_id(self):
        return self.id


class StudyBoard(models.Model):

    user_name = models.CharField('USER', unique=True, max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)
    title = models.CharField('TITLE', max_length=100, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'studyboard_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('studyboard:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
