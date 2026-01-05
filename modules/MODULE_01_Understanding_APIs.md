# Module 1: Understanding APIs

**Duration**: 2-3 hours
**Prerequisites**: None
**Goal**: Understand what APIs are and how they work

---

## Table of Contents
1. [What is an API?](#what-is-an-api)
2. [Real-World Analogy](#real-world-analogy)
3. [Why Do We Need APIs?](#why-do-we-need-apis)
4. [How APIs Work](#how-apis-work)
5. [Types of APIs](#types-of-apis)
6. [HTTP Protocol Basics](#http-protocol-basics)
7. [HTTP Methods](#http-methods)
8. [HTTP Status Codes](#http-status-codes)
9. [Request and Response](#request-and-response)
10. [JSON Format](#json-format)
11. [Practice Exercises](#practice-exercises)
12. [Quiz](#quiz)
13. [Next Steps](#next-steps)

---

## What is an API?

**API** = **Application Programming Interface**

In simple terms: **An API is a messenger that allows two applications to talk to each other.**

Think of it as a contract:
- "If you ask me for X in this way, I'll give you Y in response"

### Example in Daily Life

When you use a mobile app to check the weather:
- **Your app** asks the weather service: "What's the weather in New York?"
- **The API** carries your request to the weather service
- **The weather service** finds the data and sends it back
- **The API** delivers the response to your app
- **Your app** shows you the weather

The API is the invisible messenger making this happen!

---

## Real-World Analogy

### The Restaurant Analogy

Imagine you're at a restaurant:

1. **You (Client)**: Want to order food
2. **Menu (API Documentation)**: Shows what you can order
3. **Waiter (API)**: Takes your order and brings your food
4. **Kitchen (Server/Database)**: Prepares the food

**The Process**:
- You look at the menu (read API docs)
- You tell the waiter what you want (make a request)
- The waiter takes it to the kitchen (API processes request)
- The kitchen cooks (server processes data)
- The waiter brings your food (API returns response)
- You eat (use the data)

**Why don't you go to the kitchen yourself?**
- You don't need to know how to cook
- The kitchen stays organized
- You get exactly what you ordered
- The kitchen can serve many customers at once

This is exactly how APIs work!

---

## Why Do We Need APIs?

### 1. Separation of Concerns
- Frontend (what users see) and Backend (data/logic) are separate
- Each team can work independently
- Easier to maintain and update

### 2. Reusability
- One API can serve many clients:
  - Web browser
  - Mobile app (iOS/Android)
  - Desktop application
  - Other servers

### 3. Security
- Don't expose your database directly
- Control what data users can access
- Add authentication and authorization

### 4. Scalability
- Handle many users at once
- Distribute load across servers
- Cache common requests

### 5. Integration
- Connect different services together
- Use third-party services (payment, maps, social media)
- Build ecosystems of applications

---

## How APIs Work

### The Request-Response Cycle

```
[Client] ----request----> [API] ----query----> [Database]

[Client] <---response---- [API] <---data----- [Database]
```

### Step-by-Step Example

Let's say you want to get a list of tasks:

1. **Client sends request**:
   - "GET /tasks" - I want all tasks

2. **API receives request**:
   - Validates the request
   - Checks if user is authorized

3. **API queries database**:
   - "SELECT * FROM tasks"

4. **Database returns data**:
   - Returns all task records

5. **API formats response**:
   - Converts data to JSON
   - Adds status code

6. **Client receives response**:
   - Displays tasks to user

All of this happens in milliseconds!

---

## Types of APIs

### 1. REST API (What we'll build)
- **REST** = Representational State Transfer
- Uses HTTP protocol
- Works with URLs and standard HTTP methods
- Returns data (usually JSON)
- Stateless (each request is independent)

**Example**:
```
GET /tasks          → Get all tasks
POST /tasks         → Create a task
GET /tasks/1        → Get task with ID 1
PUT /tasks/1        → Update task 1
DELETE /tasks/1     → Delete task 1
```

### 2. GraphQL API
- Ask for exactly what you need
- Single endpoint
- Flexible queries

### 3. SOAP API
- Older protocol
- Uses XML
- More complex

### 4. WebSocket API
- Real-time, two-way communication
- Chat apps, live updates

**For this course, we focus on REST API because**:
- Most common type
- Easy to understand
- Industry standard
- Great for learning

---

## HTTP Protocol Basics

**HTTP** = **HyperText Transfer Protocol**

It's the language browsers and servers use to communicate.

### Key Concepts

1. **URLs (Uniform Resource Locator)**
   ```
   https://api.example.com:443/tasks/123?status=completed
   └─┬─┘ └──────┬──────┘ └┬┘ └──┬──┘ └───────┬────────┘
   Protocol   Domain     Port  Path      Query
   ```

2. **Client**: Makes requests (browser, mobile app, etc.)
3. **Server**: Receives requests and sends responses
4. **Request**: What the client sends
5. **Response**: What the server sends back

### HTTP is Stateless

Each request is independent - the server doesn't remember previous requests.

**Example**:
- Request 1: "What's the weather?"
- Request 2: "What about tomorrow?"
- Server doesn't remember you asked about weather

Solution: Use authentication tokens to maintain "state"

---

## HTTP Methods

HTTP methods define what action you want to perform.

### The Main Four (CRUD)

| Method | Action | CRUD | Example |
|--------|--------|------|---------|
| **GET** | Retrieve data | Read | Get all tasks |
| **POST** | Create new data | Create | Add a new task |
| **PUT** | Update data (full) | Update | Update entire task |
| **DELETE** | Remove data | Delete | Delete a task |

### Additional Methods

| Method | Action | Example |
|--------|--------|---------|
| **PATCH** | Update data (partial) | Change only task title |
| **HEAD** | Get headers only | Check if resource exists |
| **OPTIONS** | Get allowed methods | What can I do with this endpoint? |

### Examples

```
GET /tasks
→ "Give me all tasks"

POST /tasks
Body: {"title": "Learn APIs"}
→ "Create a new task with this data"

GET /tasks/5
→ "Give me task number 5"

PUT /tasks/5
Body: {"title": "Learn APIs", "completed": true}
→ "Update task 5 with this data"

DELETE /tasks/5
→ "Delete task number 5"
```

---

## HTTP Status Codes

Status codes tell you if your request succeeded or failed.

### Success Codes (2xx)

| Code | Meaning | When Used |
|------|---------|-----------|
| **200** | OK | GET request successful |
| **201** | Created | POST request successful |
| **204** | No Content | DELETE successful, nothing to return |

### Client Error (4xx)

| Code | Meaning | When Used |
|------|---------|-----------|
| **400** | Bad Request | Invalid data sent |
| **401** | Unauthorized | Need to log in |
| **403** | Forbidden | Logged in but not allowed |
| **404** | Not Found | Resource doesn't exist |
| **422** | Unprocessable Entity | Validation failed |

### Server Error (5xx)

| Code | Meaning | When Used |
|------|---------|-----------|
| **500** | Internal Server Error | Something went wrong on server |
| **502** | Bad Gateway | Server is down |
| **503** | Service Unavailable | Server overloaded |

### Quick Memory Aid

- **2xx**: Success - "Everything is good!"
- **3xx**: Redirection - "Go look over there"
- **4xx**: Client error - "You made a mistake"
- **5xx**: Server error - "I made a mistake"

---

## Request and Response

### Anatomy of an HTTP Request

```
POST /tasks HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer abc123token

{
  "title": "Learn APIs",
  "priority": "high"
}
```

**Parts**:
1. **Request Line**: Method, Path, Protocol
2. **Headers**: Metadata (content type, auth, etc.)
3. **Body**: The data you're sending (for POST/PUT)

### Anatomy of an HTTP Response

```
HTTP/1.1 201 Created
Content-Type: application/json
Date: Mon, 23 Dec 2024 10:00:00 GMT

{
  "id": 1,
  "title": "Learn APIs",
  "priority": "high",
  "created_at": "2024-12-23T10:00:00Z"
}
```

**Parts**:
1. **Status Line**: Protocol, Status Code, Status Text
2. **Headers**: Metadata about the response
3. **Body**: The data being returned

---

## JSON Format

**JSON** = **JavaScript Object Notation**

It's a way to structure data that both humans and computers can read easily.

### Basic Structure

```json
{
  "key": "value",
  "name": "John",
  "age": 30,
  "active": true
}
```

### Data Types

```json
{
  "string": "Hello",
  "number": 42,
  "decimal": 3.14,
  "boolean": true,
  "null": null,
  "array": [1, 2, 3],
  "object": {
    "nested": "value"
  }
}
```

### Example: Task Object

```json
{
  "id": 1,
  "title": "Learn APIs",
  "description": "Complete Module 1",
  "status": "in-progress",
  "priority": "high",
  "due_date": "2024-12-25",
  "tags": ["learning", "api", "backend"],
  "completed": false,
  "created_at": "2024-12-23T10:00:00Z"
}
```

### Array of Tasks

```json
[
  {
    "id": 1,
    "title": "Learn APIs",
    "completed": false
  },
  {
    "id": 2,
    "title": "Build an API",
    "completed": false
  }
]
```

---

## Practice Exercises

### Exercise 1: Identify the Parts

For this API request, identify each part:
```
GET /api/users/123?include=posts HTTP/1.1
Host: example.com
Authorization: Bearer token123
```
**Request Line**: method GET, Path=/api/users/123?include=post, Protocal HTTP/1.1
**Header** Host:example

**Questions**:
1. What is the HTTP method? GET
2. What is the path? /api/users /api/users/
3. What is the query parameter? 123?include=post
4. What is the purpose of the Authorization header? get information of user 123

### Exercise 2: Choose the Right Method

What HTTP method would you use for:
1. Getting a user's profile? GET
2. Creating a new blog post? POST
3. Deleting a comment? DELETE
4. Updating your email address? PUT
5. Marking a task as complete? Patch

### Exercise 3: Match Status Codes

Match the scenario to the correct status code:
1. User successfully created → 201
2. Task not found → 204
3. Successfully retrieved tasks → 200
4. Invalid email format → 400
5. Server crashed → 500

### Exercise 4: Design a REST API

Design endpoints for a blog:
- Get all posts GET /posts
- Get a specific post GET /posts/{postid}
- Create a new post POST /posts/insert
- Update a post PUT /posts/{postid}
- Delete a post DELETE /posts/{postid}
- Get comments for a post GET /posts/{postid}

### Exercise 5: Create JSON

Create a JSON object representing yourself:
- name
- age
- hobbies (array)
- address (nested object with city and country)
- isStudent (boolean)
```json
{
   "name": "Paramet Jailuk",
   "age": 51,
   "hobies": ["reading", "walk"],
   "address": {
      "address1": "",
      "postalcode": ""
   },
   "isStudent": false
}
```
---

## Quiz

Test your understanding:

1. **What does API stand for?**
   - a) Application Programming Interface /
   - b) Advanced Program Integration
   - c) Automated Process Interface

2. **Which HTTP method is used to retrieve data?**
   - a) POST
   - b) GET /
   - c) DELETE

3. **What does a 404 status code mean?**
   - a) Success
   - b) Not Found /
   - c) Server Error

4. **What format does REST API commonly use?**
   - a) XML
   - b) JSON   /
   - c) CSV

5. **True or False: HTTP is stateful**
   - a) True   /
   - b) False

