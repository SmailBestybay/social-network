from django.forms import ModelForm
from .models import Listing, Comment

class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid','image', 'category']

class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Comment'}
