from django.contrib import admin
# from django.conf.urls import include, url
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path(r'^polls/$', include('polls.urls'),name='polls'),
    path('polls/', include('polls.urls'),name='polls'),
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('login/' ,auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]