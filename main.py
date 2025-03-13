import click
from models import Account, Password, session

# Helper function to find an account by name
def get_account(name):
    return session.query(Account).filter_by(name=name).first()

# Helper function to add a new password
def add_password(account_name, password):
    account = get_account(account_name)
    if account:
        new_password = Password(account_name=account_name, password=password)
        session.add(new_password)
        session.commit()
        click.echo(f"Password added for account {account_name}.")
    else:
        click.echo(f"Account {account_name} does not exist.")

# CLI Command to add account
@click.command()
@click.argument('account_name')
def add_account(account_name):
    """Create a new account."""
    if get_account(account_name):
        click.echo(f"Account {account_name} already exists.")
    else:
        new_account = Account(name=account_name)
        session.add(new_account)
        session.commit()
        click.echo(f"Account {account_name} created.")

# CLI Command to add a password
@click.command()
@click.argument('account_name')
@click.argument('password')
def add_password_cli(account_name, password):
    """Add a password to an account."""
    add_password(account_name, password)

# CLI Command to list all passwords
@click.command()
def list_passwords():
    """View all passwords."""
    passwords = session.query(Password).all()
    for password in passwords:
        click.echo(f"Account: {password.account_name}, Password: {password.password}")

# CLI Command to remove a password
@click.command()
@click.argument('account_name')
def remove_password(account_name):
    """Remove a password for an account."""
    password = session.query(Password).filter_by(account_name=account_name).first()
    if password:
        session.delete(password)
        session.commit()
        click.echo(f"Password removed for account {account_name}.")
    else:
        click.echo(f"No password found for account {account_name}.")

# CLI Command to retrieve password by account name
@click.command()
@click.argument('account_name')
def get_password(account_name):
    """Retrieve a password for a given account."""
    password = session.query(Password).filter_by(account_name=account_name).first()
    if password:
        click.echo(f"Password for {account_name}: {password.password}")
    else:
        click.echo(f"No password found for account {account_name}.")

# Main CLI entry point
@click.group()
def cli():
    """Password Manager CLI"""
    pass

# Add commands to the CLI group
cli.add_command(add_account)
cli.add_command(add_password_cli)
cli.add_command(list_passwords)
cli.add_command(remove_password)
cli.add_command(get_password)

if __name__ == '__main__':
    cli()
