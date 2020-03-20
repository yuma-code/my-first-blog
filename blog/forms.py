from django import forms

from .models import Post, Comment, DEVICE_CHOICES, PURPOSE_CHOICES

DEVICE_CHOICES = [('', '---------')] + DEVICE_CHOICES
PURPOSE_CHOICES = [('', '---------')] + PURPOSE_CHOICES

class SearchForm(forms.Form):
    device = forms.ChoiceField(label='機種', widget=forms.Select, choices=DEVICE_CHOICES, required=False)
    purpose = forms.ChoiceField(label='目的', widget=forms.Select, choices=PURPOSE_CHOICES, required=False)

    # class Meta:
    #     fields = ('device', 'purpose')


# SearchFormSet = forms.formset_factory(SearchForm, extra=1)

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
