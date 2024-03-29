from django.urls import path
from .views import *

urlpatterns = [
   path('submitData/', PerevalView.as_view()),
   path('submitData/<int:pk>', PerevalRecordView.as_view()),
   path('submitData/<int:pk>/status', PerevalStatusView.as_view()),
]
