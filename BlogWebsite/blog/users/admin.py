from django.contrib import admin

from .models import User

from .models import Post

from .models import Comment

from .models import Category




class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "username", "email", "password",)


admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display2 = ("post_id", "title", "content", "category", "date published")


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display3 = ("comment_id", "id_post", "id_user", "content ", "date_posted")


admin.site.register(Comment, CommentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display4 = ("id_category", "name_category")


admin.site.register(Category, CategoryAdmin)
