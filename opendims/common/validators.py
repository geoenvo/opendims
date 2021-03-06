from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

import magic


@deconstructible
class MimetypeValidator(object):
    def __init__(self, mimetypes):
        self.mimetypes = mimetypes

    def __call__(self, value):
        try:
            mime = magic.from_buffer(value.read(1024), mime=True)
            if mime not in self.mimetypes:
                raise ValidationError(_('Invalid file type.'))
        except AttributeError:
            raise ValidationError(_('Unable to detect the file type.'))


@deconstructible
class FileSizeValidator(object):
    def __init__(self, max_size_mb):
        self.max_size_mb = max_size_mb

    def __call__(self, value):
        if value.file.size > self.max_size_mb * 1024 * 1024:
            raise ValidationError(
                "{}: {} MB".format(_('Maximum file upload size'), self.max_size_mb)
            )
