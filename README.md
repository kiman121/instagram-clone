# Instello
#### An Instagram clone web app.

#### By **Patrick Mwangangi**
## Description
This web application created was create as a clone of Instagram with a twist. Interested users are able to post their favourite photos as well as follow, comment and like other users photos.

Further to the above usage, this master piece was created as practice on concepts learnt in Python Django (at Moringa School).
## Demo

Here is a working live demo : https://instelo.herokuapp.com/
## Setup/Installaction Requirements
- Clone the repository (repo).
    ```
    git clone https://github.com/kiman121/instagram-clone.git
    ```
- Open the project on VS Code or any editor of choice.
- Navigate to the projects root directory.
- Open the virtual environment by running the `source virtual/bin/activate` command.
- Install the required packages: `pip install -r requirements.txt`
- Create a .env file and add the following data instances
    ```
    SECRET_KEY=<'your secret key'>
    DEBUG=True
    DB_NAME=<'database_name'>
    DB_USER=<'postgres_user'>
    DB_PASSWORD=<'postgres_password'>
    DB_HOST='127.0.0.1'
    MODE='dev'
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
    DISABLE_COLLECTSTATIC=1
    ```
- Run migrations to update the changes to db: `python3.9 manage.py migrate`
- Run the development server: `python3.9 manage.py runserver`
- open this url on your browser "http://127.0.0.1:5000/"
## Known Bugs

No Known bugs

## Technology Used
- HTML
- CSS
- Javascript
- Bootstrap
- Python
- Django

## Support and contact details

If you want to contact us, email us on info@instagram-clone.com

### License

[MIT licence](https://github.com/kiman121/instagram-clone/blob/master/LICENCE)
Copyright (c) 2021 **My Photo Gallery**