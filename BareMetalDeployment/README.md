# 🚀 FastAPI Deployment with Vagrant, Docker Compose, and Nginx

This project demonstrates a production-like deployment of a FastAPI application using:

- 🐳 Docker & Docker Compose
- 📦 Vagrant (with VirtualBox)
- 🌐 Nginx (as a load balancer)
- 🐘 PostgreSQL (as the database)
- 🛠️ Makefile (for automation)

---


---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://developer.hashicorp.com/vagrant/downloads)
- [Postman](https://www.postman.com/)/Swagger(Inbuilt) (for testing)

> 💡 All commands below should be run from your host machine unless specified otherwise.

---

### 🧱 Step 1: Boot the Vagrant VM

```bash
vagrant up


📦 Docker Compose Services


| Service | Description | 
| db | PostgreSQL 15 with healthcheck | 
| fastapi1 | FastAPI app container #1 | 
| fastapi2 | FastAPI app container #2 | 
| nginx | Load balancer for API containers | 




🛠️ Makefile Commands


| Command | Description | 
| make run-api | Start DB, run migrations, launch API + Nginx | 
| make db-start | Start only the database container | 
| make db-migrate | Run Alembic migrations | 
| make logs | View container logs | 
| make stop | Stop all containers | 
| make clear | Remove containers, images, volumes | 
