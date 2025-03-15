import React from 'react';
import { transactionData } from '../data/transactions';

const TransactionHistory = () => {
  return (
    <div>
      <h2>Transaction History</h2>
      <table>
        <thead>
          <tr>
            <th>Asset</th>
            <th>Type</th>
            <th>Amount</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {transactionData.map(item => (
            <tr key={item.id}>
              <td>{item.asset}</td>
              <td>{item.type}</td>
              <td>{item.amount}</td>
              <td>{item.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TransactionHistory;