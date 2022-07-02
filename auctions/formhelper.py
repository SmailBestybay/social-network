from django.forms import ModelForm, Textarea
from .models import Listing, Comment

class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid','image', 'category']

class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        # to have no label
        labels = {'content': ''}
        # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#modelform
        widgets = {'content' : Textarea(attrs={'placeholder':'Comment'}),
            }
        
