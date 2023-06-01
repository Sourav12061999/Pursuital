from django.contrib import admin
from django.urls import path
from .views import signup, signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
]
