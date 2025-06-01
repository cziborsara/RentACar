from Rent import Rent

class CarRent:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.rentals = []

    def car_add(self, car):
        self.cars.append(car)

    def rent_a_car(self, registration_number, date):
        for rent in self.rentals:
            if rent.auto.registration_number == registration_number and rent.date == date:
                return f"HIBA: Ez az autó {date}-ra már foglalt."

        for car in self.cars:
            if car.registration_number == registration_number:
                new_rent = Rent(car, date)
                self.rentals.append(new_rent)
                return f"Bérlés sikeres. Ár: {car.rental_fee} Ft"
        return "HIBA: Nincs ilyen rendszámú autó."

    def delete_rent(self, registration_number, date):
        for rent in self.rentals:
            if rent.auto.registration_number == registration_number and rent.date == date:
                self.rentals.remove(rent)
                return "Bérlés sikeresen törölve."
        return "HIBA: Ilyen bérlés nem található."

    def rent_list(self):
        if not self.rentals:
            return "Nincsenek aktuális bérlések."
        return "\n".join(str(rent) for rent in self.rentals)
