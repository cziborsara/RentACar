from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, registration_number, type, rental_fee):
        self.registration_number = registration_number
        self.type = type
        self.rental_fee = rental_fee

    def __str__(self):
        pass

class Car(Auto):
    def __init__(self, registration_number, type, rental_fee, car_seat):
        super().__init__(registration_number, type, rental_fee)
        self.car_seat = car_seat

    def __str__(self):
        return f"Személyautó: {self.registration_number}, {self.type},  {self.rental_fee} Ft/nap,  {self.car_seat} ülés"

class Truck(Auto):
    def __init__(self, registration_number, type, rental_fee, load_capacity):
        super().__init__(registration_number, type, rental_fee)
        self.load_capacity = load_capacity

    def __str__(self):
        return f"Teherautó: {self.registration_number}, {self.type}, {self.rental_fee} Ft/nap, {self.load_capacity} kg"

