# Lab 10 - Web Site Hosting
# Flask Application with PostgreSQL Database on Render

# Import Flask framework
from flask import Flask

# Import os to access environment variables
import os

# Import psycopg2 to connect to PostgreSQL database
import psycopg2

# Create Flask app
app = Flask(__name__)

# Database URL (Internal URL from Render)
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://your_local_fallback_if_needed")


# Home Route
@app.route("/")
def hello_world():
    return "<h1>Hello World from Erick Samayoa in 3308</h1>"


# db_test route to test the connection to PostgreSQL database
@app.route("/db_test")
def db_test():

    conn = psycopg2.connect(DATABASE_URL)

    conn.close()

    return "Database connection successful"


# db_create
@app.route("/db_create")
def db_create():

    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')

    conn.commit()
    conn.close()

    return "Basketball Table Created"


# db_insert
@app.route("/db_insert")
def db_insert():

    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()

    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')

    conn.commit()
    conn.close()

    return "Basketball Table Populated"


# db_select
@app.route("/db_select")
def db_select():

    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()

    cur.execute("SELECT * FROM Basketball;")

    records = cur.fetchall()

    response = "<table border='1'>"
    response += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"

    for row in records:
        response += "<tr>"
        for item in row:
            response += "<td>" + str(item) + "</td>"
        response += "</tr>"

    response += "</table>"

    conn.close()

    return response


# db_drop
@app.route("/db_drop")
def db_drop():

    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()

    cur.execute("DROP TABLE Basketball;")

    conn.commit()
    conn.close()

    return "Basketball Table Dropped"


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
