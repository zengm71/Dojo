from django.shortcuts import render, redirect
from django.contrib import messages
from app_theWall.models import User, UserManager, Comment, CommentManager, Post, PostManager
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/wall')

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/wall')

def logout(request):
    request.session.flush()
    return redirect('/')

def wall(request):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context = {
            'all_posts': Post.objects.all().order_by('created_at').reverse(),
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'wall.html', context)

def createPost(request):
    errors = Post.objects.post_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        user = User.objects.get(id=request.session["user_id"])
        post = Post.objects.create(
            message = request.POST['message'],
            postUser = user
        )
        return redirect('/wall')

def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('/wall')

def createComment(request, post_id):
    errors = Comment.objects.comment_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        user = User.objects.get(id=request.session["user_id"])
        post = Post.objects.get(id=post_id)
        Comment.objects.create(comment = request.POST['comment'], \
            commentUser = user, \
            commentPost = post)
     
        return redirect('/wall')