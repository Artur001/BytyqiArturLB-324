# LB-324 – Tagebuch-App (Flask)

## Beschreibung
Kleine **Tagebuch-App** in **Flask (Python)**.  
Man kann Einträge erfassen und zusätzlich eine **Stimmung (Happiness)** auswählen.  
Getestet mit **pytest**. Qualitätssicherung über **Pre-Commit Hooks** (Black, Pylint, Pytest).  
Git-Workflow mit Branches und Issue-Template.

---

## Installation und Start

```bash
git clone https://github.com/Artur001/BytyqiArturLB-324.git
cd BytyqiArturLB-324

# Virtuelle Umgebung
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux/Mac

# Abhängigkeiten
pip install -r requirements.txt

# App starten
flask run
```
Die App läuft unter: http://127.0.0.1:5000

## Tests ausführen

```bash
pytest -v
```

Die Tests prüfen u. a., ob ein Eintrag mit **Happiness** gespeichert/angezeigt wird.

---

## Git-Workflow

* `main` → stabile Version
* `dev` → Entwicklungs-Branch
* `feature/add-happiness` → neue Funktion (Happiness-Feld)

**Pre-Commit Hooks** (bei Commit/Push automatisch):

* **Black** – Formatierung
* **Pylint** – Linting
* **Pytest** – Tests

---

## Issues & Templates

* Issue-Template liegt unter `.github/ISSUE_TEMPLATE/issue.md`.

---

## Screenshots

Alle relevanten Screenshots (Branches, laufende App, Tests, Issues, Hooks) sind im **Lösungsdokument** enthalten.
