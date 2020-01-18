import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Privacy(models.Model):
    """
    Política de privacidade a ser aceito.
    """

    class Meta:
        verbose_name = _('Privacy Policy')
        verbose_name_plural = _('Privacy Policies')
        ordering = ('-created',)

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    content = models.TextField(
        verbose_name=_('content'),
        null=False,
        blank=False,
    )
    version = models.PositiveSmallIntegerField(
        verbose_name=_('version'),
        unique=True,
        default=1,
        null=False,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name=_('created'),
        auto_now_add=True,
        editable=False,
    )
    last_updated = models.DateTimeField(
        verbose_name=_('last updated'),
        auto_now=True,
        editable=False,
    )

    def __repr__(self):
        return '<Privacy pk: {}, version: {}>'.format(self.pk, self.version)

    def __str__(self):
        return str(self.version)
