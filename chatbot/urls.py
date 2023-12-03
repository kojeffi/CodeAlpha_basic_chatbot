from django.urls import path
from .views import chatbot_view, get_bot_response

urlpatterns = [
    path('', chatbot_view, name='chatbot_view'),
    path('get_bot_response/', get_bot_response, name='get_bot_response'),
]
