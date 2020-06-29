from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .forms import MessageForm
from .tasks import async_send_mail
from .models import Message


def home(request):
    template = 'main/index.html'
    feedback_form = MessageForm()
    context = {'form': feedback_form}
    return render(request, template, context)


def send_message(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        if request.recaptcha_is_valid:
            cd = form.cleaned_data
            body, name, email = cd['body'], cd['name'], cd['email']
            message_text = f'Отправитель:\n' \
                           f'Имя: {name}\n' \
                           f'email: {email}\n\nТекст сообщения:\n{body}'
            message = Message(body=body, name=name, email=email)
            message.save()
            async_send_mail.delay(name, message_text, settings.EMAIL_HOST_USER, settings.EMAIL_RECIPIENT, message.id)
            status = 'OK'
        else:
            status = 'CAPTCHA'

    else:
        status = form.errors

    return HttpResponse(status)
