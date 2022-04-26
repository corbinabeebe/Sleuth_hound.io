# Sleuth-hound.io

<p>

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

</p>

## Project Description

This application is a defect tracking tool.  The main focus of the tool is to allow users of the sytstem to do the follow:

- Login to the sytem via authentication
- Add projects to the system
- Add tasks or defects to the project to keep track of the life cycle of the task
- Add comments in tasks or projects to communiate with other developers working on the project

Sleuth-hound.io is a python application built with the Django framework. We chose the Django framework because it is lightweight and powerful.
The application is connected to a postgres data base to store data entered by the users.
We also chose to dockerize the project to take advantage of being able to run the application anywhere and work across multiple environments.

A few features that we would like to implement in the future can be found below:

- Ability to attach files
- Ability to sort between bugs and feature requests
- Ability to search through the database for information about past and present bugs

## How To Install Sleuth-hound.io

No matter wherer you decide to use Sleuth, we start the install process by cloning the Sleuth-hound.io repository to your machine.

### Running Sleuth via Docker

Sleuth-hound.io has a few dependencies and requirements to ensure the project is able to run locally.
We can start by installing docker if it is not already installed.  Docker can be installed by following the instructions available here: [Get Docker](<https://docs.docker.com/get-docker/>)

Once docker is installed, We are ready to instruct the system to setup our project via the docker-compose and dockerfile.

- Navigate to the locally direcotry where Sleuth-hound.io is installed
- Run **docker compose up** or if you need to re-build the project an instantiate changes run **docker compuse up --build**
- To check if the project is running, navigate to the app home page by checking [localhost:10555](<http://localhost:10555/>)
- **PROFIT!!!!**

## Running Sleuth Locally

When running Python and Django projects locally, it is recommended to use virtual environemnts(which we highly recommend).

### Install Postgres

Need install of postgres locally - [Postgres SQL](<https://www.postgresql.org/>)

It might be helpful to login to postgres with the postgres super user or pgAdmin and create a super user for yourself and the database: sluethdb to be used in steps below

### Install Virtual Environment

Details on installing a virtual environemnt can be found here: [Python Docs: Virtual Environments](<https://docs.python.org/3/tutorial/venv.html/>)
After installation of virtual environment, activate the environemnt (system specific and can be found in Vitual Env docs listed above)
With the virtual environemnt activated, in terminal/console, navigate to the project folder:

```

cd path/to/Sleuth-hound.io

```

### Open source code in IDE

Open the code base in your favorite IDE(we use VS code)

### Create a config file named .pg_service.conf

This file will have the following format and information:

```

[my_service]
host=localhost
user=your_user_name
dbname=sleuthdb
port=5432

```

### Create a pass file named .my_pgpass

```

localhost:5432:sleuthdb:YourUserName:YourPassword

```

### Install requirments and migrations

Then run one command after another:

```

pip install -r requirements.txt

python manage.py makemigrations sleuthApp

python manage.py migrate

python manage.py runserver


```

### PROFIT

## How to use Sleuth-hound.io

How to and trouble shooting will be found below!

## Tests

Tests and test plan will be found below!
