from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def services(request):
    return render(request, "core/services.html")


def projects(request):
    return render(request, "core/projects.html")


def industries(request):
    return render(request, "core/industries.html")


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        company = request.POST.get("company")
        service = request.POST.get("service")
        message = request.POST.get("message")

        subject = f"New Quote Request - {service}"

        body = f"""
New Quote Request

Name: {name}
Email: {email}
Phone: {phone}
Company: {company}

Service Required:
{service}

Project Details:
{message}
"""

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ["info@kleenchamps.com"],   # Change to your email
            fail_silently=False,
        )

        messages.success(
            request,
            "Thank you! Your request has been sent successfully."
        )

    return render(request, "core/contact.html")