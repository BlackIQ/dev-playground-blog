# Blog Application

A simple full-stack Blog application built for learning modern web development.

This project is the third step of the **Playground Learning Path**.  
The goal is to move beyond basic CRUD operations and learn how to design and work with relational databases using
SQLAlchemy,
including relationships between different entities, pagination, and more advanced data queries.

## Project Structure

This project consists of two parts:

- Backend: FastAPI REST API
- Frontend: React Application

## Learning Goals

### Backend (FastAPI)

The backend focuses on learning relational database design and building APIs with connected data models.

#### Topics

- REST API Design
- HTTP Methods
- CRUD Operations
- SQLAlchemy Models
- Pydantic Schemas
- Database Integration
- Request Validation
- Database Relationships
- One-to-Many Relationships
- Many-to-Many Relationships
- Foreign Keys
- Association Tables
- Query Joins
- Pagination
- Advanced Querying
- Timestamp Management
- Soft Delete
- API Documentation with Swagger

---

### Frontend (React)

The frontend focuses on building a content-based application and handling more complex data structures from the backend.

#### Topics

- React Components
- State Management
- Fetching Relational Data from API
- Handling Forms
- Post Creation Interface
- Markdown / Rich Text Editor
- Post Detail Pages
- Category Management UI
- Tag Management UI
- Pagination UI
- Loading States
- Error Handling
- Empty States

## Features

Users can:

- View all blog posts
- Create a new post
- Edit an existing post
- Delete a post
- View post details
- Browse posts by category
- Search posts by title and content
- Filter posts using categories and tags
- Add tags to posts
- View comments on posts
- Navigate between pages using pagination

## Database Relationships

This project focuses on relational database design.

Main entities:

- Post
- Category
- Tag
- Comment

Relationships:

- A category can have multiple posts
- A post belongs to one category
- A post can have multiple tags
- A tag can belong to multiple posts
- A post can have multiple comments

## About Playground

**Playground** is a learning project series created to practice modern web development by building small full-stack
applications.

Each project focuses on introducing new concepts step by step, from basic CRUD operations to more advanced topics like
authentication, database relationships, and real-world application architecture.

The main goal is learning through building.

## Contributors

Built by:

- Backend **FastAPI**: [Amirhossein Mohammadi](https://github.com/BlackIQ)
- Frontend **React**: [Maedeh Sadat Khorasani](https://github.com/maedehskh80)

This project is part of a collaborative learning journey between backend and frontend development.