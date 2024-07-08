# from datetime import datetime
# from parking.strategies.base import CostComputation
# from parking.models import Ticket

# class HourlyPricingStrategy(CostComputation):
#     def calculate_price(self, ticket: Ticket) -> float:
#         hours = (datetime.now() - ticket.entry_time).total_seconds() / 3600
#         return hours * ticket.parking_spot.price
    
    
    
from django.utils import timezone
from parking.strategies.base import CostComputation
from parking.models import Ticket
from decimal import Decimal

class HourlyPricingStrategy(CostComputation):
    def calculate_price(self, ticket: Ticket) -> Decimal:
        now = timezone.now()
        hours = Decimal((now - ticket.entry_time).total_seconds() / 3600)
        return hours * ticket.parking_spot.price