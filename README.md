# Job Application Panel

## Configurations before Execution

### .env Config

Fulfil **SECRET_KEY**, **DB_NAME**, **DB_PASSWORD** on the **_.env_** file.

### Requirements

Run `pip install -r requirements.txt`

### Python Script

Run the following code on **CMD** to make migrations and populate the database.  
`python manage.py makemigrations && python manage.py migrate && python manage.py loaddata customuser && python manage.py loaddata positionmodel && python manage.py loaddata applicationmodel`

### Execution

Run `python manage.py runserver`

## Populated DB Data Info

**2** HR Staff  
**15** non-staff User  
**20** Positions  
**13** Applications

### Users login info's

#### HR Accounts

hrstaff1 and hrstaff2

#### User Accounts

user1, user2, user3, ..., user13, user14, user15

#### Passwords

All the accounts' password is **123456789**