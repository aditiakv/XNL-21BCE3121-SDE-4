import unittest
from sharding_logic import insert_transaction, get_transactions

class TestShardingLogic(unittest.TestCase):
    def test_insert_and_query_transaction(self):
        # Insert a transaction
        insert_transaction(1, 1, 100.00, 'buy', '2023-01-15')

        # Query the transaction
        transactions = get_transactions(1)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][2], 100.00)  # Check amount

if __name__ == '__main__':
    unittest.main()