from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Your Title Here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Your Title_tag Here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
#            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Your Description Here'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Your Title Here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Your Title_tag Here'}),
#            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Your Description Here'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }