import requests
import json

class CurrencyConverter:
    def __init__(self):
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        self.available_currencies = None

    def get_available_currencies(self):
        try:
            if not self.available_currencies:
                response = requests.get(self.base_url)
                response.raise_for_status()  # Raise exception for non-2xx responses
                data = response.json()
                self.available_currencies = data["rates"].keys()
            return self.available_currencies
        except Exception as e:
            print("Error fetching currency data:", e)
            return []

    def convert_currency(self, amount, from_currency, to_currency):
        try:
            available_currencies = self.get_available_currencies()
            from_currency = from_currency.upper()
            to_currency = to_currency.upper()

            if not available_currencies:
                return "Error fetching currency data. Please try again later."

            if from_currency not in available_currencies or to_currency not in available_currencies:
                return "Invalid currency code. Available codes: " + ", ".join(available_currencies)

            url = f"{self.base_url}{from_currency}"
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-2xx responses
            data = response.json()
            conversion_rate = data["rates"][to_currency]
            converted_amount = amount * conversion_rate
            return converted_amount
        except Exception as e:
            return "Error converting currency: " + str(e)

if __name__ == "__main__":
    converter = CurrencyConverter()

    amount = float(input("Enter amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").strip()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").strip()

    converted_amount = converter.convert_currency(amount, from_currency, to_currency)
    if isinstance(converted_amount, str):
        print("Error:", converted_amount)
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
