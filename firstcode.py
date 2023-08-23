class FlightData:
    def __init__(self):
        self.flights = [
            {"Flight Code": "AI161E90", "Departure": "Bengaluru", "Destination": "Mumbai", "Price": 5600},
            {"Flight Code": "BR161F91", "Departure": "Mumbai", "Destination": "Bhubaneswar", "Price": 6750},
            {"Flight Code": "AI161F99", "Departure": "Bhubaneswar", "Destination": "Bengaluru", "Price": 8210},
            {"Flight Code": "VS171E20", "Departure": "Jabalpur", "Destination": "Bhubaneswar", "Price": 5500},
            {"Flight Code": "AS171G30", "Departure": "Hyderabad", "Destination": "Jabalpur", "Price": 4400},
            {"Flight Code": "AI131F49", "Departure": "Hyderabad", "Destination": "Mumbai", "Price": 3499}
        ]

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight["Departure"] == city or flight["Destination"] == city:
                result.append(flight)
        return result

    def search_flights_from(self, from_city):
        result = []
        for flight in self.flights:
            if flight["Departure"] == from_city:
                result.append(flight)
        return result

    def search_between_cities(self, from_city, to_city):
        result = []
        for flight in self.flights:
            if flight["Departure"] == from_city and flight["Destination"] == to_city:
                result.append(flight)
        return result

def main():
    flight_data = FlightData()

    while True:
        print("\nFlight Search Options:")
        print("1. Flights for a specific City")
        print("2. Flights From a City")
        print("3. Flights between two Cities")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            city = input("Enter the city name: ")
            results = flight_data.search_by_city(city)
        elif choice == "2":
            from_city = input("Enter the city name to search flights from: ")
            results = flight_data.search_flights_from(from_city)
        elif choice == "3":
            from_city = input("Enter the departure city name: ")
            to_city = input("Enter the arrival city name: ")
            results = flight_data.search_between_cities(from_city, to_city)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not results:
            print("No flights found.")
        else:
            print("\nSearch Results:")
            for flight in results:
                print(f"Flight Code: {flight['Flight Code']}, Departure: {flight['Departure']}, Destination: {flight['Destination']}, Price: {flight['Price']}")

if __name__ == "__main__":
    main()
