from django.shortcuts import render
# mixins are used as a decorator like in function view
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Group, GroupMembers

# we create a class based CRUD
# login required mixin is substitute for login required


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
