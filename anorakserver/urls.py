from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from django.contrib.auth.models import User
from anorakapi.views import register_user, login_user, Tags, Whiskeys, UserWhiskeys

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tags', Tags, 'tag')
router.register(r'whiskeys', Whiskeys, 'whiskey')
router.register(r'userwhiskeys', UserWhiskeys, 'userwhiskey')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]