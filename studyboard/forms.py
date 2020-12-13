from django import forms

class StudyboardSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')