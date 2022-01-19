from django.urls import path
from .views  import TodoList,TodoCreate, TodoUpdate, TodoDelete, UserLoginPage, SignUpPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpPage.as_view(), name='signup'),
    path('', TodoList.as_view(), name='todos'),
    path('todo-create/', TodoCreate.as_view(), name='todo-create'),
    path('todo-update/<int:pk>', TodoUpdate.as_view(), name='todo-update'),
    path('todo-delete/<int:pk>', TodoDelete.as_view(), name='todo-delete'),
]