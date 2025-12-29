# 🎓 MASTERY.AI

**AI-Powered Educational Platform** - Personalized learning with gamification and real-time collaboration.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/daaimpathan/MASTERY-AI-V2)

---

## 🚀 Quick Deploy

### Backend → Render.com

1. Go to **[render.com](https://render.com)** → Sign in with GitHub
2. Click **"New +"** → **"Web Service"**
3. Select repo: `daaimpathan/MASTERY-AI-V2`
4. Settings:
   - **Root Directory:** `backend`
   - **Build:** `pip install -r requirements.txt`
   - **Start:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add **PostgreSQL** (New + → PostgreSQL)
6. Add **Redis** (New + → Redis)
7. Environment Variables:
   ```
   DATABASE_URL=<internal-postgres-url>
   REDIS_URL=<internal-redis-url>
   SECRET_KEY=<random-secret>
   GEMINI_API_KEY=<your-key>
   ALLOWED_ORIGINS=https://your-app.netlify.app
   ```
8. **Deploy!** Copy backend URL

### Frontend → Netlify

1. Go to **[netlify.com](https://netlify.com)** → Sign in
2. **"Add site"** → Import from GitHub
3. Select: `daaimpathan/MASTERY-AI-V2`
4. Settings:
   - **Base:** `frontend`
   - **Build:** `npm run build`
   - **Publish:** `frontend/dist`
5. Environment Variables:
   ```
   VITE_API_URL=<your-render-backend-url>
   VITE_FIREBASE_API_KEY=<firebase-key>
   VITE_FIREBASE_PROJECT_ID=<project-id>
   VITE_FIREBASE_AUTH_DOMAIN=<auth-domain>
   VITE_FIREBASE_STORAGE_BUCKET=<bucket>
   VITE_FIREBASE_MESSAGING_SENDER_ID=<sender-id>
   VITE_FIREBASE_APP_ID=<app-id>
   ```
6. **Deploy!** 🎉

---

## 📱 Mobile Install (Local Dev)

1. Run `npm run dev` in frontend
2. Note the **Network URL**: `http://192.168.x.x:5173`
3. On phone (same WiFi):
   - Open Chrome/Safari
   - Go to Network URL
   - **Android:** Menu → "Install App"
   - **iOS:** Share → "Add to Home Screen"

---

## 🔐 Demo Login

**Password:** `password123`

| Role | Email |
|------|-------|
| Teacher | `teacher@mastery.ai` |
| Student | `student@mastery.ai` |
| Admin | `admin@mastery.ai` |

---

## ⚡ Local Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Edit with your config
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env  # Edit with your config
npm run dev
```

---

## 🎯 Features

- 🧠 **AI Tutor** - Gemini-powered assistance
- 📊 **Analytics** - Real-time progress tracking
- 🎮 **Gamification** - Points, badges, leaderboards
- 📝 **Assignments** - Rich media support
- 🔒 **Proof of Thought** - Anti-plagiarism system
- 🌐 **Real-time Collaboration** - Firebase integration

---

## 🛠️ Tech Stack

**Frontend:** React 18 · TypeScript · Vite · TailwindCSS · Three.js  
**Backend:** FastAPI · PostgreSQL · Redis · SQLAlchemy  
**AI:** Google Gemini · Firebase

---

## 📂 Structure

```
MASTERY-AI-V2/
├── backend/        # FastAPI + PostgreSQL
├── frontend/       # React + Vite
├── netlify.toml    # Netlify config
└── render.yaml     # Render config
```

---

## 👨‍💻 Author

**Daaim Pathan** - [@daaimpathan](https://github.com/daaimpathan)

---

<div align="center">Made with ❤️ for Education</div>
