# Password Manager CLI

This is a simple command-line password manager built using Python and SQLAlchemy. It allows users to create accounts, store passwords, view stored passwords, remove passwords, and manage account credentials in a secure manner.

## Features

- **Create Account**: Add a new account to the password manager.
- **Add Password**: Store a password for a specific account.
- **List Passwords**: View all stored passwords (for demonstration purposes, ideally, you'd secure this).
- **Remove Password**: Delete a stored password for a specific account.
- **Retrieve Password**: Retrieve a password for a specific account.

## Requirements

- Python 3.x
- SQLAlchemy (for database management)
- Click (for CLI commands)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/password-manager-cli.git
   cd password-manager-cli
   ```

2. **Create a virtual environment (optional but recommended):**

```bash
   Copy
   python3 -m venv venv
```   

3. **Install dependencies**

```bash
    Copy
    pip install -r requirements.txt
    Ensure you have the necessary dependencies installed for this project:
```

```text
    Copy
    click==8.0.3
    sqlalchemy==1.4.23
```
## Usage

The following commands are available:

1. **Create a New Account**
- To create a new account in the password manager:

```bash
    Copy
    python password_manager.py add-account <account_name>
    Example:
```

```bash
    Copy
    python password_manager.py add-account example_account
```
2. **Add a Password to an Account**
- To add a password to an existing account:

```bash
    Copy
    python password_manager.py add-password-cli <account_name> <password>
```

```bash
    Copy
    python password_manager.py add-password-cli example_account MySuperSecretPassword
```
3. **List All Passwords**
- To view all passwords stored in the password manager:

```bash
    Copy
    python password_manager.py list-passwords
```
4. **Remove a Password**
- To remove a stored password for a specific account:

```bash
    Copy
    python password_manager.py remove-password <account_name>
```

5. **Retrieve a Password**
- To retrieve the password for a specific account:

```bash
    Copy
    python password_manager.py get-password <account_name>
```
## Code Structure

- requirements.txt      # Contains your project dependencies
- README.md             # Project description and instructions
- main.py               # Main entry point for the CLI application
- model.py              # Contains your ORM models and database-related code

## License 
Distributed under MIT License

## Contact Information

Emmanuel Njeru - [Gmail](mailto:manungek@gmail.com)