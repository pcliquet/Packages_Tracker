# Package Management API

This project is a FastAPI application that implements a package management system and location history. In this version, we integrate the application with a MySQL database using SQLAlchemy ORM.

## Features

- Package management (CRUD operations)
- Location tracking for packages
- Location history
- MySQL database integration
- RESTful API

## Environment Setup

To configure and run the application, follow the steps below:

### Requirements

- Python 3.8+
- MySQL Workbench
- Python libraries listed in `requirements.txt`

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/cribeirop/Package_Tracking.git
   ```

2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment:**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Database Configuration

1. **Environment Variables Configuration:**
   - Create a `.env` file in the project root.
   - The `.env` file should include the following environment variable to define the MySQL database connection:

   ```
   DATABASE_URL=mysql://username:password@localhost/dbname
   ```

   **Notes:**
   - Replace `username` with your database username.
   - Replace `password` with your database password.
   - Replace `dbname` with the database name you created.

2. **Create Database:**
   - Create a database in MySQL.
   - Tables will be generated automatically when starting the application.

### Running the Application

1. **Start the Server:**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access Documentation:**
   - Access [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view and test available endpoints through the interactive Swagger interface.

### Entity Relationship Diagram

![ER Diagram](img/entidade_relacionamento.png)

### Relational Model

![Relational Model](img/modelo_relacional.png)

### Demo Video

Check out the demo video of the API functionality by clicking this link [https://youtu.be/zYnqHrrbyAM](https://youtu.be/zYnqHrrbyAM).

## Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```

4. **Access the frontend:**
   - Frontend will be available at: http://localhost:3000
   - API calls are proxied to: http://localhost:8000

![Frontend](img/frontend.png)

## API Documentation

Access the interactive API documentation at: http://localhost:8000/docs

## Database Schema

The application uses two main tables:
- `packages`: Stores package information
- `package_locations`: Stores location history for each package

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
