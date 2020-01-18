import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class TermAcceptance(models.Model):
    """
    Aceite do Termo de privacidade.
    """

    class Meta:
        verbose_name = _('Term of use Acceptance')
        verbose_name_plural = _('Term of use Acceptances')
        ordering = ('-created',)
        unique_together = (('member', 'version'),)

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    term = models.ForeignKey(
        verbose_name=_('privacy policy'),
        to='policy.Term',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='acceptances',
    )
    member = models.UUIDField(
        verbose_name=_('member'),
        db_index=True,
        null=False,
        blank=False,
    )
    version = models.PositiveSmallIntegerField(
        verbose_name=_('version'),
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        verbose_name=_('created'),
        auto_now_add=True,
        editable=False,
    )

    def __repr__(self):
        return '<PrivacyAcceptance pk: {}, version: {}>'.format(self.pk,
                                                                self.version)

    def __str__(self):
        return str(self.member)
