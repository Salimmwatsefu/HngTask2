# HngTask2

# API Documentation for [person_api]

## Base URL

The base URL for all API endpoints is: `http://your-api-url.com/`

## Endpoints

### Create a Person

- **Endpoint**: `/persons/`
- **Method**: POST
- **Description**: Create a new person.
- **Request Body**:
  ```json
  {
      "name": "string",
      "age": integer
  }
  ```
- **Response**:
  - **Status Code**: 201 (Created)
  - **Response Body**:
    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

### Retrieve a Person

- **Endpoint**: `/persons/<int:id>/`
- **Method**: GET
- **Description**: Retrieve a person by their ID.
- **Response**:
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

### Update a Person

- **Endpoint**: `/persons/<int:id>/`
- **Method**: PUT
- **Description**: Update a person's details.
- **Request Body**:
  ```json
  {
      "name": "string",
      "age": integer
  }
  ```
- **Response**:
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

### Partially Update a Person

- **Endpoint**: `/persons/<int:id>/`
- **Method**: PATCH
- **Description**: Partially update a person's details.
- **Request Body**:
  ```json
  {
      "name": "string" (optional),
      "age": integer (optional)
  }
  ```
- **Response**:
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

### Delete a Person

- **Endpoint**: `/persons/<int:id>/`
- **Method**: DELETE
- **Description**: Delete a person by their ID.
- **Response**:
  - **Status Code**: 204 (No Content)

## Usage Examples

### Create a Person

**Request**:
```http
POST /persons/
Content-Type: application/json

{
    "name": "John Doe",
    "age": 30
}
```

**Response**:
```json
{
    "id": 1,
    "name": "John Doe",
    "age": 30
}
```

### Retrieve a Person

**Request**:
```http
GET /persons/1
```

**Response**:
```json
{
    "id": 1,
    "name": "John Doe",
    "age": 30
}
```

### Update a Person

**Request**:
```http
PUT /persons/1
Content-Type: application/json

{
    "name": "Updated John Doe",
    "age": 35
}
```

**Response**:
```json
{
    "id": 1,
    "name": "Updated John Doe",
    "age": 35
}
```

### Partially Update a Person

**Request**:
```http
PATCH /persons/1
Content-Type: application/json

{
    "age": 40
}
```

**Response**:
```json
{
    "id": 1,
    "name": "Updated John Doe",
    "age": 40
}
```

### Delete a Person

**Request**:
```http
DELETE /persons/1
```

**Response**:
```http
HTTP/1.1 204 No Content
```
