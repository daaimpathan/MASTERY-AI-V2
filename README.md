# 🎓 MASTERY.AI - Complete Deployment Guide

**AI-Powered Educational Platform** with step-by-step deployment roadmap for Render & Netlify.

---

## 📋 Table of Contents

1. [What You'll Deploy](#what-youll-deploy)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step: Deploy Backend to Render](#step-by-step-deploy-backend-to-render)
4. [Step-by-Step: Deploy Frontend to Netlify](#step-by-step-deploy-frontend-to-netlify)
5. [Demo Credentials](#demo-credentials)
6. [Local Development](#local-development)

---

## 🎯 What You'll Deploy

- **Backend (Render.com):** FastAPI server + PostgreSQL database + Redis cache
- **Frontend (Netlify):** React app with Vite
- **Total Cost:** **FREE** (using free tiers)

---

## ✅ Prerequisites

Before starting, make sure you have:

- ✅ GitHub account (with this repo pushed)
- ✅ [Render.com](https://render.com) account (sign up with GitHub)
- ✅ [Netlify](https://netlify.com) account (sign up with GitHub)
- ✅ Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))
- ✅ Firebase project ([Create here](https://console.firebase.google.com))

---

## 🚀 Step-by-Step: Deploy Backend to Render

### Step 1: Create PostgreSQL Database

1. Go to **[Render Dashboard](https://dashboard.render.com)**
2. Click **"New +"** button (top right)
3. Select **"PostgreSQL"**
4. Fill in:
   - **Name:** `mastery-ai-db`
   - **Database:** `mastery_db`
   - **User:** `mastery_user`
   - **Region:** Choose closest to you
   - **Plan:** **Free**
5. Click **"Create Database"**
6. ⏳ Wait 2-3 minutes for database to be ready
7. 📋 **Copy "Internal Database URL"** (you'll need this later)

---

### Step 2: Create Redis Instance

1. In Render Dashboard, click **"New +"**
2. Select **"Key Value"** *(this is Redis in Render)*
3. Fill in:
   - **Name:** `mastery-ai-redis`
   - **Region:** Same as your database
   - **Plan:** **Free**
4. Click **"Create Key Value Store"**
5. ⏳ Wait 1-2 minutes
6. 📋 **Copy "Internal Redis URL"** (you'll need this later)

---

### Step 3: Create Web Service (Backend)

1. In Render Dashboard, click **"New +"**
2. Select **"Web Service"**
3. Click **"Connect a repository"**
4. Find and select: **`daaimpathan/MASTERY-AI-V2`**
5. Click **"Connect"**

---

### Step 4: Configure Backend Service

Fill in these settings:

| Field | Value |
|-------|-------|
| **Name** | `mastery-ai-backend` |
| **Region** | Same as database |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| **Plan** | **Free** |

---

### Step 5: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"** and add these:

| Key | Value | Where to get it |
|-----|-------|-----------------|
| `DATABASE_URL` | `<paste-internal-db-url>` | From Step 1 |
| `REDIS_URL` | `<paste-internal-redis-url>` | From Step 2 |
| `SECRET_KEY` | `your-random-secret-key-123` | Make up a random string |
| `GEMINI_API_KEY` | `AIza...` | [Get from Google](https://makersuite.google.com/app/apikey) |
| `ALLOWED_ORIGINS` | `https://your-app.netlify.app` | We'll update this later |
| `ALGORITHM` | `HS256` | Exactly this |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Exactly this |

**Note:** For `ALLOWED_ORIGINS`, use a placeholder for now. We'll update it after deploying frontend.

---

### Step 6: Deploy Backend

1. Click **"Create Web Service"**
2. ⏳ Wait 5-10 minutes for first deployment
3. Watch the logs - should see "Application startup complete"
4. 📋 **Copy your backend URL:** `https://mastery-ai-backend.onrender.com`
5. ✅ Test it: Open `https://mastery-ai-backend.onrender.com/docs` - should see API docs!

---

## 🎨 Step-by-Step: Deploy Frontend to Netlify

### Step 1: Go to Netlify

1. Go to **[Netlify Dashboard](https://app.netlify.com)**
2. Click **"Add new site"** → **"Import an existing project"**

---

### Step 2: Connect Repository

1. Click **"Deploy with GitHub"**
2. Authorize Netlify (if first time)
3. Search and select: **`daaimpathan/MASTERY-AI-V2`**
4. Click on the repository

---

### Step 3: Configure Build Settings

Fill in these settings:

| Field | Value |
|-------|-------|
| **Branch to deploy** | `main` |
| **Base directory** | `frontend` |
| **Build command** | `npm run build` |
| **Publish directory** | `frontend/dist` |

---

### Step 4: Add Environment Variables

Click **"Show advanced"** → **"New variable"** and add these:

| Key | Value | Where to get it |
|-----|-------|-----------------|
| `VITE_API_URL` | `https://mastery-ai-backend.onrender.com` | From backend deployment |
| `VITE_FIREBASE_API_KEY` | `AIza...` | Firebase Console → Project Settings |
| `VITE_FIREBASE_PROJECT_ID` | `your-project-id` | Firebase Console |
| `VITE_FIREBASE_AUTH_DOMAIN` | `your-project.firebaseapp.com` | Firebase Console |
| `VITE_FIREBASE_STORAGE_BUCKET` | `your-project.appspot.com` | Firebase Console |
| `VITE_FIREBASE_MESSAGING_SENDER_ID` | `123456789` | Firebase Console |
| `VITE_FIREBASE_APP_ID` | `1:123:web:abc` | Firebase Console |

**Get Firebase config:**
1. Go to [Firebase Console](https://console.firebase.google.com)
2. Select your project (or create new)
3. Click ⚙️ Settings → Project Settings
4. Scroll to "Your apps" → Web app
5. Copy all the config values

---

### Step 5: Deploy Frontend

1. Click **"Deploy site"**
2. ⏳ Wait 3-5 minutes
3. 📋 **Copy your site URL:** `https://your-app-name.netlify.app`
4. ✅ Open the URL - your app should be live! 🎉

---

### Step 6: Update Backend CORS

Now update backend to allow your frontend:

1. Go back to **Render Dashboard**
2. Open your **backend service**
3. Go to **"Environment"** tab
4. Find `ALLOWED_ORIGINS`
5. Update value to: `https://your-app-name.netlify.app`
6. Click **"Save Changes"**
7. Backend will auto-redeploy (wait 2-3 minutes)

---

## 🔐 Demo Credentials

Login with these accounts (password: `password123`):

| Role | Email | Name |
|------|-------|------|
| **Teacher** | `teacher@mastery.ai` | Theresa Teacher |
| **Student** | `student@mastery.ai` | Samuel Student |
| **Student** | `sarah@mastery.ai` | Sarah Miller |
| **Student** | `alex@mastery.ai` | Alex Thompson |
| **Admin** | `admin@mastery.ai` | Arthur Admin |

---

## 💻 Local Development

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your local config
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env
# Edit .env with your local config
npm run dev
```

**Access:** `http://localhost:5173`

---

## 📱 Mobile Install (Local Dev)

1. Run `npm run dev` in frontend folder
2. Note the **Network URL** in terminal: `http://192.168.x.x:5173`
3. On your phone (connected to same WiFi):
   - Open Chrome (Android) or Safari (iOS)
   - Go to the Network URL
   - **Android:** Menu (⋮) → "Install App"
   - **iOS:** Share button → "Add to Home Screen"

---

## 🛠️ Tech Stack

**Frontend:** React 18 · TypeScript · Vite · TailwindCSS · Three.js · Framer Motion  
**Backend:** FastAPI · PostgreSQL · Redis · SQLAlchemy · Alembic  
**AI/ML:** Google Gemini API · Firebase

---

## 📂 Project Structure

```
MASTERY-AI-V2/
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── models/       # Database models
│   │   ├── services/     # Business logic
│   │   └── config.py     # Configuration
│   ├── alembic/          # DB migrations
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── features/     # Feature modules
│   │   └── services/     # API services
│   └── package.json
├── netlify.toml          # Netlify config
└── render.yaml           # Render config
```

---

## � Troubleshooting

### Backend won't start
- Check logs in Render dashboard
- Verify all environment variables are set
- Make sure DATABASE_URL and REDIS_URL are correct

### Frontend shows API errors
- Check `VITE_API_URL` points to your Render backend
- Verify backend `ALLOWED_ORIGINS` includes your Netlify URL
- Check browser console for CORS errors

### Database connection failed
- Make sure you're using **Internal Database URL** (not External)
- Check if database is in same region as backend service

---

## �👨‍💻 Author

**Daaim Pathan** - [@daaimpathan](https://github.com/daaimpathan)

---

<div align="center">
  <strong>Made with ❤️ for Education</strong>
  <br><br>
  <a href="https://render.com">Deploy Backend</a> · 
  <a href="https://netlify.com">Deploy Frontend</a> · 
  <a href="https://github.com/daaimpathan/MASTERY-AI-V2/issues">Report Bug</a>
</div>
