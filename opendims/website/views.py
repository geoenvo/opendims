from django.shortcuts import get_object_or_404
from django.views import generic
from django.conf import settings

from categories.models import Category

from .models import Post, Attachment


class PostListView(generic.ListView):
    paginate_by = settings.ITEMS_PER_PAGE

    def get_queryset(self):
        """
        Load all posts in the category tree.
        """
        category_slug = self.kwargs.get('category_slug', None)
        category = get_object_or_404(Category, slug=category_slug, active=True)
        category_tree = [category]
        if not category.is_leaf_node():
            category_tree = category.get_descendants(include_self=True)
        queryset = Post.objects.filter(category__in=category_tree).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug', None)
        category = get_object_or_404(Category, slug=category_slug, active=True)
        context['category'] = category
        return context


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['images'] = Attachment.objects.filter(post=self.get_object(), published=True, image__isnull=False, file='')
        context['files'] = Attachment.objects.filter(post=self.get_object(), published=True, file__isnull=False, image='')
        return context
