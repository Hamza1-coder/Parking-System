from decimal import Decimal
from django.utils import timezone
from parking.strategies.base import CostComputation
from parking.models import Ticket

# class MinuteBasedPricingStrategy(CostComputation):
#     def calculate_price(self, ticket: Ticket) -> float:
#         minutes = (datetime.now() - ticket.entry_time).total_seconds() / 60
#         return minutes * ticket.parking_spot.price

class MinuteBasedPricingStrategy(CostComputation):
    def calculate_price(self, ticket: Ticket) -> Decimal:
        now = timezone.now()
        minutes = Decimal((now - ticket.entry_time).total_seconds() / 60)
        return minutes * (ticket.parking_spot.price / Decimal(60))