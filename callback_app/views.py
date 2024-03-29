from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import CallbackForm


def home(request):

    return render(request, 'index.html')


def submit_callback_form(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject,
                    f'Name: {name}\nEmail: {email}\nMobile: {mobile}\nMessage: {message}',
                    'callback@reeskk.org',
                    ['info@reeskk.org'],
                    fail_silently=False,
                )
                return JsonResponse({'message': 'Form submitted successfully!'}, status=200)
            except Exception as e:
                return JsonResponse({'message': f'Failed to send email: {str(e)}'}, status=500)
        else:
            return JsonResponse({'message': 'Form data is invalid.'}, status=400)

    return JsonResponse({'message': 'Invalid request.'}, status=400)
