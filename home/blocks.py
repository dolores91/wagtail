from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


# base
class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        icon = "doc-full"
        label = "Text"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        label = "Image"


class GalleryBlock(blocks.ListBlock):
    def __init__(self, **kwargs):
        super().__init__(ImageChooserBlock(), **kwargs)

    class Meta:
        icon = "image"
        label = "Galery"


class VideoEmbedBlock(EmbedBlock):
    class Meta:
        icon = "media"
        label = "Video"


class DividerBlock(blocks.StaticBlock):
    class Meta:
        icon = "horizontalrule"
        label = "divider"


class CTABlock(blocks.StructBlock):
    text = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_url = blocks.URLBlock()

    class Meta:
        icon = "placeholder"
        label = "call to action"


# estructuras
class TwoColumnsBlock(blocks.StructBlock):
    left = blocks.RichTextBlock()
    right = blocks.RichTextBlock()

    class Meta:
        icon = "grip"
        label = "two columns"


class SectionBlock(blocks.StreamBlock):
    class Meta:
        icon = "folder-open-inverse"
        label = "Container"


# INSTITUCIONALES
class FeatureItemBlock(blocks.StructBlock):
    icon = blocks.CharBlock(required=False)
    title = blocks.CharBlock()
    text = blocks.TextBlock()


class FeaturesBlock(blocks.ListBlock):
    def __init__(self, **kwargs):
        super().__init__(FeatureItemBlock(), **kwargs)

    class Meta:
        icon = "list-ul"
        label = "Features / lists"


class TestimonialBlock(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock()

    class Meta:
        icon = "openquote"
        label = "quotes"


class HighlightBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()

    class Meta:
        icon = "warning"
        label = "Highlight"


# news
class ExternalNewsEmbedBlock(blocks.StructBlock):
    source = blocks.CharBlock(help_text="Fuente (ej: El País)")
    embed = EmbedBlock()
    description = blocks.TextBlock(required=False)

    class Meta:
        icon = "site"
        label = "embed news"


class ExternalNewsListItem(blocks.StructBlock):
    title = blocks.CharBlock()
    url = blocks.URLBlock()
    source = blocks.CharBlock()


class ExternalNewsListBlock(blocks.ListBlock):
    def __init__(self, **kwargs):
        super().__init__(ExternalNewsListItem(), **kwargs)

    class Meta:
        icon = "list-ol"
        label = "list news"


# home
class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    subtitle = blocks.CharBlock(required=False)
    image = ImageChooserBlock()
    cta_text = blocks.CharBlock(required=False)
    cta_url = blocks.URLBlock(required=False)

    class Meta:
        icon = "home"
        label = "Hero"


class FeaturedNewsBlock(blocks.StaticBlock):
    class Meta:
        icon = "doc-full-inverse"
        label = "Highlighted news"
