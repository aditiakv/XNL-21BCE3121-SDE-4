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

# Populate assets table
try:
    for i in range(1, 11):  # Insert 10 assets with asset_id from 1 to 10
        name = f"Asset_{i}"  # Asset name
        symbol = f"ASSET{i}"  # Unique symbol for the asset
        price = fake.pydecimal(left_digits=5, right_digits=2, positive=True)  # Random price
        market_cap = fake.pydecimal(left_digits=10, right_digits=2, positive=True)  # Random market cap
        cur.execute(
            "INSERT INTO assets (name, symbol, price, market_cap) VALUES (%s, %s, %s, %s)",
            (name, symbol, price, market_cap)
        )
    conn.commit()
    print("Inserted 10 assets into the assets table!")
except Exception as e:
    print(f"Error inserting assets: {e}")
    conn.rollback()

# Insert 1000 fake users
try:
    for i in range(1, 1001):  # Ensure user_id starts from 1 and goes up to 1000
        cur.execute("SELECT 1 FROM users WHERE user_id = %s", (i,))
        if not cur.fetchone():  # Only insert if user_id does not exist
            name = fake.name()
            email = f"{fake.user_name()}{i}@example.com"  # Ensure unique email
            password_hash = fake.sha256()
            cur.execute(
                "INSERT INTO Users (user_id, name, email, password_hash) VALUES (%s, %s, %s, %s)",
                (i, name, email, password_hash)  # Explicitly set user_id
            )
            if i % 100 == 0:  # Print progress every 100 rows
                print(f"Inserted {i} users so far...")
    conn.commit()
    print("Inserted 1000 users into the Users table!")
except Exception as e:
    print(f"Error inserting users: {e}")
    conn.rollback()  # Rollback in case of error

# Verify the number of users in the database
cur.execute("SELECT COUNT(*) FROM users;")
user_count = cur.fetchone()[0]
print(f"Total users in the database: {user_count}")

# Insert 1000 fake transactions
try:
    for i in range(1, 1001):  # Use user_id from 1 to 1000
        user_id = i
        asset_id = fake.random_int(min=1, max=10)   # Random asset_id between 1 and 10
        amount = fake.pydecimal(left_digits=5, right_digits=2, positive=True)  # Random amount
        type = fake.random_element(elements=('buy', 'sell'))  # Random type (buy/sell)
        timestamp = fake.date_time_this_year()  # Random timestamp within the current year
        print(f"Inserting transaction: user_id={user_id}, asset_id={asset_id}, amount={amount}, type={type}, timestamp={timestamp}")
        
        # Check if the user exists before inserting the transaction
        cur.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
        if cur.fetchone():
            cur.execute(
                "INSERT INTO Transactions (user_id, asset_id, amount, type, timestamp) VALUES (%s, %s, %s, %s, %s)",
                (user_id, asset_id, amount, type, timestamp)
            )
        else:
            print(f"User with user_id={user_id} does not exist in the users table. Skipping transaction.")
        
        if i % 100 == 0:  # Print progress every 100 rows
            print(f"Inserted {i} transactions so far...")
    conn.commit()
    print("Inserted 1000 transactions into the Transactions table!")
except Exception as e:
    print(f"Error inserting transactions: {e}")
    conn.rollback()  # Rollback in case of error
finally:
    cur.close()
    conn.close()
    print("Database connection closed.")