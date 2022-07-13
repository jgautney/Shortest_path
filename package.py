# package class

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, mass, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.location = 'at the HUB'
        self.time_delivered = 'N/A'

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                           self.zip_code, self.deadline, self.mass, self.notes,
                                                           self.location, self.time_delivered)
