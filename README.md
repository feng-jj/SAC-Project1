# SAC Data Dashboard
A dashboard for Sexual Assault Center's operational data

## Table of Contents
* [Introduction](#Introduction)
* [Prerequisites](#Prerequisites)
* [Installation](#Installation)
* [Instructions](#Instructions)
* [Acknowledgements](#Acknowledgements)
* [About the Creators](#About-The-Creators) 

## Introduction
This WebApp is a data dashboard for the Sexual Assault Center in Nashville, TN containing three elements: 
* An authentication system to gain access to the dashboard
* A data entry portal
* Data visualization dashboards
Once logged in, SAC employees can input their team's operational data which is visualized in a team-specific dashboard through various graphs and charts. Visualizations display data month-to-month. Additionally, employees can retroactively modify their team's inputted data, but not the data of other teams. A registered admnistrative "super-user" can modify any team's data. 

## Prerequisites
Before proceeding, please make sure you have the following installed:
* [Django](https://www.djangoproject.com/download/)
* [Python](https://www.python.org/downloads/)

## Installation 
1. Follow the instructions outlined on this link:
https://docs.djangoproject.com/en/3.1/howto/windows/

2. Install the following packages using the following lines:
pip3 install import_export
pip3 install multiselectfield

## Instructions
**To be updated once we have more stuff done**
1. Upon launching the WebApp, you will be directed to an authentication page. Enter your username and password to gain access to the dashboard. *(image once complete)*
2. Once logged in, you will automatically be taken to your team's dashboard. *(image once complete)*
3. The navigation menu on the left allows you to view the main SAC dashboard as well as any team's dashboard. To view a certain dashboard, simply click on the team name in the navigation menu.
4. In order to input data, click on the "Data Entry" tab in the navigation menu. **(Is the system going to automatically direct users to the appropriate data entry page based on their login credentials?)** 
5. Your team's dashboard should automatically update once you submit new data. 

## Acknowledgements
This project used the "Prologue" template from [HTML5 UP](https://html5up.net/)

## About the Creators
### Jesse Feng
Jesse is a rising senior at Vanderbilt University majoring in Computer Engineering with extensive knowledge working with C++ and data analytics using Python's 
webscraping and API frameworks. He is excited for the opportunity to utilize his prior experience working in the research and development 
of social robotics to create innovative and user-friendly software solutions for non-profit organizations in need.

### Reena Zhang
Reena is a junior at Vanderbilt University studying Psychology and Computer Science. She is excited to bring her background in computational cognitive science and psychology research to build user-friendly technology for SAC.

### Daniel Kim
Daniel is a rising junior at Vanderbilt University majoring in Economics. With experience working at a software startup in the Silicon Valley, Daniel is passionate about leveraging his skills in java, html/css, advanced data visualization with excel, and strategic social media marketing to drive positive and sustainable results for amazing nonprofits.

### Jin Heo
Jin is a rising senior at Vanderbilt University majoring in Public Policy Studies. Despite having little formal coding experience, Jin has advocated for victims of domestic violence and sexual assault at two district attorney offices and regularly works with several Nashville nonprofits in the realm of criminal justice reform. He is highly interested in how technology can contribute to creating a more civil society.

## Built With
* [Django](https://www.djangoproject.com/download/): a Python-based web framework 
