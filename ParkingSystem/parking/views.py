from django.shortcuts import render, get_object_or_404
from parking.models import ParkingSpot, Ticket, Vehicle
from parking.factories import CostComputationFactory

def book_spot(request):
    if request.method == 'POST':
        vehicle_number = request.POST['vehicle_number']
        vehicle_type = request.POST['vehicle_type']
        vehicle = Vehicle.objects.create(vehicle_number=vehicle_number, vehicle_type=vehicle_type)
        
        print("MY VEHICLE", vehicle, vehicle.vehicle_type)
        
        # Logic to find and book a parking spot
        parking_spot = ParkingSpot.objects.filter(is_empty=True).first()
        
        if not parking_spot:
            return render(request, 'book_spot.html', {'error': 'No available parking spots.'})
        
        parking_spot.vehicle = vehicle
        parking_spot.is_empty = False
        parking_spot.save()
        
        ticket = Ticket.objects.create(vehicle=vehicle, parking_spot=parking_spot)
        return render(request, 'ticket.html', {'ticket': ticket})
    
    return render(request, 'book_spot.html')

def exit_gate(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    computation = CostComputationFactory.get_cost_computation(ticket.vehicle.vehicle_type)
    price = computation.calculate_price(ticket)
    
    # free up the parking spot
    parking_spot = ticket.parking_spot
    parking_spot.is_empty = True
    parking_spot.vehicle = None
    parking_spot.save()
    
    ticket.delete()
    return render(request, 'exit.html', {'price': price})
    