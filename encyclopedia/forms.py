from django import forms

class new_page(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'rows': '6',
                                                           'placeholder': 'Enter the Markdown content for the page'}))