# 🗻 Fujisan Travel Agency

[![Django](https://img.shields.io/badge/Framework-Django%204.2-092e20?logo=django)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind%20CSS-38b2ac?logo=tailwind-css)](https://tailwindcss.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)](https://www.postgresql.org/)
[![Vercel](https://img.shields.io/badge/Deployment-Vercel-black?logo=vercel)](https://vercel.com/)
[![Cloudinary](https://img.shields.io/badge/Storage-Cloudinary-3448C5?logo=cloudinary)](https://cloudinary.com/)

A premium, modern travel platform designed to showcase the soul of Japan. This application features a stunning, interactive user interface built with **Django** and **Tailwind CSS**, offering curated travel packages, insightful travel stories, and a seamless cloud-synced experience.

---

## ✨ Premium Features

-   **🏯 Dynamic Japan Explorer**: Curated travel packages with real-time detail updates.
-   **✍️ Professional Blog Engine**: Full Markdown support for immersive travel storytelling.
-   **⛅ Cloud-Native Media**: Automated image hosting via **Cloudinary** for persistent, fast delivery.
-   **💎 State-of-the-Art UI**: Includes Glassmorphism, Dark Mode support, and Scroll-Reveal animations.
-   **🐘 Multi-Cloud DB Ready**: Seamlessly switches between **Render** and **Supabase** PostgreSQL.

## 🛠️ Pro Tech Stack

-   **Backend**: Python 3.12 / Django 4.2
-   **Frontend**: Tailwind CSS 3.x, Alpine.js
-   **Database**: PostgreSQL (Production) / SQLite (Local)
-   **Storage**: Cloudinary (Cloud Media Storage)
-   **Server**: Gunicorn / WhiteNoise (Static serving)

---

## 🚀 Quick Start Guide

### 1. Initialization
```bash
git clone https://github.com/rofik-dyt/fujisan-travel-agency.git
cd fujisan-travel-agency
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Setup
Create a `.env.local` file in the root directory:
```text
SECRET_KEY=your-secure-key
DEBUG=True
DATABASE_URL=postgresql://user:pass@host:port/db
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### 3. Launch
```bash
python manage.py migrate
python manage.py runserver
```
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📦 Cloud Deployment

### Database (Render/Supabase)
1.  Provision a PostgreSQL instance.
2.  Obtain your **Connection URI**. 
3.  Note: Special characters (like `@` or `#`) in passwords must be **URL-encoded**.

### Media Storage (Cloudinary)
1.  Create a free account at [Cloudinary](https://cloudinary.com/).
2.  Provide `CLOUD_NAME`, `API_KEY`, and `API_SECRET` to the environment.
3.  Images will persist across redeploys automatically!

### Web Hosting (Vercel)
1.  Connect your GitHub repository.
2.  Vercel will detect the `vercel.json` and `wsgi.py` automatically.
3.  Add your environment variables in the Vercel Dashboard.

---

## 📄 License
This project is licensed under the MIT License.

---
*Crafted with precision by Antigravity - Advanced Agentic Coding.*
