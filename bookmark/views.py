from django.views.generic import ListView, DetailView
from bookmark.models import Notice, Member, StudyBoard

class NoticeLV(ListView):
    model = Notice
    context_object_name = 'notics'
    paginate_by = 5

class NoticeDV(DetailView):
    model = Notice

class MemberDV(DetailView):
    model = Member

class StudyBoardLV(ListView):
    model = StudyBoard
    context_object_name = 'study board'
    paginate_by = 10
