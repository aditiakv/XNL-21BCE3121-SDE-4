// src/App.js
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Portfolio from './pages/Portfolio';
import Transactions from './pages/Transactions';
import Market from './pages/Market';
import Login from './components/Login.tsx';
import Navbar from './components/Navbar';
import Home from './pages/Home'; // Import the Home component

function App() {
  return (
    <Router>
      <Navbar />
      <div className="main-content">
        <Routes>
          <Route path="/portfolio" element={<Portfolio />} />
          <Route path="/transactions" element={<Transactions />} />
          <Route path="/market" element={<Market />} />
          <Route path="/login" element={<Login />} />
          <Route path="/" element={<Home />} /> {/* Use Home component for the default route */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;