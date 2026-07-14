<div align="center">

# 🚆 Scalable Railway Reservation System on AWS

### High Availability • Auto Scaling • Serverless Ticket Generation • Temporary Seat Locking

A cloud-native Railway Reservation System built using AWS services to simulate an **IRCTC-like booking platform** capable of handling high traffic (Tatkal bookings) with scalable infrastructure, automated ticket generation, and cloud-native monitoring.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge&logo=amazonaws)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)

</div>

---

# 📖 Table of Contents

- Project Overview
- Features
- AWS Architecture
- Technology Stack
- Booking Workflow
- Auto Scaling Strategy
- AWS Services Used
- Monitoring & Logging
- Project Structure
- Future Enhancements
- Author

---

# 📌 Project Overview

This project demonstrates a **scalable Railway Reservation System** deployed on AWS.

It is designed to:

- 🔍 Search trains
- 🎫 Book railway tickets
- 🔒 Prevent double booking using temporary seat locking
- 📄 Generate PDF tickets automatically
- 📧 Send tickets through Email
- 📈 Handle Tatkal traffic automatically using Auto Scaling
- ☁️ Deploy a highly available cloud architecture

---

# ✨ Features

## 👤 User Features

- User Registration & Login
- Train Search
- Seat Availability Check
- Ticket Booking
- PNR Generation
- Booking History
- PDF Ticket Download
- Email Notification

---

## ☁️ Cloud Features

- High Availability Architecture
- Multi EC2 Instances
- Application Load Balancer
- Auto Scaling Group
- Scheduled Scaling for Tatkal Booking
- Route 53
- CloudFront
- AWS WAF
- DynamoDB Seat Locking (TTL)
- Amazon RDS PostgreSQL
- SNS Event Notification
- Lambda Serverless Processing
- Amazon S3 Ticket Storage
- Amazon SES Email Service
- Amazon CloudWatch Monitoring
- AWS CloudTrail Auditing
- AWS X-Ray Distributed Tracing

---

# 🏗 AWS Architecture

```
## 🏗 AWS Architecture

<p align="center">
  
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/9ee1dc0a-7ccd-453e-8f45-a5c8df26cf01" />

</p>
```

---

# 🔄 End-to-End Booking Workflow

```
User Login
      │
      ▼
Search Train
      │
      ▼
Check Availability
      │
      ▼
Temporary Seat Lock
(DynamoDB TTL)
      │
      ▼
Booking Saved
(Amazon RDS)
      │
      ▼
SNS Publishes Event
      │
      ▼
Lambda Triggered
      │
      ▼
Generate Ticket PDF
      │
      ▼
Upload PDF to S3
      │
      ▼
Send Email using SES
```

---

# ⚡ Auto Scaling Strategy

| Time | Action | EC2 Instances |
|------|--------|--------------:|
| Before 10:50 AM | Normal Traffic | 2 |
| 10:50 AM | Scale Out | 10 |
| After 11:15 AM | Scale In | 2 |

This simulates the **Tatkal booking rush**, ensuring that the application automatically scales during peak demand.

---

# 🛠 Technology Stack

## Backend

- Python
- Flask

## Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

## Database

- Amazon RDS PostgreSQL
- Amazon DynamoDB

## AWS Services

- Amazon EC2
- Auto Scaling Group
- Application Load Balancer
- Amazon Route 53
- Amazon CloudFront
- AWS WAF
- Amazon DynamoDB
- Amazon RDS PostgreSQL
- Amazon SNS
- AWS Lambda
- Amazon S3
- Amazon SES
- Amazon CloudWatch
- AWS CloudTrail
- AWS X-Ray

---

# ☁️ AWS Services Used

| Service | Purpose |
|----------|---------|
| Amazon EC2 | Hosts Flask Application |
| Auto Scaling | Handles traffic spikes |
| ALB | Load Distribution |
| Route 53 | DNS Management |
| CloudFront | Content Delivery |
| AWS WAF | Web Application Firewall |
| DynamoDB | Temporary Seat Locking (TTL) |
| Amazon RDS | Booking Database |
| Amazon SNS | Publish Booking Events |
| AWS Lambda | Ticket PDF Generation |
| Amazon S3 | Store Ticket PDFs |
| Amazon SES | Send Email to Users |
| CloudWatch | Monitoring & Alarms |
| CloudTrail | API Auditing |
| AWS X-Ray | Distributed Tracing |

---

# 📊 Monitoring & Logging

### Amazon CloudWatch

- EC2 Metrics
- ALB Metrics
- Lambda Monitoring
- RDS Monitoring
- Application Logs
- Dashboards
- CloudWatch Alarms

---

### AWS CloudTrail

- API Activity Logs
- Resource Changes
- IAM Activity
- Security Auditing

---

### AWS X-Ray

- Request Tracing
- Database Calls
- Lambda Execution
- Service Performance
- End-to-End Request Analysis

---

# 📂 Project Structure

```
railway-reservation/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
├── static/
│
├── screenshots/
│   ├── home.png
│   ├── login.png
│   ├── booking.png
│   ├── dashboard.png
│   ├── ticket.png
│   └── architecture.png
│
└── docs/
```

---

# 🚀 Future Enhancements

- Payment Gateway Integration
- QR Code Based Ticket Verification
- Live Train Status
- AI Seat Recommendation
- Mobile Application
- Multi-language Support

---

# 📷 Screenshots

> Add project screenshots here.

- Home Page
- Login Page
- Dashboard
- Booking Page
- Ticket PDF
- Email Notification
- AWS Architecture Diagram

---

# 👨‍💻 Author

## Om Jadhav

**AWS Cloud & DevOps Enthusiast**

- GitHub: https://github.com/omcloud4
- LinkedIn: *(Add your LinkedIn Profile)*

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star.

</div>
