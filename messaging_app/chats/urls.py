
from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/', views.MessageViewSet, name='messages'),
    path('conversations/', views.ConversationViewSet, name='conversations'),
]
