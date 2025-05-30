import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PlayerStatus = ({ playerId }) => {
  const [status, setStatus] = useState({ health: 0, hunger: 0, thirst: 0, radiation: 0 });

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/players/${playerId}`);
        setStatus(response.data);
      } catch (error) {
        console.error('Error fetching player status:', error);
      }
    };
    fetchStatus();
  }, [playerId]);

  const handleEat = async () => {
    try {
      const response = await axios.post('http://localhost:8000/player/eat', { player_id: playerId, amount: 20 });
      setStatus((prev) => ({ ...prev, hunger: response.data.hunger }));
    } catch (error) {
      console.error('Error eating:', error);
    }
  };

  const handleDrink = async () => {
    try {
      const response = await axios.post('http://localhost:8000/player/drink', { player_id: playerId, amount: 30 });
      setStatus((prev) => ({ ...prev, thirst: response.data.thirst }));
    } catch (error) {
      console.error('Error drinking:', error);
    }
  };

  return (
    <div>
      <h2>Player Status</h2>
      <p>Health: {status.health}%</p>
      <p>Hunger: {status.hunger}%</p>
      <p>Thirst: {status.thirst}%</p>
      <p>Radiation: {status.radiation}%</p>
      <button onClick={handleEat}>Eat</button>
      <button onClick={handleDrink}>Drink</button>
    </div>
  );
};

export default PlayerStatus;