from django.shortcuts import render, redirect
from .forms import ContactForm 
from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
# Create your views here.
def HomeView(request):
    return render(request, 'simpleweb/home.html')

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            template = get_template('simpleweb/contact.txt')
            subject = 'Website user feedback'
            content = {
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'company': form.cleaned_data.get('company'),
                'phone': form.cleaned_data.get('phone'),
                'message': form.cleaned_data.get('message')
            }
            content = template.render(content)
            try:
                send_mail(subject, content, settings.EMAIL_HOST_USER, ['creativestudents11@gmail.com'], fail_silently=False)
                messages.success(request, f'Thank you for contacting us. We will get back to you soon')
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'simpleweb/contact.html', {'form':form})        

def SuccessView(request):
    return render(request, 'simpleweb/contact_success.html')