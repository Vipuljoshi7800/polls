from django import forms
from .models import Post
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description','category','comment_count','email','post_status','color_choices','created_date')
        # labels = {"text": "title", "public": "label for public"}

class MyForm(forms.Form):

    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    CHOICES2 = (('Option 1', 'option 1',),('Option 2', 'option 2',),('Option 3', 'option 3',),('Option 4', 'option 4',))
    field = forms.ChoiceField(choices=CHOICES)
    field2 = forms.ChoiceField(choices = CHOICES2)
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

