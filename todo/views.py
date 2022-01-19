from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import ToDo
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class UserLoginPage(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todos')

class SignUpPage(FormView):
    template_name = 'todo/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todos')
        return super(SignUpPage, self).get(*args, **kwargs)



class TodoList(LoginRequiredMixin,ListView):
    model = ToDo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(user=self.request.user)
        context['count'] = context['todos'].filter(complete=False).count()
        return context



class TodoCreate(LoginRequiredMixin,CreateView):
    model = ToDo
    fields = ['title', 'complete']
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)

class TodoUpdate(LoginRequiredMixin,UpdateView):
    model = ToDo
    fields = ['title', 'complete']
    success_url = reverse_lazy('todos')

class TodoDelete(LoginRequiredMixin,DeleteView):
    model = ToDo
    success_url = reverse_lazy('todos')


