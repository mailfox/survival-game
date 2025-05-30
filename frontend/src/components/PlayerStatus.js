// /home/mailfox/survival-game/frontend/src/PlayerStatus.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { gsap } from 'gsap';

// Базовый URL для бэкенда
const API_URL = 'http://127.0.0.1:8000';

const PlayerStatus = ({ playerId }) => {
  const [player, setPlayer] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPlayer = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`${API_URL}/player/${playerId}`);
        console.log('Player response:', response.data); // Отладка
        setPlayer(response.data);
      } catch (error) {
        console.error('Error fetching player:', error.response || error.message); // Отладка
        setError('Failed to load player data');
      } finally {
        setLoading(false);
      }
    };

    if (playerId) {
      fetchPlayer();
    }
  }, [playerId]);

  const handleRadiate = async () => {
    try {
      const response = await axios.post(`${API_URL}/player/${playerId}/radiate`, { amount: 10 });
      console.log('Radiate response:', response.data); // Отладка
      setPlayer(response.data);
      setError(null);

      gsap.to('.radiation-level', {
        duration: 1,
        backgroundColor: '#ff0000',
        ease: 'power2.out',
        onComplete: () => {
          gsap.to('.radiation-level', { backgroundColor: '#ffffff', duration: 0.5 });
        },
      });

      if (response.data.health === 0) {
        gsap.to('.player-status', {
          opacity: 0,
          duration: 1,
          onComplete: () => alert('Player died from radiation!'),
        });
      }
    } catch (error) {
      const errorMessage = error.response?.data?.detail || 'Error applying radiation';
      console.error('Error applying radiation:', error.response || error.message); // Отладка
      setError(errorMessage);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div className="text-red-500">Error: {error}</div>;

  return (
    <div className="player-status p-4 bg-gray-800 text-white rounded-lg">
      <h2 className="text-xl">Player Status</h2>
      <p>Health: {player.health}</p>
      <p>Hunger: {player.hunger}</p>
      <p>Thirst: {player.thirst}</p>
      <p className="radiation-level">Radiation: {player.radiation}</p>
      {error && <p className="text-red-500">{error}</p>}
      <button
        onClick={handleRadiate}
        className="mt-2 px-4 py-2 bg-red-600 hover:bg-red-700 rounded"
        disabled={player.health === 0}
      >
        Radiate
      </button>
    </div>
  );
};

export default PlayerStatus;