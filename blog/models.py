from django.db import models
from django.core.exceptions import ValidationError
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import TextBlock
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

class BlogIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogDetail']

    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['blog_post'] = BlogDetail.objects.live().public()
        return context

class BlogPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'blog.BlogDetail',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

class BlogDetail(Page):
    parent_page_types = ['blog.BlogIndex']
    subpage_types = []

    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    body = StreamField(
        [
            ('text', TextBlock()),
            ('image', ImageChooserBlock()),
        ],
        block_counts={
            'text': {'min_num':1},
            'image': {'max_num':2},
        },
        use_json_field=True,
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('tags'),
    ]