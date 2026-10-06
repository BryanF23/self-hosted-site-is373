import os
import psycopg2
from flask import Flask

app = Flask(__name__)


def check_database():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        connection.close()
        return True
    except Exception:
        return False


@app.route("/")
def home():
    db_status = "Connected" if check_database() else "Not Connected"

    return f"""
    <html>
        <head>
            <title>Bryan's Self-Hosted Site</title>
        </head>
        <body>
            <h1>Bryan's Self-Hosted Site</h1>
            <p>This website is running on a DigitalOcean Droplet.</p>
            <p>Powered by Python, Flask, Docker, and Traefik.</p>
            <p>PostgreSQL Database: <strong>{db_status}</strong></p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
