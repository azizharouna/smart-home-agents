from pydantic import BaseModel
from typing import Optional

class CleaningState(BaseModel):
    battery_level: float = 100.0
    current_room: str = "living_room"
    cleaning_path: list[str] = []

class LowBatteryError(Exception):
    """Raised when battery level is critically low"""
    pass

class AdvancedCleaningAgent:
    def __init__(self, iot_client):
        self.state = CleaningState()
        self.iot = iot_client
        
    def check_battery(self):
        """Check battery level and raise error if too low"""
        if self.state.battery_level < 20:
            raise LowBatteryError("Returning to dock")
            
    def update_sensors(self):
        """Update state from IoT sensors"""
        self.state.battery_level = self.iot.get_battery_level()
        self.state.current_room = self.iot.get_current_room()