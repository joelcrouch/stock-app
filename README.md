# Stock Trading App

A simple Flask application that allows users to log in with Google OAuth, view their profile information, and start building stock-related functionality.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Setup the Virtual Environment](#setup-the-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run the App](#run-the-app)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a basic Flask web application that integrates Google OAuth for authentication. Users can log in with their Google account and access their profile information. The app can be extended to add more features like stock tracking, purchase/sale functionality, and historical data analysis.

## Features

- **Google OAuth Integration**: Users can log in using their Google account.
- **Database Integration**: Stores user data (name, email, profile picture) in a SQLite database.
- **Home Page**: Displays user information after successful login.
- **User Authentication**: Prevents unauthorized access.

## Technologies

This project is built using the following technologies:

- **Flask**: A Python web framework.
- **Flask-Dance**: OAuth integration for Flask (used for Google OAuth).
- **SQLAlchemy**: ORM for database management.
- **SQLite**: Lightweight database used for development.
- **Python**: Programming language used to build the app.

## Setup and Installation

Follow the steps below to set up and run the app on your local machine.

### Prerequisites

- **Python 3.x**: Ensure that you have Python 3.x installed.
- **Google Developer Account**: You need to set up OAuth credentials in the Google Developer Console to get your `client_id` and `client_secret`.

### Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/stock-app.git
cd stock-app
```

### Setup the Virtual Environment

```bash
python3 -m venv stock-trading-env
source stock-trading-env/bin/activate  # On Windows, use `.\stock-trading-env\Scripts\activate`

```

### Install Dependecies

```bash
python app.py
```

### Run the App

```
python3 app.py
```

## Contributing

We welcome contributions to this project! If you would like to contribute, please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes and commit them (git commit -am 'Add new feature').
    Push to your branch (git push origin feature-branch).
    Create a pull request to the main branch.

## LICENSE TODO

This project is licensed under the MIT License - see the LICENSE file for details.
