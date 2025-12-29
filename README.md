# 🎓 MASTERY.AI - AI-Powered Educational Platform

> A comprehensive learning management system with AI-driven personalization, gamification, and real-time collaboration tools.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---

## 📱 How to Install on Mobile

I enabled **"Network Mode"** for your app so your phone can see it.

### Step 1: Restart Server

1. Stop the server (`Ctrl+C`)
2. Run `npm run dev` again
3. **Look closely at the output** - It will show something like:

```
➜  Local:   http://localhost:5173/
➜  Network: http://192.168.1.5:5173/  <-- THIS IS YOUR KEY 🔑
```

### Step 2: Connect Phone

1. Make sure your phone is on the **Same Wi-Fi** as your computer
2. Open Chrome (Android) or Safari (iOS)
3. Type that **Network URL** (e.g., `http://192.168.1.x:5173`)

### Step 3: Install

- **Android (Chrome):** Tap the "Three Dots" menu → "Install App" (or "Add to Home Screen")
- **iOS (Safari):** Tap the "Share" button (Square with arrow) → Scroll down → "Add to Home Screen"

---

## 🔐 Demo Credentials

**Password for all:** `password123`

| Role | Email | Name |
|------|-------|------|
| **Teacher** | `teacher@mastery.ai` | Theresa Teacher |
| **Student** | `student@mastery.ai` | Samuel Student |
| **Student** | `sarah@mastery.ai` | Sarah Miller |
| **Student** | `alex@mastery.ai` | Alex Thompson |
| **Admin** | `admin@mastery.ai` | Arthur Admin |

---

## ✨ Features

### 🎯 For Students
- **Personalized Learning Paths** - AI-driven curriculum adaptation
- **Interactive Assignments** - Real-time collaboration and submission
- **Progress Tracking** - Visual analytics and mastery metrics
- **Gamification** - Points, badges, and leaderboards
- **Resource Library** - Curated learning materials
- **AI Tutor Bot** - 24/7 intelligent assistance

### 👨‍🏫 For Teachers
- **Class Management** - Student enrollment and monitoring
- **Assignment Creation** - Rich media support and auto-grading
- **Analytics Dashboard** - Student performance insights
- **Resource Sharing** - Upload and organize materials
- **Real-time Feedback** - Instant student engagement metrics
- **Proof of Thought** - Anti-plagiarism verification system

### 🔧 For Admins
- **User Management** - Role-based access control
- **System Analytics** - Platform-wide metrics
- **Content Moderation** - Quality assurance tools

---

## 🚀 Tech Stack

### Frontend
- **React 18** with TypeScript
- **Vite** - Lightning-fast build tool
- **TailwindCSS** - Utility-first styling
- **Zustand** - State management
- **Three.js** - 3D visualizations
- **Framer Motion** - Smooth animations

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational database
- **Redis** - Caching and sessions
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations
- **JWT** - Authentication

### AI/ML
- **Google Gemini API** - AI-powered features
- **Firebase** - Real-time database

---

## 🛠️ Installation & Setup

### Prerequisites
- **Node.js** 18+ and npm
- **Python** 3.9+
- **PostgreSQL** 14+
- **Redis** 6+

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Start the server:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Setup environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start development server:**
   ```bash
   npm run dev
   ```

5. **Access the app:**
   - Local: `http://localhost:5173`
   - Network: Check terminal output for network URL

---

## 📝 Environment Variables

### Backend (.env)
```env
DATABASE_URL=postgresql://user:password@localhost:5432/mastery_db
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key
```

### Frontend (.env)
```env
VITE_API_URL=http://localhost:8000
VITE_FIREBASE_API_KEY=your-firebase-api-key
VITE_FIREBASE_PROJECT_ID=your-project-id
```

---

## 🎮 Usage

1. **Start Backend:** `cd backend && uvicorn app.main:app --reload --host 0.0.0.0`
2. **Start Frontend:** `cd frontend && npm run dev`
3. **Login:** Use demo credentials from table above
4. **Explore:** Navigate through dashboard, assignments, resources

---

## 📦 Project Structure

```
MASTERY-AI-V2/
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── models/       # Database models
│   │   ├── services/     # Business logic
│   │   └── config.py     # Configuration
│   ├── alembic/          # Database migrations
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── features/     # Feature modules
│   │   ├── services/     # API services
│   │   └── store/        # State management
│   └── package.json
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Daaim Pathan**
- GitHub: [@daaimpathan](https://github.com/daaimpathan)

---

## 🙏 Acknowledgments

- Google Gemini API for AI capabilities
- Firebase for real-time features
- Open source community for amazing tools

---

## 📞 Support

For support, email support@mastery.ai or open an issue on GitHub.

---

<div align="center">
  <strong>Made with ❤️ for Education</strong>
</div>
