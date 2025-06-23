import os
import django

    # Set up Django environment
    # Replace 'myproject.settings' with your actual project's settings file if different
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

    # Define the staff user's attributes
username = 'hiiromatsuoka'
password = 'Bran8222'
email = 'hiiro.bran.gin378@icloud.com'

print(f"Attempting to create staff user: {username}")

try:
        # Try to get the user if they already exist
        user = User.objects.get(username=username)
        print(f"User '{username}' already exists. Updating attributes if necessary.")
        # Update attributes if needed (e.g., if email or password was wrong)
        if user.email != email:
            user.email = email
        user.set_password(password) # Set password (it hashes it automatically)
        user.is_staff = True
        user.save()
        print(f"User '{username}' updated successfully.")

except ObjectDoesNotExist:
        # If the user does not exist, create a new one
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_staff = True  # Make this user a staff user
            user.save()
            print(f"Staff user '{username}' created successfully!")
        except Exception as e:
            print(f"Error creating user '{username}': {e}")
except Exception as e:
        print(f"An unexpected error occurred: {e}")
# This script creates a staff user in a Django project.
# It checks if the user already exists and updates their attributes if necessary.
# If the user does not exist, it creates a new staff user with the specified username,
# password, and email. It handles exceptions for user creation and updates.
# Make sure to run this script in the Django environment where your project is set up.
# You can run this script using the Django shell or as a standalone script after setting up Django.
