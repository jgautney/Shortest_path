import csv_data
from datetime import timedelta


# truck class
class Truck:
    def __init__(self):
        self.packages = []
        self.speed = 18
        self.current_location = 'HUB'
        self.total_miles = 0
        self.time = None


# list to track packages delivered and provide delivery details to user
delivered_packages = []


# method for loading packages onto all three trucks simultaneously. Deadlines of 10:30 am or earlier go on truck 1 as
# well as packages that need to be delivered together.
# delayed packages or packages specified to be on truck 2 go on truck 2
# rest of packages go on truck 3
def load_trucks(truck1, truck2, truck3):
    special_notes = 'truck 2'
    delay = 'Delayed'
    for i in range(len(csv_data.addresses.map)):
        if len(truck1) < 16:
            if 'EOD' not in csv_data.addresses.get(i + 1).deadline and \
                    delay not in csv_data.addresses.get(i + 1).notes:
                truck1.append(csv_data.addresses.get(i + 1))
            elif 'Deliver with' in csv_data.addresses.get(i + 1).notes:
                truck1.append(csv_data.addresses.get(i + 1))
            elif len(truck2) < 16 and csv_data.addresses.get(i + 1) is not None:
                if special_notes in csv_data.addresses.get(i + 1).notes:
                    truck2.append(csv_data.addresses.get(i + 1))
                elif delay in csv_data.addresses.get(i + 1).notes:
                    truck2.append(csv_data.addresses.get(i + 1))
                    csv_data.addresses.get(i + 1).current_location = 'En route'
                elif len(truck3) < 16:
                    if csv_data.addresses.get(i + 1) is not None:
                        truck3.append(csv_data.addresses.get(i + 1))
                        csv_data.addresses.get(i + 1).current_location = 'En route'
                elif len(truck2) < 16 and csv_data.addresses.get(i + 1) is not None:
                    truck2.append(csv_data.addresses.get(i + 1))
                    csv_data.addresses.get(i + 1).current_location = 'En route'


# very simple greedy algorithm. Uses the trucks current location address and finds the address
# that is closest using the method find_distance from csv_data. updates truck location with the nearest address and
# adds the distance to the trucks total miles.
def deliver_packages(truck):
    min_dist = 100
    delivered_package = None
    for package in range(len(truck.packages)):
        truck.packages[package].location = 'En Route'
        closest_neighbor = truck.packages[package].address
        temp_dist = csv_data.find_distance(truck.current_location, closest_neighbor)
        if truck.packages[package] not in delivered_packages:
            if temp_dist < min_dist:
                min_dist = temp_dist
                delivered_package = truck.packages[package]
    delivered_package.location = 'Delivered'
    truck.total_miles += min_dist
    truck.time += timedelta(hours=min_dist / 18)
    delivered_package.time_delivered = truck.time
    delivered_packages.append(delivered_package)
    truck.current_location = delivered_package.address
    truck.packages.remove(delivered_package)
    if len(truck.packages) == 0:
        dist_to_hub = csv_data.find_distance(truck.current_location, 'HUB')
        truck.total_miles += dist_to_hub
        truck.time += timedelta(hours=dist_to_hub / 18)
        truck.current_location = 'HUB'
