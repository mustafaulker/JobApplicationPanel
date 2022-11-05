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