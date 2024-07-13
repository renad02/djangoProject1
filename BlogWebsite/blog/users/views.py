from django.http import HttpResponse

from django.template import loader

from .models import User

from .models import Post

from .models import Comment

from .models import Category

def users(request):
  myusers = User.objects.all().values()
  template = loader.get_template('all_users.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def blogs(request):
  blogs = Post.objects.all().values()
  template = loader.get_template('blogs.html')
  context = {
    'blogs': blogs,
  }
  return HttpResponse(template.render(context, request))


def blogdetails(request, id):
  blog = Post.objects.get(id=id)
  template = loader.get_template('blogdetails.html')
  context = {
    'blog': blog,
  }
  return HttpResponse(template.render(context, request))


def comments(request):
  comments = Comment.objects.all().values()
  template = loader.get_template('comments.html')
  context = {
    'comments': comments,
  }
  return HttpResponse(template.render(context, request))


def categories(request):
  categories = Category.objects.all().values()
  template = loader.get_template('categories.html')
  context = {
    'categories': categories,
  }
  return HttpResponse(template.render(context, request))