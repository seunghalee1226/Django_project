from django.views.generic import ListView, DetailView
from userlist.models import Userlist


class UserlistLV(ListView):

    model = Userlist


class UserlistDV(DetailView):

    model = Userlist
