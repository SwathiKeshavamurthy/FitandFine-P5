<p align="center">
  <img src="static/images/favicon.JPG" alt="Fit&Fine Logo" style="width: 100px; height: auto;">
</p>
<h1 align="center">Fit&Fine</h1>

[Fit&Fine Django Rest Framework API Backend Live Link](https://fitandfine-drf-be560b223a3b.herokuapp.com/)

[Fit&Fine React Frontend Live Link](https://fitandfine-react-p5-f5d23da9d77c.herokuapp.com/)

[Fit&Fine React Frontend Github Repo](https://github.com/SwathiKeshavamurthy/fitandfine-react-p5)

## Project Goals

Fit&Fine is designed to be a comprehensive fitness companion for users of all levels, from beginners to seasoned athletes. The primary goals of the web app are to:
1) Provide users with tools to set fitness challenges, track daily routines, and monitor their progress, fostering a supportive and motivating community.
2) Deliver a user-friendly and engaging platform where users can create and share posts, follow other users, and collaborate on fitness activities.
3) Ensure a streamlined experience with essential features like personalized daily routines, community challenges, and the ability to manage profiles, posts, and comments.

The backend is implemented using Django Rest Framework API for the [Fit&Fine Website](https://fitandfine-react-p5-f5d23da9d77c.herokuapp.com/). It is designed to support both web and future mobile applications providing robust and secure APIs for the Fit&Fine React frontend application, ensuring seamless integration and future scalability.

## Table of contents
- [Project Goals](#project-goals)
- [Table of contents](#table-of-contents)
- [Planning](#planning)
  - [Project Overview](#project-overview)
  - [Objectives](#objectives)
  - [Timeline](#timeline)
- [Data Models](#data-models)
  - [1. Profiles Model](#1-profiles-model)
  - [2. Posts Model](#2-posts-model)
  - [3. Comments Model](#3-comments-model)
  - [4. Daily Routines Model](#4-daily-routines-model)
  - [5. Challenges Model](#5-challenges-model)
  - [6. Collaborate Model](#6-collaborate-model)
  - [7. Likes Model](#7-likes-model)
  - [8. Follower Model](#8-follower-model)
- [API Endpoints](#api-endpoints)
  - [Example Requests and Responses](#example-requests-and-responses)
- [Frameworks, Libraries, and Dependencies](#frameworks-libraries-and-dependencies)
  - [Django Framework and Extensions](#django-framework-and-extensions)
  - [Database Management](#database-management)
  - [Authentication and Security](#authentication-and-security)
  - [Storage and Image Handling](#storage-and-image-handling)
  - [Application Server](#application-server)
  - [Utility Libraries](#utility-libraries)

## Planning

The planning phase for the Fit&Fine project encompasses several key areas to ensure the successful development and deployment of both the backend and frontend components. Here is a comprehensive plan to guide the development process:

### Project Overview

Fit&Fine is a comprehensive fitness platform designed to help users achieve their health and wellness goals. The platform includes features such as challenges, daily routines, and social interaction to create a supportive and motivating environment for users.

### Objectives

1. Develop a robust backend API using Django Rest Framework to handle data management and user authentication.
2. Build an intuitive and responsive frontend using React to provide a seamless user experience.
3. Integrate key features such as user profiles, posts, comments, likes, challenges, and daily routines.

### Timeline

1. **Week 1: Project Setup and Initial Development**
   - Set up backend and frontend repositories.
   - Configure Django Rest Framework for the backend.
   - Initialize React project for the frontend.
   - Set up initial project structure and environment configurations.

2. **Week 2: User Authentication and Profile Management**
   - Implement user registration, login, and logout functionality.
   - Develop user profile creation and editing features.
   - Ensure secure password handling and authentication processes.

3. **Week 3: Core Features Development**
   - Develop the functionality for creating, editing, and deleting posts.
   - Implement comments and likes features for posts.
   - Develop daily routines and challenges features, including creation and management.

4. **Week 4: Frontend Integration and Styling**
   - Integrate backend API with the frontend.
   - Develop responsive and user-friendly UI components.
   - Apply consistent styling using CSS modules or a CSS framework.

5. **Week 5: Testing and Debugging**
   - Conduct thorough testing of all features.
   - Fix any bugs or issues identified during testing.
   - Perform user acceptance testing (UAT) to ensure the platform meets user needs.

6. **Week 6: Deployment and Documentation**
   - Deploy the backend API to a cloud service (e.g., Heroku, AWS).
   - Deploy the frontend application to a hosting service (e.g., Netlify, Vercel).
   - Write comprehensive documentation, including setup instructions, API documentation, and user guides.

## Data Models

The Fit&Fine backend project is organized into several key models, each representing different aspects of the Fit&Fine platform. Below is an overview of the primary data models used in the project:

### 1. Profiles Model
   - **Profile**: Stores user-specific information such as username, password, profile image, bio, email, and birthday.

**Fields**:
  - `user`: ForeignKey to the User model
  - `bio`: TextField
  - `image`: ImageField
  - `email`: EmailField
  - `birthday`: DateField
  - `followers_count`: IntegerField
  - `following_count`: IntegerField
  - `posts_count`: IntegerField

### 2. Posts Model
   - **Post**: Represents user-generated content, including fields for the title, content, image, tags, creation date, and owner.
   
**Fields**:
  - `owner`: ForeignKey to Profile
  - `title`: CharField
  - `content`: TextField
  - `image`: ImageField
  - `tags`: CharField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField
  - `comments_count`: IntegerField
  - `likes_count`: IntegerField

### 3. Comments Model
  - **Comment**: Allows users to comment on posts, with fields for the content, creation date, post it belongs to, and owner.
  - 
**Fields**:
  - `owner`: ForeignKey to Profile
  - `post`: ForeignKey to Post
  - `content`: TextField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### 4. Daily Routines Model
   - **DailyRoutine**: Tracks daily activities and health metrics, including fields for date, wake-up time, meal times, calorie intake, water intake, workout minutes, sleep time, junk food consumption, and mood.
  
**Fields**:
  - `owner`: ForeignKey to Profile
  - `date`: DateField
  - `wake_up_time`: TimeField
  - `breakfast_time`: TimeField
  - `lunch_time`: TimeField
  - `dinner_time`: TimeField
  - `total_calorie_intake`: IntegerField
  - `water_intake`: IntegerField
  - `sleep_time`: TimeField
  - `workout_minutes`: IntegerField
  - `junk`: BooleanField
  - `mood`: CharField

### 5. Challenges Model
   - **Challenge**: Represents fitness challenges that users can participate in, with fields for title, description, start and end dates, sport type, and an associated image.
   - **Participant**: Tracks users who are participating in a particular challenge.

**Fields**:
  - `title`: CharField
  - `description`: TextField
  - `start_date`: DateField
  - `end_date`: DateField
  - `sport`: CharField
  - `image`: ImageField

### 6. Collaborate Model
   - **Collaborate**: Handles collaboration requests and messages between users, including fields for the name, email, message content, and date of submission.

**Fields**:
  - `name`: CharField
  - `email`: EmailField
  - `message`: TextField
  - `submitted_at`: DateTimeField

### 7. Likes Model
- **Like**: Tracks which users have liked a particular post.
and Followers Models

**Fields**:
  - `owner`: ForeignKey to Profile
  - `post`: ForeignKey to Post
   
### 8. Follower Model   
- **Follower**: Manages follower-following relationships between users.

**Fields**:
  - `owner`: ForeignKey to Profile
  - `following`: ForeignKey to Profile

Sure, here's the updated API Endpoints section with CRUD operation and View Type columns added:

Here's the table formatted for a README.md file:

## API Endpoints

The Fit&Fine backend provides a RESTful API to interact with the various models. Below is a list of the primary API endpoints for each model, including their respective HTTP methods and descriptions.

| Endpoint                    | HTTP Method | CRUD Operation | View Type         | Description                                               |
|-----------------------------|-------------|----------------|-------------------|-----------------------------------------------------------|
| **Authentication Endpoints**                                                                 |
| `/dj-rest-auth/login/`      | POST        | Create         | Auth              | Log in a user and obtain authentication tokens.           |
| `/dj-rest-auth/logout/`     | POST        | Delete         | Auth              | Log out a user and invalidate their authentication tokens.|
| `/dj-rest-auth/registration/`| POST       | Create         | Auth              | Register a new user.                                      |
| **Profile Endpoints**                                                                       |
| `/profiles/`                | GET         | Read           | List              | Retrieve a list of profiles.                              |
|                             | POST        | Create         | Create            | Create a new profile (admin only).                        |
| `/profiles/<id>/`           | GET         | Read           | Detail            | Retrieve a specific profile by ID.                        |
|                             | PUT         | Update         | Update            | Update a specific profile by ID.                          |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific profile by ID.                |
|                             | DELETE      | Delete         | Delete            | Delete a specific profile by ID (admin only).             |
| **Post Endpoints**                                                                          |
| `/posts/`                   | GET         | Read           | List              | Retrieve a list of posts.                                 |
|                             | POST        | Create         | Create            | Create a new post.                                        |
| `/posts/<id>/`              | GET         | Read           | Detail            | Retrieve a specific post by ID.                           |
|                             | PUT         | Update         | Update            | Update a specific post by ID.                             |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific post by ID.                   |
|                             | DELETE      | Delete         | Delete            | Delete a specific post by ID.                             |
| **Comment Endpoints**                                                                       |
| `/comments/`                | GET         | Read           | List              | Retrieve a list of comments.                              |
|                             | POST        | Create         | Create            | Create a new comment.                                     |
| `/comments/<id>/`           | GET         | Read           | Detail            | Retrieve a specific comment by ID.                        |
|                             | PUT         | Update         | Update            | Update a specific comment by ID.                          |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific comment by ID.                |
|                             | DELETE      | Delete         | Delete            | Delete a specific comment by ID.                          |
| **Daily Routine Endpoints**                                                                |
| `/dailyroutines/`           | GET         | Read           | List              | Retrieve a list of daily routines.                        |
|                             | POST        | Create         | Create            | Create a new daily routine.                               |
| `/dailyroutines/<id>/`      | GET         | Read           | Detail            | Retrieve a specific daily routine by ID.                  |
|                             | PUT         | Update         | Update            | Update a specific daily routine by ID.                    |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific daily routine by ID.          |
|                             | DELETE      | Delete         | Delete            | Delete a specific daily routine by ID.                    |
| **Challenge Endpoints**                                                                   |
| `/challenges/`              | GET         | Read           | List              | Retrieve a list of challenges.                            |
|                             | POST        | Create         | Create            | Create a new challenge.                                   |
| `/challenges/<id>/`         | GET         | Read           | Detail            | Retrieve a specific challenge by ID.                      |
|                             | PUT         | Update         | Update            | Update a specific challenge by ID.                        |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific challenge by ID.              |
|                             | DELETE      | Delete         | Delete            | Delete a specific challenge by ID.                        |
| `/challenges/<id>/join/`    | POST        | Create         | Action            | Join a specific challenge.                                |
| `/challenges/<id>/leave/`   | POST        | Create         | Action            | Leave a specific challenge.                               |
| **Collaborate Endpoints**                                                                 |
| `/collaborate/`             | GET         | Read           | List              | Retrieve a list of collaboration messages.                |
|                             | POST        | Create         | Create            | Create a new collaboration message.                       |
| `/collaborate/<id>/`        | GET         | Read           | Detail            | Retrieve a specific collaboration message by ID.          |
|                             | DELETE      | Delete         | Delete            | Delete a specific collaboration message by ID.            |
| **Like Endpoints**                                                                         |
| `/likes/`                   | GET         | Read           | List              | Retrieve a list of likes.                                 |
|                             | POST        | Create         | Create            | Create a new like.                                        |
| `/likes/<id>/`              | DELETE      | Delete         | Delete            | Delete a specific like by ID.                             |
| **Follower Endpoints**                                                                     |
| `/followers/`               | GET         | Read           | List              | Retrieve a list of followers.                             |
|                             | POST        | Create         | Create            | Follow a user.                                            |
| `/followers/<id>/`          | DELETE      | Delete         | Delete            | Unfollow a user by ID.                                    |

### Example Requests and Responses

**Example: Create a Post**

**Request:**
```http
POST /posts/
{
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "tags": "fitness, health"
}
```

**Response:**
```json
201 Created
{
  "id": 1,
  "owner": "username",
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "tags": "fitness, health",
  "created_at": "2023-05-30T12:34:56.789Z",
  "updated_at": "2023-05-30T12:34:56.789Z",
  "comments_count": 0,
  "likes_count": 0
}
```

**Example: Retrieve Profile**

**Request:**
```http
GET /profiles/1/
```

**Response:**
```json
200 OK
{
  "id": 1,
  "user": "username",
  "bio": "This is a sample bio.",
  "image": "http://example.com/media/profile_images/sample.jpg",
  "email": "user@example.com",
  "birthday": "1990-01-01",
  "followers_count": 10,
  "following_count": 5,
  "posts_count": 3
}
```
## Frameworks, Libraries, and Dependencies

The Fit&Fine project leverages a variety of frameworks, libraries, and dependencies to ensure robust functionality and performance. Below is a detailed list of the key components used:

### Django Framework and Extensions

1. **Django** (`Django==3.2.25`):
   - A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django handles much of the complexity of web development, allowing developers to focus on writing their app without needing to reinvent the wheel.

2. **Django REST Framework** (`djangorestframework==3.15.1`):
   - A powerful and flexible toolkit for building Web APIs in Django. It provides various features such as serialization, authentication, and view sets that simplify API development.

3. **Django Allauth** (`django-allauth==0.44.0`):
   - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

4. **Django REST Auth** (`dj-rest-auth==2.1.9`):
   - Provides a set of REST API endpoints for handling user registration and authentication tasks. It’s built on top of Django Allauth and Django REST Framework.

5. **Django Filter** (`django-filter==2.4.0`):
   - Simplifies the process of filtering querysets in Django REST Framework.

6. **Django CORS Headers** (`django-cors-headers==4.3.1`):
   - A Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

### Database Management

7. **dj-database-url** (`dj-database-url==0.5.0`):
   - Allows you to utilize the DATABASE_URL environment variable to configure your Django application.

8. **psycopg2** (`psycopg2==2.9.9`):
   - PostgreSQL database adapter for Python.

### Authentication and Security

9. **djangorestframework-simplejwt** (`djangorestframework-simplejwt==4.7.2`):
   - Provides JSON Web Token (JWT) authentication for Django REST Framework.

10. **oauthlib** (`oauthlib==3.2.2`):
    - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python.

11. **requests-oauthlib** (`requests-oauthlib==2.0.0`):
    - OAuthlib support for Python-Requests, the ubiquitous HTTP library for Python.

12. **PyJWT** (`PyJWT==2.8.0`):
    - A Python library which allows you to encode and decode JSON Web Tokens (JWT).

### Storage and Image Handling

13. **Pillow** (`Pillow==8.2.0`):
    - Python Imaging Library (PIL) fork that supports opening, manipulating, and saving many different image file formats.

14. **Cloudinary** (`cloudinary==1.40.0`):
    - A library that integrates your application with the Cloudinary service for managing media assets such as images and videos.

15. **django-cloudinary-storage** (`django-cloudinary-storage==0.3.0`):
    - Facilitates the integration of Django with Cloudinary for storing media files.

### Application Server

16. **Gunicorn** (`gunicorn==22.0.0`):
    - A Python WSGI HTTP Server for UNIX that serves your Django application and allows it to handle multiple requests simultaneously.

### Utility Libraries

17. **asgiref** (`asgiref==3.8.1`):
    - A reference implementation of ASGI, the emerging Python standard for asynchronous web servers and applications.

18. **sqlparse** (`sqlparse==0.5.0`):
    - A non-validating SQL parser for Python.

19. **python3-openid** (`python3-openid==3.2.0`):
    - A set of Python packages to support OpenID authentication.

20. **pytz** (`pytz==2024.1`):
    - World timezone definitions, modern and historical.

This combination of frameworks, libraries, and dependencies ensures that Fit&Fine is robust, scalable, and secure, providing a seamless user experience for managing fitness routines and social interactions.

