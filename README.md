# Student Records CRUD (Django + HTML)

## Run in VS Code
1. Open this folder in VS Code (File > Open Folder), then open the terminal (Ctrl + `).
2. Create and activate a virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - Mac/Linux: `python3 -m venv venv` then `source venv/bin/activate`
3. Install Django: `pip install -r requirements.txt`
4. Create the database: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
6. Open http://127.0.0.1:8000/ in your browser.

## Operations
- Create: click "Add Student"
- Read: the home page lists all students
- Update: click "Edit" on a row
- Delete: click "Delete" on a row, then confirm

## Submission (GitHub)
Take screenshots of each operation and save them in a `screenshots/` folder, then:
```
git add .
git commit -m "Student CRUD app with Django"
git push origin main
```
Submit your forked repository URL.
