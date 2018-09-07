from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static
from django.template.defaultfilters import truncatechars
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from wagtail_tag_manager.models import Tag, Trigger, Constant, Variable


class ConstantModelAdmin(ModelAdmin):
    model = Constant
    menu_icon = 'snippet'
    list_display = ('name_display', 'key', 'value',)
    search_fields = ('name', 'key', 'value', 'description',)

    def name_display(self, obj):
        if obj.description:
            description = truncatechars(obj.description, 64)
            return mark_safe(f"{obj.name}<br/><small>{description}</small>")
        return obj.name
    name_display.short_description = _('Name')


class VariableModelAdmin(ModelAdmin):
    model = Variable
    menu_icon = 'snippet'
    list_display = ('name_display', 'key', 'variable_type',)
    list_filter = ('variable_type',)
    search_fields = ('name', 'key', 'description',)
    form_view_extra_js = [static('variable_form_view.bundle.js')]

    def name_display(self, obj):
        if obj.description:
            description = truncatechars(obj.description, 64)
            return mark_safe(f"{obj.name}<br/><small>{description}</small>")
        return obj.name
    name_display.short_description = _('Name')


class TagModelAdmin(ModelAdmin):
    model = Tag
    menu_icon = 'code'
    list_display = (
        'name_display', 'tag_type', 'tag_location', 'tag_loading', 'active',)
    list_filter = ('active', 'tag_type', 'tag_location', 'tag_loading',)
    search_fields = ('name', 'description', 'content',)
    form_view_extra_js = [static('tag_form_view.bundle.js')]

    def name_display(self, obj):
        if obj.description:
            description = truncatechars(obj.description, 64)
            return mark_safe(f"{obj.name}<br/><small>{description}</small>")
        return obj.name
    name_display.short_description = _('Name')


class TriggerModelAdmin(ModelAdmin):
    model = Trigger
    menu_icon = 'media'
    list_display = ('name_display', 'tags_count', 'active',)
    list_filter = ('active',)
    search_fields = ('name', 'description',)

    def name_display(self, obj):
        if obj.description:
            description = truncatechars(obj.description, 64)
            return mark_safe(f"{obj.name}<br/><small>{description}</small>")
        return obj.name
    name_display.short_description = _('Name')

    def tags_count(self, obj):
        return f"{obj.tags.count()} tag(s)"
    tags_count.short_description = _('Tags')


class TagManagerAdminGroup(ModelAdminGroup):
    menu_label = _("Tag Manager")
    menu_icon = 'code'
    menu_order = 640
    items = (
        TagModelAdmin, ConstantModelAdmin, VariableModelAdmin,
        TriggerModelAdmin)


modeladmin_register(TagManagerAdminGroup)
