from django.shortcuts import get_object_or_404
from django.views import generic
from django.conf import settings

from categories.models import Category

from .models import Post, Attachment
from .forms import PostSearchForm


class PostListView(generic.ListView):
    paginate_by = settings.ITEMS_PER_PAGE

    def get(self, request, *args, **kwargs):
        """
        Show all posts in a category (including subcategories).
        If category is part of Gallery category tree pass the
        gallery flag to template.
        """
        category_slug = kwargs.pop('category_slug', None)
        self.category = get_object_or_404(
            Category,
            slug=category_slug,
            active=True
        )
        self.category_tree = [self.category]
        if not self.category.is_leaf_node():
            self.category_tree = self.category.get_descendants(include_self=True)
        self.object_list = self.get_queryset()
        gallery_category = get_object_or_404(Category, slug='gallery', active=True)
        gallery_subcategories = gallery_category.get_descendants(include_self=True)
        self.gallery = False
        if self.category in gallery_subcategories:
            self.gallery = True
        context = self.get_context_data(
            object_list=self.object_list,
            category=self.category,
            gallery=self.gallery
        )
        return self.render_to_response(context)

    def get_queryset(self):
        """
        Load all posts in the category tree.
        """
        queryset = Post.objects.filter(category__in=self.category_tree, published=True).order_by('-created')
        return queryset


class PostSearchView(generic.ListView):
    paginate_by = settings.ITEMS_PER_PAGE

    def get(self, request):
        """
        Search case-insensitive post title.
        """
        form = PostSearchForm(self.request.GET or None)
        self.q = None
        if form.is_valid():
            self.q = form.cleaned_data.get('q')
        self.object_list = self.get_queryset()
        context = self.get_context_data(
            object_list=self.object_list,
            search=True,
            form=form,
            q=self.q
        )
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = Post.objects.filter(published=True).order_by('-created')
        if self.q:
            queryset = queryset.filter(title__icontains=self.q)
        return queryset


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        gallery = get_object_or_404(Category, slug='gallery', active=True)
        gallery_subcategories = gallery.get_descendants(include_self=True)
        if post.category in gallery_subcategories:
            context['gallery'] = True
        context['images'] = Attachment.objects.filter(post=post, published=True, file='').exclude(image='')
        context['files'] = Attachment.objects.filter(post=post, published=True, image='').exclude(file='')
        return context
