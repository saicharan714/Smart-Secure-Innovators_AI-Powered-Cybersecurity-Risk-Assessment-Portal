# API Documentation

## Cybersecurity Risk Assessment Portal - REST API

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Health Check
**GET** `/health`

Check API service status.

**Response:**
```json
{
  "status": "healthy",
  "service": "Cybersecurity Risk Assessment Portal API",
  "version": "1.0"
}
```

#### 2. Vulnerability Assessment
**POST** `/assess`

Assess vulnerability risk based on input data.

**Request Body:**
```json
{
  "hostname": "server-01",
  "ports": [22, 80, 443],
  "services": ["ssh", "http", "https"]
}
```

**Response:**
```json
{
  "status": "success",
  "risk_level": "High",
  "vulnerabilities": [...],
  "recommendations": [...]
}
```

#### 3. Dashboard
**GET** `/dashboard`

Get real-time risk dashboard data.

**Response:**
```json
{
  "total_vulnerabilities": 45,
  "high_risk": 12,
  "medium_risk": 23,
  "low_risk": 10
}
```

#### 4. Report Generation
**GET** `/report/<report_id>`

Generate assessment report.

**Response:**
```json
{
  "report_id": "report_001",
  "status": "completed",
  "download_url": "/reports/report_001.pdf"
}
```

### Error Responses

All errors return appropriate HTTP status codes with error details:

```json
{
  "status": "error",
  "message": "Detailed error description"
}
```

### Authentication
To be implemented in production version.

---

**API Version:** 1.0  
**Last Updated:** November 23, 2025
