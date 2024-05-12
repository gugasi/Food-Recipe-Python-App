# Food-Recipe-Python-App

# Food Recipe Project

## Introduction

This project is a food recipe website developed using Python, Django, HTML, and SQLite3. It allows users to browse, search, and share their favorite food recipes.

## Technologies Used

- **Python**: The backend of the website is built using Python, a powerful and flexible programming language.
- **Django**: Django, a high-level Python web framework, is used for developing the application. It encourages rapid development and clean, pragmatic design.
- **HTML**: HTML is used to structure the content on the web page.
- **SQLite3**: SQLite3 is used as the database for this project. It is a C library that provides a lightweight disk-based database.

## Setup and Installation

1. **Clone the Repository**: First, clone this repository to your local machine using `git clone <repository_link>`.
2. **Install Dependencies**: Install the necessary dependencies by running `pip install -r requirements.txt`.
3. **Set Up the Database**: Set up the SQLite3 database by running `python manage.py makemigrations` and `python manage.py migrate`.
4. **Run the Server**: Start the Django server using `python manage.py runserver`.

## Features

- **User Registration/Login**: Users can create accounts using email, name, and password. The same email can NOT be used.
- **Browse Recipes**: Users can browse through a variety of food recipes.
- **Search Recipes**: Users can search for recipes using the search functionality.
- **Share Recipes**: Users can share their own recipes on the website.

## Admin Panel & SQL
There is currently only one admin account added through the script code and when you user heads to admin page, they are asked to login using admin credentials to enter admin panel and have access to users,sql tables, recipes, and so on.
- **Users Edit Feature**: Admin has power to edit/remove users recipes as well as delete their profiles if the name is inappropriate or remove their name as a feature to give them a chance to change their name to something more appropriate.


## Contributing

Contributions are welcome! Please read the contributing guidelines first.

## License

This project is licensed under the terms of the MIT license by Guram Sikharulidze. See the LICENSE file for details.
