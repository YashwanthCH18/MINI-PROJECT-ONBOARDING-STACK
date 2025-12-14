# Onboarding Profile Stack

FastAPI microservice for managing user onboarding profiles.

**Base URL:** `https://c3a24cwqti.execute-api.ap-south-1.amazonaws.com/Prod/`

## 📚 Integration Guide
For detailed API usage, request/response formats, and frontend integration flows, please see **[INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)**.

## Features
- **User Profile Management**: Single endpoint for creating and updating profiles.
- **Supabase Integration**: Direct secure connection to `profiles` table.
- **JWT Authentication**: Validates Supabase Auth tokens (Access Tokens).
- **Serverless**: Deployed on AWS Lambda via SAM.

## Setup & Development

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Local Development
To run locally, you must have a valid Supabase `.env` file.
```bash
uvicorn app.main:app --reload --port 8001
```

### 3. Deployment
Deployed via AWS SAM (Serverless Application Model).

```bash
# Build
sam build

# Deploy (Interactive)
sam deploy --guided
```
**Required Secrets during deployment:** `SupabaseUrl`, `SupabaseKey`, `SecretKey`.

## Database Tables

### `profiles`
- `id` (uuid, primary key) - Matches Supabase Auth User ID
- `full_name`, `date_of_birth`, `address`...
- `skills` (text[])
- `career_preferences` (jsonb)
- `education` (jsonb)
- `onboarding_completed` (boolean)

## Troubleshooting
- **401 Unauthorized**: Ensure your token is fresh and from Supabase (not a custom signed token).
- **Invalid Audience**: Ensure the token has `"aud": "authenticated"`.
- **500 Internal Server Error**: Check Lambda environment variables in AWS Console.