6. **Which status code means "Created successfully"?**
   - a) 200
   - b) 201 /
   - c) 204

7. **What does CRUD stand for?**
   - a) Create, Read, Update, Delete   /
   - b) Connect, Request, Upload, Download   
   - c) Code, Run, Update, Debug

**Answers at the end of the module**

---

## Key Takeaways

After this module, you should understand:

✓ APIs are messengers between applications
✓ REST APIs use HTTP methods and URLs
✓ GET retrieves, POST creates, PUT updates, DELETE removes
✓ Status codes tell you if requests succeeded
✓ JSON is the common format for API data
✓ Requests have methods, headers, and body
✓ Responses have status codes, headers, and body

---

## Next Steps

1. Review any concepts you found confusing
2. Answer the practice exercises
3. Check your answers against the solutions
4. Move on to Module 2: Setting Up Your Development Environment

---

## Quiz Answers

1. a) Application Programming Interface
2. b) GET
3. b) Not Found
4. b) JSON
5. b) False (HTTP is stateless)
6. b) 201
7. a) Create, Read, Update, Delete

---

## Additional Resources

Want to learn more?
- MDN Web Docs: HTTP Guide
- REST API Tutorial website
- Play with public APIs (list in exercises folder)

---

**Congratulations!** You've completed Module 1. You now understand what APIs are and how they work. Ready for Module 2?
