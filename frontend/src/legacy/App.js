import Player from './components/Player';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Survival Game</h1>
      <Player id={1} />
    </div>
  );
}

import Inventory from './components/Inventory';

function App() {
  return (
    <div className="App">
      <Player id={1} />
      <Inventory playerId={1} />
    </div>
  );
}
export default App;
