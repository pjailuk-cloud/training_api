# Module 2: Development Environment Setup

**Duration**: 1-2 hours
**Prerequisites**: Module 1
**Goal**: Set up your computer for API development

---

## Table of Contents
1. [What We'll Install](#what-well-install)
2. [Check Python Installation](#check-python-installation)
3. [Understanding Virtual Environments](#understanding-virtual-environments)
4. [Create Virtual Environment](#create-virtual-environment)
5. [Install FastAPI and Dependencies](#install-fastapi-and-dependencies)
6. [Install Development Tools](#install-development-tools)
7. [Your First "Hello World" API](#your-first-hello-world-api)
8. [Testing Your API](#testing-your-api)
9. [Understanding What Happened](#understanding-what-happened)
10. [Troubleshooting](#troubleshooting)
11. [Next Steps](#next-steps)

---

## What We'll Install

### Required
- ✅ **Python 3.8+** - Programming language (You have 3.14!)
- ✅ **pip** - Python package manager (You have it!)
- **virtualenv** - Isolated Python environments
- **FastAPI** - Web framework for building APIs
- **Uvicorn** - Web server to run your API

### Optional (Recommended)
- **VS Code** - Code editor with great Python support
- **Postman** or **Thunder Client** - Test your APIs visually
- **Git** - Version control (save your progress)

### NOT Needed Yet
- ❌ Docker - We'll use this later for deployment
- ❌ PostgreSQL - We'll start with SQLite (built-in)

---

## Check Python Installation

You already have Python installed! Let's verify:

### On Windows (PowerShell or CMD)
```bash
python --version
```

**Expected output**: `Python 3.14.0` ✅ (or 3.8+)

### Check pip
```bash
pip --version
```

**Expected output**: `pip 25.2...` ✅

**If you see version numbers, you're ready!**

---

## Understanding Virtual Environments

### What is a Virtual Environment?

Think of it as a **separate workspace** for your project:
- Each project has its own packages
- No conflicts between projects
- Easy to share requirements with others

### Real-World Analogy

Imagine you're a chef:
- **Without virtual env**: One kitchen for all recipes - spices mix, tools get confused
- **With virtual env**: Separate kitchen for each cuisine - organized, no mixing

### Why Use It?

```
Project A needs FastAPI 0.100.0
Project B needs FastAPI 0.95.0

Without virtual env: CONFLICT! ❌
With virtual env: Both work perfectly! ✅
```

---

## Create Virtual Environment

### Step 1: Navigate to Project Directory

You're already here!
```bash
cd C:\training_api
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

**What this does**:
- `python -m venv` - Use Python's built-in venv module
- `venv` - Name of the folder to create (conventional name)

**Wait a few seconds...** This creates a `venv/` folder with a fresh Python installation.

### Step 3: Activate Virtual Environment

**On Windows (PowerShell)**:
```bash
venv\Scripts\Activate.ps1
```

**On Windows (CMD)**:
```bash
venv\Scripts\activate.bat
```

**On Mac/Linux**:
```bash
source venv/bin/activate
```

**How to know it worked?**

You'll see `(venv)` at the start of your terminal prompt:
```
(venv) C:\training_api>
```

### Step 4: Verify Isolated Environment

```bash
which python  # Mac/Linux
where python  # Windows
```

Should point to `venv/Scripts/python` or similar.

---

## Install FastAPI and Dependencies

Now that your virtual environment is active, let's install packages!

### Install FastAPI

```bash
pip install fastapi
```

**What you'll see**:
```
Collecting fastapi
Downloading fastapi-0.xxx.x-py3-none-any.whl
Installing collected packages: ...
Successfully installed fastapi-0.xxx.x
```

### Install Uvicorn (Web Server)

```bash
pip install "uvicorn[standard]"
```

**Why Uvicorn?**
- FastAPI needs a server to run
- Uvicorn is fast and recommended
- `[standard]` includes useful extras

### Install Other Essentials

```bash
pip install pydantic sqlalchemy python-dotenv
```

**What these do**:
- **pydantic** - Data validation (comes with FastAPI but we're being explicit)
- **sqlalchemy** - Database ORM (for later modules)
- **python-dotenv** - Manage environment variables

### Verify Installation

```bash
pip list
```

You should see:
- fastapi
- uvicorn
- pydantic
- sqlalchemy
- and their dependencies

### Save Requirements

Create a `requirements.txt` file to remember what you installed:

```bash
pip freeze > requirements.txt
```

**Why?**
- Share your project with others
- Reinstall packages on another computer
- Track exact versions

---

## Install Development Tools

### 1. Code Editor (If you don't have one)

**Recommended: VS Code**
- Download: https://code.visualstudio.com/
- Free and popular
- Great Python support

**After installing VS Code**:
Install Python extension:
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search "Python"
4. Install "Python" by Microsoft

### 2. API Testing Tool

**Option A: Thunder Client (VS Code Extension)**
1. In VS Code Extensions
2. Search "Thunder Client"
3. Install it
4. Icon appears in sidebar

**Option B: Postman (Standalone App)**
- Download: https://www.postman.com/downloads/
- More features but separate app

**For beginners**: Thunder Client is easier!

### 3. Git (Optional but Recommended)

**Check if you have it**:
```bash
git --version
```

**If not installed**:
- Windows: https://git-scm.com/download/win
- Mac: `brew install git` or download from site
- Linux: `sudo apt install git`

---

## Your First "Hello World" API

Let's create your very first API! 🎉

### Step 1: Create the File

Create a new file: `C:\training_api\app\main.py`

**Full code**:
```python
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Create your first endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {
        "name": "Task Manager API",
        "version": "1.0",
        "description": "My first API!"
    }
```

### Step 2: Understand the Code

Let's break it down:

```python
from fastapi import FastAPI
```
- Import the FastAPI class

```python
app = FastAPI()
```
- Create an instance of FastAPI
- This `app` is your entire API

```python
@app.get("/")
```
- **Decorator** that creates an endpoint
- `@app` - Using the FastAPI instance
- `.get` - HTTP GET method
- `("/")` - URL path (root)

```python
def read_root():
    return {"message": "Hello World"}
```
- Function that runs when endpoint is called
- Returns a Python dictionary
- FastAPI automatically converts to JSON!

### Step 3: Run Your API

In your terminal (with venv activated):

```bash
uvicorn app.main:app --reload
```

**Breaking down the command**:
- `uvicorn` - The server program
- `app.main` - File location (app folder, main.py file)
- `:app` - The variable name in main.py
- `--reload` - Auto-restart when you change code (dev mode)

**Expected output**:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Your API is now running!** 🎉

---

## Testing Your API

### Method 1: Browser

Open your browser and go to:
- http://localhost:8000

**You should see**:
```json
{"message":"Hello World"}
```

Try the other endpoint:
- http://localhost:8000/about

### Method 2: Interactive API Documentation

FastAPI automatically creates beautiful documentation!

**Open in browser**:
- http://localhost:8000/docs

**You'll see**:
- Swagger UI with all your endpoints
- Click "Try it out" to test
- See request/response examples
- All automatically generated!

**Alternative docs**:
- http://localhost:8000/redoc (different style)

### Method 3: Command Line (curl)

```bash
curl http://localhost:8000
```

### Method 4: Thunder Client / Postman

**Thunder Client**:
1. Open Thunder Client in VS Code
2. Click "New Request"
3. Enter: `http://localhost:8000`
4. Click "Send"

**Postman**:
1. Open Postman
2. Create new request
3. GET `http://localhost:8000`
4. Click "Send"

---

## Understanding What Happened

### The Request-Response Flow

1. **You** opened `http://localhost:8000` in browser
2. **Browser** sent HTTP GET request to your API
3. **Uvicorn** received the request
4. **FastAPI** matched the request to `@app.get("/")`
5. **Your function** `read_root()` executed
6. **Returned** `{"message": "Hello World"}`
7. **FastAPI** converted dict to JSON
8. **Uvicorn** sent HTTP response back
9. **Browser** displayed the JSON

All in milliseconds!

### What is localhost:8000?

- **localhost** = Your own computer (IP: 127.0.0.1)
- **8000** = Port number (like an apartment number)
- Only accessible from your computer (for now)

### What is --reload?

- Watches your files for changes
- Automatically restarts server when you save
- **Only use in development!**
- Press `Ctrl+C` to stop the server

---

## Project Structure So Far

```
training_api/
├── venv/                    # Virtual environment (don't edit)
├── app/
│   └── main.py             # Your API code ✨
├── modules/                 # Learning materials
├── requirements.txt         # Installed packages
└── ... (other docs)
```

---

## Troubleshooting

### Issue: "python not recognized"

**Solution**: Python not in PATH
- Reinstall Python
- Check "Add Python to PATH" during installation

### Issue: "No module named fastapi"

**Solution**: Virtual environment not activated
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

Then install again:
```bash
pip install fastapi uvicorn
```

### Issue: "Address already in use"

**Solution**: Port 8000 is taken
- Stop other server (Ctrl+C)
- Or use different port:
  ```bash
  uvicorn app.main:app --reload --port 8001
  ```

### Issue: "Cannot activate virtual environment (PowerShell)"

**Solution**: Execution policy restricted
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again.

### Issue: Can't access http://localhost:8000

**Checklist**:
- [ ] Is server running? (Check terminal)
- [ ] Any error messages in terminal?
- [ ] Correct URL? (localhost:8000, not 0.0.0.0:8000)
- [ ] Firewall blocking?

---

## Practice Exercises

### Exercise 1: Add a New Endpoint

Add a `/hello/{name}` endpoint that greets a person:

```python
@app.get("/hello/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}!"}
```

Test: http://localhost:8000/hello/John

### Exercise 2: Add a Health Check

Create `/health` endpoint:
```python
@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": "2024-12-23T10:00:00Z"}
```

### Exercise 3: Return Different Data

Create `/stats` endpoint with multiple fields:
```python
@app.get("/stats")
def get_stats():
    return {
        "total_users": 100,
        "active_tasks": 25,
        "completed_tasks": 75,
        "api_version": "1.0.0"
    }
```

### Exercise 4: Explore Auto Docs

1. Add all 3 endpoints above
2. Go to http://localhost:8000/docs
3. Try each endpoint using the "Try it out" button
4. Notice how the documentation updated automatically!

---

## Development Workflow

Your daily routine will be:

1. **Activate virtual environment**
   ```bash
   venv\Scripts\activate
   ```

2. **Start the server**
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Make changes** to code

4. **Test** (browser or /docs)

5. **See changes** automatically (thanks to --reload)

6. **Stop server** when done
   ```bash
   Ctrl+C
   ```

---

## Key Takeaways

After this module, you should understand:

✓ What virtual environments are and why to use them
✓ How to install packages with pip
✓ How to create a basic FastAPI application
✓ How to run your API with Uvicorn
✓ How to test endpoints in browser and /docs
✓ The request-response cycle
✓ Auto-generated documentation

---

## Checklist

Before moving to Module 3, make sure you can:

- [ ] Activate your virtual environment
- [ ] See (venv) in your terminal
- [ ] Run `uvicorn app.main:app --reload`
- [ ] Access http://localhost:8000
- [ ] See your API response in browser
- [ ] Access http://localhost:8000/docs
- [ ] Test endpoints in Swagger UI
- [ ] Add a new endpoint
- [ ] See it appear in docs automatically

---

## What's Next?

In **Module 3**, you'll learn:
- Path parameters (e.g., `/tasks/123`)
- Query parameters (e.g., `/tasks?status=completed`)
- Request bodies (sending data)
- Response models
- Multiple endpoints for CRUD operations

---

## Commands Cheat Sheet

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install packages
pip install fastapi uvicorn

# Save requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Run API
uvicorn app.main:app --reload

# Run on different port
uvicorn app.main:app --reload --port 8001

# Deactivate virtual environment
deactivate
```

---

## Additional Resources

- FastAPI Documentation: https://fastapi.tiangolo.com/
- Python venv Guide: https://docs.python.org/3/library/venv.html
- Uvicorn Documentation: https://www.uvicorn.org/

---

**Congratulations!** 🎉 You've set up your development environment and created your first API! Ready for Module 3?
