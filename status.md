# Статус проекта: Zemlya Mertvykh: Survival
Дата: 30 мая 2025
Версия: v1.0

## Прогресс
- Бэкенд: FastAPI, PostgreSQL. Работают маршруты:
  - GET /players/{id}
  - POST /player/eat, /player/drink
  - GET /inventory/{player_id}
  - POST /location/explore
- Фронтенд: React, Phaser, GSAP. Работают:
  - PlayerStatus.js (здоровье, голод, жажда)
  - Inventory.js (drag-and-drop, удаление предметов)
  - MapScene.js (локации с анимацией)
- Данные: игрок id=1, предметы (Bandage, Water), локации (Bunker, Forest, Factory).

## Следующие шаги
- Реализовать систему радиации (POST /player/radiate, кнопка в PlayerStatus.js).
- Добавить иконки предметов в Inventory.js.
