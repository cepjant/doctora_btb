from django.urls import path
from .views import home, send_message
from .decorators import check_recaptcha

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('send_message/', check_recaptcha(send_message), name='feedback')
]