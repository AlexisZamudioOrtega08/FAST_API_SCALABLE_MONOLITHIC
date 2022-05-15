# FAST_API_SCALABLE

## This repository is a fast API scalable due to its architecture.

### The API support the following features:
    READ Employees: return a list of employees.
    CREATE EMPLOYEE: create a new employee.
    READ Timesheets: return a list of timesheets.
    CREATE Timesheet: create a new timesheet.

#### GET all employees
```http
  method: GET
  localhost:8000/api/v1/employee/all
```

#### POST employee
```http
  method: POST
  localhost:8001/api/v1/employee/add
```

| Parameter      | Type     | Description                         |
| :------------- | :------- | :---------------------------------  |
| `id`           | `int`    | **Required**. Employee id           |
| `first_name`   | `string` | **Required**. Employee first name   |
| `surname`      | `string` | **Required**. Employee surname      |

```http
    {
        "id": 1,
        "first_name": "John",
        "surname": "Doe"
    }
```

#### GET all timesheet entries
```http
  method: GET
  localhost:8000/api/v1/timesheet/all
```

#### POST employee
```http
  method: POST
  localhost:8001/api/v1/timesheet/add
```

| Parameter      | Type     | Description                         |
| :------------- | :------- | :---------------------------------  |
| `emp_id`       | `int`    | **Required**. Employee id           |

```http 
    Example of request: POST
    http://127.0.0.1:8000/api/v1/timesheet/add/?emp_id=2
```

| Parameter      | Type     | Description                         |
| :------------- | :------- | :---------------------------------  |
| `id`           | `int`    | **Required**. Entry id              |
| `hours`        | `int`    | **Required**. Hours worked by emp   |
| `description`  | `string` | **Required**. Description           |


```http
    {
    "id": 0,
    "hours": 0,
    "description": "string"
    }
```

### NOTE: THIS API IS USING A SQLITE AND MYSQL DATABASE TO STORE DATA AND RETRIEVE DATA.

### For installation, please create a python virtual environment and install requirements.txt.

    pip install -r requirements.txt

### Prior to run any steps, you must have installed a mysql database.

    In db folder:
        Create a file called .env
        with the following content:
        ```MYSQL_HOST=<host>
            MYSQL_USER=<user>
            MYSQL_PASSWORD=<password>
            MYSQL_PORT=<port>
            MYSQL_DB=<database_name>
        ```

### Once installated and activated, follow the next steps.
    On terminal:
        Go to app/:
           Crete a environment variable called API_PREFIX with below line:
                export API_PREFIX=/api/v1/
           Run the server:
                uvicorn main:app --reload


#### If the step before was completed successfully, you must have running the server on your local host.

    In order to test the API, you can use the following URL:
            localhost:8000/docs (for the API documentation)