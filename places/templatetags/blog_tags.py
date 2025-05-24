from django.template import Library

from ..models import Category

register = Library()


@register.simple_tag
def get_categories():
    return Category.objects.filter(is_active=True, parent__isnull=False).prefetch_related('childs')
