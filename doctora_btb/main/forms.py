from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control p-3 rounded-0', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control p-3 rounded-0', 'id': 'email'}),
            'body': forms.Textarea(attrs={'class': 'form-control p-3 rounded-0', 'rows': '10', 'cols': '30',
                                          'id': 'body'})
        }