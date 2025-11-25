
# SCMxPertLite - Supply Chain Management System
 
![SCMxPertLite Dashboard](static/Shipment%20illustration.jpg)
 
A modern supply chain management system with real-time tracking, user management, and shipment monitoring capabilities.
 
## Features
 
- **Role-Based Access Control**
  - Admin and User roles with different permissions
  - Admin can manage all users and shipments
  - Users can manage their own shipments
 
- **Authentication & Security**
  - JWT token-based authentication
  - Password hashing with bcrypt
  - Session expiry after 30 minutes
  - CSRF protection
 
- **Shipment Management**
  - Create, view, update, and delete shipments
  - Filter shipments by container ID and date
  - Automatic shipment ID generation
 
- **Real-Time Monitoring**
  - WebSocket integration for device data
  - Kafka message queue for data processing
  - MongoDB for persistent storage
 
- **Admin Dashboard**
  - Manage all users (CRUD operations)
  - View and edit all shipments
  - Modify user roles and permissions
 
## Tech Stack
 
**Backend:**
- Python 3.9
- FastAPI
- MongoDB
- Kafka
- JWT Authentication
 
**Frontend:**
- HTML5, CSS3
- Jinja2 Templating
- Font Awesome Icons
 
**DevOps:**
- Docker
- Docker Compose
- Environment Variables
 
## Project Structure
 
```
/SCM
├── .env                    # Environment variables
├── docker-compose.yml      # Multi-container setup
├── Dockerfiles/            # Container configurations
├── kafka/                  # Kafka producers/consumers
├── routers/                # FastAPI route handlers
├── static/                 # Static assets
├── templates/              # HTML templates
├── models.py               # Data models
├── utils.py                # Helper functions
├── schemas.py              # Pydantic schemas
├── requirements.txt        # Python dependencies
└── main.py                 # Application entry point
```
 
## Installation
 
### Prerequisites
- Docker 20.10+
- Docker Compose 1.29+
- Python 3.9 (for development)
 
### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/NeelakanteswaraP/Main
   cd SCMxPertLite
   ```
 
2. Create `.env` file:
   ```bash
   cp .env.example .env
   # Edit with your credentials
   ```
 
3. Start services:
   ```bash
   docker-compose up -d
   ```
 
4. Access the application:
   - Frontend: http://localhost:8000
   - API Docs: http://localhost:8000/docs
 
## Usage
 
### User Roles
 
**Admin User:**
- Email: admin@example.com
- Password: admin123 (change in production)
- Can access all features
 
**Regular User:**
- Register through signup page
- Can manage own shipments
 
### API Endpoints
 
| Endpoint | Method | Description | Access |
|----------|--------|-------------|--------|
| `/auth/login` | POST | User login | Public |
| `/auth/signup` | POST | User registration | Public |
| `/shipments` | GET | List shipments | User |
| `/admin/users` | GET | List all users | Admin |
 
## Development
 
1. Set up virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
 
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
 
3. Run development server:
   ```bash
   uvicorn main:app --reload
   ```
 
## Deployment
 
For production deployment:
 
1. Configure HTTPS:
   ```nginx
   server {
       listen 443 ssl;
       server_name yourdomain.com;
       
       ssl_certificate /path/to/cert.pem;
       ssl_certificate_key /path/to/key.pem;
       
       location / {
           proxy_pass http://app:8000;
       }
   }
   ```
 
2. Set environment variables:
   ```bash
   export SECRET_KEY=your_strong_secret
   export MONGO_URI=mongodb://production-db:27017
   ```