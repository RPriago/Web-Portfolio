from django.shortcuts import render, HttpResponse
import smtplib
import ssl
from django.core.mail import send_mail, EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from item.models import Category, Item
from django.conf import settings
from .forms import ContactForm
from django.http import JsonResponse

def index(request):
    items = Item.objects.all().order_by('-date')
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Message from {name}'
            full_message = f'From: {name} <{email}>\n\n{message}'

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            return JsonResponse({'message': "Thanks for contacting us!"})
    else:
        form = ContactForm()

    for category in categories:
        print(f'Category: {category.name}')
    for item in items:
        print(f'Item: {item.name}, Category: {item.category.name}')

    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
        'form' : form,
    })