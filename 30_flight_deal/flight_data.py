class FlightData:

    def __init__(self, dest_city: str):
        self.city = dest_city
        self.price = 0
        self.departure = ""
        self.destination = ""
        self.date_begin = ""
        self.date_end = ""
        self.stops = 0

    def set_lower_price(self, flight_data: dict, initial_date: str,
                        end_date: str):
        price_float = float(flight_data["price"]["total"])
        if self.departure == "" or price_float < self.price:
            self.price = price_float
            full_itinerary = flight_data["itineraries"][0]["segments"]
            self.departure = full_itinerary[0]["departure"]["iataCode"]
            self.destination = full_itinerary[-1]["arrival"]["iataCode"]
            self.date_begin = initial_date
            self.date_end = end_date
            self.stops = len(full_itinerary)
