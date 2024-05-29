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

## Planning
- [Project Goals](#project-goals)
- [Table of contents](#table-of-contents)
- [Planning](#planning)
  - [Project Overview](#project-overview)
  - [Objectives](#objectives)
  - [Timeline](#timeline)
- [Data Models](#data-models)
  - [1. User Profile Model](#1-user-profile-model)
  - [2. Posts Model](#2-posts-model)
  - [3. Comments Model](#3-comments-model)
  - [4. Daily Routines Model](#4-daily-routines-model)
  - [5. Challenges Model](#5-challenges-model)
  - [6. Collaborate Model](#6-collaborate-model)
  - [7. Likes Model](#7-likes-model)
  - [8. Follower Model](#8-follower-model)
- [API Endpoints](#api-endpoints)
  - [Authentication Endpoints](#authentication-endpoints)
  - [Profile Endpoints](#profile-endpoints)
  - [Post Endpoints](#post-endpoints)
  - [Comment Endpoints](#comment-endpoints)
  - [Daily Routine Endpoints](#daily-routine-endpoints)
  - [Challenge Endpoints](#challenge-endpoints)
  - [Collaborate Endpoints](#collaborate-endpoints)
  - [Like Endpoints](#like-endpoints)
  - [Follower Endpoints](#follower-endpoints)
  - [Example Requests and Responses](#example-requests-and-responses)
    - [Example: Create a Post](#example-create-a-post)
    - [Example: Retrieve Profile](#example-retrieve-profile)
- [Frameworks, Libraries, and Dependencies](#frameworks-libraries-and-dependencies)
  - [Django Framework and Extensions](#django-framework-and-extensions)
  - [Database Management](#database-management)
  - [Authentication and Security](#authentication-and-security)
  - [Storage and Image Handling](#storage-and-image-handling)
  - [Application Server](#application-server)
  - [Utility Libraries](#utility-libraries)

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

