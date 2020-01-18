from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from . import models


class TermAdminForm(forms.ModelForm):
    class Meta:
        model = models.Term
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class PrivacyAdminForm(forms.ModelForm):
    class Meta:
        model = models.Privacy
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


@admin.register(models.Term)
class TermAdmin(admin.ModelAdmin):
    form = TermAdminForm
    list_display = [
        'version',
        'created',
        'last_updated',
    ]
    readonly_fields = [
        'created',
        'last_updated',
        'pk',
    ]

    def get_changeform_initial_data(self, request):
        initial = dict()

        last_term = models.Term.objects.order_by('created').last()
        if last_term and last_term.version:
            initial['version'] = last_term.version + 1

        return initial


@admin.register(models.Privacy)
class TermAdmin(admin.ModelAdmin):
    form = PrivacyAdminForm
    list_display = [
        'version',
        'created',
        'last_updated',
    ]
    readonly_fields = [
        'created',
        'last_updated',
        'pk',
    ]

    def get_changeform_initial_data(self, request):
        initial = dict()

        last_term = models.Privacy.objects.order_by('created').last()
        if last_term and last_term.version:
            initial['version'] = last_term.version + 1

        return initial


@admin.register(models.PrivacyAcceptance)
class PrivacyAcceptanceAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'version',
        'created',
    ]
    readonly_fields = (
        'pk',
        'privacy',
        'member',
        'version',
    )
    list_filter = ('version',)
    search_fields = ('member',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.TermAcceptance)
class TermAcceptanceAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'version',
        'created',
    ]
    readonly_fields = (
        'pk',
        'term',
        'member',
        'version',
    )
    list_filter = ('version',)
    search_fields = ('member',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
