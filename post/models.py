from django.db import models
from martor.models import MartorField
from django.contrib.auth.models import User
from django.utils import timezone
#from django.utils.html import mark_safe
#from markdown import markdown
# Create your models here.


class Tag(models.Model):
    tag_text = models.CharField(max_length=255, unique=True)
    #description = models.Char
    def __str__(self):
        return self.tag_text
    pass


class Post(models.Model):
    class Meta:
        permissions = (("can_create", "Create Posts"),
                       ("can_edit", "Edit Posts"),
        )
        pass
    title = models.CharField(max_length=255)
    body = MartorField()#models.CharField(max_length=20000)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField('date published')
    # mod_date = models.DateTimeField('date modified')
    #def get_message_as_markdown(self):
    #    return mark_safe(markdown(self.body,safe_mode='escape'))
    #pass

    def __str__(self):
        return self.title
    pass



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    content = MartorField()
    created_date = models.DateTimeField('date published')
    pass

    
