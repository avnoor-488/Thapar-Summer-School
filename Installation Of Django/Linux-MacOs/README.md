
# Setup guide of Django for  Linux-Mac Users




## Pre-Requisites


## Step 1 — Open Terminal
First, you need to open Terminal on your PC.

Now that you have opened PowerShell on your computer, you’ll verify the installation of Python in the next section.


## Step 2  - Creating a Project Directory

In this section, you will create a directory that will contain your Django application. We will name it django_project since this tutorial is a demo. But in a real project, you can give the directory a suitable name, such as combo-offer, multi-disease, etc.

Change into your Desktop directory with the cd command:

```bash
$ cd Desktop
```

Create the directory using the mkdir command:

```bash
$ mkdir django_project
```
Move into the django_project directory using the cd command:
```bash
$ cd django_project
```
Your prompt should now show you that you’re in the django_project directory as shown in the following output:
```bash
shikari@shikari:~/Desktop/django_project$ 
```

Now that you’ve created the working directory for your project, you’ll create a virtual environment where you’ll install Django.


## Step 3 - Installing and Creating the Virtual Environment

You'll first need to install the virtual environment package in global system to use it in project directories .

```bash 
$ pip install virtualenv
```

Next step, you’ll create a virtual environment for your project. A virtual environment is an isolated environment in Python where you can install the project dependencies without affecting other Python projects. This lets you create different projects that use different versions of Django.

If you don’t use a virtual environment, your projects in your system will use the same Django version installed globally. This might look like a good thing until the latest version of Django comes out with breaking changes causing your projects to fail altogether.

You can learn more about the virtual environment by following Python Virtual Environments: A Primer.

To create a virtual environment, type the following command and wait for a few seconds:

```bash
$ virtualenv env
```

The command will create a directory called env inside your project directory.

Next, confirm the env directory has been created by listing the directory contents using the ls command:

```bash
$ ls 
```

You should see the directory env in the output as shown in the following screenshot:


Now you’ve created the virtual environment directory, you’ll activate the environment.


## Step 4 - Activating the Virtual Environment

In this section, you’ll activate the virtual environment in your directory.

Run the following command to activate the virtual environment:
```bash
$ source env/bin/activate
```

After you run the command, you will see 
a (env) at the beginning of the prompt. This shows that the virtual environment is activated:

```bash
(env) shikari@shikari:~/Desktop/django_project$ 
```

Now that you’ve activated the virtual environment for your project, the moment you’ve been waiting for is here. It’s time to install Django!

## Step 6 - Installing Django
In this section, you will install Django on your system using pip.

Run the following command to install the latest version of Django using pip install:
```bash
(env)> pip install django

```

If you want to install a different Django version, you can specify the version as follows:

```bash
(env)> pip install django==3.2.9

```
Once the installation finishes, you need to verify that Django has been installed. To do that, type the following command:
```bash 
(env)> django-admin --version

```
You will get output showing you the Django version installed on your system:

```bash
(env) shikari@shikari:~/Desktop/django_project$ django-admin --version
3.2.9
```

At the time of writing, the latest Django version is 3.2.9, and that’s why my output shows that.

You’ve now installed Django on your system, great job! You’ll begin to create a Django project.


## Step 7 - Creating the Django Project

Now it’s time to create a project. A project has a different meaning from what you may be used to. The Django documentation defines it as:

A Python package – i.e. a directory of code – that contains all the settings for an instance of Django. This would include database configuration, Django-specific options and application-specific settings.

You create a project by using the command-line utility django-admin that comes with Django. The command generates files where you can configure the settings for your database, add third-party packages for your project to mention a few.

Create the project using the django-admin startproject command:

```bashh
(env)> django-admin startproject test_project
```
Change into the test_project directory:

```bash
(env)> cd test_project
```
Type the following command to see the contents in the project directory:

```bash
(env)> ls test_project
```
You will get output similar to this:

```bash
(env) shikari@shikari:~/Desktop/django_project/test_project$ ls

   Directory: shikari@shikari:~/Desktop/django_project/test_project$

Mode                LastWriteTime         Length Name

----                -------------         ------ ----

d-----         9/4/2021   1:25 AM                test_project

-a----         9/4/2021   1:25 AM            690 manage.py
```


The directory test_project contains Django configuration files. The manage.py file comes in handy when starting a development server, and that’s what you will do in the next step.
## Step 9 - Running the Development Server
Now that the project has been created, we will start the Django development server.

Start the development server using the manage.py runserver command:
```bash 
(env)> python manage.py runserver
```

Next, visit http://127.0.0.1:8000/ in your web browser. You should see a page similar to the following screenshot

![alt text](https://www.stanleyulili.com/assets/images/posts/2019-08-31-how-to-install-django-on-windows/server-running.jpg)



Tip You can stop the server by holding CTRL+C. To deactivate the virtual environment, you can type deactivate on the prompt.

Now, you are ready to start developing your project, see you there in the session with multiple projects.
## References
https://docs.djangoproject.com/
