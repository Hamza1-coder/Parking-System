from abc import ABC, abstractmethod
from parking.models import Ticket

class CostComputation(ABC):
    @abstractmethod
    def calculate_price(self, ticket: Ticket) -> float:
        pass
    
    

