# NG-ach
> Simple imageboard website :trollface:


*Create threads in themes that interest you, make posts with pictures, and have fun!*


## Using the website from the client side

**Main page**

The main page welcomes us with a list of available themes. By clicking on them, we can navigate to the desired topic.

**Theme page**

On the theme page, we will see threads written by other users. Additionally, we can create our own thread or navigate to an existing one :shipit:

**Thread page**

The thread page is the main place where people communicate and have fun. Here, we can create a post with text and images, and we will also see posts from other users.


### Using the website from the admin side
>Below are examples of what admins can do

**Main page**

+ Create theme
+ Delete an existing theme

**Theme page**

+ Delete and existing thread

**Thread page**

+ Delete posts

### Server mini-guide

To start the server, we need to navigate to the ***api/...*** folder and run the following command in the terminal: ***flask run***.

In ***auth.py***, we can modify the secret key for admin registration.

To have a DB we need to be in ***api/*** and use ***flask db init***

[Flask migrations](https://flask-migrate.readthedocs.io/en/latest/)

