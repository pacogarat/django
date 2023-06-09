from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('persons/', views.PersonListView.as_view()),
    path('person/', views.PersonView.as_view()),
    path('person/<uuid:id>', views.PersonView.as_view()),
    path('groups/', views.GroupListView.as_view()),
    path('group/', views.GroupView.as_view()),
    path('group/<uuid:id>', views.GroupView.as_view())
]