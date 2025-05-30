import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { DndContext, closestCenter } from '@dnd-kit/core';
import { SortableContext, useSortable, rectSortingStrategy, arrayMove } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';

const SortableItem = ({ id, name, weight, size, onDelete }) => {
  const { attributes, listeners, setNodeRef, transform, transition } = useSortable({ id });
  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    width: `${size[0] * 50}px`,
    height: `${size[1] * 50}px`,
    border: '1px solid #ccc',
    backgroundColor: '#f0f0f0',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    margin: '2px',
    cursor: 'grab',
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      {...attributes}
      {...listeners}
      onContextMenu={(e) => {
        e.preventDefault();
        if (window.confirm(`Delete ${name}?`)) onDelete(id);
      }}
    >
      {name} ({weight} кг)
    </div>
  );
};

const Inventory = ({ playerId }) => {
  const [items, setItems] = useState([]);
  const maxWeight = 50;

  useEffect(() => {
    const fetchInventory = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/inventory/${playerId}`);
        setItems(response.data.items);
      } catch (error) {
        console.error('Error fetching inventory:', error);
      }
    };
    fetchInventory();
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

  const deleteItem = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/inventory/${playerId}/item/${id}`);
      setItems((prev) => prev.filter((item) => item.id !== id));
    } catch (error) {
      console.error('Error deleting item:', error);
    }
  };

  const totalWeight = items.reduce((sum, item) => sum + item.weight, 0);

  return (
    <div>
      <h2>Inventory</h2>
      <p>Weight: {totalWeight} / {maxWeight} кг</p>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(8, 50px)', width: '400px', height: '300px', border: '1px solid #000' }}>
        <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
          <SortableContext items={items.map((item) => item.id)} strategy={rectSortingStrategy}>
            {items.map((item) => (
              <SortableItem
                key={item.id}
                id={item.id}
                name={item.name}
                weight={item.weight}
                size={item.size}
                onDelete={deleteItem}
              />
            ))}
          </SortableContext>
        </DndContext>
      </div>
    </div>
  );
};

export default Inventory;