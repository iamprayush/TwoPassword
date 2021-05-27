# TwoPassword
## Objective
Keeping strong passwords on the services that you use on the Internet is important. It is also important to not re-use passwords across different services. Religiously doing these two things can save you from a lot of pain when any of the services that you use get compromised unfortunately. Your job is to build a password manager, called **TwoPassword**, that helps users generate and store passwords for the different services they use.

## Functionalities added
- **User Management**
	- [x] Login, Register, and Logout pages.
	- [x] Restriction of views, based on user login status, to the main Dashboard.
- **Dashboard**
	- [x] Paginated list of all passwords entries created by the user.
	- [x] Password entry creation and deletion.
	- [x] Search for password based on website address.
		- The password entry table is indexed on the website address attribute for search query optimization.
	- [x] Restriction to view a password using the master password.
		- The password entry is only revealed if the user enters the correct master password. The validity is tracked via a boolean session variable called master_is_authenticated. If it is false, or not present, the user is redirected to a form to enter their password.
	- [x] Autogenerate random password from UI.

## Demo
https://user-images.githubusercontent.com/35144226/119908492-55b37a00-bf70-11eb-9d84-70ae145ceba1.mp4

## Technologies used
- Django (Backend Framework)
- SQLite (Database)
- Bootstrap and JQuery (Frontend)

## Local setup
1. Clone the repo.
2. Create and activate a virtual env using python3.
3. Install dependancies: `pip install -r requirements.txt`.
4. Create migration files: `python manage.py makemigrations`.
5. Migrate the database: `python manage.py migrate`.
6. Start the server: `python manage.py runserver`.
7. Access the website at `localhost:8000`.
