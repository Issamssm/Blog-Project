from django import forms
from .models import Post


# from for comments
        
        
        
        
class PostCreatForm(forms.ModelForm):
    title = forms.CharField(label='Title of Post')
    title1 = forms.CharField(label='Title of the first paragraph', help_text='Title of first paragraph', required=False)
    title2 = forms.CharField(label='Title of the second paragraph', help_text='If you have a second paragraph, enter its title here', required=False)
    content = forms.CharField(label='Content of first paragraph', widget = forms.Textarea)
    content2 = forms.CharField(label='if you have a seconde paragraph', widget = forms.Textarea, help_text='If you have a second paragraph, enter it here', required=False)
    image2 = forms.ImageField(label='if you have second image', required=False)
    class Meta:
        model = Post
        fields = ['title','title1', 'content','title2','content2', 'image', 'image2','categry']
        
        

        
        
        