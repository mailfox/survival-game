from db.session import SessionLocal
from models.player import Player

db = SessionLocal()

# Создаем нового игрока (только с существующими полями)
new_player = Player(
    health=100,
    hunger=100,
    thirst=100
    # stamina и radiation добавятся со значениями по умолчанию
)

db.add(new_player)
db.commit()
print(f"Создан игрок с ID: {new_player.id}")
db.close()