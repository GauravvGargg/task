# Task Management Application

## 2.1.3.1. Overview of What Is Being Built

This project is a **Task Management Application** that enables users to register, log in, and manage their personal task lists. Features include creating, reading/searching, updating, and deleting tasks. The project is built using Python (Django framework), MySQL, and plain HTML/CSS with Bootstrap for styling.

## 2.1.3.2. Explanation of DB Design

### 2.1.3.2.1. ER Diagram

```
User
│
├── id (PK)
└── username, password, ...

Task
├── id (PK)
├── title
├── description
├── due_date
├── status
├── remarks
├── created_on
├── updated_on
├── created_by (FK → User)
└── updated_by (FK → User)
```

# Task Management System - Entity Relationship Diagram

This ER diagram represents the database structure for the Task Management application using crow's foot notation.
```
mermaid
erDiagram
    USER {
        int id PK "Primary Key"
        string username "Unique username"
        string email "Email address"
        string first_name "First name"
        string last_name "Last name"
        datetime date_joined "Account creation date"
        boolean is_active "Account status"
        boolean is_staff "Staff status"
        boolean is_superuser "Superuser status"
    }
    
    TASK {
        int id PK "Primary Key"
        string title "Task title (max 255 chars)"
        text description "Detailed task description"
        date due_date "Task deadline"
        string status "Task status (max 50 chars)"
        text remarks "Additional remarks (optional)"
        datetime created_on "Creation timestamp"
        datetime updated_on "Last update timestamp"
        int created_by_id FK "Creator user ID"
        int updated_by_id FK "Last updater user ID"
    }
    
    USER ||--o{ TASK : "creates"
    USER ||--o{ TASK : "updates"
    USER ||--o{ TASK : "deletes"
```
![ER Diagram](https://kroki.io/mermaid/svg/eNqVU01vwjAMve9XWDnBAWmaxGU3NECaugMacK5MY5hHv5akEwj235ePUspaIS2HxI3fsx0_l9SUcacwewC71svZO5y86RbnBljCIgKxUJyhOkJER9H4tVGc76DSpHLMCMQ656-KmosOkjLkFMTMHyilIq07oC0rbeIQcO5s6I2VYoN6ww5IoiHD1umM-LPgnCSISZIUlX1UoggNF7n3XkmbokgJc2AdY2L4m64MbdBUuhdqXdstiKU_7uGqkpRrjcU2Zhv_43e_rSbL6P9CGDaprXmFel_bgwwP8DQeQ_KBSg-vDEMHA5J0orj0nRBTMlYV2yXj6C3XbVNBVhR7I-SRhDK13e0UE15Wo-oPX874sb8aZadD7S1jIiW7xJg2d4OiDDfDHom9miRj94qXi7LOY7NmZQ-hKmVD8LMTLvo4fJkWC98cYyvCPKqzFMoPOrxOb-GX6Fd4K8cfTkty_--dz6NRcQryP4MImevx6AOEoHcAklJygF_Xqy9g)


## Relationship Explanations

- *USER creates TASK*: One-to-Many relationship where one user can create multiple tasks
- *USER updates TASK*: One-to-Many relationship where one user can update multiple tasks  
- *USER deletes TASK*: One-to-Many relationship where one user can delete multiple tasks

## Key Features

- Each task tracks both the creator (created_by) and last updater (updated_by)
- Timestamps automatically track creation and modification times
- Users have full CRUD operations on their tasks
- Foreign key relationships maintain data integrity


### 2.1.3.2.2. Data Dictionary

| Field Name   | Type         | Description                          |
|--------------|--------------|--------------------------------------|
| id           | Integer (PK) | Unique Task ID                       |
| title        | Varchar(255) | Task title                           |
| description  | Text         | Detailed description                 |
| due_date     | Date         | Due date for the task                |
| status       | Varchar(50)  | Task status (e.g., Pending, Done)    |
| remarks      | Text         | Additional comments                  |
| created_on   | DateTime     | Created timestamp                    |
| updated_on   | DateTime     | Updated timestamp                    |
| created_by   | FK (User)    | Creator (user)                       |
| updated_by   | FK (User)    | Last editor (user)                   |

### 2.1.3.2.3. Documentation of Indexes Used

- **id** and **foreign keys**: Auto indexed by MySQL.
- **Additional indexes**: `title`, `status`, `due_date` may be indexed for faster searches.

### 2.1.3.2.4. Code First or DB First?

**Code First** approach is used, leveraging Django models to define the schema. This provides controlled, versionable migrations, making updates and teamwork straightforward.

## 2.1.3.3. Structure of the Application

### 2.1.3.3.1./2.1.3.3.2. SPA/MPA Choice

- **Standard MVC server-side page rendering (MPA)** is used. Each page (login, registration, task list, add/edit) is rendered on the server, not as a single-page web app.
- No RESTful API or SPA frameworks are used; all form submissions and navigation use standard Django routing and views.

## 2.1.3.4. Frontend Structure

### 2.1.3.4.1. What Kind of Frontend and Why?

- The frontend is a **web page** using manually written HTML and Bootstrap for styling.
- **Why**: This approach is beginner-friendly, uses little JavaScript, and closely aligns with traditional MVC design. It’s easier to verify, debug, and maintain.

### 2.1.3.4.2. Web vs Mobile

- A standard web frontend is used for accessibility and assignment requirements. A mobile app was not built, but the UI is responsive thanks to Bootstrap.

## 2.1.3.5. Build and Install

### 2.1.3.5.1. Environment Details & Dependencies

- **Python 3.x**
- **Django 5.2.4**
- **MySQL Server**
- **mysqlclient** Python package
- **Bootstrap CDN** for styling

### 2.1.3.5.2. Build/Compile Instructions

```bash
pip install django mysqlclient
```

### 2.1.3.5.3. Run/Install Instructions

1. Create your MySQL database:

   ```sql
   CREATE DATABASE task CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. Configure database settings in `settings.py`.

3. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. (Optional) Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/`.
