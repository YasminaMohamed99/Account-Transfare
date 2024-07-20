# Django Account Transfer Project

## Overview

This Django project implements a basic account management system with functionality for transferring funds between accounts, importing accounts from files, and viewing transaction history. It includes pagination for listing accounts and use the messaging system to display success and error messages to users.

## Features

- **List Accounts**: List all accounts and appear information for each account.
- **File Import**: Import accounts from CSV, TSV, XLS, and XLSX files.
- **Fund Transfer**: Transfer funds between accounts with transaction recording.
- **Transaction History**: View transaction history for each transaction for specific account.
- **Pagination**: Paginate the list of accounts and transaction history for better usability.
- **Testing**: Apply unit test on urls, forms, models, views.
- **Docker**: Build an image to run this web app on docker.

## Technologies Used

- **Django**: Web framework for building the application.
- **Sqlite**: Database for storing account and transaction data.
- **Docker**: Containerization for deployment.
- **Python 3.12**: Programming language.

## Getting Started

### Prerequisites

- Python 3.12
- Docker (for containerized deployment)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YasminaMohamed99/Account-Transfare.git
   cd Account-Transfer
   ```
2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv env 
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations**

   ```bash
   python manage.py migrate
   ```
5. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```
   
6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```
7. **Docker Deployment**

   ```bash
   docker build -t account-transfer .
   docker run -p 8000:8000 account-transfer
   ```
8. **Testing**
   * Run tests to ensure everything is working correctly:
   ```bash
   python manage.py test
   ```


   