// /home/mailfox/survival-game/frontend/src/Inventory.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { DndContext, closestCenter } from '@dnd-kit/core';
import { SortableContext, useSortable, arrayMove } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import { gsap } from 'gsap';

const API_URL = 'http://127.0.0.1:8000';

const SortableItem = ({ id, item, onRemove }) => {
  const { attributes, listeners, setNodeRef, transform, transition } = useSortable({ id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
  };

  const handleRemove = () => {
    gsap.to(`#item-${id}`, {
      scale: 0.8,
      opacity: 0,
      duration: 0.3,
      onComplete: () => onRemove(item.id),
    });
  };

  return (
    <div
      id={`item-${id}`}
      ref={setNodeRef}
      style={style}
      {...attributes}
      {...listeners}
      className="flex items-center p-2 bg-gray-600 mb-2 rounded hover:bg-gray-500"
    >
      <img
        src={item.icon_url || '/images/default.png'}
        alt={item.name}
        className="w-8 h-8 mr-2"
        onError={(e) => {
          console.error(`Failed to load image: ${item.icon_url}`);
          e.target.src = '/images/default.png';
        }}
      />
      <span>{item.name} ({item.type})</span>
      <button
        onClick={handleRemove}
        className="ml-auto px-2 py-1 bg-red-600 hover:bg-red-700 rounded"
      >
        Remove
      </button>
    </div>
  );
};

const Inventory = ({ playerId }) => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchInventory = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`${API_URL}/inventory/${playerId}`);
        console.log('Inventory response:', response.data);
        setItems(response.data.items || []);
      } catch (error) {
        console.error('Error fetching inventory:', error.response || error.message);
        setError('Failed to load inventory');
      } finally {
        setLoading(false);
      }
    };

    if (playerId) {
      fetchInventory();
    }
  }, [playerId]);

  const handleDragEnd = (event) => {
    const { active, over } = event;
    if (active.id !== over.id) {
      setItems((items) => {
        const oldIndex = items.findIndex((item) => item.id === active.id);
        const newIndex = items.findIndex((item) => item.id === over.id);
        return arrayMove(items, oldIndex, newIndex);
      });
    }
  };

  const handleRemoveItem = async (itemId) => {
    try {
      await axios.delete(`${API_URL}/inventory/${itemId}`);
      setItems(items.filter((item) => item.id !== itemId));
    } catch (error) {
      console.error('Error removing item:', error.response || error.message);
    }
  };

  if (loading) return <p>Loading inventory...</p>;
  if (error) return <p>{error}</p>;

  return (
    <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
      <SortableContext items={items.map((item) => item.id)}>
        <div className="inventory p-4 bg-gray-700 text-white rounded-lg">
          <h2 className="text-xl mb-2">Inventory</h2>
          {items.length === 0 ? (
            <p>Inventory is empty</p>
          ) : (
            items.map((item) => (
              <SortableItem
                key={item.id}
                id={item.id}
                item={item}
                onRemove={handleRemoveItem}
              />
            ))
          )}
        </div>
      </SortableContext>
    </DndContext>
  );
};

export default Inventory;