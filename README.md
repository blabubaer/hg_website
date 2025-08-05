# Herbert & Gransow - Planung GmbH Website

Eine moderne, professionelle Website für das Ingenieurbüro Herbert & Gransow - Planung GmbH, spezialisiert auf Technische Gebäudeausrüstung und Elektrotechnik.

## Features

- **Moderne, responsive Design** mit Bootstrap 5
- **Admin-Panel** für einfache Verwaltung von Projekten und Kontaktanfragen
- **Projekt/Referenzen-Verwaltung** mit Bildergalerie
- **Kontaktformular** mit E-Mail-Benachrichtigung
- **SEO-optimiert** und schnell ladend
- **Deployment-ready** für Render, Railway oder andere Hosting-Plattformen

## Technologie-Stack

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5, Font Awesome
- **Datenbank**: SQLite (Development), PostgreSQL (Production)
- **Deployment**: Render (Free Tier)

## Lokale Entwicklung

### Voraussetzungen

- Python 3.8+
- uv (Python Package Manager)

### Installation

1. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd hg_website
   ```

2. **Dependencies installieren**
   ```bash
   uv sync
   ```

3. **Umgebungsvariablen konfigurieren**
   ```bash
   cp env.example .env
   # Bearbeiten Sie .env mit Ihren Einstellungen
   ```

4. **Datenbank migrieren**
   ```bash
   uv run python manage.py migrate
   ```

5. **Superuser erstellen**
   ```bash
   uv run python manage.py createsuperuser
   ```

6. **Entwicklungsserver starten**
   ```bash
   uv run python manage.py runserver
   ```

Die Website ist dann unter `http://localhost:8000` verfügbar.

## Admin-Panel

Das Admin-Panel ist unter `http://localhost:8000/admin` verfügbar und bietet:

- **Projektverwaltung**: Projekte hinzufügen, bearbeiten, kategorisieren
- **Bildverwaltung**: Bilder zu Projekten hochladen und verwalten
- **Kontaktanfragen**: Eingehende Nachrichten verwalten und als gelesen/beantwortet markieren
- **Benutzerfreundlich**: Einfach zu bedienen für nicht-technische Benutzer

## Deployment auf Render

### 1. Render Account erstellen
- Gehen Sie zu [render.com](https://render.com)
- Erstellen Sie ein kostenloses Konto

### 2. Neues Web Service erstellen
- Klicken Sie auf "New +" → "Web Service"
- Verbinden Sie Ihr GitHub Repository

### 3. Konfiguration
- **Name**: `hg-website` (oder gewünschter Name)
- **Environment**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn hg_website.wsgi:application`

### 4. Environment Variables setzen
Fügen Sie folgende Umgebungsvariablen hinzu:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Deploy
- Klicken Sie auf "Create Web Service"
- Render wird automatisch deployen

## E-Mail-Konfiguration

Für das Kontaktformular benötigen Sie E-Mail-Einstellungen:

### Gmail (Empfohlen)
1. 2-Faktor-Authentifizierung aktivieren
2. App-Passwort generieren
3. In `.env` eintragen:
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

## Projektstruktur

```
hg_website/
├── core/                 # Haupt-App (Home, About, Services)
├── projects/            # Projekt/Referenzen-Verwaltung
├── contact/             # Kontaktformular
├── templates/           # HTML-Templates
├── static/              # Statische Dateien (CSS, JS, Bilder)
├── media/               # Hochgeladene Dateien
├── requirements.txt     # Python-Dependencies
├── build.sh            # Render Build-Script
└── manage.py           # Django Management
```

## Anpassungen

### Design anpassen
- Bearbeiten Sie `templates/base.html` für das Hauptdesign
- CSS-Variablen in `templates/base.html` für Farben
- Bootstrap 5 Klassen für Layout

### Inhalte anpassen
- Texte in `templates/core/` bearbeiten
- Kontaktdaten in `templates/base.html` und `templates/contact/contact.html`
- Firmeninformationen in `templates/core/home.html`

### Neue Features hinzufügen
- Django Apps in `INSTALLED_APPS` registrieren
- Models in `models.py` definieren
- Views in `views.py` erstellen
- Templates in entsprechenden Ordnern

## Support

Bei Fragen oder Problemen:
- GitHub Issues erstellen
- Dokumentation: [Django Docs](https://docs.djangoproject.com/)
- Bootstrap: [Bootstrap Docs](https://getbootstrap.com/docs/)

## Lizenz

Dieses Projekt ist für Herbert & Gransow - Planung GmbH erstellt.
