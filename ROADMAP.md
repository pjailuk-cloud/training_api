# API Learning Roadmap

This roadmap takes you from zero knowledge to building a fully functional API with database integration.

## Phase 1: Foundations (Modules 1-3)

### Module 1: Understanding APIs and HTTP
**Goal**: Learn what APIs are and how the web communicates

Topics:
- What is an API and why do we need them?
- Client-Server architecture
- HTTP protocol basics
- HTTP methods: GET, POST, PUT, DELETE
- Status codes: 200, 201, 404, 500, etc.
- Request and Response structure
- Headers, Body, and Parameters

**Practice**:
- Explore existing public APIs
- Use a tool like Postman to make API requests
- Understand JSON format

**Duration**: 2-3 hours

---

### Module 2: Setting Up Your Development Environment
**Goal**: Get your computer ready for API development

Topics:
- Install Python (3.8+)
- Install pip (Python package manager)
- Create a virtual environment
- Install FastAPI and Uvicorn
- Install development tools (code editor, API testing tool)

**Practice**:
- Create your first "Hello World" API
- Run the server
- Make your first API request

**Duration**: 1-2 hours

---

### Module 3: Your First API Endpoints
**Goal**: Create basic API endpoints

Topics:
- What are endpoints/routes?
- Path parameters vs Query parameters
- Creating GET endpoints
- Creating POST endpoints
- Request body and response models
- FastAPI automatic documentation

**Practice**:
- Create a GET endpoint that returns a welcome message
- Create a GET endpoint with path parameters
- Create a POST endpoint that accepts data
- Explore the automatic API docs at /docs

**Duration**: 3-4 hours

---

## Phase 2: Data Management (Modules 4-6)

### Module 4: Working with Data
**Goal**: Understand data validation and models

Topics:
- What is data validation and why it matters
- Pydantic models for data validation
- Request schemas vs Response schemas
- Data types and validation rules
- Handling validation errors

**Practice**:
- Create a Task schema with validation
- Test valid and invalid data
- Return structured responses

**Duration**: 2-3 hours

---

### Module 5: Introduction to Databases
**Goal**: Learn how to store data permanently

Topics:
- What is a database?
- SQL vs NoSQL databases
- SQLite basics
- Database tables, rows, and columns
- Primary keys and relationships
- SQL basics: SELECT, INSERT, UPDATE, DELETE

**Practice**:
- Create a SQLite database
- Create a tasks table
- Manually insert and query data
- Understand database connections

**Duration**: 3-4 hours

---

### Module 6: Connecting API to Database
**Goal**: Integrate database with your API

Topics:
- SQLAlchemy ORM (Object-Relational Mapping)
- Database models vs Pydantic schemas
- CRUD operations with database
- Database sessions and connections
- Handling database errors

**Practice**:
- Create Task database model
- Connect FastAPI to SQLite
- Implement CREATE task endpoint
- Implement READ tasks endpoint
- Implement UPDATE task endpoint
- Implement DELETE task endpoint

**Duration**: 4-5 hours

---

## Phase 3: Real-World Features (Modules 7-9)

### Module 7: Advanced Querying
**Goal**: Add filtering, searching, and pagination

Topics:
- Query parameters for filtering
- Searching data
- Sorting results
- Pagination (limit and offset)
- Counting records

**Practice**:
- Filter tasks by status (completed/pending)
- Search tasks by title
- Sort tasks by creation date
- Add pagination to task list

**Duration**: 2-3 hours

---

### Module 8: Error Handling and Validation
**Goal**: Make your API robust and user-friendly

Topics:
- HTTP status codes in detail
- Exception handling
- Custom error responses
- Input validation
- Edge cases (empty data, not found, etc.)

**Practice**:
- Handle "task not found" errors
- Validate task input data
- Return meaningful error messages
- Test error scenarios

**Duration**: 2-3 hours

---

### Module 9: API Organization and Best Practices
**Goal**: Write clean, maintainable code

Topics:
- Project structure and organization
- Routers for grouping endpoints
- Dependency injection
- Environment variables and configuration
- Logging and debugging
- Code comments and documentation

**Practice**:
- Organize code into modules
- Create separate routers for different resources
- Add logging to track requests
- Create configuration file

**Duration**: 3-4 hours

---

## Phase 4: Security and Deployment (Modules 10-12)

### Module 10: Authentication and Authorization
**Goal**: Secure your API with user authentication

Topics:
- What is authentication vs authorization?
- User registration and login
- Password hashing
- JWT tokens
- Protected endpoints
- User sessions

**Practice**:
- Create user registration endpoint
- Create login endpoint
- Generate JWT tokens
- Protect task endpoints (users see only their tasks)
- Add user ownership to tasks

**Duration**: 4-5 hours

---

### Module 11: Testing Your API
**Goal**: Ensure your API works correctly

Topics:
- Why testing matters
- Unit tests vs Integration tests
- Testing with pytest
- Testing database operations
- Testing authentication
- Test coverage

**Practice**:
- Write tests for task creation
- Write tests for task retrieval
- Write tests for error cases
- Run all tests and check coverage

**Duration**: 3-4 hours

---

### Module 12: Advanced Topics and Next Steps
**Goal**: Learn about deployment and advanced concepts

Topics:
- CORS (Cross-Origin Resource Sharing)
- Rate limiting
- API versioning
- Documentation best practices
- Deployment basics
- Monitoring and logging
- Database migrations
- Relationships between tables (categories, tags)

**Practice**:
- Add task categories feature
- Implement CORS
- Prepare API for deployment
- Create comprehensive documentation

**Duration**: 4-5 hours

---

## Total Learning Time
**Estimated**: 35-45 hours (can be spread over several weeks)

## Learning Tips

1. **Go in Order**: Each module builds on previous ones
2. **Code Along**: Type the code yourself, don't copy-paste
3. **Experiment**: Try breaking things to understand how they work
4. **Take Breaks**: Better to learn well than learn fast
5. **Ask Questions**: Take notes when confused
6. **Build Extra**: Add your own features to practice

## After Completion

You'll be able to:
- Build REST APIs from scratch
- Connect APIs to databases
- Implement authentication
- Handle errors properly
- Write tests
- Deploy APIs
- Read and understand API documentation
- Debug API issues

## Next Learning Paths

- Learn React/Vue to build a frontend for your API
- Learn Docker for containerization
- Learn PostgreSQL for production databases
- Learn API design patterns
- Build a microservices architecture
- Learn GraphQL as an alternative to REST

---

Ready to start? Let's go to Module 1!
