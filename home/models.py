from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from . import blocks
from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import StreamField
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


# HOME
class HomePage(Page):
    body = StreamField(
        [
            ("hero", blocks.HeroBlock()),
            ("highlight", blocks.HighlightBlock()),
            ("featured_news", blocks.FeaturedNewsBlock()),
            ("cta", blocks.CTABlock()),
            ("divider", blocks.DividerBlock()),
        ],
        use_json_field=True,
        blank=True,
        default=list,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    subpage_types = ["home.StandardPage"]


# Standard page
class StandardPage(Page):
    intro = models.CharField(max_length=250, blank=True)

    body = StreamField(
        [
            ("text", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("gallery", blocks.GalleryBlock()),
            ("video", blocks.VideoEmbedBlock()),
            ("two_columns", blocks.TwoColumnsBlock()),
            ("features", blocks.FeaturesBlock()),
            ("testimonial", blocks.TestimonialBlock()),
            ("highlight", blocks.HighlightBlock()),
            ("cta", blocks.CTABlock()),
            ("divider", blocks.DividerBlock()),
            ("section", blocks.SectionBlock()),
        ],
        use_json_field=True,
        blank=True,
        default=list,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []


# SNIPPETS
# menu item
class MenuItem(Orderable):
    menu = ParentalKey("Menu", related_name="menu_items", on_delete=models.CASCADE)
    link_title = models.CharField(
        max_length=50, blank=True, help_text="Texto del enlace"
    )
    link_url = models.CharField(
        max_length=500, blank=True, help_text="URL externa (ej: https://google.com)"
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
        help_text="O selecciona una página interna",
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url

    @property
    def title(self):
        if self.link_title:
            return self.link_title
        if self.link_page:
            return self.link_page.title
        return "Sin título"


# menu container
@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Id")

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label="Menu items"),
    ]

    def __str__(self):
        return self.title
