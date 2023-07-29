from engine import WilloughbyEngine, SpindlerBattery, CapuletEngine, sternmanEngine
from battery import NubbinBattery
from car import Car




class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(battery, engine)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(battery, engine)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = sternmanEngine(warning_light_on)
        return Car(battery, engine)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(battery, engine)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(battery, engine)
