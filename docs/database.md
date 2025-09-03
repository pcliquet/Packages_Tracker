# Database Setup

This project uses MySQL with SQLAlchemy ORM.

1. **Install MySQL**

    ```
    brew install mysql
    ```

2. **Start MySQL**
    
    ```
    brew services start mysql
    ```

3. **Secure MySQL**

    ```
    mysql_secure_installation
    ```

4. **Login into the Database**
    
    ```
    mysql -u root -p
    ```

4. **Create Database** 
    
    ```
    CREATE DATABASE package_tracking; 
    ```

5. **Set .env**

    ```
    DATABASE_URL=mysql://username:password@localhost/package_tracking
    ```
