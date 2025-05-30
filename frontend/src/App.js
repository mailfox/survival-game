import React, { useEffect } from 'react';
import Phaser from 'phaser';
import MapScene from './scenes/MapScene';
import Inventory from './components/Inventory';
import PlayerStatus from './components/PlayerStatus';

const App = () => {
  useEffect(() => {
    const config = {
      type: Phaser.AUTO,
      width: 800,
      height: 600,
      parent: 'game-container',
      scene: [MapScene],
    };
    new Phaser.Game(config);
  }, []);

  return (
    <div id="game-container">
      <h1>Zemlya Mertvykh: Survival</h1>
      <PlayerStatus playerId={1} />
      <Inventory playerId={1} />
    </div>
  );
};

export default App;