import React from 'react';
import { portfolioData } from '../data/portfolio';
import { transactionData } from '../data/transactions';
// Assuming you have market data, import it similarly
// import { marketData } from '../data/market';

const HomeDashboard = () => {
  return (
    <div className="container mt-5">
      <h2 className="mb-4">Home Dashboard</h2>

      <section className="mb-5">
        <h3>Portfolio</h3>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Asset</th>
              <th>Value</th>
              <th>Performance</th>
            </tr>
          </thead>
          <tbody>
            {portfolioData.map(item => (
              <tr key={item.id}>
                <td>{item.asset}</td>
                <td>${item.value}</td>
                <td>{item.performance}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      <section className="mb-5">
        <h3>Transactions</h3>
        <table className="table table-striped">
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
      </section>

      {/* Add a similar section for market data if available */}
      {/* <section className="mb-5">
        <h3>Market</h3>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Market</th>
              <th>Price</th>
              <th>Change</th>
            </tr>
          </thead>
          <tbody>
            {marketData.map(item => (
              <tr key={item.id}>
                <td>{item.market}</td>
                <td>${item.price}</td>
                <td>{item.change}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section> */}
    </div>
  );
};

export default HomeDashboard; 