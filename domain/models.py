from pydantic import BaseModel
from enum import Enum

class Room(str, Enum):
    LIVING = "living_room"
    KITCHEN = "kitchen"
    BEDROOM = "bedroom"
    BATHROOM = "bathroom"

class CleaningState(BaseModel):
    battery_level: float
    current_room: Room
    cleaning_path: list[Room]
    last_cleaned: dict[Room, str] = {}

class AgentStatus(BaseModel):
    is_active: bool = True
    last_heartbeat: str = ""
    error_count: int = 0