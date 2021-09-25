# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from django.contrib.auth import views

from .views import login_view, register_user, activate_account
from apps.authentication.forms import EmailValidationOnForgotPassword

urlpatterns = [

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('password_reset/', views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword),
         name="password_reset"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('activate/<uidb64>/<token>/', activate_account, name='activate')
]