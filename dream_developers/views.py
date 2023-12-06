from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name', '')
        number = request.POST.get('number', '')
        email = request.POST.get('email', '')
        project = request.POST.get('project', '')
        message = request.POST.get('message', '')
        subject = f"New Message from {name}"
        message_body = f"Name: {name}\nNumber: {number} \nEmail: {email}\nProject: {project}\nMessage: {message}"

        sender_email = 'contact.dream.developers@gmail.com'

        send_mail(subject, message_body, sender_email, ['contact.dream.developers@gmail.com'])

        return redirect('index')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        number = request.POST.get('number', '')
        email = request.POST.get('email', '')
        project = request.POST.get('project', '')
        message = request.POST.get('message', '')
        subject = f"New Message from {name}"
        message_body = f"Name: {name}\nNumber: {number} \nEmail: {email}\nProject: {project}\nMessage: {message}"

        sender_email = 'contact.dream.developers@gmail.com'

        send_mail(subject, message_body, sender_email, ['contact.dream.developers@gmail.com'])

        return redirect('contact')
        

    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')
def project(request):
    return render(request, 'project.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def error_template(request):
    return render(request, '404.html')
def blog(request):
    return render(request, 'blog.html')