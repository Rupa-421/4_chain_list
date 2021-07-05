from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
