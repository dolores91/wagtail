Perfect — here is your **updated README in English**, reflecting the new block architecture and page structure.

---

# 🦅 Wagtail CMS Project – Developer Guide

This project is built with **Django + Wagtail CMS**.

Unlike traditional Django projects, content here is:

* Hierarchical (Page Tree)
* Component-based (StreamField Blocks)
* Fully editable through the Wagtail Admin

The structure is designed to give editors flexibility **without breaking design consistency**.

---

# 🚀 1. Installation & Running

## Setup locally

```bash
# 1. Activate virtual environment (Windows)
.\mysiteenv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations (ALWAYS after changing models.py)
python manage.py makemigrations
python manage.py migrate

# 4. Create superuser
python manage.py createsuperuser

# 5. Run server
python manage.py runserver
```

Frontend:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Admin Panel:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

# 🧱 2. Content Architecture (StreamField Blocks)

The project uses a structured block system divided into categories.

This prevents design chaos while keeping content flexible.

---

## 🧱 BASE BLOCKS (Reusable)

👉 Available in `StandardPage`
👉 Some also available in `HomePage`

---

# 📄 3. Page Models & Allowed Blocks

Block availability is intentionally restricted per page type.

---

## 🏠 HomePage

**Goal:** Impact, navigation, conversions

Allowed blocks:

* `HeroBlock`
* `HighlightBlock`
* `FeaturedServicesBlock`
* `FeaturedNewsBlock`
* `CTABlock`
* `DividerBlock`

Not allowed:

* Free embeds
* Long unstructured text

---

## 📄 StandardPage

**Goal:** Flexible structured content

Allowed blocks:

* `RichTextBlock`
* `ImageBlock`
* `GalleryBlock`
* `VideoEmbedBlock`
* `TwoColumnsBlock`
* `FeaturesBlock`
* `TestimonialBlock`
* `HighlightBlock`
* `CTABlock`
* `DividerBlock`
* `SectionBlock`

Used for:

* About us
* Services
* Contact (text + CTA to form)

---

## 📰 News Page (Specialized StandardPage)

News content is external and curated.

Use a restricted block set:

Allowed:

* `ExternalNewsEmbedBlock`
* `ExternalNewsListBlock`
* `RichTextBlock` (intro only)
* `HighlightBlock`
* `DividerBlock`

Editors curate — no direct article writing.

---

## 🔍 Search Page

* No StreamField
* Not editable
* Functional only

---

# 🎨 4. Template Cheatsheet

Always load:

```html
{% load static wagtailcore_tags wagtailimages_tags %}
```

---

### Displaying Rich Text

```html
{{ page.body|richtext }}
```

---

### Displaying Images

```html
{% image page.main_image original %}
{% image page.main_image fill-300x300 %}
{% image page.main_image width-500 %}
```

---

### Internal Page Links

```html
<a href="{% pageurl page.link_page %}">Go to page</a>
```

---

# 🍔 5. Menu Management (Snippets)

Admin Panel → Snippets → Menus

In `base.html`:

* `header` (main navigation)
* `footer` (footer menu)


# 🛠 6. Common Troubleshooting

### Invalid filter: 'richtext'

You forgot:

```html
{% load wagtailcore_tags %}
```

---

### Images not loading

Ensure `urls.py` serves media in DEBUG:

```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### 404 After Creating a Page

* Is it Published?
* Is the Home page assigned in Settings → Sites?

---

# 📦 7. Styles

The project uses **Bootstrap 5 via CDN**.

Custom styles should extend Bootstrap rather than override core layout behavior.


