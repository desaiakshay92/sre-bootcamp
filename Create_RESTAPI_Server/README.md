# 🚀 FastAPI Project

## 📦 Quickstart

1. Clone this repo.
2. Set up the environment:  
   👉 See [`docs/setup-conda.md`](docs/setup-conda.md)

3. 📦 Install Dependencies
    
    Go to the Project Directory
    
    pip install -r requirements.txt

4. ⚙️ Verify Database
    Make sure **PostgreSQL is running locally** and your connection string is properly set in the `.env` file.  
    
    Example:

    .env
    DATABASE_URL=postgresql://username:password@localhost:5432/your_database

5.  ✅ Verify the App
    
    make makemigrations
    
    make upgrade
    
    make run