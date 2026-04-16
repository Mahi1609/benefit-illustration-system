# Architecture & Design Explanation

## System Design Approach

The system is designed using a layered architecture to ensure:

* Separation of concerns
* Testability
* Scalability
* Maintainability

---

## API Layer

Handles:

* Request validation
* Routing
* Authentication checks

Stateless design enables horizontal scaling.

---

## Business Logic Layer (Engine)

Core of the system:

* Independent from API
* Deterministic outputs
* Unit testable

This layer can be extracted into:

* Background workers
* Distributed processing nodes

---

## Data Access Layer

* Handles database operations
* Abstracts DB logic from business logic
* Enables easy migration to other DB systems

---

## Authentication System

* JWT-based stateless authentication
* Password hashing using bcrypt
* Suitable for distributed systems

---

## Security Design

* Passwords stored as hashes
* Sensitive data should be masked/encrypted
* Logging avoids PII exposure
* Environment variables for secrets

---

## Scalability Strategy

### Current:

* Synchronous API-based processing

### Future Scalable Design:

1. Introduce Message Queue:

   * Kafka / Redis / RabbitMQ

2. Worker Layer:

   * Multiple workers process jobs in parallel

3. Horizontal Scaling:

   * Add more workers for higher throughput

4. Batch Processing:

   * Process large datasets efficiently

5. Database Optimization:

   * Indexing
   * Read replicas

---

## Trade-offs

* SQLite used for simplicity → not production scale
* JSON storage → flexible but less queryable
* No async processing yet → design-ready but not implemented

---

## Conclusion

The system is built with:

* Strong modular design
* Clear scalability path
* Clean separation of concerns

It is ready to evolve into a production-grade distributed system.
