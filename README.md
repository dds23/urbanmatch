# Marriage Matchmaking App

## Introduction

The Marriage Matchmaking App is a backend application designed to help users find potential matches based on their profile information. The app allows users to create, read, update, and delete profiles with details such as name, age, gender, email, city, and interests.

## Features

1. **Create User Endpoint**: Allows the creation of a new user profile.
2. **Read Users Endpoint**: Retrieves a list of user profiles.
3. **Read User by ID Endpoint**: Retrieves a user profile by ID.
4. **Update User Endpoint**: Updates user details by ID.
5. **Delete User Endpoint**: Deletes a user profile by ID.
6. **Find Matches for a User**: Finds potential matches for a user based on their profile information.
7. **Email Validation**: Ensures that the email field in user profiles contains valid email addresses.

## Approach

### 1. Basic Project Structure

The project structure includes:
- `main.py`: The main application file with basic CRUD operations for user profiles.
- `models.py`: SQLAlchemy models defining the User schema.
- `database.py`: Database configuration and setup.
- `schemas.py`: Pydantic schemas for data validation and serialization.
- `crud.py`: Contains the logic for interacting with the database.
- `config.py`: Contains the settings required to run the application.
- `.env`: Conatins the database url to connect to the database.

### 2. Database Configuration

The application uses PostgreSQL as the database to store user profiles. SQLAlchemy is used for ORM, and Pydantic is used for data validation.

### 3. Endpoints Implementation

#### Create User Endpoint
Implemented in `main.py` to create a new user profile and return the created user data.

#### Read Users Endpoint
Implemented in `main.py` to retrieve a list of user profiles.

#### Read User by ID Endpoint
Implemented in `main.py` to retrieve a user profile by ID.

#### Update User Endpoint
Implemented in `main.py` and `crud.py` to update user details by ID. The `UserUpdate` schema allows partial updates by making all fields optional. The update function applies only the provided fields.

#### Delete User Endpoint
Implemented in `main.py` and `crud.py` to delete a user profile by ID.

#### Find Matches for a User
Implemented in `main.py` and `crud.py` to find potential matches based on overlapping interests.

#### Email Validation
Implemented using Pydantic's `EmailStr` type to ensure the email field contains valid email addresses.

## Assumptions

1. **Database**: The application uses PostgreSQL for a more robust database.
2. **Interests**: Interests are stored as an array of strings. Users are matched based on at least one overlapping interest.
3. **Validation**: Email validation is done using Pydantic's `EmailStr` type.
4. **Environment**: Assumes that all required Python packages are installed and the virtual environment is set up correctly.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/dds23/urbanmatch.git
   cd urbanmatch
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv my_env
   source my_env/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Create a `.env` file in the root directory of the project and add your database connection URL:
   ```
   DB_URL=postgresql://username:password@localhost/dbname
   ```

### Running the Project

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. The API will be available at `http://localhost:8000`.
