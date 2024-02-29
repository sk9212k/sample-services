import os
import requests

# Define your authentication credentials using environment variables
username = os.getenv('AUTH_USERNAME')  # Replace 'AUTH_USERNAME' with the actual name of your environment variable
password = os.getenv('AUTH_PASSWORD')  # Replace 'AUTH_PASSWORD' with the actual name of your environment variable

# Make sure both username and password are not None before proceeding
if username is None or password is None:
    raise ValueError("Missing environment variables for authentication")

les = {
    'raw.asset1': ('zap-alerts.txt', open('zap-alerts.txt', 'rb')),  # Adjust file name and path accordingly
    'raw.asset2': ('zap-alerts-world.txt', open('zap-alerts-world.txt', 'rb')),  # Adjust file name and path accordingly
}
# Define additional data
data = {
    'raw.directory': directory_path,  # Adjust directory path if necessary
    'raw.asset1.filename': 'zap-alerts.txt',  # Adjust file name accordingly
    'raw.asset2.filename': 'zap-alerts-world.txt',  # Adjust file name accordingly
}
# Make the POST request with the authentication credentials from environment variables
response = requests.post('http://localhost:8081/service/rest/v1/components?repository=zap-reports', params=params, files=files, data=data, auth=(username, password))

# Check the response status code
if response.status_code == 204:
    print("Files uploaded successfully!")
else:
    print(f"Failed to upload files. Status code: {response.status_code}")

