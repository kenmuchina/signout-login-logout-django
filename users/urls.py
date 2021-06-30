from django.urls import path
from . import views

urlpatterns = [
    path('', views.account),
    path('clear_db/', views.clear_db),
    path('users/', views.view_db),
    path('signup/', views.signup),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('restricted/', views.restricted)
]