from __future__ import unicode_literals

from django.core import urlresolvers
from django.db import models


class CommonAbstractModel(models.Model):
    class Meta:
        abstract = True
    
    def get_admin_url(self):
        return urlresolvers.reverse(
            'admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=(self.id,)
        )
