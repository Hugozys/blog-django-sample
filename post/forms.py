from django.forms import ModelForm, Textarea
from .models import Post, Comment, Tag
from martor.widgets import MartorWidget
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =  ['title','tags', 'body']
        widgets = {
          'body': MartorWidget(attrs={'rows':50, 'cols':100}),
        }
        pass
    pass


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields =  ['tag_text']
        pass
    pass

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content':MartorWidget(attrs={'rows':20,'cols':100}),
        }
        pass
    
    def save(self, commit=True):
        comment = super(CommentForm,self).save(commit=False)
        if commit:
            comment.save()
            pass
        return comment
    pass


