# UAVRental






# UAV Rental Management System

The UAV Rental Management System is a web application designed to manage the rental of Unmanned Aerial Vehicles (UAVs). It provides a platform for users to browse available UAVs, make rental reservations, and manage their rental history.

## Features

- Browse a list of available UAVs with details such as brand, model, weight, and category.
- View rental history, including past and upcoming reservations.
- Make new rental reservations with specified start and end dates.
- User authentication and authorization to ensure data privacy and security.
- API endpoints for programmatic access to UAV data.
- Docker support for easy project setup and deployment.
- Well-crafted documentation and comments throughout the codebase.
- Unit testing to ensure code reliability.
- Use of the DataTable library for listing pages.
- Implementation of server-side DataTable for efficient data handling.
- Integration of asynchronous techniques Fetch on the frontend.
- Organization of relational tables for better database structure.
- Utilization of additional Django libraries for enhanced functionality.
- Choice of frontend frameworks such as Bootstrap.

### Membership and Login Screen
- Users can register for membership and log in securely.

### UAV Management
- Add, delete, update, and list UAVs with features such as Brand, Model, Weight, Category, and more.

### Rental Management
- Users can rent UAVs, specifying date and time ranges for rental.
- Members can view their UAV rental records.

## Technologies Used

- Django: A high-level Python web framework used for the backend development.
- Django REST framework: An extension of Django for building RESTful APIs.
- HTML, CSS, and JavaScript: Used for the frontend user interface.
- PostgreSQL: A powerful open-source relational database for storing data.
- Docker: Used for containerization and simplifying deployment.
- pytest: A testing framework for writing and running unit tests.

## Usage

- Log in as an admin user to manage UAVs and user accounts.
- Log in as a regular user to browse and manage available UAVs, make reservations, and view rental history.

## API Endpoints

The application provides API endpoints for programmatic access to UAV data. Examples include:

- GET /api/uavlists/: Get a list of all available UAVs.
- POST /api/uavlists/: Create a new UAV entry.
- GET /api/uavlists/<uav_id>/: Get details of a specific UAV.
- PUT /api/uavlists/<uav_id>/update_uav: Update details of a specific UAV.
- DELETE /api/uavlists/<uav_id>/delete_uav: Delete a specific UAV.

- `GET /api/users/`: Get a list of all registered users.
- `POST /api/users/`: Create a new user account.
- `GET /api/users/<user_id>/`: Get details of a specific user.
- `PUT /api/users/<user_id>/`: Update details of a specific user.
- `DELETE /api/users/<user_id>/`: Delete a specific user account.


## Testing

To run tests for the application, you can use the following command:
- pytest tests/test_models.py
- pytest tests/test_views.py

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

<img width="1552" alt="Screen Shot 2023-09-25 at 12 01 51 PM" src="https://github.com/OmarSabouni96/UAVRental/assets/70510356/2ce4c639-0c28-4118-8d53-3704db69e93b">

