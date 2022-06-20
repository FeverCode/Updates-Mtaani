# By FeverCode

## Updates Mtaani

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Running Tests](#running-tests)
+ [User Stories](#user-stories)
+ [BDD](#bdd)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description

If you are like me, You really do not know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death would you not like to know about it. Updates Mtaani is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

Live link to the project
[Updates Mtaani](https://github.com/FeverCode/Updates-Mtaani)

## Requirements

+ A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```-Python version 3.8
    -Django
    -Pip
    -virtualenv
```

## Installation

+ Open Terminal {Ctrl+Alt+T} on ubuntu
+ git clone `https://github.com/FeverCode/Updates-Mtaani`
+ cd GAwards
+ code . or atom . based on prefered text editor

## Running Project

+ On terminal where you have opened the cloned project
  + `sudo pip3 install virtualenv` - To install virtual enviroment
  + `virtualenv venv` - To create virtual enviroment
  + `source venv/bin/activate` - To activate virtual enviroment
  + `pip install -r requirements.txt` - To install requirements
  + Setup your database User, Password, Host, Port and Database Name.
  + `make makemigrations` - To create migrations
  + `make migrate` - To migrate database  
  + `make` - to start the server

## Running Tests

+ To run test for the project
  + `$ make test`

## User Stories

+ Sign in with the application to start using.
+ Set up a profile about me and a general location and my neighborhood name.
+ Find a list of different businesses in my neighborhood.
+ Find Contact Information for the health department and Police authorities near my neighborhood.
+ Create Posts that will be visible to everyone in my neighborhood.
+ Change My neighborhood when I decide to move out.
+ Only view details of a single neighborhood.

## BDD

+ Landing page with various neighbourhoods. A navigation bar with home, login and register routes.
+ Create an account with a unique username,an email and password.
+ User can also create and update their profile.
+ Click on the add post to add a new post

## Technologies Used

+ python3.8
+ django 3.2
+ Cloudninary (for hosting images)
+ Heroku (for hosting the project)
+ Rest framework (for API)

## Licence

MIT License

Copyright (c) [2022] [FeverCode]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors Info

LinkedIn - [https://www.linkedin.com/in/gedion-onsongo-112543210/]

Reddit - [https://www.reddit.com/user/stainscode]

