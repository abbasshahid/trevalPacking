Project Title
A brief description of what this project does and who it's for.

Installation
Follow these steps to set up the project environment.

Prerequisites
Python (preferably Python 3)
pip (Python package manager)
Setup
Install Python:

Download and install Python (ideally Python 3) from python.org.
During installation, ensure that Python is added to your system's PATH.
Install pip:

Python 3 comes with pip pre-installed. If for any reason pip is not installed, follow these instructions to install it manually.
Install Django and Dependencies:

Open your command line interface (CLI) and navigate to your project directory.
Run the following commands to uninstall any existing versions of django-crispy-forms and install the latest version:

pip uninstall django-crispy-forms
pip install django-crispy-forms
Start the Django Server:

Within your project directory, execute the following command:
python3 manage.py runserver
If you encounter any errors, it likely means some dependencies are missing. Install any missing dependencies as prompted and repeat the above steps.
Usage
Creating an Account
Register:
Navigate to the registration page and create an account. You may also create additional accounts to simulate different users (e.g., your friends).
Using the Application
Login:

After registering, use your credentials to log in.
Viewing Trips:

Upon logging in, you'll land on the Trips page, which lists all the trips.
Adding a Trip:

Click on 'Add Trip' in the header to create a new trip. During this process, you can select participants for your trip.
Adding Items to a Trip:

Use the 'Add Item' option to add items to your trip's packing list.
Viewing Trip Details:

On the Trips page, click on a trip's link to view its details, including the packing list and assigned items.
Note
This application is designed for managing trip packing lists. It allows users to create trips, add items to trips, and assign those items to trip participants.