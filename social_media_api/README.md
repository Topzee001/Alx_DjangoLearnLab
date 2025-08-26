📌 Social Media API (Django + DRF)
This project is a social media backend API built with Django and Django REST Framework (DRF).
It provides functionality for user authentication, following/unfollowing, personalized feeds, and real-time notifications.
🚀 Features
User Authentication
Registration (with token retrieval)
Login (JWT authentication)
User Interactions
Follow and unfollow other users
Feed
Get posts from users you follow
Notifications
Get activity notifications when users interact (follow/unfollow, post, like, etc.)
📂 Project Structure
social_api/
│── accounts/          # Handles user registration, login, follow/unfollow
│   ├── models.py      # Custom User model
│   ├── serializers.py # Serializers for registration, login
│   ├── views.py       # Registration, login, follow/unfollow APIs
│
│── feed/              # Handles posts and user feeds
│   ├── models.py      # Post model
│   ├── serializers.py # Post serializer
│   ├── views.py       # Feed APIView (class-based)
│
│── notifications/     # Handles user notifications
│   ├── models.py      # Notification model
│   ├── serializers.py # Notification serializer
│   ├── views.py       # Notification list API
│
│── social_api/
│   ├── settings.py    # Django settings
│   ├── urls.py        # Project-wide routes
⚙️ Installation & Setup
Clone the repository
git clone https://github.com/your-username/social_api.git
cd social_api
Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
Run migrations
python manage.py migrate
Create superuser
python manage.py createsuperuser
Run server
python manage.py runserver
🔑 Authentication
This project uses JWT (JSON Web Tokens) for authentication.
After login/registration, the user receives a token which must be passed in headers:
Authorization: Bearer <your_token>
📡 API Endpoints
Accounts
POST /api/accounts/register/ → Register a new user
POST /api/accounts/login/ → Login & get token
POST /api/accounts/follow/<user_id>/ → Follow a user
POST /api/accounts/unfollow/<user_id>/ → Unfollow a user
Feed
GET /api/feed/ → Get posts from users you follow
Notifications
GET /api/notifications/ → List all notifications for authenticated user
🔔 Notifications Explained
The Notification model is central to how activity is tracked.
Each notification stores what happened, who did it, and what it was about.
Model
class Notification(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    verb = models.CharField(max_length=255)  # e.g. "followed", "liked", "commented"
    target = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="targeted_notifications")
    action_object = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE, related_name="action_notifications")
    created_at = models.DateTimeField(auto_now_add=True)
Field Explanation
actor → The user who performed the action
Example: User A
verb → The action performed
Example: "followed"
target → The user who the action was performed on
Example: User B
action_object → (Optional) The object related to the action
Example: A Post that was liked or commented on
created_at → Timestamp of when the action occurred
Example
If User A follows User B:
actor = User A
verb = "followed"
target = User B
action_object = None
Stored as:
{
  "actor": "User A",
  "verb": "followed",
  "target": "User B",
  "action_object": null,
  "created_at": "2025-08-24T10:00:00Z"
}
If User A likes User B’s post:
actor = User A
verb = "liked"
target = User B
action_object = Post (id=1)
Stored as:
{
  "actor": "User A",
  "verb": "liked",
  "target": "User B",
  "action_object": "Post 1",
  "created_at": "2025-08-24T10:05:00Z"
}
Serializer
class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.StringRelatedField()
    action_object = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'action_object', 'created_at']
View
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(target=self.request.user)
✅ Example Flow
User A registers & logs in → gets token.
User A follows User B → A Notification is created for User B.
User A posts something → Followers see it in their feed.
User B checks notifications → sees "User A followed you".
🛠️ Tech Stack
Python 3.x
Django 5.x
Django REST Framework
JWT Authentication
📜 License
This project is licensed under the MIT License.
Would you like me to also add a visual diagram (flow chart of how notifications are created and consumed) to your README? That could make it easier for anyone reading it to quickly understand.






Post endpoints (/api/posts/) → list, create, retrieve, update, delete.
Comment endpoints (/api/comments/) → list, create, retrieve, update, delete.
Example payloads (like above).
Mention pagination + filtering (?search=hello).

Likes
POST /posts/<id>/like/ → Like a post
POST /posts/<id>/unlike/ → Unlike a post


Notifications
GET /notifications/ → List of user’s notifications
Sample response:
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