# Social Media API (Django + DRF)

A feature-rich **Social Media Backend API** built with **Django** and **Django REST Framework (DRF)**.  
The API powers core social media features including authentication, posts, comments, follows, likes, feeds, and notifications.  

**Live Deployment**: [Social Media API on Render](https://social-media-api-sysh.onrender.com)  
**Repository**: [GitHub Repo](https://github.com/Topzee001/Alx_DjangoLearnLab/tree/main/social_media_api)

---

## Features

- **User Authentication**
  - Register & login (JWT authentication)
  - Profile management
- **Posts & Comments**
  - Create, view, update, delete posts & comments
  - Pagination & filtering (`?search=<query>`)
- **User Interactions**
  - Follow/unfollow users
  - Personalized feed from followed users
- **Likes & Notifications**
  - Like/unlike posts
  - Receive real-time notifications (follows, likes, comments)

---

## Project Structure

social_media_api/  
│── accounts/ # User authentication, follow/unfollow  
│── posts/ # Posts, comments, likes, feeds  
│── notifications/ # User notifications  
│── social_media_api/ # Core project settings & routes  

---

## Installation & Setup

```bash:disable-run ```
# Clone repository
git clone https://github.com/Topzee001/social_media_api.git
cd social_api

# Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (admin access)
python manage.py createsuperuser

# Run server
python manage.py runserver

## Authentication
This project uses **JWT Authentication**.  
After login/registration, you’ll receive a token.  
Include it in headers for protected endpoints:

Authorization: Bearer <your_token>

---

## API Endpoints

### Accounts
- **POST** `/api/accounts/register/` → Register user  
- **POST** `/api/accounts/login/` → Login & get token
- **GET** `/api/accounts/profile/` → Profile
- **POST** `/api/accounts/follow/<user_id>/` → Follow user  
- **POST** `/api/accounts/unfollow/<user_id>/` → Unfollow user  

### Posts & Comments
- **GET** `/api/posts/` → List posts  
- **POST** `/api/posts/` → Create post  
- **GET** `/api/posts/<id>/` → Retrieve post  
- **PUT** `/api/posts/<id>/` → Update post  
- **DELETE** `/api/posts/<id>/` → Delete post  
- **POST** `/api/posts/<id>/like/` → Like post  
- **POST** `/api/posts/<id>/unlike/` → Unlike post  

### Comments
- **POST** `/api/comments/` → Create comment  
- **PUT** `/api/comments/<id>/` → Update comment  
- **DELETE** `/api/comments/<id>/` → Delete comment  

### Feed
- **GET** `/api/feed/` → Posts from followed users  

### Notifications
- **GET** `/api/notifications/` → User’s notifications  

---

### Example Response

```json
[
  {
    "id": 1,
    "actor": "jane_doe",
    "verb": "liked your post",
    "target": "My first post",
    "timestamp": "2025-08-24T21:12:00Z",
    "read": false
  }
]
```

## Notifications Model (Simplified)

```python
class Notification(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  
    target = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    action_object = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```
## Tech Stack
Backend: Django 5, Django REST Framework

Database: PostgreSQL/MySQL

Auth: JWT Authentication

Hosting: Render

Tools: Postman

