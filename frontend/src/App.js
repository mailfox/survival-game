// /home/mailfox/survival-game/frontend/src/App.js
import React, { useState } from 'react';
import PlayerStatus from './components/PlayerStatus';
import Inventory from './components/Inventory';
import MapScene from './scenes/MapScene';

function App() {
  const playerId = 1; // Тестовый ID игрока
  const [refreshKey, setRefreshKey] = useState(0); // Для принудительного обновления компонентов

  const handleExplore = (exploreData) => {
    console.log('Explore data received in App:', exploreData);
    // Принудительно обновляем PlayerStatus и Inventory, чтобы они сделали новые запросы
    setRefreshKey((prev) => prev + 1);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <h1>Zemlya Mertvykh: Survival</h1>
      <div style={{ width: '800px', height: '600px' }}>
        <MapScene onExplore={handleExplore} />
      </div>
      <div style={{ display: 'flex', gap: '20px', marginTop: '20px' }}>
        <PlayerStatus key={`player-${refreshKey}`} playerId={playerId} />
        <Inventory key={`inventory-${refreshKey}`} playerId={playerId} />
      </div>
    </div>
  );
}

export default App;