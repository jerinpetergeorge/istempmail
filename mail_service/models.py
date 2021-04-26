from django.db import models

from accounts.models import User


class AbstractDomain(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.name = self.name.lower()
        super().save(**kwargs)


class BlackListDomain(AbstractDomain):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="blacklist_domains",
        related_query_name="blacklist_domain",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "BlackList Domain"
        verbose_name_plural = "BlackList Domains"


class WhiteListDomain(AbstractDomain):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="whitelist_domains",
        related_query_name="whitelist_domain",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "WhiteList Domain"
        verbose_name_plural = "WhiteList Domains"
