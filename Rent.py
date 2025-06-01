class Rent:
    def __init__(self, auto, date):
        self.auto = auto
        self.date = date

    def __str__(self):
        return f"Bérlés: {self.auto.registration_number} - {self.date} - {self.auto.rental_fee} Ft/nap"
