# My Awesome shops and Authentication Project

# Description
  My project display a website that allow users to contact us, also view the different items along with the specific image they would like the purchase.The app will also take in data from the user and store it on the website in the conatact page allowing the user to interact with any complaints and suggestions etc ,the app also allow the user to make changes to the questions and choices they submitted . It's essential to leave rooms for errors which can be change again on a later stage if there are anything the user would like to change 
#  Table of content

- Installing

- Executing program

# Installing

#### Before any user can run the program you will need to set up your environment
### Install Python and Django:
### Django is a Python web framework. Ensure you have Python installed 
### you can install Django by simply clicking the link below:
[Feel free to copy the Django link here](https://pypi.org/project/Django/)
## To install Django, open your terminal or command prompt and run:
    pip install django

## Create a Virtual Environment:    
##### Virtual environments keep dependencies isolated. Create one for your project:
    python -m venv myenv

## Activate the virtual environment:
##### On Windows:
    myenv\Scripts\activate

##### On macOS and Linux:
    source myenv/bin/activate

## Install Project Dependencies:
##### Install the required libraries using:
    pip install -r requirements.txt

# Executing Program
#### Now that your environment is all set up, you can now run your project locally

#### Run the Development Server:
#### Navigate to your project directory (where manage.py is located).
 ## Start the development server with this command:

    python manage.py runserver

### Click the link below in your web browser to access your Django app.
 - http://localhost:8000 



#### You will first need to run Docker Desktop
### docker link below:
[feel free to copy or click the link here](https://www.docker.com/)

### Pull container from Docker Hub ,make sure to use the    following 
     docker pull jays95/Django-shop

### Run the container image by using
   docker-run -d -p 8000 jays95/shop-repo

---
