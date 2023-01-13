from .views import UserRecordView
from django.urls import path

app_name = 'Hi_Teens_API'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
]