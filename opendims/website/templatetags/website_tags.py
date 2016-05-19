from django import template
from django.core.exceptions import MultipleObjectsReturned
from django.utils import timezone

from categories.models import Category

from website.models import Post, Welcome, SiteHeader, Partner, Link, Resource

register = template.Library()


@register.simple_tag
def get_siteheaders():
    """
    Return site headers valid for today.
    """
    today = timezone.localtime(timezone.now()).date()
    siteheaders = SiteHeader.objects.filter(
        published=True,
        start__lte=today,
        end__gte=today
    ).order_by('pk')
    return siteheaders


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
        slideshow_enabled=True
    ).exclude(slideshow_image='').order_by('-created')
    return posts


@register.simple_tag
def get_posts_by_category(category):
    """
    Return all posts that are part of the category's tree.
    """
    try:
        category = Category.objects.get(slug=category)
    except MultipleObjectsReturned:
        category = Category.objects.filter(slug=category)[:1]
        category = category[0]
    category_tree = [category]
    if not category.is_leaf_node():
        category_tree = category.get_descendants(include_self=True)
    posts = Post.objects.filter(
        published=True,
        category__in=category_tree
    ).order_by('-created')
    return posts


@register.simple_tag
def get_category_tree(category):
    """
    Return a category's tree structure. Render the tree using recursetree.
    """
    try:
        category = Category.objects.get(slug=category)
    except MultipleObjectsReturned:
        category = Category.objects.filter(slug=category)[:1]
        category = category[0]
    category_tree = category.get_descendants(include_self=True)
    return category_tree


@register.simple_tag
def get_welcomes():
    """
    Return the welcome text.
    """
    welcomes = Welcome.objects.filter(
        published=True
    ).order_by('-created')
    return welcomes


@register.simple_tag
def get_partners():
    partners = Partner.objects.filter(
        published=True
    ).order_by('name')
    return partners


@register.simple_tag
def get_links():
    links = Link.objects.filter(
        published=True
    ).order_by('order')
    return links


@register.simple_tag
def get_resources():
    resources = Resource.objects.filter(
        published=True
    ).order_by('order')
    return resources
