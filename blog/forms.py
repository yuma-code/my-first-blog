from django import forms

from .models import Post, Comment, DEVICE_CHOICES, PURPOSE_CHOICES, RANK_CHOICES, NUM_CHOISES

DEVICE_CHOICES = [('', '指定なし')] + DEVICE_CHOICES
PURPOSE_CHOICES = [('', '指定なし')] + PURPOSE_CHOICES

class SearchForm(forms.Form):
    device = forms.ChoiceField(label='機種', widget=forms.Select, choices=DEVICE_CHOICES, required=False)
    purpose = forms.ChoiceField(label='目的', widget=forms.Select, choices=PURPOSE_CHOICES, required=False)
    rank = forms.ChoiceField(label='ランク', widget=forms.Select, choices= RANK_CHOICES, required=False)
    num = forms.ChoiceField(label='ランクレベル', widget=forms.Select, choices=NUM_CHOISES, required=False)

    # class Meta:
    #     fields = ('device', 'purpose')


# SearchFormSet = forms.formset_factory(SearchForm, extra=1)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('psid', 'comment', 'device', 'purpose','rank','num')
        labels = {
            'psid' : 'ID',
            'comment' : 'コメント',
            'device' : '機種',
            'purpose' : '目的',
            'rank' : 'ランク',
            'num' : 'ランクレベル'
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
