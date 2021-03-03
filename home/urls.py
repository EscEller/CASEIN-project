from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home_page, name='home'),

    path('norm_docks/', norm_docks, name='norm_docks'),
    path('polit_bez/', polit_bez, name='polit_bez'),
    path('instructions/', instructions, name='instructions'),
    path('korpculture/', korpculture, name='corp_culture'),

    path('test/', home_page, name='test'),

    path('my_team/', team_page, name='my_team'),

    path('contacts/', contacts, name='contacts'),

    path('start/', start_page, name='start')
]
