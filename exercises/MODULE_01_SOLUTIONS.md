# Module 1: Practice Exercise Solutions

Solutions and explanations for Module 1 exercises.

---

## Exercise 1: Identify the Parts

**Request**:
```
GET /api/users/123?include=posts HTTP/1.1
Host: example.com
Authorization: Bearer token123
```

**Answers**:

1. **What is the HTTP method?**
   - **GET** - Used to retrieve data

2. **What is the path?**
   - **/api/users/123** - The URL path to the resource

3. **What is the query parameter?**
   - **include=posts** - A query parameter asking to include related posts

4. **What is the purpose of the Authorization header?**
   - Provides authentication credentials (Bearer token) to prove identity

**Complete breakdown**:
```
GET                      → HTTP Method
/api/users/123           → Path to resource
?include=posts           → Query parameter
HTTP/1.1                 → Protocol version
Host: example.com        → Header: server address
Authorization: Bearer... → Header: authentication
```

---

## Exercise 2: Choose the Right Method

**Questions and Answers**:

1. **Getting a user's profile?**
   - **GET** - Retrieving data, no modifications

2. **Creating a new blog post?**
   - **POST** - Creating new resource

3. **Deleting a comment?**
   - **DELETE** - Removing a resource

4. **Updating your email address?**
   - **PATCH** or **PUT**
     - **PATCH**: If updating only the email field (partial update)
     - **PUT**: If updating the entire user profile (full update)
   - Best practice: **PATCH** for changing one field

5. **Marking a task as complete?**
   - **PATCH** - Partial update of task status
   - Could also be **POST** to `/tasks/123/complete` if designed as an action

**Summary**:
- **GET**: Read/Retrieve
- **POST**: Create
- **PUT**: Replace entire resource
- **PATCH**: Update part of resource
- **DELETE**: Remove

---

## Exercise 3: Match Status Codes

**Scenarios and Codes**:

1. **User successfully created**
   - **201 Created** - Resource was created successfully
   - Server should also return the created user in the response

2. **Task not found**
   - **404 Not Found** - The requested resource doesn't exist
   - Example: GET /tasks/999 when task 999 doesn't exist

3. **Successfully retrieved tasks**
   - **200 OK** - Request successful, data returned
   - Most common success code

4. **Invalid email format**
   - **400 Bad Request** or **422 Unprocessable Entity**
   - 400: Generic client error
   - 422: Specifically for validation errors (more precise)

5. **Server crashed**
   - **500 Internal Server Error** - Something went wrong on the server
   - The client's request was fine, but server failed to process it

**Remember**:
- **2xx**: Success
- **4xx**: Client made a mistake
- **5xx**: Server made a mistake

---

## Exercise 4: Design a REST API

**Blog API Design**:

```
# Posts
GET    /posts              # Get all blog posts
GET    /posts/{id}         # Get a specific post
POST   /posts              # Create a new post
PUT    /posts/{id}         # Update entire post
PATCH  /posts/{id}         # Update part of post
DELETE /posts/{id}         # Delete a post

# Comments (nested under posts)
GET    /posts/{id}/comments         # Get all comments for a post
GET    /posts/{id}/comments/{cid}   # Get specific comment
POST   /posts/{id}/comments         # Create comment on a post
PUT    /posts/{id}/comments/{cid}   # Update a comment
DELETE /posts/{id}/comments/{cid}   # Delete a comment
```

**Alternative design** (if comments are independent):
```
GET    /comments?post_id={id}   # Get comments filtered by post
GET    /comments/{id}           # Get specific comment
POST   /comments                # Create comment (with post_id in body)
PUT    /comments/{id}           # Update comment
DELETE /comments/{id}           # Delete comment
```

**Best practices demonstrated**:
- Plural nouns (posts, not post)
- Nested resources for related data
- Consistent URL structure
- Proper HTTP methods

---

## Exercise 5: Create JSON

**Sample Solution**:

```json
{
  "name": "Sarah Johnson",
  "age": 28,
  "hobbies": [
    "reading",
    "hiking",
    "photography",
    "coding"
  ],
  "address": {
    "city": "San Francisco",
    "country": "USA"
  },
  "isStudent": false
}
```

**Key points**:
- Strings in double quotes: `"name": "Sarah"`
- Numbers without quotes: `"age": 28`
- Arrays use square brackets: `[...]`
- Objects use curly braces: `{...}`
- Booleans lowercase: `true` or `false`
- Proper comma placement (no trailing comma after last item)

**Another example**:

```json
{
  "name": "Alex Chen",
  "age": 22,
  "hobbies": [
    "gaming",
    "music production"
  ],
  "address": {
    "city": "Toronto",
    "country": "Canada"
  },
  "isStudent": true
}
```

---

## Additional Practice

### Practice 1: Build a Complete Request

Create a POST request to create a task:

**Solution**:
```
POST /tasks HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer your-token-here

{
  "title": "Complete Module 1",
  "description": "Finish all exercises and quiz",
  "priority": "high",
  "due_date": "2024-12-25"
}
```

### Practice 2: Understand Response

If the above request succeeds, what response would you expect?

**Solution**:
```
HTTP/1.1 201 Created
Content-Type: application/json
Location: /tasks/15

{
  "id": 15,
  "title": "Complete Module 1",
  "description": "Finish all exercises and quiz",
  "priority": "high",
  "due_date": "2024-12-25",
  "status": "pending",
  "completed": false,
  "created_at": "2024-12-23T10:00:00Z",
  "updated_at": "2024-12-23T10:00:00Z"
}
```

**Why this response?**:
- **201 Created**: Resource was created
- **Location header**: Tells you where the new resource is
- **Response body**: Returns the created task with server-generated fields (id, timestamps)
- **Content-Type**: Tells you the format (JSON)

### Practice 3: Error Scenario

What if you tried to create a task without a title?

**Solution**:
```
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
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

## Common Mistakes to Avoid

1. **Wrong HTTP method**
   - ✗ GET /tasks/create
   - ✓ POST /tasks

2. **Verbs in URLs**
   - ✗ /getTasks
   - ✓ /tasks

3. **Singular nouns**
   - ✗ /task
   - ✓ /tasks

4. **Invalid JSON**
   - ✗ `{name: "John"}` (missing quotes on key)
   - ✓ `{"name": "John"}`

5. **Wrong status code**
   - ✗ 200 OK when creating
   - ✓ 201 Created when creating

---

## Review Checklist

Before moving to Module 2, make sure you understand:

- [ ] What an API is and why we use them
- [ ] The difference between GET, POST, PUT, DELETE
- [ ] What HTTP status codes mean
- [ ] How to read and write JSON
- [ ] The structure of HTTP requests and responses
- [ ] REST API URL conventions
- [ ] Query parameters vs path parameters

If any of these are unclear, review the relevant section in Module 1.

---

**Great job completing the exercises!** You're ready for Module 2.
