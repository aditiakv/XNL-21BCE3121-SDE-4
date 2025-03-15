# Fintech Platform Database Design

## Schema Overview
This database schema is designed for a high-performance, scalable fintech platform. It supports real-time financial transactions, user portfolios, and market analytics.

### Tables
1. **Users**: Stores user information.
2. **Assets**: Stores financial assets (e.g., Bitcoin, Ethereum).
3. **Portfolios**: Tracks user investment portfolios.
4. **Transactions**: Records financial transactions (e.g., buys, sells).
5. **Orders**: Tracks buy/sell orders placed by users.

### Relationships
- A user can have multiple transactions (`Users` → `Transactions`).
- A user can have multiple portfolio entries (`Users` → `Portfolios`).
- Transactions and portfolios reference assets (`Transactions` → `Assets`, `Portfolios` → `Assets`).

### Indexes
- Indexes are added on frequently queried columns (e.g., `user_id`, `timestamp`).

### Synthetic Data
- Synthetic data was generated using Python and inserted into the database for testing.

### Optimization
- Sharding and partitioning strategies were implemented for scalability.
- Query performance was optimized using `EXPLAIN ANALYZE`.

## How to Run

### Backend
1. Clone the repository.
2. Navigate to the backend directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - The database dump is located in the `fintech-platform.sql` directory. Use it to create the database schema.
5. Run the backend:
   ```bash
   python3 -m fintech_backend.run
   ```

### Frontend
1. Navigate to the frontend directory.
2. Install the required dependencies:
   ```bash
   npm install
   ```
3. Run the frontend:
   ```bash
   npm start
   ```
4. **Note**: The frontend is not currently hooked to the backend. Connecting the frontend to the backend is a TODO and could be done if more time is available.

### Postman Collection
- The Postman collection is available in `postman_collection.json` in the root directory. It can be imported to test individual API calls as required.

### Sharding and Partitioning Logic
- The sharding and partitioning logic is contained in `sharding_logic.py` in the root directory.