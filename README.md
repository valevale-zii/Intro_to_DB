# Library Management System (Django)

This is a Django-based Library Management System project.  
It provides functionality for managing books, borrowing and returning books, checking book availability, maintaining a list of members, and displaying a welcome page.

---

## Features Implemented

### 1. **Welcome Page**
- A simple landing page that introduces the system.  
- URL: `http://127.0.0.1:8000/`

---

### 2. **Books Management**
- Add, view, and manage books via the Django Admin panel.  
- Each book contains details such as:
  - Title
  - Author
  - ISBN
  - Availability status  

- Admin Link: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

### 3. **Borrow Books**
- Members can borrow books if available.  
- Borrowing logic ensures:
  - A book cannot be borrowed if already borrowed.
  - Records are saved in the `Borrow` model.  

---

### 4. **Return Books**
- Members can return borrowed books.  
- Returning logic updates the availability status of the book.  

---

### 6. **Members List**
- Maintains a list of library members.  
- Each member has:
  - Name
  - Contact info  

- Managed in the **Django Admin Panel**.

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default for Django projects)
- **Frontend:** HTML (Django Templates)
- **Admin Panel:** Django Admin

---
