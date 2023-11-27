# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Warehouse(models.Model):

    #__Warehouse_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    #__Warehouse_FIELDS__END

    class Meta:
        verbose_name        = _("Warehouse")
        verbose_name_plural = _("Warehouse")


class Shelf(models.Model):

    #__Shelf_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    warehouse = models.CharField(max_length=255, null=True, blank=True)
    max_capacity = models.CharField(max_length=255, null=True, blank=True)
    current_capacity = models.CharField(max_length=255, null=True, blank=True)

    #__Shelf_FIELDS__END

    class Meta:
        verbose_name        = _("Shelf")
        verbose_name_plural = _("Shelf")


class Glasstype(models.Model):

    #__Glasstype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    height = models.CharField(max_length=255, null=True, blank=True)
    width = models.CharField(max_length=255, null=True, blank=True)
    thickness = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)

    #__Glasstype_FIELDS__END

    class Meta:
        verbose_name        = _("Glasstype")
        verbose_name_plural = _("Glasstype")


class Glassremoval(models.Model):

    #__Glassremoval_FIELDS__
    glass_on_shelf = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Glassremoval_FIELDS__END

    class Meta:
        verbose_name        = _("Glassremoval")
        verbose_name_plural = _("Glassremoval")


class Glassmovement(models.Model):

    #__Glassmovement_FIELDS__
    glass_on_shelf = models.CharField(max_length=255, null=True, blank=True)
    from_shelf = models.CharField(max_length=255, null=True, blank=True)
    to_shelf = models.CharField(max_length=255, null=True, blank=True)

    #__Glassmovement_FIELDS__END

    class Meta:
        verbose_name        = _("Glassmovement")
        verbose_name_plural = _("Glassmovement")


class Glassonshelf(models.Model):

    #__Glassonshelf_FIELDS__
    glas_type = models.CharField(max_length=255, null=True, blank=True)
    szelf = models.CharField(max_length=255, null=True, blank=True)
    order_on_shelf = models.CharField(max_length=255, null=True, blank=True)
    is_spacer = models.CharField(max_length=255, null=True, blank=True)

    #__Glassonshelf_FIELDS__END

    class Meta:
        verbose_name        = _("Glassonshelf")
        verbose_name_plural = _("Glassonshelf")


class Activity(models.Model):

    #__Activity_FIELDS__
    activity_type = models.CharField(max_length=255, null=True, blank=True)
    glass_on_shelf = models.CharField(max_length=255, null=True, blank=True)
    shelf = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)

    #__Activity_FIELDS__END

    class Meta:
        verbose_name        = _("Activity")
        verbose_name_plural = _("Activity")



#__MODELS__END
