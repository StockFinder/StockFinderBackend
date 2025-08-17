import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = True


def humanize_last_update(updated_at: datetime) -> str:
    if updated_at.tzinfo is None:
        updated_at = updated_at.replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)

    diff = now - updated_at
    seconds = diff.total_seconds()
    minutes = int(seconds // 60)
    hours = int(seconds // 3600)
    days = int(seconds // 86400)

    if seconds < 3600:
        if minutes < 1:
            return "Hace menos de 1 minuto"
        elif minutes == 1:
            return "Hace 1 minuto"
        else:
            return f"Hace {minutes} minutos"
    elif hours < 24:
        if hours == 1:
            return "Hace 1 hora"
        else:
            return f"Hace {hours} horas"
    else:
        if days == 1:
            return "Hace 1 día"
        else:
            return f"Hace {days} días"
