# Onboarding Profile Stack

FastAPI microservice for managing user onboarding profiles and job search settings.

## Features

- User profile management (onboarding data including career preferences)
- JWT authentication with Supabase
- Development mode for easy testing
- CORS-enabled for frontend integration

## Setup

### 1. Create Virtual Environment

```bash
cd "d:\Projects\RESUME MINI PROJECT\ONBOARDING"
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows PowerShell:**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**
```bash
.\venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

The `.env` file is already configured with Supabase credentials. Make sure `DEV_MODE=true` is set for testing.

## Running the Server

```bash
uvicorn app.main:app --reload --port 8001
```

The server will start at: `http://localhost:8001`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

## Endpoints

### Health Check
- **GET** `/health` - Service health status

### Onboarding Profile
- **GET** `/v1/onboarding` - Get user's profile
- **PUT** `/v1/onboarding` - Update/create profile (includes career preferences)

## Testing with Postman

### Authentication (Dev Mode)

Since `DEV_MODE=true`, you can use a simple user ID as the token:

**Header:**
```
Authorization: Bearer test-user-123
```

Replace `test-user-123` with any user ID. The service will create/update records for that user ID.

### Example: Create/Update Profile

**Request:**
```
PUT http://localhost:8001/v1/onboarding
```

**Headers:**
```
Authorization: Bearer test-user-123
Content-Type: application/json
```

**Body:**
```json
{
  "full_name": "John Doe",
  "data_of_birth": "1995-05-15",
  "secondary_email": "john.secondary@example.com",
  "address": "123 Main St, Bangalore",
  "linkedin_url": "https://linkedin.com/in/johndoe",
  "github_username": "johndoe",
  "skills": "Python, FastAPI, AWS, Docker",
  "career_preferences": {
    "roles_targeted": ["Backend Developer", "DevOps Engineer"],
    "min_target_lpa": 12,
    "preferred_locations": ["Bangalore", "Remote"]
  },
  "education": {
    "degree": "B.Tech",
    "field": "Computer Science",
    "institution": "XYZ University",
    "year": 2020
  },
  "onboarding_completed": true
}
```

**Response:**
```json
{
  "id": "test-user-123",
  "full_name": "John Doe",
  "data_of_birth": "1995-05-15",
  "secondary_email": "john.secondary@example.com",
  ...
  "created_at": "2025-11-25T17:15:00",
  "updated_at": "2025-11-25T17:15:00"
}
```

### Example: Get Profile

**Request:**
```
GET http://localhost:8001/v1/onboarding
```

**Headers:**
```
Authorization: Bearer test-user-123
```

### Example: Update Job Settings

**Request:**
```
PUT http://localhost:8001/v1/settings/job
```

**Headers:**
```
Authorization: Bearer test-user-123
Content-Type: application/json
```

**Body:**
```json
{
  "search_active": true,
  "auto_apply": false,
  "portals": ["LinkedIn", "Naukri", "Indeed"],
  "roles": ["Backend Developer", "Full Stack Developer"],
  "locations": ["Bangalore", "Hyderabad", "Remote"],
  "min_lpa": 12,
  "company_types": ["Startup", "Product"]
}
```

## Database Tables

### profiles
- `id` (uuid, primary key) - User ID from Supabase Auth
- `full_name` (text)
- `date_of_birth` (date)
- `secondary_email` (text)
- `address` (text)
- `linkedin_url` (text)
- `github_username` (text)
- `skills` (text[]) - Array of skills
- `career_preferences` (jsonb) - Contains roles, min LPA, locations, etc.
- `onboarding_completed` (boolean)
- `created_at` (timestamptz)
- `updated_at` (timestamptz)
- `profile_photo_url` (text)
- `govt_id_url` (text)
- `education` (jsonb)
- `api_keys` (jsonb)

## Production Deployment

For production:

1. Set `DEV_MODE=false` in `.env`
2. Configure proper JWT secret from Supabase
3. Update CORS origins to your frontend domain
4. Deploy to AWS Lambda using SAM or similar
5. Ensure Supabase service role key is stored securely

## Troubleshooting

### Virtual Environment Issues
If you get execution policy errors on Windows:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Port Already in Use
Change the port number:
```bash
uvicorn app.main:app --reload --port 8002
```

### Supabase Connection Issues
- Verify `SUPABASE_URL` and `SUPABASE_KEY` in `.env`
- Check if tables exist in Supabase dashboard
- Ensure service role key has proper permissions
