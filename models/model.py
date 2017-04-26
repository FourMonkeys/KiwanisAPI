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
    def __init__(self, id, date, description, address, address2, coordinator, image):
        self.id = id
        self.date = date
        self.description = description
        self.address = address
        self.address2 = address2
        self.coordinator = coordinator
        self.image = image

    def dictify(self):
        return {
            "Id": self.id,
            "Date": self.date,
            "Description": self.description,
            "Address": self.address,
            "Address2": self.address2,
            "Coordinator": self.coordinator,
            "Image": self.image
        }