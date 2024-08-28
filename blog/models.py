from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class BlogIndex(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]
    
class BlogDetail(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]