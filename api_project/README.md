### API Authentication

This project uses token-based authentication.

#### How to Get a Token
POST to `/api-token-auth/` with:
- `username`
- `password`

#### Use Token:
Send in headers:
Authorization: Token <token_value>

### Permissions
- `UserViewSet`: requires authentication.
- `GroupViewSet`: admin-only access.
