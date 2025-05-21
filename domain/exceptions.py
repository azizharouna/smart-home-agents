class SmartHomeError(Exception):
    """Base exception for all smart home agent errors"""
    pass

class LowBatteryError(SmartHomeError):
    """Raised when agent battery is critically low"""
    def __init__(self, message="Battery level below 20%"):
        self.message = message
        super().__init__(self.message)

class SensorError(SmartHomeError):
    """Raised when IoT sensor communication fails"""
    pass

class NavigationError(SmartHomeError):
    """Raised when agent encounters pathfinding issues"""
    pass