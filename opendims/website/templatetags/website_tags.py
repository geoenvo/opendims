from django import template

from website.models import Post

register = template.Library()


@register.simple_tag
def get_posts_by_category(post):
    category_posts = Post.objects.filter(
        category=post.category, 
        published=True).exclude(pk=post.pk).order_by('-created')[:10]
    return category_posts

@register.simple_tag
def get_latest_slideshow():
    posts = Post.objects.filter(
        published=True,
        slideshow_enabled=True
    ).order_by('-created')[:8]
    return posts
   
@register.simple_tag
def get_latest_category_post(category):
    posts = Post.objects.filter(
        published=True,
        category__name__iexact=category
    ).order_by('-created')[:4]
    return posts