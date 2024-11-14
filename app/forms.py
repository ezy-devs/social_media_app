from django import forms

from .models import Post

INPUT_CLASSES = 'text-input'

class PostCreationForm(forms.ModelForm):
    user = forms.CharField(label='Username', widget=forms.TextInput(attrs=
                                        {'class': INPUT_CLASSES,
                                        'placeholder': 'Your Username'}))

    fields = [
        '__all__'
    ]