# coding: utf-8
# Last modified: 2014 Jul 24 05:04:37 PM
# xh

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 20, min_length = 5)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(max_length=200, min_length=10, widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Not enough words!')
        return message
