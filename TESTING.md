# Fit&Fine DRF API Testing

## Table of contents

- [Fit\&Fine DRF API Testing](#fitfine-drf-api-testing)
  - [Table of contents](#table-of-contents)
  - [Manual Testing](#manual-testing)
    - [Authentication Endpoints](#authentication-endpoints)
    - [Profile Endpoints](#profile-endpoints)
    - [Post Endpoints](#post-endpoints)
    - [Comment Endpoints](#comment-endpoints)
    - [Daily Routine Endpoints](#daily-routine-endpoints)
    - [Challenge Endpoints](#challenge-endpoints)
    - [Collaborate Endpoints](#collaborate-endpoints)
    - [Like Endpoints](#like-endpoints)
    - [Follower Endpoints](#follower-endpoints)

##  Manual Testing

A series of manual tests were devised for each endpoint. The test data set included various users with different roles (admin, user). The API and front-end application were tested to ensure that they function as expected. Users should be able to access their own data, while admin users should have additional privileges, such as creating and editing user profiles, posts, comments, daily routines, challenges, and contacts. All users should be able to create events but only interact with their own posts and comments.

Tests were performed using the Django Rest Framework HTML interface running on a test server.

### Authentication Endpoints

| Endpoint                 | Method | CRUD Operation | Description                                      | Expected Result                  | Actual Result | Pass/Fail |
|--------------------------|--------|----------------|--------------------------------------------------|----------------------------------|---------------|-----------|
| `/dj-rest-auth/login/`   | POST   | Create         | Log in a user and obtain authentication tokens   | User logged in, tokens returned  | User logged in, tokens returned | PASS       |
| `/dj-rest-auth/logout/`  | POST   | Delete         | Log out a user and invalidate tokens             | User logged out, tokens invalidated | User logged out, tokens invalidated | PASS       |
| `/dj-rest-auth/registration/` | POST | Create      | Register a new user                              | User registered, details returned | User registered, details returned | PASS       |

### Profile Endpoints

| Endpoint                | Method | CRUD Operation | Description                               | Expected Result                          | Actual Result | Pass/Fail |
|-------------------------|--------|----------------|-------------------------------------------|------------------------------------------|---------------|-----------|
| `/profiles/`            | GET    | Read           | Retrieve a list of profiles               | List of profiles returned                | List of profiles returned | PASS       |
| `/profiles/`            | POST   | Create         | Create a new profile (admin only)         | Profile created, details returned        | Profile created, details returned | PASS       |
| `/profiles/<id>/`       | GET    | Read           | Retrieve a specific profile by ID         | Profile details returned                 | Profile details returned | PASS       |
| `/profiles/<id>/`       | PUT    | Update         | Update a specific profile by ID           | Profile updated, updated details returned | Profile updated, updated details returned | PASS       |
| `/profiles/<id>/`       | PATCH  | Update         | Partially update a specific profile by ID | Profile partially updated, updated details returned | Profile partially updated, updated details returned | PASS       |
| `/profiles/<id>/`       | DELETE | Delete         | Delete a specific profile by ID (admin only) | Profile deleted                          | Profile deleted | PASS       |

### Post Endpoints

| Endpoint             | Method | CRUD Operation | Description                          | Expected Result                         | Actual Result | Pass/Fail |
|----------------------|--------|----------------|--------------------------------------|-----------------------------------------|---------------|-----------|
| `/posts/`            | GET    | Read           | Retrieve a list of posts             | List of posts returned                  | List of posts returned | PASS       |
| `/posts/`            | POST   | Create         | Create a new post                    | Post created, details returned          | Post created, details returned | PASS       |
| `/posts/<id>/`       | GET    | Read           | Retrieve a specific post by ID       | Post details returned                   | Post details returned | PASS       |
| `/posts/<id>/`       | PUT    | Update         | Update a specific post by ID         | Post updated, updated details returned  | Post updated, updated details returned | PASS       |
| `/posts/<id>/`       | PATCH  | Update         | Partially update a specific post by ID | Post partially updated, updated details returned | Post partially updated, updated details returned | PASS       |
| `/posts/<id>/`       | DELETE | Delete         | Delete a specific post by ID         | Post deleted                            | Post deleted | PASS       |

### Comment Endpoints

| Endpoint              | Method | CRUD Operation | Description                             | Expected Result                          | Actual Result | Pass/Fail |
|-----------------------|--------|----------------|-----------------------------------------|------------------------------------------|---------------|-----------|
| `/comments/`          | GET    | Read           | Retrieve a list of comments             | List of comments returned                | List of comments returned | PASS       |
| `/comments/`          | POST   | Create         | Create a new comment                    | Comment created, details returned        | Comment created, details returned | PASS       |
| `/comments/<id>/`     | GET    | Read           | Retrieve a specific comment by ID       | Comment details returned                 | Comment details returned | PASS       |
| `/comments/<id>/`     | PUT    | Update         | Update a specific comment by ID         | Comment updated, updated details returned | Comment updated, updated details returned | PASS       |
| `/comments/<id>/`     | PATCH  | Update         | Partially update a specific comment by ID | Comment partially updated, updated details returned | Comment partially updated, updated details returned | PASS       |
| `/comments/<id>/`     | DELETE | Delete         | Delete a specific comment by ID         | Comment deleted                          | Comment deleted | PASS       |

### Daily Routine Endpoints

| Endpoint                   | Method | CRUD Operation | Description                               | Expected Result                          | Actual Result | Pass/Fail |
|----------------------------|--------|----------------|-------------------------------------------|------------------------------------------|---------------|-----------|
| `/dailyroutines/`          | GET    | Read           | Retrieve a list of daily routines         | List of daily routines returned          | List of daily routines returned | PASS       |
| `/dailyroutines/`          | POST   | Create         | Create a new daily routine                | Daily routine created, details returned  | Daily routine created, details returned | PASS       |
| `/dailyroutines/<id>/`     | GET    | Read           | Retrieve a specific daily routine by ID   | Daily routine details returned           | Daily routine details returned | PASS       |
| `/dailyroutines/<id>/`     | PUT    | Update         | Update a specific daily routine by ID     | Daily routine updated, updated details returned | Daily routine updated, updated details returned | PASS       |
| `/dailyroutines/<id>/`     | PATCH  | Update         | Partially update a specific daily routine by ID | Daily routine partially updated, updated details returned | Daily routine partially updated, updated details returned | PASS       |
| `/dailyroutines/<id>/`     | DELETE | Delete         | Delete a specific daily routine by ID     | Daily routine deleted                    | Daily routine deleted | PASS       |

### Challenge Endpoints

| Endpoint                  | Method | CRUD Operation | Description                              | Expected Result                          | Actual Result | Pass/Fail |
|---------------------------|--------|----------------|------------------------------------------|------------------------------------------|---------------|-----------|
| `/challenges/`            | GET    | Read           | Retrieve a list of challenges            | List of challenges returned              | List of challenges returned | PASS       |
| `/challenges/`            | POST   | Create         | Create a new challenge                   | Challenge created, details returned      | Challenge created, details returned | PASS       |
| `/challenges/<id>/`       | GET    | Read           | Retrieve a specific challenge by ID      | Challenge details returned               | Challenge details returned | PASS       |
| `/challenges/<id>/`       | PUT    | Update         | Update a specific challenge by ID        | Challenge updated, updated details returned | Challenge updated, updated details returned | PASS       |
| `/challenges/<id>/`       | PATCH  | Update         | Partially update a specific challenge by ID | Challenge partially updated, updated details returned | Challenge partially updated, updated details returned | PASS       |
| `/challenges/<id>/`       | DELETE | Delete         | Delete a specific challenge by ID        | Challenge deleted                        | Challenge deleted | PASS       |
| `/challenges/<id>/join/`  | POST   | Create         | Join a specific challenge                | Joined challenge                         | Joined challenge | PASS       |
| `/challenges/<id>/leave/` | POST   | Create         | Leave a specific challenge               | Left challenge                           | Left challenge | PASS       |

### Collaborate Endpoints

| Endpoint                    | Method | CRUD Operation | Description                                  | Expected Result                           | Actual Result | Pass/Fail |
|-----------------------------|--------|----------------|----------------------------------------------|-------------------------------------------|---------------|-----------|
| `/collaborate/`             | GET    | Read           | Retrieve a list of collaboration messages    | List of collaboration messages returned   | List of collaboration messages returned | PASS       |
| `/collaborate/`             | POST   | Create         | Create a new collaboration message           | Collaboration message created, details returned | Collaboration message created, details returned | PASS       |
| `/collaborate/<id>/`        | GET    | Read           | Retrieve a specific collaboration message by ID | Collaboration message details returned    | Collaboration message details returned | PASS       |
| `/collaborate/<id>/`        | DELETE | Delete         | Delete a specific collaboration message by ID | Collaboration message deleted             | Collaboration message deleted | PASS       |

### Like Endpoints

| Endpoint             | Method | CRUD Operation | Description                           | Expected Result                     | Actual Result | Pass/Fail |
|----------------------|--------|----------------|---------------------------------------|-------------------------------------|---------------|-----------|
| `/likes/`            | GET    | Read           | Retrieve a list of likes              | List of likes returned              | List of likes returned | PASS       |
| `/likes/`            | POST   | Create         | Create a new like                     | Like created, details returned      | Like created, details returned | PASS       |
| `/likes/<id>/`       | DELETE | Delete         | Delete a specific like by ID          | Like deleted                        | Like deleted | PASS       |

### Follower Endpoints

| Endpoint               | Method | CRUD Operation | Description                          | Expected Result                     | Actual Result | Pass/Fail |
|------------------------|--------|----------------|--------------------------------------|-------------------------------------|---------------|-----------|
| `/followers/` | GET    | Read           | Retrieve a list of followers         | List of followers returned          | List of followers returned | PASS       |
| `/followers/`          | POST   | Create         | Follow a user                        | Follow successful                   | Follow successful | PASS       |
| `/followers/<id>/`     | DELETE | Delete         | Unfollow a user by ID                | Unfollow successful                 | Unfollow successful | PASS       |

This table provides a clear overview of the API endpoints tested, including their HTTP methods, descriptions, CRUD operations, expected and actual results, and whether the test passed or failed.