from django import forms
from .models import Comment, Subscription

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['your_email', ]


