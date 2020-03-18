from django import forms

from .models import Post, Comment

GENDER_CHOICES=(
    ('ps4','PS4'),
    ('pc','PC')
)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
    gender_r = forms.ChoiceField(
        label='device',
        widget=forms.Select,
        choices=GENDER_CHOICES,
        required=True,
    )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
