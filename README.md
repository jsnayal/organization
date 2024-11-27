# FastAPI Organization Project

## Overview
This project is a FastAPI application designed for organization management by admin users. 
It includes routes to create and get organizations and admin login functionality

## Installation
Prerequisites
Ensure you have the following installed:

Python 3.7 or higher
pip (Python package installer)

## Steps to run project

Locally
1. Clone the Repository
2. Create Virtual environment. We used venv
3. Install dependencies 
pip install -r requirements.txt
4. Run the application
uvicorn src.main:app --reload

Docker
1. Clone the Repository
2. Make sure you have docker installed. cd to the directory organization
3. Build docker image with => sudo docker build --no-cache -t organization .
4. Run docker image with => sudo docker run -d -p 8000:8000 organization

## API Endpoints
/org/create
Method: POST

Request Body: JSON object with organization details

Response: A message indicating the created organization details and database path

/org/get
Method: GET

Description: Get an organization by name

Request Body: JSON object with details (organization_name).

Response: A message with organization details

/admin/login
Method: POST

Description: Login an admin and returns the auth token

Request Body: JSON object with admin email and password

Response: A message with auth token information 


## Future scope

1. Implement a different database strategy like mysql, mongodb in database.py
2. More exception handling and logging capabilities
3. We can log some performance metrics like API response time, No of requests etc to improve the performance and robustness of the system
4. Adding Unit Tests for the classes and functions to improve robustness of the system
