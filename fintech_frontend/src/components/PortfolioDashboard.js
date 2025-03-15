import React from 'react';
import { portfolioData } from '../data/portfolio';

const PortfolioDashboard = () => {
  return (
    <div>
      <h2>Portfolio Dashboard</h2>
      <table>
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
    </div>
  );
};

export default PortfolioDashboard;