from abc import ABC, abstractmethod
class Battery(ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    @abstractmethod
    def needs_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        if self.current_date - self.last_service_date > 2:
            return True
        else:
            return False
        
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        if self.current_date - self.last_service_date > 4:
            return True
        else:
            return False
