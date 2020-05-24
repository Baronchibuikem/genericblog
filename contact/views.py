from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Category
from django.contrib import messages

def contact(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    form = ContactForm()
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = ['baronchibuike@gmail.com']
        if cc_myself:
            recipients.append(sender)
        send_mail(subject, message, sender, recipients)
        messages.add_message(request, messages.INFO, 'Your Comment has been submitted for review. It will be added shortly')
        return HttpResponseRedirect()
    context = {'form': form,
      'category': category, 
        'categories': categories,}
    return render(request, 'contact/contact.html',context)

