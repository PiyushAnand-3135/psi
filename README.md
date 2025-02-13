<!-- project directory Explained -->

/my-project
│── /frontend               # Next.js App (App Router, Tailwind, Supabase)
│   │── /src                # Source code folder
│   │   ├── /app            # Next.js App Router Pages
│   │   │   ├── /auth       # Authentication pages
│   │   │   │   ├── login
│   │   │   │   │   ├── page.jsx   # Login page ("/auth/login")
│   │   │   │   ├── signup
│   │   │   │   │   ├── page.jsx   # Signup page ("/auth/signup")
│   │   │   ├── /dashboard  # Dashboard pages
│   │   │   │   ├── page.jsx # Dashboard home ("/dashboard")
│   │   │   ├── /api        # API Routes (Server Actions, Route Handlers)
│   │   │   │   ├── auth
│   │   │   │   │   ├── route.js  # API for authentication
│   │   ├── /components     # Reusable UI components
│   │   │   ├── Navbar.jsx
│   │   │   ├── Footer.jsx
│   │   ├── /hooks          # Custom hooks (fetching data, auth)
│   │   ├── /context        # Context API (AuthProvider, ThemeProvider)
│   │   ├── /utils          # Helper functions
│   │   │   ├── supabaseClient.js  # Supabase config
│   │   ├── layout.jsx      # Global Layout
│   │   ├── page.jsx        # Home Page
│   ├── /public             # Static assets (images, icons)
│   ├── tailwind.config.js  # Tailwind config
│   ├── next.config.js      # Next.js config
│   ├── .eslintrc.json      # ESLint config
│   ├── jsconfig.json       # Import aliases
│   ├── package.json        # Dependencies
│   ├── .env.local          # Env variables for frontend
│── /backend                # Python Backend (FastAPI or Flask, No PostgreSQL)
│   │── /src                # Backend source code
│   │   ├── /routes         # API endpoints
│   │   │   ├── auth.py     # Authentication endpoints (if needed)
│   │   │   ├── users.py    # User-related API
│   │   ├── /services       # Business logic services
│   │   ├── /utils          # Utility functions
│   │   ├── main.py         # Entry point for FastAPI/Flask
│   │── requirements.txt    # Python dependencies
│   │── config.py           # Configurations
│   │── .env                # Env variables for backend
│── README.md               # Documentation
