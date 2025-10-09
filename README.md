# 🍒 Fullstack Login Template

[![FastAPI](https://img.shields.io/badge/FastAPI-0.118.0-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SvelteKit](https://img.shields.io/badge/SvelteKit-2.43.2-ff3e00?logo=svelte&logoColor=white)](https://kit.svelte.dev/)
[![SQLModel](https://img.shields.io/badge/SQLModel-0.0.25-3776ab?logo=python&logoColor=white)](https://sqlmodel.tiangolo.com/)
[![Passlib](https://img.shields.io/badge/Passlib-1.7.4-3776ab?logo=python&logoColor=white)](https://passlib.readthedocs.io/)
[![Vite](https://img.shields.io/badge/Vite-7.1.7-646cff?logo=vite&logoColor=white)](https://vitejs.dev/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

**Fullstack Login Template** is a ready-to-use, copy-paste solution for authentication in modern web apps. Built with FastAPI (Python) for the backend and SvelteKit for the frontend, it provides a secure, scalable, and developer-friendly starting point for login and registration flows. No need to build authentication from scratch—just clone, configure, and go!

This repository is a [GitHub Template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository), so you can use it to bootstrap new projects instantly.

---

## Features

- 🔒 **User Registration & Login** (JWT-based authentication)
- 🧑‍💻 **FastAPI Backend** with SQLModel ORM
- ⚡ **SvelteKit Frontend** with modern UI
- 🗄️ **SQLite Database** (easy to swap for other DBs)
- 🛡️ **Password Hashing** (bcrypt via Passlib)
- 🚦 **Rate Limiting** (SlowAPI)
- 🌍 **CORS Support**
- 🧪 **Ready for Testing & Extension**
- 📝 **Swagger Docs** (protected with HTTP Basic Auth)
- 🏷️ **Role-based Access Control** (easy to extend)

---

## Getting Started

### 1. Clone as Template

Click `Use this template` on GitHub, or run:

```sh
gh repo create my-login-app --template <this-repo-url>
```

### 2. Backend Setup

```sh
cd backend
cp .env.example .env
# Fill in .env with your secrets and DB URL
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python scripts/create_db.py
uvicorn main:app --reload
```

### 3. Frontend Setup

```sh
cd frontend
npm install
npm run dev
```

---

## Environment Variables

See [`backend/.env.example`](backend/.env.example) for all required variables:

- `DATABASE_URL` — SQLite or other DB connection string
- `JWT_SECRET_KEY`, `JWT_ALGORITHM`, `JWT_ACCESS_TOKEN_EXPIRE_MINUTES`
- `ALLOWED_ORIGINS` — CORS origins
- `DOCS_USERNAME`, `DOCS_PASSWORD` — Swagger docs protection

---

## Folder Structure

```
backend/
  main.py
  data_access/
  routers/
  scripts/
  security/
  validations/
frontend/
  src/
  static/
  package.json
  ...
```

---

## API Endpoints

- `POST /auth/login` — Login with username & password
- `POST /auth/register` — Register new user
- `GET /` — API health check
- `GET /docs` — Swagger UI (HTTP Basic protected)

See [`backend/routers/auth.py`](backend/routers/auth.py) for details.

---

## Customization

- Add fields to [`backend/data_access/models.py`](backend/data_access/models.py) for user profiles.
- Extend validation in [`backend/validations/schemas.py`](backend/validations/schemas.py).
- Customize frontend UI in [`frontend/src/routes/`](frontend/src/routes/).

---

## License

MIT © [Nehuen Lian](https://github.com/NehuenLian)

---

## Contributing

Feel free to open issues or PRs for improvements