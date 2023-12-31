from django.urls import path

from core.dashboard.auth import sign_in, sign_out
from core.dashboard.view import index


urlpatterns = [

    path("", index, name='home'),

    # auth
    path("login/", sign_in, name='login'),
    path('logout/', sign_out, name='log-out'),

]
