# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth import views

urlpatterns = [

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

]