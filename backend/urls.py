# from django.urls import path
# from . import views
# from .views import SignUpView, LoginView, LogoutView, check_user_active

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('api/check_user_active/<str:username>/', check_user_active, name='check_user_active'),
# ]

from django.contrib import admin
from django.urls import path
from . import views
# from .views import SignUpView, LoginView, LogoutView, check_user_active

# Admin panel customization
admin.site.site_header = 'Altermail'
admin.site.site_title = 'Altermail'
admin.site.index_title = 'Welcome to Altermail'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('api/check_user_active/<str:username>/', views.check_user_active, name='check_user_active'),
]
