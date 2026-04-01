Little Lemon Restaurant API
===========================

Setup:
1. Create a MySQL database called 'littlelemon'
2. Update database credentials in littlelemon/settings.py if needed
3. Install dependencies: pip install django djangorestframework djoser mysqlclient
4. Run migrations: python manage.py makemigrations && python manage.py migrate
5. Create superuser: python manage.py createsuperuser
6. Run server: python manage.py runserver

API Paths:
----------
/restaurant/                        - Home page (static HTML)
/restaurant/api/menu/               - Menu items (GET, POST)
/restaurant/api/menu/<id>/          - Single menu item (GET, PUT, DELETE)
/restaurant/booking/tables/         - Table bookings (GET, POST) - requires auth token
/restaurant/booking/tables/<id>/    - Single booking (GET, PUT, DELETE) - requires auth token

Authentication:
---------------
/auth/users/                        - User registration (POST)
/auth/token/login/                  - Obtain auth token (POST)
/auth/token/logout/                 - Logout (POST)

To test authenticated endpoints, include the header:
Authorization: Token <your-token>
