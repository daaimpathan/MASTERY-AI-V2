import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { mockDb, mockOnValue } from "./mockPollService";

// Check if Firebase is properly configured
const hasFirebaseConfig =
    import.meta.env.VITE_FIREBASE_API_KEY &&
    import.meta.env.VITE_FIREBASE_API_KEY !== "YOUR_API_KEY" &&
    import.meta.env.VITE_FIREBASE_DATABASE_URL &&
    import.meta.env.VITE_FIREBASE_DATABASE_URL !== "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com";

let db: any;
let isUsingMock = false;

if (hasFirebaseConfig) {
    // Use real Firebase
    const firebaseConfig = {
        apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
        authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
        databaseURL: import.meta.env.VITE_FIREBASE_DATABASE_URL,
        projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
        storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
        messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
        appId: import.meta.env.VITE_FIREBASE_APP_ID
    };

    try {
        const app = initializeApp(firebaseConfig);
        db = getDatabase(app);
        console.log("✅ Firebase Realtime Database connected");
    } catch (error) {
        console.warn("⚠️ Firebase initialization failed, using mock service:", error);
        db = mockDb;
        isUsingMock = true;
    }
} else {
    // Use mock service
    console.warn("⚠️ Firebase not configured. Using localStorage mock service for polls.");
    console.warn("📝 To use real Firebase, add credentials to .env file");
    db = mockDb;
    isUsingMock = true;
}

// Export db and helper functions
export { db, isUsingMock };

// Export Firebase functions with mock fallbacks
export { ref, set, remove, push } from "firebase/database";

// Conditionally export onValue
import { onValue as firebaseOnValue } from "firebase/database";
export const onValue = isUsingMock ? mockOnValue : firebaseOnValue;

