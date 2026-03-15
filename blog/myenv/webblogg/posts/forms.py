from django import forms
from .models import PostsArticle

class ArticleForm(forms.ModelForm):
    class Meta:
        model = PostsArticle
        # These are the fields from your Postgres table you want to fill in
        fields = ['slug', 'image', 'title', 'body', 'published_date', 'author', 'handle']
        
        # This part makes the form look nice with Tailwind/CSS
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4'}),
            'body': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4', 'rows': 5}),
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border border-gray-300 rounded mb-4'}),
            'slug': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4'}),
            'image': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4', 'placeholder': 'URL to image'}),
            'author': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4'}),
            'handle': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4'}),
        }