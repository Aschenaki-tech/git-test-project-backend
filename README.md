Song List Backend

## Overview
The Song List Backend is a Django REST Framework application that provides an API for managing songs, languages, and genres. It supports user registration and authentication.

## Technologies Used
- Django
- Django REST Framework
- Django REST Framework Simple JWT for authentication
- SQLite (or any other database of your choice)

## Features
- User registration and login
- CRUD operations for songs
- Manage languages and genres
- Token-based authentication

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd song-list-backend

Set up a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
bash
pip install -r requirements.txt

Apply migrations:
bash
python manage.py migrate

Create a superuser (optional):
bash
python manage.py createsuperuser

Start the development server:
bash
python manage.py runserver 5000

The API will be available at http://localhost:5000/api/.
API Endpoints
POST /api/auth/register/: Register a new user.
POST /api/auth/login/: Log in and receive a token.
GET /api/songs/: Retrieve the list of songs.
POST /api/songs/: Add a new song.
PUT /api/songs/{id}/: Update an existing song.
DELETE /api/songs/{id}/: Delete a song.
Authentication
Use token-based authentication for protected endpoints. Include the token in the Authorization header as follows:
text
Authorization: [AllowAny]
