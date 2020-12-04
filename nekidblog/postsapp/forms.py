from django.contrib.auth.forms import AuthenticationForm
from django import forms
from postsapp.models import Post
from django.contrib.auth.models import User as BlogAuthor


class BlogAuthorLoginForm(AuthenticationForm):

    class Meta:
        model = BlogAuthor
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(BlogAuthorLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       exclude = ('author', 'date_created', )
       #exclude = ('date_created', )

   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field_name, field in self.fields.items():
           field.widget.attrs['class'] = 'form-control'