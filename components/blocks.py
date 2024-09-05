from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class TextBlock(blocks.TextBlock):
    def  __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            help_text="Enter text in this block",
            max_length=5,
            min_length=2,
            required=False,
        )
    class Meta:
        # template = "components/text_block.html"
        ...

class InfoBlock(blocks.StaticBlock):
    class Meta:
        # template = "components/info_block.html"
        admin_text = "ini namanya info block"
        label = "Info"

class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock()
    answer = blocks.RichTextBlock(
        features=['bold', 'italic']
    )
class FAQListBlock(blocks.ListBlock):
    def __init__(self, **kwargs):
        super().__init__(FAQBlock(), **kwargs,)
    class Meta:
        # template = "components/faq_list_block.html"
        min_num = 1
        max_num = 5
        label = "FAQ"

class CarouselBlock(blocks.StreamBlock):
    image = ImageChooserBlock()
    quotation = blocks.StreamBlock([
        ('text', blocks.TextBlock()),
        ('author', blocks.CharBlock()),
    ])
    class Meta:
        # template = "components/carousel_block.html"
        label = "Carousel"

class CallToAction1Block(blocks.StructBlock):
    text = blocks.RichTextBlock(
        features=['bold', 'italic'],
        required=True,
    )
    page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock(
        max_length=100,
        required=False
    )
    class Meta:
        # template = "components/call_to_action_1_block.html"
        label = "CTA #1"
        
class ImageBlock(ImageChooserBlock):
    class Meta:
        # template = "components/image_block.html"
        ...