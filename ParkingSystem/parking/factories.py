from parking.models import Vehicle
from parking.strategies.hourly import HourlyPricingStrategy
from parking.strategies.minute_based import MinuteBasedPricingStrategy

class CostComputationFactory:
    @staticmethod
    def get_cost_computation(vehicle_type: str):
        if vehicle_type == 'TW':
            return HourlyPricingStrategy()
        elif vehicle_type == 'FW':
            return MinuteBasedPricingStrategy()
        else:
            raise ValueError('Unknown vehicle type')