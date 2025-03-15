from faker import Faker
import psycopg2

# Initialize Faker
fake = Faker()

# Database connection parameters
db_params = {
    "dbname": "fintech_platform",
    "user": "postgres",
    "password": "Aditi",  # Replace with your PostgreSQL password
    "host": "localhost",
    "port": "5433"
}

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    print("Connected to the database!")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Insert 1000 fake users
try:
    for i in range(1000):
        name = fake.name()
        email = f"{fake.user_name()}{i}@example.com"  # Ensure unique email
        password_hash = fake.sha256()
        cur.execute(
            "INSERT INTO Users (name, email, password_hash) VALUES (%s, %s, %s)",
            (name, email, password_hash)
        )
        if i % 100 == 0:  # Print progress every 100 rows
            print(f"Inserted {i} users so far...")
    conn.commit()
    print("Inserted 1000 users into the Users table!")
except Exception as e:
    print(f"Error inserting data: {e}")
finally:
    cur.close()
    conn.close()
    print("Database connection closed.")