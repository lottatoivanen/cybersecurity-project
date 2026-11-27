# Cyber Security Base project

This web application is made for Cyber Security Base course as a project. It works as a note taking app for small notes, reminders or todos.
The application contains two premade test users.

### Security Warning 

This app is _intentionally_ insecure made for a course project. Do not deploy it.
The SECRET_KEY in settings.py is a throwaway development key (flaw A05).

## Intentional Security Flaws

All of the security flaws in this application are taken from the [OWASP Top 10 (2021)](https://top10.owasp.org/2021/).
Each vulnerability is documented in the source code, alongside comments explaining how it could be fixed.

The implemented vulnerabilities include:
- [A01 Broken Access Control](https://top10.owasp.org/2021/A01_2021-Broken_Access_Control/)
- [A02 Cryptographic Failures](https://top10.owasp.org/2021/A02_2021-Cryptographic_Failures/)
- [A03 Injection](https://top10.owasp.org/2021/A03_2021-Injection/)
- [A05 Security Misconfiguration](https://top10.owasp.org/2021/A05_2021-Security_Misconfiguration/)
- [A07 Identification and Authentication Failures](https://top10.owasp.org/2021/A07_2021-Identification_and_Authentication_Failures/)

## Installation and Launch

This application was made using the [starter website instructions](https://docs.djangoproject.com/en/6.1/intro/tutorial01/) for Django version 6.1 and Python 3.12 or later.

1. Clone the repository and go to the project folder:

   ```bash
   git clone https://github.com/lottatoivanen/cybersecurity-project.git
   cd cybersecurity-project/notesapp
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install Django:

   ```bash
   python -m pip install "django>=6.1,<6.2"
   ```

4. Create the database (this also creates the test users):

   ```bash
   python manage.py migrate
   ```

5. Start the server:

   ```bash
   python manage.py runserver
   ```

6. Open the web application: http://127.0.0.1:8000/

### Test users

The following users are made for testing purposes:

- alice, password: redqueen
- bob, password: 123