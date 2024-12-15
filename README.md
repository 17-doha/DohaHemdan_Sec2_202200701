# Book API with Flask and Docker

This project is a simple Book API built with Flask and Docker. It allows you to manage books, including adding, listing, searching, updating, and deleting books. The API also provides a Swagger UI interface for easy interaction and testing of endpoints.

### Prerequisites

- Docker (Ensure Docker is installed on your machine)
- Python 3.9 or more (Used in the Docker image)
- Flask and Flask-Swagger-UI libraries (installed in the Docker container)

### Step-by-Step Instructions

---

## a. **Building and Running the Docker Container**

### 1. Clone the repository:

First, clone this repository to your local machine or download the files.

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Build the Docker image:

Once inside the project directory, run the following command to build the Docker image.

```bash
docker build -t flask-book-api .
```

### 3. Run the Docker container:

After building the image, you can run the container with the following command:

```bash
docker run -p 5000:5000 --name flask_app flask-book-api
```

# Accessing Swagger

### 1. Open Swagger UI

Once the container is running, open your web browser and navigate to:

```bash
http://localhost:5000/api-docs
```

### 2. Test the API


=======
View detailed API documentation for all available routes  
Use the Swagger UI interface to send requests (GET, POST, PUT, DELETE) and see responses directly in the browser  
Example routes available in the documentation:  


POST /books/add-book: Add a new book  
GET /books/list-all-books: List all books  
GET /books/search-books: Search for books based on author, year, or genre  
PUT /books/<isbn>: Update a book by its ISBN  
DELETE /books/<isbn>: Delete a book by its ISBN  
