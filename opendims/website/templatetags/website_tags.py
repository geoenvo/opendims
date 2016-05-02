from django import template

from website.models import Post

register = template.Library()


@register.simple_tag
def get_posts_by_category(post):
    category_posts = Post.objects.filter(category=post.category, published=True).exclude(pk=post.pk).order_by('-created')[:10]
    return category_posts
