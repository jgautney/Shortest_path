import csv
from package import Package
from hashtable import Hashtable

distance_file = "WGUPS Distance Table_1.csv"
address_file = "WGUPS Package File_1.csv"
addresses = Hashtable()
address_data = []


# Load data from csv file into hash map 'addresses'
def load_package_data(file):
    with open(file) as data_file:
        package_data = csv.reader(data_file, delimiter=',')
        next(package_data)
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            weight = package[6]
            notes = package[7]

            package = Package(package_id, address, city, state, zip_code, deadline, weight,
                              notes)

            addresses.add(package_id, package)


# load addresses from adjacency matrix into list address_data to help with finding distances
def load_addresses(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for col in csv_reader:
            address_data.append(col[0])

    for item in address_data:
        if item == '':
            address_data.remove(item)


# load csv files into the program
load_addresses(distance_file)
load_package_data(address_file)


# search through the adjacency matrix to find the distance between current_address and next_address
# uses address_data index to find the corresponding x and y values to use look up distance in the matrix
def find_distance(current_address, next_address):
    with open(distance_file, 'r') as file:
        reader = csv.reader(file)
        row = 0
        current_address = address_data.index(current_address) + 1
        next_address = address_data.index(next_address) + 1
        for i in reader:
            if row == next_address:
                cell = i[current_address]
                return float(cell)
            row += 1
