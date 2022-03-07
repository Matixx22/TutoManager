# Tuto Manager

Tuto Manager is a Django app that helps you manage your tutoring income.

## Quick start

1. Run ``git clone https://github.com/Matixx22/TutoManager.git`` to clone repository and enter into it.

2. (Optional) Create a virtual evironment ex. ``python -m venv venv`` and activate it ex. ``venv/Scripts/activate``

3. Run  ``pip install -r requirements.txt`` to install requirements

2. Run following commands:
   ```bash 
   python manage.py makemigrations
   python manage.py sqlmigrate TutoManager 0001
   python manage.py migrate
   ```

3. Run ``python manage.py runserver`` to run server on localhost.

4. Visit http://127.0.0.1:8000 to see te web app.

