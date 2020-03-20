from django.shortcuts import redirect
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostForm,CommentForm, SearchForm

def start(request):
    return render(request, 'blog/home.html')

def post_list_apex(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list-apex.html', {'posts': posts})

def post_list_fortnight(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/post_list_fortnight.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# @login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

# @login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('apex')

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('comeon')

# 絞り込み検索
def index(request):
    # post_list = Profile.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    form = SearchForm(request.GET or None)
    if request.method == 'GET':
        # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
        if form.is_valid():

            # Qオブジェクトを格納するリスト
            queries = []

            # 各フォームの入力をもとに、Qオブジェクトとして検索条件を作っていく
            # for form in forms:
            # Qオブジェクトの引数になる。
            # {gender: 1, height__gte: 170} → Q(gender=1, height__gte=170)
            q_kwargs = {}
            device = form.cleaned_data['device']
            print(form.cleaned_data['device'])
            if device:
                q_kwargs['device'] = device

            purpose = form.cleaned_data['purpose']
            if purpose:
                q_kwargs['purpose'] = purpose

            # ここは、そのフォームに入力があった場合にのみ入る。
            # フォームが空なら、q_kwargsは空のままです。
            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

            if queries:
                # filter(Q(...) & Q(...) & Q(...))を動的に行っている。
                base_query = queries.pop()
                for query in queries:
                    base_query &= query
                posts = posts.filter(base_query)

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'blog/post_list-apex.html', context)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
