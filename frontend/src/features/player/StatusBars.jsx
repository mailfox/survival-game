import React from 'react';
import './StatusBars.css';

export const StatusBars = ({ stats }) => (
  <div className="status-bars">
    <div className="bar health" style={{ width: `${stats.health}%` }}></div>
    <div className="bar hunger" style={{ width: `${stats.hunger}%` }}></div>
    <div className="bar thirst" style={{ width: `${stats.thirst}%` }}></div>
    {stats.radiation > 0 && (
      <div className="bar radiation" style={{ width: `${stats.radiation}%` }}></div>
    )}
  </div>
);