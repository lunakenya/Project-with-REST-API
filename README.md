# FastAPI REST API Example

This project is a basic REST API built with **FastAPI**. It includes a simple "Hello, World!" endpoint and uses **Ngrok** to expose the application to the internet for testing and external access.

## Features
- **FastAPI**: Lightweight Python framework for building APIs.
- **Ngrok**: Tool to create a secure tunnel to expose the API publicly.
- **Automatic Documentation**: Includes Swagger UI at `/docs` and ReDoc at `/redoc`.

## Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Ngrok (installed and configured)

## Installation
1. Clone this repository:
   ```bash
   git clone 
   cd fastapi-rest-api
2. Create a virtual environment and activate it:
   - **On Windows**:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
   - **On Linux/MacOS**:
     ```bash
     python -m venv env
     source env/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn

## Running the Application

Start the FastAPI server:
    
    uvicorn main:app --reload --port 8080

Ngrok:
    
    (https://fc33-2800-bf0-249-1291-1c45-4f9e-e335-f8d5.ngrok-free.app/)

