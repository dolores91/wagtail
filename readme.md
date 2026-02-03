🦅 Wagtail CMS Project - Developer Guide
This project is built with Django and Wagtail CMS. Unlike traditional Django, content here is hierarchical (Page Tree) and highly editable via the administration panel.

🚀 1. Installation & Running
To set up the project in your local environment:

Bash
## 1. Activate virtual environment (Windows)
.\mysiteenv\Scripts\activate

## 2. Install dependencies
pip install -r requirements.txt

## 3. Apply migrations (ALWAYS do this after changing models.py)
python manage.py makemigrations
python manage.py migrate

## 4. Create superuser 
python manage.py createsuperuser

# 5. Run the server
python manage.py runserver
Frontend: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

📄 2. How to Create New Pages (Models)
In Wagtail, every "Page Type" (Home, Blog, Contact) is defined as a model in models.py.

Step A: Define the Model (home/models.py)
Python
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class BlogPage(Page):
    # 1. Database fields
    date = models.DateField("Post Date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    
    # 2. Editor panels (Admin interface)
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
    
    # 3. (Optional) Specific template. 
    # By default, it looks for: home/templates/home/blog_page.html
    template = "home/blog_page.html"

🎨 3. Templates Cheatsheet (HTML)
To display content, Wagtail uses specific tags. Always load these at the top of your HTML file:

    HTML
    {% load static wagtailcore_tags wagtailimages_tags %}
    Displaying Text
    HTML
    <h1>{{ page.title }}</h1>

    <div class="content">
        {{ page.body|richtext }}
    </div>
    Displaying Images
    Do not use {{ page.image }} directly. Use the {% image %} tag:

    HTML
    {% image page.main_image original %}

    {% image page.main_image fill-300x300 class="img-fluid rounded" %}

    {% image page.main_image width-500 %}
    Links to internal pages
    If you have a field linking to another internal page (PageChooserBlock or ForeignKey):

    HTML
    <a href="{% pageurl page.link_page %}">Go to page</a>

🍔 4. Menu Management (Snippets)

In the Admin Panel:
Go to Snippets > Menus.

Create/Edit a menu.

IMPORTANT: The slug must be header (for the main menu) or footer (for the footer).

In the Code (base.html):
We use our custom tag navigation_tags.

    HTML
    {% load navigation_tags %}

    {% get_menu "header" as nav_menu %}

    {% if nav_menu %}
    <ul>
        {% for item in nav_menu.menu_items.all %}
        <li>
            <a href="{{ item.link }}" class="{% if request.path == item.link %}active{% endif %}">
                {{ item.title }}
            </a>
        </li>
        {% endfor %}
    </ul>
    {% endif %}
🛠 5. Common Troubleshooting

"TemplateSyntaxError: Invalid filter: 'richtext'"
Solution: You forgot to add {% load wagtailcore_tags %} at the top of your HTML file.

"Images are broken / not loading"
Solution: Ensure that your urls.py (project level) is configured to serve static media files in debug mode:

Python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"I created a page but get a 404 Error"
Solution:

Is the page Published? (Check "Publish" vs "Save Draft").

If it's the Home page, verify in Settings > Sites that it is assigned as the Root page for localhost (port 8000).

📦 6. Styles

The project uses Bootstrap 5 via CDN.
