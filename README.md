FastAPI Task Manager

A simple, Docker-ready task manager API built with **FastAPI**, featuring:

- Create, Read, Update, Delete (CRUD) task operations
- Optional file-based persistence (`task.json`)
-  Easy setup with or without Docker
- Type-safe with `pydantic`
- Ready for integration testing or CI/CD

Project Structure

fastapi-task-manager/ ├── app.py # Main FastAPI application ├── task.json # Optional file-based storage ├── requirements.txt # Python dependencies ├── Dockerfile # For containerized deployment └── README.md # You're reading it!

Getting Started (Local)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-task-manager.git
cd fastapi-task-manager

python3 -m venv appenv
source appenv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload
Visit: http://localhost:8000/docs for Swagger UI.

#using DOcker to Build Image
sudo docker build -t task-manager-app .
sudo docker run -d -p 8000:8000 --name task-manager-container task-manager-app

#Create Task
curl -X POST http://localhost:8000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title":"Write README", "description":"Explain the API", "completed":false}'

View All Task
curl http://localhost:8000/tasks

Get Task by id
curl http://localhost:8000/tasks/1

Udpate Task
curl -X PUT http://localhost:8000/tasks/1 \
     -H "Content-Type: application/json" \
     -d '{"title":"Update README", "description":"Improve details", "completed":true}'


Delete Task
curl -X DELETE http://localhost:8000/tasks/1

