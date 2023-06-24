from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', include(obtain_auth_token)),
    path('people_in_group/<uuid:group_id>', views.api_home),
    path('persons/', views.PersonListView.as_view()),
    path('person/', views.PersonView.as_view()),
    path('person/<uuid:id>', views.PersonView.as_view()),
    path('groups/', views.GroupListView.as_view()),
    path('group/', views.GroupView.as_view()),
    path('group/<uuid:id>', views.GroupView.as_view())
]