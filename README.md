# The Bucket-List App 

## A Description

This is a Web Application desined to allow users to maintain an online record of their
aspirations, i.e., the things on their bucket list. It basically shows a list of achievements that the user hopes to some day achieve, along with a badge showing the estimated time by when the achievement should be achieved.

## Application Features:
The App's UI has the following pages:

 * A Register page - designed to allow new users to create an account, which is necessary 
 	before a user can Create a bucket list or View one. Features a form that takes  a valid email address, a user-name and two instances of a password
    
 * A Login page - Allows user to access the app, and subsequently to access their bucket list. Features a form that takes an email address and a password.
 
 * A View page - user here sees items already on bucket list. Items arranged in a numbered list. User can modify or delete items from list, or mark them as done.
 
 * A Create page -user can add new items to the bucket list. Requires user to fill a form with provision for item title (a small description of the achievement aspired to), and a badge (a tag, estimating the due date for the achievement)
 

## Application Development Prerequisites
The App was developed using the following:

 *  HTML/CSS/Bootstrap and JS- in designing the UI
 *  Flask microframework - for writing the App's backend framework
 *  Visual Studio Code editor

 ##To run app:
 * Install all dependencies in requirements.txt, preferably in a virtualenv
 * Run the app's main code file, the views.py
 * Access `localhost:5000` on your browser. And voila. The links in the app's UI work just fine.