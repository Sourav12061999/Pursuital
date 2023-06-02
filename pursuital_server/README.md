# Pursuital Server

## Packages Needed:-

1. Django
2. djangorestframework
3. mysqlcient
4. python-decouple

## Running the application:-

1. Create a `.env` file in the root of your django app

2. Put all the below data related to your mysql database:-

   - DATABASE_USER(root for me)
   - DATABASE_PASSWORD(your db password)
   - DATABASE_HOST(localhost for now)
   - DATABASE_PORT(3306 for mysql)

3. Run the following commands to start the app:-
   - `python manage.py makemigrations`
   - `python manage.py migrate`
   - `python manage.py runserver`

## APIs:-

- `/api/signup/`(POST):- Signup
  Send the following data in the body:-
  ```
  {
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123",
  "role": "user"
  }
  ```
- `/api/signin/`(POST):- Signin
  Send the following data in the body:-
  ```
  {
  "email": "john@example.com",
  "password": "password123"
  }
  ```
*** Other than signup and signin all apis will be authenticated ***
- `api/user/`(POST):- Get User Details
  1. In the Header put a key called `Authorization`
  2. The value will be `Token <Your Token the you get after signin>`
  3. `<Your Token the you get after signin>` make sure to replace this part with the acctual token

- ``
