# Backend Practice Notes

## Day 1 – Project Setup
- Created Django project and users app
- Configured Django REST Framework
- Implemented health check API to verify setup

## Day 2 – User APIs & Pagination
- Implemented RESTful CRUD APIs for UserProfile
- Added custom pagination using PageNumberPagination
- Used get_object_or_404 for safe object retrieval
- Implemented proper HTTP status codes for all responses
- Tested all APIs using Postman

### Implemented APIs
- GET (list) → Fetch users with pagination
- GET (detail) → Fetch single user by ID
- POST → Create a new user
- PUT → Full update of user data
- PATCH → Partial update of user data
- DELETE → Delete user with confirmation response

### Pagination
- Custom PageNumberPagination
- Improves performance for large datasets
- Returns count, next, previous, and results

### Error Handling
- Used appropriate HTTP status codes (200, 201, 204, 400, 404)
- Validation handled using DRF serializers
- Handled missing objects using get_object_or_404
