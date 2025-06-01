from Car import Car, Truck
from CarRent import CarRent
from Rent import Rent

def fillin(rental):
    car1 = Car("ABC123", "Toyota Corolla", 10000, 5)
    car2 = Car("DEF456", "Volkswagen Golf", 12000, 5)
    car3 = Truck("GHI789", "Ford Transit", 15000, 1200)
    rental.car_add(car1)
    rental.car_add(car2)
    rental.car_add(car3)

    rental.rentals.append(Rent(car1, "2025-06-02"))
    rental.rentals.append(Rent(car2, "2025-06-01"))
    rental.rentals.append(Rent(car3, "2025-06-03"))
    rental.rentals.append(Rent(car1, "2025-06-04"))

def menu():
    print("\n--- Autókölcsönző Rendszer ---")
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Kilépés")

def main():
    rental = CarRent("City Rent")
    fillin(rental)

    while True:
        menu()
        choice = input("Válassz műveletet: ")

        if choice == "1":
            registration_number = input("Add meg az autó rendszámát: ")
            date = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            print(rental.rent_a_car(registration_number, date))

        elif choice == "2":
            registration_number = input("Add meg a rendszámot: ")
            date = input("Add meg a dátumot (YYYY-MM-DD): ")
            print(rental.delete_rent(registration_number, date))

        elif choice == "3":
            print(rental.rent_list())

        elif choice == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
