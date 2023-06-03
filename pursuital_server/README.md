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
#### User:- 
- `api/user/`(POST):- Get User Details
  1. In the Header put a key called `Authorization`
  2. The value will be `Token <Your Token the you get after signin>`
  3. `<Your Token the you get after signin>` make sure to replace this part with the acctual token

#### Batches:- 
- `api/batches/list/`(GET):- Get all the batches
- `api/batches/create/`(POST):- Add a new Batch
#### Campaigns:- 
- `api/campaigns/create/`(POST):- Add a new Campaign
- `api/campaigns/list/`(POST):- Get all the Campaigns
- `api/campaigns/update/:id`(PUT):- Update the Campaign with the id
- `api/campaigns/delete/:id`(Delete):- Delete a campaign
#### CampaignUser:-
- `api/campaigns-users/create`(POST):- Create a new Campaign User
- `api/campaigns-users/list/<int:campaign_id>/`(GET) -> Get all the Campaign Users of a perticular campaign
- `api/campaigns-users/delete/<int:user_id>/<int:campaign_id>/`(Delete):- Delete a CampaignUser which is of a User and belongs to a Campaign
#### Goals:- 
- `api/goals/create/`(POST):- Create a goal
- `api/goals/list/<int:goal_id>/`(GET):- Return a goal by its id
#### Goal User:-
- `api/goals-users/create/`(POST):- Create a GoalUser
- `api/goals-users/list/`(GET):- It can take `user_id` and `campaign_id` as query params(Both Optional) and return the filtered
- `api/goals-users/delete/<int:goaluserid>/`(Delete):- delete the goaluser

*** This same format of Goals and GoalUser is followed for Milestone and MilestoneUsers ***
