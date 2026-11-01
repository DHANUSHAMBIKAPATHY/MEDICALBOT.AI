# 🏥 MEDICALBOT.AI – AI-Powered Healthcare Platform

MEDICALBOT.AI is a healthcare-focused software project that combines an AI-powered healthcare chatbot with a full-stack doctor appointment management system. It aims to make healthcare information more accessible and simplify the process of finding doctors and managing appointments.

## 🚀 Project Modules

### 1. MindMate AI – Healthcare Chatbot

An AI-powered chatbot that allows users to interact with an AI general physician assistant and receive general healthcare information.

**Features**
- Interactive AI-powered healthcare conversations.
- Natural language processing using OpenAI.
- Responses to common health-related questions.
- Basic health guidance and general wellness information.
- Medical safety instructions encouraging users to consult licensed healthcare professionals.

**Technologies**
- Python
- Flask
- OpenAI API
- HTML
- CSS
- JavaScript

### 2. Prescripto – Doctor Appointment Booking System

A full-stack web application that connects patients with doctors and provides appointment management functionality.

**Patient Features**
- User registration and login.
- Browse available doctors.
- View doctor profiles and specializations.
- Check available appointment slots.
- Book appointments.
- View and cancel appointments.
- Online payment integration.

**Doctor Features**
- Doctor login.
- View scheduled appointments.
- Manage availability.
- Update profile information.
- Track appointments and earnings.

**Admin Features**
- Admin authentication.
- Add and manage doctors.
- View appointments.
- Manage appointment status.
- Dashboard with patient, doctor and appointment information.

**Technologies**
- React.js
- Node.js
- Express.js
- MongoDB
- Mongoose
- Tailwind CSS
- JWT Authentication
- Cloudinary
- Razorpay
- Stripe

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Languages | Python, JavaScript |
| Frontend | React.js, HTML, CSS, Tailwind CSS |
| Backend | Flask, Node.js, Express.js |
| Database | MongoDB |
| AI Integration | OpenAI API |
| Authentication | JWT |
| Cloud Storage | Cloudinary |
| Payment Integration | Razorpay, Stripe |
| Development Tools | VS Code, Git, GitHub |

## 📂 Project Structure

```text
MEDICALBOT.AI/
│
├── Medmat ai/
│   └── Mindmate_ai/
│       ├── app.py
│       ├── requirements.txt
│       ├── templates/
│       │   └── index.html
│       └── static/
│           ├── style.css
│           ├── script.js
│           └── doraemon.png.jpg
│
└── meddoc ai/
    └── prescripto-full-stack/
        │
        ├── frontend/
        │   ├── src/
        │   ├── public/
        │   └── package.json
        │
        ├── admin/
        │   ├── src/
        │   └── package.json
        │
        └── backend/
            ├── config/
            ├── controllers/
            ├── middleware/
            ├── models/
            ├── routes/
            ├── server.js
            └── package.json
```

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the applications:

- Python 3.10+
- Node.js and npm
- MongoDB database
- Git
- OpenAI API key

### 1. Clone the Repository

```bash
git clone https://github.com/DHANUSHAMBIKAPATHY/MEDICALBOT.AI.git

cd MEDICALBOT.AI
```

### 2. Run MindMate AI

Navigate to the chatbot directory:

```bash
cd "Medmat ai/Mindmate_ai"
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Start the Flask application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

### 3. Run the Prescripto Application

Open separate terminals for the frontend, admin panel and backend.

**Backend**

```bash
cd "meddoc ai/prescripto-full-stack/backend"

npm install
```

Create a `.env` file with the required configuration:

```env
PORT=4000
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret

ADMIN_EMAIL=your_admin_email
ADMIN_PASSWORD=your_admin_password

CLOUDINARY_NAME=your_cloudinary_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_SECRET_KEY=your_cloudinary_secret

CURRENCY=INR

RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_secret

STRIPE_SECRET_KEY=your_stripe_secret
```

Start the backend:

```bash
npm run server
```

**Patient Frontend**

```bash
cd "meddoc ai/prescripto-full-stack/frontend"

npm install
npm run dev
```

**Admin Panel**

```bash
cd "meddoc ai/prescripto-full-stack/admin"

npm install
npm run dev
```

Configure the frontend and admin environment variables for the backend API URL according to the application configuration.

## 🔐 Security

- Store API keys and credentials in environment variables.
- Never commit `.env` files or private API keys.
- Use `.gitignore` to exclude environment files and dependency folders.
- Use secure authentication practices when deploying.

## 🎯 Project Objectives

- Explore the integration of Artificial Intelligence into healthcare applications.
- Provide accessible general healthcare information through an AI chatbot.
- Simplify doctor discovery and appointment booking.
- Develop practical experience in frontend and backend development.
- Understand API integration, database management and authentication.

## ⚠️ Medical Disclaimer

MindMate AI provides general healthcare information and is not a replacement for professional medical advice, diagnosis or treatment. Users should consult qualified healthcare professionals for medical concerns. Do not use this application for emergencies.

## 👨‍💻 Developer

**Dhanush A**

GitHub: https://github.com/DHANUSHAMBIKAPATHY

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback.

**Built with Python, JavaScript, React, Node.js, MongoDB and AI.**
