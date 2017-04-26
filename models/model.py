class Member:
    def __init__(self, name, email, phone, image, role):
        self.name = name
        self.email = email
        self.phone = phone
        self.image = image
        self.role = role

    def dictify(self):
        return {
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Image": self.image,
            "Role": self.role
        }


class Event:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.date = ''
        self.description = ''
        self.address = ''
        self.address2 = ''
        self.coordinator = ''
        self.image = ''

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_description(self, description):
        self.description = description

    def set_address(self, address):
        self.address = address

    def set_address2(self, address):
        self.address2 = address

    def set_coordinator(self, coordinator):
        self.coordinator = coordinator

    def set_image(self, image):
        self.image = image

    def dictify(self):
        return {
            "Id": self.id,
            "Name": self.name,
            "Date": self.date,
            "Description": self.description,
            "Address": self.address,
            "Address2": self.address2,
            "Coordinator": self.coordinator,
            "Image": self.image
        }