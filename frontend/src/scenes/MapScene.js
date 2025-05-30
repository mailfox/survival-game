import Phaser from 'phaser';
import axios from 'axios';
import gsap from 'gsap';

class MapScene extends Phaser.Scene {
  constructor() {
    super('MapScene');
  }

  create() {
    this.add.text(100, 100, 'Map: Select a location', { color: '#0f0' });
    ['Bunker', 'Forest', 'Factory'].forEach((loc, index) => {
      const text = this.add.text(100, 150 + index * 50, loc, { color: '#0f0' }).setInteractive();
      text.on('pointerdown', () => {
        gsap.to(text, { alpha: 0.5, duration: 2.5, repeat: 1, yoyo: true });
        axios.post('http://localhost:8000/location/explore', { location_name: loc })
          .then(response => {
            this.add.text(300, 150 + index * 50, JSON.stringify(response.data), { color: '#fff' });
          })
          .catch(error => {
            console.error('Error exploring location:', error);
          });
      });
    });
  }
}

export default MapScene;