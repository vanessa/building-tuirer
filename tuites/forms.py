from django import forms

from tuites.models import Tuite


class PostTuiteForm(forms.ModelForm):
    class Meta:
        model = Tuite
        fields = ('content', 'author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.initial['user'].id
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['content'].label = 'O que você está pensando?'

    def clean(self):
        cleaned_data = super().clean()

        content = self.cleaned_data.get('content')
        if 'Temer' in content:
            raise forms.ValidationError('FORA TEMER')

        if not self.initial.get('user') == cleaned_data.get('author'):
            raise forms.ValidationError('Não tente burlar o sistema!')

        return cleaned_data
