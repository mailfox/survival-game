from datetime import datetime, timedelta
from sqlalchemy.orm import Session

def update_survival_stats(db: Session, player):
    now = datetime.utcnow()
    time_diff = now - player.last_update
    hours_passed = time_diff.total_seconds() / 3600
    
    # Ухудшение показателей
    player.hunger = max(0, player.hunger - int(5 * hours_passed))
    player.thirst = max(0, player.thirst - int(8 * hours_passed))
    
    # Урон от голода/жажды
    if player.hunger == 0:
        player.health = max(0, player.health - int(2 * hours_passed))
    if player.thirst == 0:
        player.health = max(0, player.health - int(3 * hours_passed))
    
    # Обновляем время последнего изменения
    player.last_update = now