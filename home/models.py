from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel


class HomePage(Page):
    body = RichTextField(
        blank=True, null=True, features=["bold", "italic", "h2", "h3", "ol", "ul"]
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        # related_name="+",
    )

    content_panels = Page.content_panels + [FieldPanel("body"), FieldPanel("image")]

    template = "home/home_page.html"


# 1. El item individual del menú (un enlace)
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


# 2. El contenedor del menú (ej: "Header", "Footer")
@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, help_text="Identificador único (ej: header-menu)"
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label="Elementos del Menú"),
    ]

    def __str__(self):
        return self.title
