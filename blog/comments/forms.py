from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'post']
        
class CommentUpdateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']