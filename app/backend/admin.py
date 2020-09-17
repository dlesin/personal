from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Department


class UserCreationForm(forms.ModelForm):
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    search_fields = ('last_name', 'first_name',)
    list_display = ('last_name', 'first_name', 'department',)
    ordering = ('last_name',)
    readonly_fields = ('image_tag',)
    fieldsets = (
        (_('User'), {
            'classes': ('wide',),
            'fields': ('last_name', 'first_name', 'password', 'email', 'department')}),
        (_('Other'), {
            'classes': ('wide',),
            'fields': ('avatar', 'image_tag', 'description', 'is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (_('Create User'), {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'password', 'department')}
         ),
        (_('Other information'), {
            'classes': ('wide',),
            'fields': ('is_superuser', 'is_staff', 'is_active', 'is_teamlead', 'is_director', 'avatar', 'description')}
         ),
    )


admin.site.register(Department)
admin.site.register(User, UserAdmin)
