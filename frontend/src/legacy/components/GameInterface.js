import React, { useState, useEffect } from 'react';
import axios from 'axios';

function GameInterface() {
  const [player, setPlayer] = useState(null);
  const [items, setItems] = useState([]);

  // 1. Загрузка данных игрока
  const fetchPlayer = async (id) => {
    try {
      const response = await axios.get(`http://localhost:8000/player/${id}`);
      setPlayer(response.data);
    } catch (error) {
      console.error('Ошибка загрузки игрока:', error);
    }
  };

  // 2. Создание предмета
  const createItem = async () => {
    try {
      const newItem = { name: "Меч", price: 150 };
      await axios.post('http://localhost:8000/items/', newItem);
      alert('Предмет создан!');
    } catch (error) {
      console.error('Ошибка создания предмета:', error);
    }
  };

  // 3. Автозагрузка при монтировании
  useEffect(() => {
    fetchPlayer(1);
  }, []);

  return (
    <div className="game-ui">
      {player && (
        <div className="player-card">
          <h2>{player.name}</h2>
          <p>Здоровье: {player.health}</p>
          <button onClick={() => fetchPlayer(1)}>
            Обновить данные
          </button>
        </div>
      )}

      <div className="inventory">
        <button onClick={createItem}>
          Создать меч
        </button>
      </div>
    </div>
  );
}

export default GameInterface;
