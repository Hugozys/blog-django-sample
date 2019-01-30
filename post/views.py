from django.shortcuts import get_object_or_404, render, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Tag
from .forms import PostForm, CommentForm, TagForm
from django.utils import timezone
from django.forms import modelformset_factory
from django.contrib.auth.decorators import permission_required


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    tags = Tag.objects.filter(post__id=post_id)
    if (request.method == 'POST'):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.created_date = timezone.now()
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return render(request,'post/detail.html',{'post':post,'tags':tags,'form':form})
    else:
        form = CommentForm()
        pass
    return render(request, 'post/detail.html',{'post':post,'tags':tags,'form':form})



def index(request):
    post_list = Post.objects.exclude(tags__tag_text="travel")
    context = {'post_list': post_list,'tagname':'Articles'}
    return render(request, 'post/index.html',context)


def tagIndex(request,tag_slug):
    post_list = Post.objects.filter(tags__tag_text=tag_slug)
    context = {'post_list': post_list, 'tagname':tag_slug}
    return render(request, 'post/index.html',context)

@permission_required('post.can_create',login_url="authe:oops")
def create(request):
    print("Creating")
    if (request.method == 'POST'):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.pub_date = timezone.now()
            new_post.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("post:index"))
    else:
        form = PostForm()
        pass
    return render(request, "post/create.html",{'form':form})


@permission_required('post.can_edit',login_url="authe:oops")
def edit(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if (request.method == 'POST'):
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.pub_date = timezone.now()
            new_post.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("post:index"))
    else:
        form = PostForm(instance=post)
        pass
    return render(request, "post/edit.html",{'form':form, 'post_id': post_id })


@permission_required('post.can_edit',login_url="authe:oops")    
def editTags(request):
    tag_num = Tag.objects.count()
    TagFormSet = modelformset_factory(Tag,can_delete=True,fields=("tag_text",),
                                      extra=2,
                                      min_num=tag_num,
                                      max_num=20,
                                      validate_max=True,
    )
    if (request.method == 'POST'):
        formset = TagFormSet(request.POST, request.FILES)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for obj in formset.deleted_objects:
                obj.delete()
                pass
            
            for instance in instances:
                instance.save()
                pass
            
            return HttpResponseRedirect(reverse("post:index"))
        pass
    else:
        formset = TagFormSet(queryset=Tag.objects.all())
        pass
    return render(request, "post/edit_tag.html",{'formset':formset})
    

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post:index')
    pass



# Create your views here.
