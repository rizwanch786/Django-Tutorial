from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'home'),
    path('contact/', contact, name = 'contact-us'),
    path('about/', about, name = 'about-us'),
    path('dynamic/<slug>', dynamic_urls, name = 'dynamic'),
    path('todo/', todo_app, name='todo-app'),
    path('del/<str:item_id>', remove_todo, name="del-todo"),
    path('mark/<str:item_id>', mark_completed, name="mark-completed"),
    path('login', signin, name='login'),
    path('signup', registration, name='signup'),
    path('logout/', logout_view, name='logout')
]
