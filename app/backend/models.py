from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class Department(models.Model):
    name = models.CharField(_('department'), max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('departments')
        verbose_name_plural = _('departments')


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=256, null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    description = models.CharField(_('description'), max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department, related_name='user_department', on_delete=models.SET_NULL, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active status'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=True)
    is_teamlead = models.BooleanField(_('lead status'), default=False)
    is_director = models.BooleanField(_('director status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    def get_short_name(self):
        return self.first_name

    def image_tag(self):
        if self.avatar:
            return mark_safe(f'<img src="{settings.MEDIA_URL}{self.avatar}" width="64px" height="64px"/>')
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
