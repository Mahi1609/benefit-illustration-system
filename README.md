# ProjectX System (Backend - Python)

## Overview

This project implements a scalable backend system to generate benefit illustrations for insurance policies based on predefined business logic.

The system focuses on:

* Accurate calculation logic based on provided Excel sheet
* Clean layered architecture
* Secure authentication and data handling
* Extensibility for future policy types
* Scalability for bulk processing

---

## Architecture

The system follows a layered architecture:

1. **API Layer (FastAPI)**

   * Handles HTTP requests/responses
   * Performs input validation using Pydantic

2. **Business Logic Layer (Engine)**

   * Core calculation logic
   * IRR computation
   * Illustration generation

3. **Data Access Layer (Repositories)**

   * Database interactions
   * Stores user and calculation data

---

## System Architecture Diagram

```
Frontend/UI → FastAPI → Routes → Engine → Repository → Database
```

---

## Features

* User Authentication (JWT-based)
* Policy Calculation Engine
* Benefit Illustration Table Generation
* Calculation History per User
* Input Validation (as per business rules)
* Unit Tested Calculation Logic

---

## Security

* Passwords are hashed using bcrypt
* JWT-based authentication (stateless)
* Sensitive fields (e.g., DOB) should be masked/encrypted at rest
* No sensitive data is logged in plaintext
* Environment-based configuration recommended for secrets

---

## Calculation Engine

* Implements logic based on provided Excel sheet
* Supports:

  * Premium calculation
  * Bonus accumulation
  * IRR computation
* Deterministic and unit-testable
* Completely isolated from API layer

---

## Testing

Includes:

* Unit tests for calculation engine
* API tests for authentication and policy endpoints

Run tests:

```
pytest -v
```

---

## Database Design

Tables:

* Users
* Calculations

Design Decisions:

* Normalized schema
* JSON storage for flexible result data
* Easily extensible for additional policy types and riders

---

## Scalability Design

To support millions of records:

* Introduce async job queues (Celery / Kafka / Redis Queue)
* Worker-based execution for calculation engine
* Batch processing for large datasets
* Horizontal scaling of worker nodes
* API layer remains stateless and horizontally scalable
* Add caching layer for repeated calculations
* Implement idempotent job processing for reliability

---

## Future Improvements

* Add policy types and rider modeling
* Implement encryption for sensitive fields
* Add rate limiting
* Introduce bulk upload APIs
* Replace SQLite with PostgreSQL
* Improve frontend with React

---

## How to Run

```
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Summary

This project demonstrates:

* Clean backend architecture
* Strong separation of concerns
* Deterministic business logic
* Scalable system design approach
* Secure authentication practices

---
