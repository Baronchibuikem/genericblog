from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(max_length= 100)
    message = forms.CharField(widget=forms.Textarea, help_text="Please type your message here")
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
