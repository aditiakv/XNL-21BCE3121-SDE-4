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
1. Clone the repository.
2. Run the SQL scripts to create the database schema.
3. Use the Python script to generate synthetic data.
4. Run queries to test the system.

## ER Diagram
