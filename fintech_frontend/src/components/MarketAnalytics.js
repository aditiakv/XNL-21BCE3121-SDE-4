import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { marketData } from '../data/market';

const MarketAnalytics = () => {
  return (
    <div>
      <h2>Market Analytics</h2>
      <LineChart width={600} height={300} data={marketData}>
        <XAxis dataKey="name" />
        <YAxis />
        <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
        <Line type="monotone" dataKey="price" stroke="#8884d8" />
        <Tooltip />
        <Legend />
      </LineChart>
    </div>
  );
};

export default MarketAnalytics;