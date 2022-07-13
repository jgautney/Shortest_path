# main.py
# Josh Gautney

import sys
import truck
from truck import Truck
from datetime import timedelta, datetime
from csv_data import addresses

# create truck objects and set their starting time
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()
truck1.time = timedelta(hours=8, minutes=00)
truck2.time = timedelta(hours=9, minutes=5)
truck3.time = truck1.time

print("\n------------------------------------------------")
print("Welcome to the Delivery Tracking Software!")
print("------------------------------------------------\n")


# print package data. Package ID, address, etc.
def get_package_data(package_id):
    print("\n----------------------------------------------------")
    print(f"Package ID: {addresses.get(package_id).package_id}")
    print(f"Package address: {addresses.get(package_id).address}")
    print(f"Package city: {addresses.get(package_id).city}")
    print(f"Package state: {addresses.get(package_id).state}")
    print(f"Package zip code: {addresses.get(package_id).zip_code}")
    print(f"Package deadline: {addresses.get(package_id).deadline}")
    print(f"Package mass(kilos): {addresses.get(package_id).mass}")
    print(f"Package notes: {addresses.get(package_id).notes}")
    print(f"Package location: {addresses.get(package_id).location}")
    print(f"Package time delivered: {addresses.get(package_id).time_delivered}")
    print("----------------------------------------------------\n")


# print package data for all packages on the specified truck
def print_truck_storage(vehicle):
    for index in range(len(vehicle.packages)):
        print(f"Package ID: {vehicle.packages[index].package_id}")
        print(f"Package address: {vehicle.packages[index].address}")
        print(f"Package city: {vehicle.packages[index].city}")
        print(f"Package state: {vehicle.packages[index].state}")
        print(f"Package zip code: {vehicle.packages[index].zip_code}")
        print(f"Package deadline: {vehicle.packages[index].deadline}")
        print(f"Package mass(kilos): {vehicle.packages[index].mass}")
        print(f"Package notes: {vehicle.packages[index].notes}")
        print(f"Package location: {vehicle.packages[index].location}")
        print(f"Package time delivered: {vehicle.packages[index].time_delivered}")
        print("----------------------------------------------------\n")


# run user interface
def run_interface():
    is_done = False
    user_input = input("What would you like to do? Please enter the corresponding message: \n"
                       "Look up a packages status: look up\n"
                       "Go to certain time: time\n"
                       "Print all packages (both delivered and on trucks): print\n"
                       "Deliver all packages: deliver\n"
                       "Exit program: exit\n").lower()

    if user_input == 'look up':
        user_input = int(input("\nPlease enter a package ID:\n"))
        get_package_data(user_input)
        run_interface()
    elif user_input == 'time':
        user_input = input("Please specify a time (HH:MM):\n")
        td = datetime.strptime(user_input, '%H:%M')
        user_time = timedelta(hours=td.hour, minutes=td.minute)
        print("\n----------------------------------------\n")
        print(f"The current time is : {user_time}")
        while user_time > truck3.time:
            if len(truck1.packages) > 0:
                truck.deliver_packages(truck1)
                truck3.time = truck1.time
            if truck1.time > truck2.time:
                if len(truck2.packages) > 0:
                    truck.deliver_packages(truck2)
            if truck1.current_location == 'HUB' and len(truck1.packages) == 0:
                truck.deliver_packages(truck3)
                if truck3.time > timedelta(hours=10, minutes=2):
                    for i in range(len(truck3.packages)):
                        if truck3.packages[i].package_id == 9:
                            truck3.packages[i].address = '410 S State St'
                            truck3.packages[i].city = 'Salt Lake City'
                            truck3.packages[i].state = 'UT'
                            truck3.packages[i].zip_code = '84111'
                            truck3.packages[i].notes = '* Address corrected'
            if len(truck3.packages) == 0:
                break
        print("\n------------------------------------------------\n")
        run_interface()
    elif user_input == 'print':
        user_input = input("Which truck: type 1, 2, 3, delivered, or all \n").lower()
        if user_input == '1':
            print("\n--------------------Truck 1 Storage------------------------------")
            if len(truck1.packages) == 0:
                print("Truck 1 has delivered all packages!")
            print_truck_storage(truck1)
        elif user_input == '2':
            print("\n--------------------Truck 2 Storage------------------------------")
            if len(truck2.packages) == 0:
                print("Truck 2 has delivered all packages!")
            print_truck_storage(truck2)
        elif user_input == '3':
            print("\n--------------------Truck 3 Storage------------------------------")
            if len(truck3.packages) == 0:
                print("Truck 3 has delivered all packages!")
            print_truck_storage(truck3)
        elif user_input == 'delivered':
            for i in range(len(truck.delivered_packages)):
                print(truck.delivered_packages[i].package_id, truck.delivered_packages[i].address,
                      truck.delivered_packages[i].city, truck.delivered_packages[i].state,
                      truck.delivered_packages[i].zip_code, truck.delivered_packages[i].deadline,
                      truck.delivered_packages[i].location, truck.delivered_packages[i].time_delivered)
                print("-----------------------------------\n")
        elif user_input == 'all':
            for i in range(len(addresses.map) + 1):
                if addresses.get(i) is not None:
                    print(addresses.get(i))
            print("")
        run_interface()
    elif user_input == 'deliver':
        while not is_done:
            if len(truck1.packages) > 0:
                truck.deliver_packages(truck1)
                truck3.time = truck1.time
            if len(truck2.packages) > 0:
                truck.deliver_packages(truck2)
            if truck1.current_location == 'HUB' and len(truck1.packages) == 0:
                truck.deliver_packages(truck3)
            if len(truck3.packages) == 0:
                is_done = True
                print("\n------------------------------------------------")
                print(f"Truck 1 total miles: {truck1.total_miles}")
                print(f"Truck 1 location: {truck1.current_location}")
                print(f"Truck 1 completed at: {truck1.time}\n")
                print(f"Truck 2 total miles: {truck2.total_miles}")
                print(f"Truck 2 location: {truck1.current_location}")
                print(f"Truck 2 completed at: {truck2.time}\n")
                print(f"Truck 3 total miles: {truck3.total_miles}")
                print(f"Truck 3 location: {truck1.current_location}")
                print(f"Truck 3 completed at: {truck3.time}\n")
                print(f"\nCurrent time: {truck3.time}")
                print(f"\nTotal miles: {truck1.total_miles + truck2.total_miles + truck3.total_miles}")
                print("------------------------------------------------\n")
                run_interface()
    elif user_input == 'exit':
        sys.exit()
    else:
        print("\nInvalid command, please try again\n")
        run_interface()


# load trucks and call run_interface
truck.load_trucks(truck1.packages, truck2.packages, truck3.packages)
run_interface()

