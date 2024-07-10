from django.urls import path
from common.views import *


urlpatterns = [
    path('config/', SettingsListAPIView.as_view(), name='config')
]