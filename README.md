# exercise_with_url
Short app designed for shortening URLs

## Getting started
    Open your terminal
    $ sudo easy_install pip # installs Pip package manager
    $ git clone https://github.com/bartoszbad/exercise_with_url
    $ cd exercise_with_url # Browse into the repo root directory
    $ pip install virtualenv # Virtualenv is a tool to create isolated Python environments.
    $ virtualenv venv #Create virtual enviroment
    $ source venv/bin/activate # Launch the environment
    $ pip3 install -r requirements #Install dependiences
    $ python3 manage.py migrate #Migrate models
    $ python3 manage.py createsuperuser #Create Django Admin, some functions requires Admin.auth
    $ python3 manage.py runserver


## What it is about:
Przygotować aplikację skracającą URLe. Aplikacja ma za zadanie:

• App takes from (anonymouse user) URL link

• App generates shoreten URL `<domain>/<shortcut>` 

• App returns link

• After requesting `<domain>/<shortcut>` user is automaticaly redirected to orign URL

• In admin interface you can view URL list

## Technology used:
• Django

## Additional:
Aplication is avaliable online: 
http://bartoszbad.pythonanywhere.com/

Administrator dashboard:
http://bartoszbad.pythonanywhere.com/admin/
login: admin
password: admin

## License
* Please see LICENSE file
