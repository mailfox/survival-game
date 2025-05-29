import React, { useState, useEffect } from 'react';
import { fetchPlayer, updateHealth } from '../api/client';

export default function Player({ id }) {
  const [player, setPlayer] = useState(null);

  useEffect(() => {
    fetchPlayer(id).then(res => setPlayer(res.data));
  }, [id]);

  const handleHeal = () => {
    updateHealth(id, 100).then(() => {
      fetchPlayer(id).then(res => setPlayer(res.data));
    });
  };

  return (
    <div className="player-card">
      {player && (
        <>
          <h2>{player.name}</h2>
          <p>Health: {player.health}</p>
          <button onClick={handleHeal}>Heal</button>
        </>
      )}
    </div>
  );
}
