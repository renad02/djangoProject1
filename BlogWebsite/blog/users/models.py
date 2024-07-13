
from django.db import models


class User(models.Model):
  user_id = models.SmallIntegerField(null=True)
  username = models.CharField(max_length=250)
  email = models.EmailField(null=True)
  password = models.TextField(null=True)


  def __str__(self):
    return f"{self.user_id} "


class Post(models.Model):
  post_id = models.SmallIntegerField(null=True)
  title = models.CharField(max_length=250)
  content = models.TextField(null=True)
  category = models.CharField(max_length=250)
  date_published = models.DateTimeField(null=True)

  def __str__(self):
    return f"{self.post_id} "


class Comment(models.Model):
  comment_id = models.SmallIntegerField(null=True)
  id_post = models.ForeignKey("Post", on_delete=models.CASCADE)
  id_user = models.ForeignKey("User", on_delete=models.CASCADE)
  content_c = models.TextField(null=True)
  date_posted = models.DateTimeField(null=True)




class Category(models.Model):
  id_category = models.SmallIntegerField(null=True)
  name_category = models.CharField(max_length=250)

