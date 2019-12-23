# EntryManagementSystem(EMS)
## A Django project.


EMS is used to record the entries of all the visitors and then inform the host with mails and messages, which includes all the details of the visitor.

EMS also has an option for regular visitors to create an account to register the entries and view the records of all previous visits.

## Tech Stack Used
***
__Django__ 
v.2.2.5

__HTML__ 5

__CSS__ v.3

__Redis-Server__ v.3.3.11

__Celery__ v.4.4.0


## __Installation__
***

All the required modules are available in the file requirements.txt

I recommend to create a virtual environment before pulling this project. 

To install all the requirements 
> pip install -r  requirements.txt

Install Redis-Server
> sudo apt-get install redis-server

Redis Server is a task broker for celery.
Celery is a asynchronous task queue/job queue based on distributed message passsing. Task queues are used as a mechanism to distribute work
accross threads or machines.  

## __Run the application__
***
Replace all the ***** with required data.

After installation, 

run
>python manage.py makemigrations

>python manage.py migrate

run the django server, redis server and celery.
> redis-server & celery -A app_name worker -l info & python manage.py runserver

Disadvantage of this approach - redis and celery will work in the background even after a shutdown of django dev server. So you need to terminate this processes.

To find and kill the process
You can use the ps command to find the process ID for the process and then use the PID to kill the process.

>ps -eaf|grep runserver

replace *process_id* with the process id

>kill *process_id*

## __Incomplete parts__
***

1. Messaging module -> After visitors entry, application should trigger a message to the host.
2. Password Hashing -> Password hasing is not yet implemented.


## __Later...__
***

This project is developed in the process of learning django. 

*The code is not clean.*  

## Interested?
***
If anyone who is interested in developing this project, to make it clean and easy to learn I would really be excited to collaborate.

