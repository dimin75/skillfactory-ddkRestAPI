from django.urls import path
from .views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



urlpatterns = [
   path('submitData/', PerevalView.as_view()),
   path('submitData/<int:pk>', PerevalRecordView.as_view()),
   path('submitData/<int:pk>/status', PerevalStatusView.as_view()),
   path('help/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('generate_yaml/', schema_view.without_ui(cache_timeout=0), name='generate-yaml'),
   path('swagger.yaml', schema_view.without_ui(cache_timeout=0)),
]
