from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text, extensions=['extra', 'sane_lists']))

@register.filter(name='markdown_snippet')
def markdown_snippet(text):
    """Converts markdown to HTML and strips all tags for a clean preview."""
    from django.utils.html import strip_tags
    html = markdown.markdown(text)
    return strip_tags(html)
