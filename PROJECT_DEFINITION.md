# Project Definition: Personal Task Manager API

## Project Overview

**Name**: Training API - Personal Task Manager
**Type**: RESTful API
**Purpose**: Educational - Learn API development from scratch
**Complexity**: Beginner to Intermediate

## What You'll Build

A fully functional REST API for managing personal tasks with the following capabilities:

### Core Features

1. **Task Management**
   - Create new tasks
   - View all tasks
   - View a specific task
   - Update task details
   - Delete tasks
   - Mark tasks as complete/incomplete

2. **Task Properties**
   - Title (required)
   - Description (optional)
   - Status (pending, in-progress, completed)
   - Priority (low, medium, high)
   - Due date
   - Creation timestamp
   - Update timestamp

3. **Advanced Features** (Later modules)
   - User authentication and authorization
   - Task categories/tags
   - Search and filtering
   - Task statistics
   - Data validation

## Technical Specifications

### Architecture
- **Pattern**: REST API (Representational State Transfer)
- **Style**: Resource-based URLs
- **Data Format**: JSON

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | API health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get specific task |
| POST | `/tasks` | Create new task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |
| PATCH | `/tasks/{id}/complete` | Mark task complete |

### Database Schema

**Tasks Table**:
```
- id (Integer, Primary Key, Auto-increment)
- title (String, Required, Max 200 chars)
- description (Text, Optional)
- status (String, Default: "pending")
- priority (String, Default: "medium")
- due_date (DateTime, Optional)
- created_at (DateTime, Auto)
- updated_at (DateTime, Auto)
- user_id (Integer, Foreign Key) [Later module]
```

### Technology Stack

1. **Backend Framework**: FastAPI
   - Why? Fast, modern, automatic docs, beginner-friendly

2. **Programming Language**: Python 3.8+
   - Why? Easy to learn, readable syntax

3. **Database**: SQLite → PostgreSQL (later)
   - Why SQLite? No setup needed, file-based
   - Why PostgreSQL later? Production-ready

4. **ORM**: SQLAlchemy
   - Why? Simplifies database operations

5. **Validation**: Pydantic
   - Why? Built into FastAPI, automatic validation

6. **Testing**: pytest
   - Why? Industry standard for Python

7. **API Testing**: Postman or Thunder Client
   - Why? Visual interface for testing

## Learning Objectives

By completing this project, you will:

### Fundamental Knowledge
- ✓ Understand what APIs are and how they work
- ✓ Learn HTTP methods and status codes
- ✓ Understand request/response cycle
- ✓ Learn JSON data format

### Practical Skills
- ✓ Set up a Python development environment
- ✓ Build REST API endpoints
- ✓ Connect APIs to databases
- ✓ Perform CRUD operations
- ✓ Validate user input
- ✓ Handle errors gracefully
- ✓ Implement authentication
- ✓ Write API tests
- ✓ Read and write documentation

### Best Practices
- ✓ Code organization and structure
- ✓ Error handling
- ✓ Security basics
- ✓ API design principles
- ✓ Version control with Git

## Project Phases

### Phase 1: Foundation (Week 1)
- Understand APIs conceptually
- Set up development environment
- Create first basic endpoints
- Learn HTTP and JSON

### Phase 2: Data Layer (Week 2)
- Learn database basics
- Connect API to database
- Implement CRUD operations
- Data validation

### Phase 3: Enhancement (Week 3)
- Add filtering and search
- Implement error handling
- Organize code properly
- Add logging

### Phase 4: Production Ready (Week 4)
- Add authentication
- Write tests
- Security improvements
- Documentation

## Success Criteria

You'll know you've succeeded when you can:
1. ✓ Explain what an API is to someone else
2. ✓ Create API endpoints from scratch
3. ✓ Connect your API to a database
4. ✓ Test your API using Postman
5. ✓ Handle errors properly
6. ✓ Implement user authentication
7. ✓ Deploy your API (bonus)
8. ✓ Build a simple frontend that uses your API (bonus)

## Development Workflow

For each feature:
1. **Understand**: Read about the concept
2. **Plan**: Design the endpoint/feature
3. **Code**: Implement the feature
4. **Test**: Verify it works
5. **Debug**: Fix any issues
6. **Document**: Add comments and docs
7. **Commit**: Save your progress (Git)

## Tools You'll Need

1. **Code Editor**: VS Code (recommended) or PyCharm
2. **Python**: Version 3.8 or higher
3. **API Client**: Postman or Thunder Client (VS Code extension)
4. **Terminal**: Command line interface
5. **Browser**: To view automatic API documentation
6. **Git**: Version control (recommended)

## Resources Included

- `README.md`: Project overview and introduction
- `ROADMAP.md`: Detailed learning path with modules
- `modules/`: Step-by-step learning modules
- `exercises/`: Practice problems
- `solutions/`: Reference implementations
- `cheatsheets/`: Quick reference guides

## Timeline

- **Casual Pace**: 4-6 weeks (1-2 hours per day)
- **Regular Pace**: 2-3 weeks (2-3 hours per day)
- **Intensive**: 1-2 weeks (4+ hours per day)

Remember: **Quality over speed!** Take time to understand concepts.

## What Makes This Project Special

1. **Progressive Learning**: Starts simple, gradually adds complexity
2. **Hands-On**: You write every line of code
3. **Real-World**: Same patterns used in production APIs
4. **Self-Paced**: Learn at your own speed
5. **Complete**: From concept to deployment

## After This Project

You'll be ready to:
- Build APIs for your own projects
- Understand API documentation
- Integrate with third-party APIs
- Learn advanced frameworks
- Contribute to API projects
- Interview for backend positions (junior level)

---

Ready to start? Open `ROADMAP.md` and begin with Module 1!
