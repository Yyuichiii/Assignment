# Referral System API

This repository contains a referral system API (Assignment) built with Django, deployed using Docker and Docker Compose.

## Installation and Setup

### Prerequisites
- Docker
- Docker Compose

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Yyuichiii/Assignment.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Assignment
   ```

3. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

4. Once the containers are running, you can access the API at [http://localhost:8000](http://localhost:8000).

## API Endpoints

### User Registration
- **URL:** `/api/register/`
- **Method:** POST
- **Request Body Example:**
  ```json
  {
    "email": "test@example.com",
    "password": "password123",
    "password2": "password123",
    "Code": "ASDFGG" (Optional)
  }
  ```
- **Response Example (Success):**
  ```json
   {
    "msg": "Registration Success",
    "User_ID": 1,
    "token": [
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyNTIwMjY2LCJpYXQiOjE3MTI1MTk2NjYsImp0aSI6IjM3MTdlZmU0MWJmYTQxNDFhMjlkNmU3MzdmNDQwZGQ3IiwidXNlcl9pZCI6OH0.rJVrMt1n_WBDkU2he3V9rLBKZxb0NsHOXCiu4217c3o"
    ]
  }
  ```
- **Response Example (Error):**
  ```json
  {
    "error": "Email already exists"
  }
  ```

### User Login
- **URL:** `/api/login/`
- **Method:** POST
- **Request Body Example:**
  ```json
  {
    "email": "test@example.com",
    "password": "password123"
  }
  ```

### User Profile
- **URL:** `/api/profile/`
- **Method:** GET
- **Authorization Header:** `Bearer access token_here`
- **Response Example:**
  ```json
  {
    "email": "test@example.com",
    "name": "test",
    "referral_code": "TBO6IL",
    "created_at": "2024-04-08T01:23:09.609395+05:30",
    "points": 7
  },
      
  ```


### User Referrals
- **URL:** `/api/referral/`
- **Method:** GET
- **Authorization Header:** `Bearer access token_here`
- **Response Example:**
  ```json
  {
    "referred_user": [
      {
        "name": "test",
        "email": "test@example.com",
        "created_at": "2024-04-08T01:24:06.048867+05:30"
      },

      {
        "name": "test2",
        "email": "test2@example.com",
        "created_at": "2024-04-08T01:24:06.048867+05:30"
      },
      
  ```
