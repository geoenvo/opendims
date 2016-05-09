from django import template

from categories.models import Category

from website.models import Post

register = template.Library()


@register.simple_tag
def get_similar_posts(post):
    """
    Return all posts belonging in the same category.
    """
    category_posts = Post.objects.filter(
        category=post.category,
        published=True
    ).exclude(pk=post.pk).order_by('-created')
    return category_posts


@register.simple_tag
def get_slideshow_posts():
    """
    Return posts that have slideshow images.
    """
    posts = Post.objects.filter(
        published=True,
        slideshow_enabled=True,
        slideshow_image__isnull=False
    ).order_by('-created')
    return posts


@register.simple_tag
def get_posts_by_category(category):
    """
    Return all posts that are part of the category's tree.
    """
    category = Category.objects.get(slug=category)
    category_tree = [category]
    if not category.is_leaf_node():
        category_tree = category.get_descendants(include_self=True)
    posts = Post.objects.filter(
        published=True,
        category__in=category_tree
    ).order_by('-created')
    return posts
