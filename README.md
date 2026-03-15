
# 📚 Minimal Blogging Platform (Django + PostgreSQL)

A clean, writing-focused blogging platform built with **Django, PostgreSQL, and Tailwind CSS**, designed to provide a **minimal and distraction-free reading experience** inspired by long-form essay blogs.

The project demonstrates how to build a **content-driven web application** with clean architecture, SEO-friendly URLs, and dynamic article rendering.

---

# 🚀 Features

* Dynamic article management with **PostgreSQL**
* **SEO-friendly slug URLs**
* Clean **long-form reading layout**
* **Create / Edit / Delete articles** (authenticated users)
* **Responsive UI** built with Tailwind CSS
* **Open Graph metadata** for social sharing
* Native **share and copy link functionality**
* Drop-cap typography for article readability

---

# 🏗 Project Architecture

```
Browser
   │
   │ HTTP Request
   ▼
Django URL Router
   │
   ▼
Views (Business Logic)
   │
   ▼
Django ORM
   │
   ▼
PostgreSQL Database
   │
   ▼
Templates (HTML + Tailwind CSS)
   │
   ▼
Rendered Web Page
```

### Architecture Principles

* **Separation of concerns**
* **Clean template rendering**
* **Database-driven content**
* **SEO-friendly routing**

---

# 📂 Project Structure

```
blog_project/
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── posts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
│   ├── article.html
│   ├── detail_page.html
│   ├── edit_article.html
│   └── delete_article.html
│
├── static/
│
├── manage.py
│
└── requirements.txt
```

---

# 🧱 Database Schema

### Article Table

| Field          | Type    | Description                |
| -------------- | ------- | -------------------------- |
| id             | Integer | Primary key                |
| slug           | Slug    | SEO-friendly article URL   |
| title          | Text    | Article title              |
| body           | Text    | Plain text article content |
| image          | Text    | Article preview image      |
| author         | String  | Author name                |
| handle         | String  | Author handle              |
| published_date | Date    | Publish date               |

Example Django model:

```python
class Article(models.Model):
    slug = models.SlugField(unique=True)
    title = models.TextField()
    body = models.TextField()
    image = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100)
    handle = models.CharField(max_length=50)
    published_date = models.DateField()
```

---

# 🔗 URL Structure

| Page           | URL                       |
| -------------- | ------------------------- |
| Homepage       | `/`                       |
| Article page   | `/article/my-first-blog/` |
| Edit article   | `/article/edit/1/`        |
| Delete article | `/article/delete/1/`      |

Slug URLs improve **SEO and shareability**.

---

# ⚙️ Installation Guide

### 1️⃣ Clone the repository

```bash
git clone https://github.com/RahulPal-rhine/SEO-Friendly-Blogging-Platform-with-Django-PostgreSQL.git
cd blog
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv myenv
```

Activate environment:

Windows

```
myenv\Scripts\activate
```

Mac/Linux

```
source myenv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure PostgreSQL

Update database settings in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 5️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create superuser

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

# 🧠 Key Concepts Demonstrated

* Django ORM database integration
* Slug-based routing for SEO
* Template-based content rendering
* Authentication-protected admin actions
* Dynamic content management
* Secure HTML rendering

---

# 🔒 Security Considerations

* Article body stored as **plain text**
* HTML formatting handled in templates
* Avoids unsafe HTML rendering
* Prevents XSS vulnerabilities

---

# 📈 Future Improvements

Planned enhancements:

* Article search
* Pagination
* Markdown editor
* Reading progress bar
* Previous / next article navigation
* Comment system
* RSS feed
* Tagging system
* Rich text editor
* Image upload system

---

# 💻 Tech Stack

Backend

* Python
* Django
* PostgreSQL

Frontend

* HTML
* Tailwind CSS
* JavaScript

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 🤝 Contributions

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

