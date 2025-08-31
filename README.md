# Library Management System (Django)

This is a Django-based Library Management System project.  
It provides functionality for managing books, borrowing and returning books and maintaining a list of members.

---

## Features Implemented

### 1. **Books Management**
- Add, view, and manage books via the Django Admin panel.  
- Each book contains details such as:
  - Title
  - Author
  - ISBN
- Admin Link: [Admin Panel](http://127.0.0.1:8000/admin/)

---

### 2. **Borrow Books**
- Members can borrow books if available.  
- Borrowing logic ensures:
  - A book cannot be borrowed if already borrowed.
  - Records are saved in the `Borrow` model.  
- Admin link to view borrowed books: [Borrow Records – Admin](http://127.0.0.1:8000/admin/library_app/borrow/)

---

### 3. **Return Books**
- Members can return borrowed books.  
- Returning logic updates the availability status of the book.  

*(Viewing returned books is done via the Django Admin for now.)*

---

### 4. **Check Available Books**
- Displays a list of all books that are currently available.  
- URL: [Available Books](http://127.0.0.1:8000/available-books/)

---

### 5. **Members List**
- Maintains a list of library members.  
- Each member has:
  - Name
  - Membership ID
  - Contact info  
- Admin link to view members: [Members – Admin](http://127.0.0.1:8000/admin/library_app/member/)

---

## Tech Stack

- **Backend:** Django (Python)  
- **Database:** SQLite (default for Django projects)  
- **Frontend:** HTML (Django Templates)  
- **Admin Panel:** Django Admin
