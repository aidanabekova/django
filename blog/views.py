from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from . import models, forms


def get_posts(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


def post_detail(request, id):
    try:
        post = models.Post.objects.get(id=id)
        try:
            comment = models.Comment.objects.filter(post_id=id).order_by('created_date')
        except models.Comment.DoesNotExist:
            return HttpResponse('no comments!')

    except models.Post.DoesNotExist:
        raise Http404('post does nor exist!')

    return render(request, 'post_detail.html', {'post': post, 'post_comment': comment})


def add_post(request):
    method = request.method
    if method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        print(form.data)
        models.Post.objects.create(title=form.data['title'],
                                   description=form.data['description'],
                                   image=request.FILES['image'])
        return redirect('/posts/')
    else:
        form = forms.PostForm()
    return render(request, 'add_post.html', {'form': form})


def add_comment(request):
    method = request.method
    if method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponse("comment created Successfully!")
    else:
        form = forms.CommentForm
    return render(request, 'add_comment.html', {'form': form})
