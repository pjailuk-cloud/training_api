# HTTP & REST API Cheatsheet

Quick reference guide for API development.

---

## HTTP Methods

| Method | CRUD | Safe | Idempotent | Use Case |
|--------|------|------|------------|----------|
| GET | Read | ✓ | ✓ | Retrieve resources |
| POST | Create | ✗ | ✗ | Create new resource |
| PUT | Update | ✗ | ✓ | Replace entire resource |
| PATCH | Update | ✗ | ✗ | Update part of resource |
| DELETE | Delete | ✗ | ✓ | Remove resource |

**Safe**: Doesn't modify data
**Idempotent**: Same result if called multiple times

---

## HTTP Status Codes

### 2xx - Success
| Code | Text | Meaning |
|------|------|---------|
| 200 | OK | Request successful |
| 201 | Created | Resource created |
| 204 | No Content | Success, no body returned |

### 3xx - Redirection
| Code | Text | Meaning |
|------|------|---------|
| 301 | Moved Permanently | Resource moved forever |
| 302 | Found | Resource moved temporarily |
| 304 | Not Modified | Use cached version |

### 4xx - Client Errors
| Code | Text | Meaning |
|------|------|---------|
| 400 | Bad Request | Invalid syntax |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method |
| 422 | Unprocessable Entity | Validation error |
| 429 | Too Many Requests | Rate limited |

### 5xx - Server Errors
| Code | Text | Meaning |
|------|------|---------|
| 500 | Internal Server Error | Generic error |
| 502 | Bad Gateway | Invalid response |
| 503 | Service Unavailable | Temporarily down |
| 504 | Gateway Timeout | No response in time |

---

## Common Headers

### Request Headers
```
Authorization: Bearer <token>      # Authentication
Content-Type: application/json     # Body format
Accept: application/json           # Desired response format
User-Agent: MyApp/1.0             # Client info
```

### Response Headers
```
Content-Type: application/json     # Response format
Content-Length: 1234              # Body size in bytes
Cache-Control: no-cache           # Caching rules
Location: /tasks/123              # New resource location (201)
```

---

## REST API URL Structure

```
https://api.example.com:443/v1/tasks/123?status=completed&sort=date
└─┬─┘ └──────┬──────┘ └┬┘ └┬┘└─┬─┘└─┬┘ └──────────┬────────────┘
 Protocol   Domain     Port Version Path ID        Query Parameters
```

---

## REST Endpoint Patterns

### Collections vs Resources

```
GET    /tasks              # Get all tasks (collection)
POST   /tasks              # Create task
GET    /tasks/123          # Get specific task (resource)
PUT    /tasks/123          # Update task
PATCH  /tasks/123          # Partially update task
DELETE /tasks/123          # Delete task
```

### Nested Resources

```
GET    /users/5/tasks      # Get tasks for user 5
POST   /users/5/tasks      # Create task for user 5
GET    /tasks/10/comments  # Get comments for task 10
```

### Actions

```
POST   /tasks/123/complete    # Mark task complete
POST   /tasks/123/assign      # Assign task
PATCH  /tasks/123/priority    # Change priority
```

---

## Query Parameters

### Filtering
```
GET /tasks?status=completed
GET /tasks?priority=high&status=pending
```

### Sorting
```
GET /tasks?sort=created_at
GET /tasks?sort=-created_at    # Descending (- prefix)
```

### Pagination
```
GET /tasks?limit=10&offset=20
GET /tasks?page=3&per_page=10
```

### Search
```
GET /tasks?search=learn
GET /tasks?q=api
```

### Field Selection
```
GET /tasks?fields=id,title,status
```

---

## JSON Examples

### Single Object
```json
{
  "id": 1,
  "title": "Learn APIs",
  "completed": false,
  "created_at": "2024-12-23T10:00:00Z"
}
```

### Array
```json
[
  {"id": 1, "title": "Task 1"},
  {"id": 2, "title": "Task 2"}
]
```

### Nested Object
```json
{
  "id": 1,
  "title": "Learn APIs",
  "user": {
    "id": 5,
    "name": "John"
  }
}
```

### Wrapped Response
```json
{
  "data": [...],
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 10
  }
}
```

---

## Request Examples

### GET Request
```
GET /tasks/123 HTTP/1.1
Host: api.example.com
Accept: application/json
```

### POST Request
```
POST /tasks HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "title": "New Task",
  "priority": "high"
}
```

### PUT Request
```
PUT /tasks/123 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "id": 123,
  "title": "Updated Task",
  "priority": "low",
  "completed": true
}
```

### DELETE Request
```
DELETE /tasks/123 HTTP/1.1
Host: api.example.com
```

---

## Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "title",
        "message": "Title is required"
      }
    ]
  }
}
```

---

## REST Best Practices

1. **Use nouns, not verbs** in URLs
   - ✓ `/tasks`
   - ✗ `/getTasks`

2. **Use plural nouns** for collections
   - ✓ `/tasks`
   - ✗ `/task`

3. **Use proper HTTP methods**
   - ✓ `DELETE /tasks/123`
   - ✗ `GET /tasks/123/delete`

4. **Return appropriate status codes**
   - ✓ 201 Created for POST
   - ✗ 200 OK for everything

5. **Version your API**
   - ✓ `/v1/tasks`
   - ✓ Header: `API-Version: 1.0`

6. **Use JSON** for data
   - Standard, readable, widely supported

7. **Be consistent** in naming
   - ✓ `created_at` everywhere
   - ✗ `createdAt`, `creation_date` mixed

8. **Provide filtering, sorting, pagination**
   - Don't return thousands of records

9. **Use HTTPS** in production
   - Security and encryption

10. **Document your API**
    - Provide examples and explanations

---

## Authentication Patterns

### Bearer Token
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### API Key
```
X-API-Key: your-api-key-here
```

### Basic Auth
```
Authorization: Basic base64(username:password)
```

---

## Common Patterns

### Pagination Response
```json
{
  "data": [...],
  "pagination": {
    "total": 100,
    "count": 10,
    "per_page": 10,
    "current_page": 1,
    "total_pages": 10,
    "links": {
      "next": "/tasks?page=2",
      "prev": null
    }
  }
}
```

### Timestamp Formats
```
ISO 8601: "2024-12-23T10:00:00Z"
Unix: 1703328000
```

---

## Quick Reference

| Task | Method | Endpoint | Body | Response |
|------|--------|----------|------|----------|
| List | GET | /tasks | - | 200 + array |
| Get | GET | /tasks/1 | - | 200 + object |
| Create | POST | /tasks | object | 201 + object |
| Update | PUT | /tasks/1 | object | 200 + object |
| Delete | DELETE | /tasks/1 | - | 204 |

---

Keep this handy while developing your API!
