
from categories.models import CategoryBase


class Galery(CategoryBase):
    # add extra fields, like images, "featured" and such here
    pass

    class Meta:
        verbose_name_plural = 'galeries'


class News(CategoryBase):
    # add extra fields, like images, "featured" and such here
    pass

    class Meta:
        verbose_name_plural = 'news'


class E_Library(CategoryBase):
    # add extra fields, like images, "featured" and such here
    pass

    class Meta:
        verbose_name_plural = 'elibraries'


"""
class MusicCategory(CategoryBase):
    # add extra fields, like images, "featured" and such here
    pass

class Artist(CategoryBase):
    name       = models.CharField(max_length=255,)
    categories = models.ManyToManyField(MusicCategory, related_name="artists")

    def __unicode__(self):
        return self.name

class Song(models.Model):
    slug        = AutoSlugField(populate_from='title', unique=True)
    title       = models.CharField(max_length=255,)
    artist      = models.ForeignKey(Artist, related_name="songs", on_delete=models.PROTECT)
    categories  = models.ManyToManyField(MusicCategory, related_name="songs")
    description = models.TextField()

    def __unicode__(self):
        return self.title
"""
