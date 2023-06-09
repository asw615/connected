import os
from app import create_app

# Set the working directory to the root of the Flask app
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = create_app()

app.secret_key = "45d9e09272ba0094e767d11bc3b06f66"

# Rename 'app' to 'application' to match the gunicorn command
application = app

if __name__ == "__main__":
    application.run(debug=True, port=8000)
