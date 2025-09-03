# Getting Started

Follow these instructions to set up and run the project locally.

!!! warning "**Prerequisites**"

    - Python 3.11+
    - MySQL or MariaDB
    - Node.js & npm


#### **Installation**

##### **Backend Setup**

1. Create a virtual environment:
    
    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

2. Install Python dependencies:

    ```
    pip3 install -r requirements.txt
    ```

3. Configure the database:
    Make sure MySQL is running.
    Create a database named package_tracking (see [Database Setup](database.md)).

4. Run the backend:
    
    ```
    uvicorn app.main:app --reload
    ```
    
5. Backend links:
    - Backend API: <http://localhost:8000>
    - Backend API Docs: <http://localhost:8000/docs>

##### Frontend Setup
1. Navigate to frontend directory
    ```
    cd frontend
    ```
2. Install node modules:
    ```
    npm install
    ```

3. Start the frontend:
    ```
    npm start
    ```
5. Frontend links:
    - Frontend: <http://localhost:3000>