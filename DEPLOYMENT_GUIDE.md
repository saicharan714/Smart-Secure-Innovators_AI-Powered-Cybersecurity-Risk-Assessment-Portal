# Deployment Guide

## Smart Secure Innovators - Deployment Instructions

### Prerequisites
- Docker (optional)
- Python 3.8+
- Node.js 14+
- AWS account (for cloud deployment)

### Local Development Setup

#### 1. Python Backend
```bash
cd src/web_app/backend
pip install -r ../../requirements.txt
python app.py
```

Server runs on `http://localhost:5000`

#### 2. React Frontend
```bash
cd src/web_app/frontend
npm install
npm start
```

App runs on `http://localhost:3000`

#### 3. AI Model
```bash
cd src/ai_model
jupyter notebook model_training.ipynb
```

### Production Deployment (Docker)

#### Build Docker Image
```bash
docker build -t cybersecurity-portal:1.0 .
```

#### Run Container
```bash
docker run -p 5000:5000 -p 3000:3000 cybersecurity-portal:1.0
```

### AWS Deployment

1. Create EC2 instance
2. Install Docker
3. Push Docker image to ECR
4. Deploy using ECS or EKS

### Configuration

Environment variables in `.env`:
```
FLASK_ENV=production
REACT_APP_API_URL=https://api.example.com
DATABASE_URL=postgresql://user:pass@db-host:5432/db_name
```

---

**Deployment Guide Version:** 1.0  
**Last Updated:** November 23, 2025
