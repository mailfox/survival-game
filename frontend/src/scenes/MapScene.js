// /home/mailfox/survival-game/frontend/src/scenes/MapScene.js
import React, { useEffect, useRef } from 'react';
import Phaser from 'phaser';
import axios from 'axios';
import gsap from 'gsap';

// Базовый URL для бэкенда
const API_URL = 'http://127.0.0.1:8000';

const MapScene = ({ onExplore }) => {
  const gameRef = useRef(null);
  const phaserGameRef = useRef(null);

  useEffect(() => {
    const sceneConfig = {
      key: 'MapScene',
      preload() {
        console.log('Preload phase'); // Отладка
        // Можно загрузить фоновое изображение, если нужно
        // this.load.image('background', '/images/background.png');
      },
      create() {
        console.log('Create phase'); // Отладка
        // Добавляем заголовок
        this.add.text(100, 100, 'Map: Select a location', { color: '#0f0' });

        // Создаём текстовые метки для локаций
        ['Bunker', 'Forest', 'Factory'].forEach((loc, index) => {
          const text = this.add.text(100, 150 + index * 50, loc, { color: '#0f0' }).setInteractive();
          text.on('pointerdown', async () => {
            // Анимация при клике
            gsap.to(text, { alpha: 0.5, duration: 2.5, repeat: 1, yoyo: true });

            try {
              const response = await axios.post(`${API_URL}/location/explore`, {
                location_name: loc,
                player_id: 1, // Тестовый ID игрока
              });
              console.log('Explore response:', response.data); // Отладка
              // Отображаем результат
              this.add.text(300, 150 + index * 50, JSON.stringify(response.data), { color: '#fff' });

              // Уведомляем App.js об изменениях, чтобы обновить PlayerStatus и Inventory
              if (onExplore) {
                onExplore(response.data);
              }
            } catch (error) {
              console.error('Error exploring location:', error.response || error.message);
              this.add.text(300, 150 + index * 50, 'Error exploring', { color: '#f00' });
            }
          });
        });
      },
    };

    const config = {
      type: Phaser.AUTO,
      width: 800,
      height: 600,
      parent: gameRef.current,
      scene: sceneConfig,
    };

    if (!phaserGameRef.current) {
      phaserGameRef.current = new Phaser.Game(config);
      console.log('Phaser game initialized'); // Отладка
    }

    return () => {
      if (phaserGameRef.current) {
        phaserGameRef.current.destroy(true);
        phaserGameRef.current = null;
        console.log('Phaser game destroyed'); // Отладка
      }
    };
  }, [onExplore]);

  return <div ref={gameRef} style={{ width: '800px', height: '600px' }} />;
};

export default MapScene;