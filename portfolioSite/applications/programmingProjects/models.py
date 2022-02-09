from django.db import models
from django.utils import timezone  # takes timezone settings into account
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from django.urls import reverse

# Create your models here.


# class Tag(models.Model):
#     tag_name = models.CharField(
#         max_length=100,
#         null=True,
#         unique=False,
#         blank=True,
#         verbose_name=_("tag name"),
#         help_text=_("format:  max-100"),
#     )

#     class Meta:
#         ordering = ["tag_name"]

#     def __str__(self):
#         return self.tag


class ProjectCategory(models.Model):
    category_name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        # verbose_name=_("project category"),
        # help_text=_("format: required, max-100"),
    )

    class Meta:
        # verbose_name = _("project category")
        # verbose_name_plural = _("project categories")
        ordering = ["category_name"]


class Project(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        # # verbose_name=_("project title"),
        # help_text=_("format: required, max-100"),
    )

    description = models.TextField(
        unique=False,
        null=False,
        # blank=False,
        # verbose_name=_("project description"),
        # help_text=_("format: required"),
    )

    github = models.URLField(
        max_length=150,
        unique=False,
        null=False,
        blank=True,
        # verbose_name=_("github url"),
        # help_text=_("format: required"),
    )

    website = models.URLField(
        max_length=150,
        unique=False,
        null=False,
        blank=True,
        # verbose_name=_("project website"),
        # help_text=_("format: required"),
    )

    img_url = models.URLField(
        max_length=150,
        unique=False,
        null=False,
        blank=True,
        # verbose_name=_("project image url"),
        # help_text=_("format: required"),
    )

    tags = ArrayField(models.CharField(max_length=35, blank=True))

    project_category = models.ManyToManyField(ProjectCategory)

    date_posted = models.DateTimeField(default=timezone.now)
    # deletes all user's posts with CASCADE
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]

    # added to make easier to understand
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})


# get tags list before
# if removed one of tags
# if tag has no other refs
# delete tag


# @receiver(post_save, sender=Project, dispatch_uid="delete_tags_with_no_project")
# def delete_tags_with_no_project(sender, instance, **kwargs):

# for each tag
# check if tag has other references, if not delete tag
# if not Server.objects.filter(contact=instance.contact):
#     instance.contact.delete()

# @receiver(post_delete, sender=Project, dispatch_uid="delete_tags_with_no_project")
