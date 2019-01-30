from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from .views import UserCreate, NotFound
from . import views
app_name = 'authe'

urlpatterns=[
    path('oops/', NotFound.as_view(),name = 'oops'),
    path('login/', auth_views.LoginView.as_view(), name = 'login' ),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
    path('signup/',UserCreate.as_view(),name = 'signup'),
    path('chpwd/', views.UserChangePassword.as_view(), name='chpwd'),
    path('chpwd/success', auth_views.PasswordChangeDoneView.as_view(), name ='chpwddone'),
    path('resetpwd/',views.UserResetPassword.as_view(),name ='pwdreset'),
    path('resetpwd/confirm/<uidb64>/<token>/', views.UserResetConfirm.as_view(), name='pwdresetconfirm'),
    path('resetpwd/done',auth_views.PasswordResetDoneView.as_view(),name = 'pwdresetdone'),
    path('resetpwd/complete/',auth_views.PasswordResetCompleteView.as_view(),name ='pwdresetcomp'),
]
