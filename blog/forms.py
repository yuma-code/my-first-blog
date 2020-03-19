from django import forms

from .models import Post, Comment



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('psid', 'comment', 'device', 'purpose')
        labels = {
            'psid' : 'ID',
            'comment' : 'コメント',
            'device' : '機種',
            'purpose' : '目的',
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
