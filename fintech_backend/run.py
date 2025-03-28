# run.py
from flask import Flask
from fintech_backend.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)