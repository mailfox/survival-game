import React, { useEffect, useState } from 'react';
import { getInventory } from '../api/client';

export default function Inventory({ playerId }) {
  const [items, setItems] = useState([]);

  useEffect(() => {
    getInventory(playerId).then(res => setItems(res.data));
  }, [playerId]);

  return (
    <div className="inventory">
      {items.map(item => (
        <div key={item.id} className="item">
          {item.name} (x{item.quantity})
        </div>
      ))}
    </div>
  );
}
