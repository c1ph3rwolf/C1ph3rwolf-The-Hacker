## What is Django



> [!done] Django
> Django is a Python framework that makes it easier to create web sites using Python^[Django takes care of the difficult stuff so that you can concentrate on building your web applications.] ^[Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).]
> > [How does Django Works](https://www.w3schools.com/django/django_intro.php)


# Table of Contents

0. [[#What is Django]]
1. [[#How does Django Works ?]]
2. [[#Create Virtual Environment]]
	1. [[#Create Virtual Environment]]
	2. [[#Activate the Environment]]
3. [[#Install Django]]
	1. [[#windows]]
	2. [[#linux]]
4. [[#Check Versions]]
	1. [[#Python]]
	2. [[#Django]]
5. 

# The Mind-Map
![[Getting Started with Django.canvas|Working of Django]]
![[Django App.canvas|Django App]]
# The Contents

## How does Django Works ?

Django follows the MVT design pattern (Model View Template).

- Model - The data you want to present, usually data from a database.
- View - A request handler that returns the relevant template and content - based on the request from the user.
- Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

#### Model

The model provides data from the database.

In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.

The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.

The models are usually located in a file called `models.py`.

#### View

A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.

The views are usually located in a file called `views.py`.
#### Template

A template is a file where you describe how the result should be represented.

Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.

Django uses standard HTML to describe the layout, but uses Django tags to add logic:

```django
<h1>My Homepage</h1>

<p>My name is {{ firstname }}.</p>
```

The templates of an application is located in a folder named `templates`.
#### URLs

Django also provides a way to navigate around the different pages in a website.
When a user requests a URL, Django decides which _view_ it will send it to.
This is done in a file called `urls.py`.
#### So, What is Going On?


When you have installed Django and created your first Django web application, and the browser requests the URL, this is basically what happens:

1. Django receives the URL, checks the `urls.py` file, and calls the view that matches the URL.
2. The view, located in `views.py`, checks for relevant models.
3. The models are imported from the `models.py` file.
4. The view then sends the data to a specified template in the `template` folder.
5. The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.

Django can do a lot more than this, but this is basically what you will learn in this tutorial, and are the basic steps in a simple web application made with Django.

> [!done]  Django History
> Django was invented by Lawrence Journal-World in 2003, to meet the short deadlines in the newspaper and at the same time meeting the demands of experienced web developers.
> > Initial release to the public was in July 2005.
> > Latest version of Django is 4.0.3 (March 2022).
## Create Virtual Environment

It is suggested to have a dedicated virtual environment for each Django Project, and one way to manage a virtual environment is `venv` which is in-built in python.
#### Command to Create `venv`

```python
python -m venv myworld
```

#### Activate the Environment

> Windows

```python
myworld\Scripts\activate.bat
```

> Linux

```python
source myworld/bin/activate
```

## Install Django
Now, that we have created a virtual environment, we are ready to install Django.
Django is installed using pip, with this command:


#### windows
```
(myworld) > py -m pip install Django
```

#### linux
```
(myworld) ... $ python -m pip install Django
```

That's it! Now you have installed Django in your new project, running in a virtual environment!

## Check Versions

#### Python

> Windows

```
py --version
```

> Linux

```
python --version
```
#### Django

```python
(myworld) > django-admin --version
```
## Create Django App

#### What is an App?

> [!done] Django App
> An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database. ^[In this tutorial we will create an app that allows us to list and register members in a database.]

But first, let's just create a simple Django app that displays "Hello World!".


#### Create App

- [ ] I will name my app `members`.
- [ ] Start by navigating to the selected location where you want to store the app, in my case the `my_tennis_club` folder, and run the command below.
- [ ] press` [CTRL]` `[BREAK]`, or `[CTRL] [C]` to stop the server. ^[If the server is still running, and you are not able to write commands. so you need to to stop the server]

```python
py manage.py startapp members
```
Django creates a folder named `members` in my project, with this content:
```
my_tennis_club  
    manage.py  
    my_tennis_club/  
    members/  
        migrations/  
            __init__.py  
        __init__.py  
        admin.py  
        apps.py  
        models.py  
        tests.py  
        views.py
```

These are all files and folders with a specific meaning. 

First, take a look at the file called `views.py`.