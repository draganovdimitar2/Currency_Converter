from dotenv import load_dotenv  
import os  
import requests  

# Load environment variables from a .env file
load_dotenv()

# Base URL for the exchange rate API
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

# API key for the exchange rate API, loaded from environment variables
API_KEY = os.getenv('API_KEY')

# Function to get the base currency (currency code) from the user
def first_currency():
    currency_one = input('Please enter the first (base) currency:').upper()  # Choosing base currency
    return currency_one

# Function to get the list of available currencies and their conversion rates
def get_currencies(currency_one):
    # Construct the API endpoint for the latest exchange rates for the base currency
    endpoint = f'{API_KEY}/latest/' + currency_one
    url = BASE_URL + endpoint

    # Make a GET request to the API and parse the JSON response    
    data = requests.get(url).json()['conversion_rates']

    # Convert the dictionary of conversion rates to a list of tuples and sort it    
    data = list(data.items())
    data.sort()

    return data

# Function to convert from one currency to another
def convert(currency_one, currency_two):
    endpoint = f'{API_KEY}/pair/{currency_one}/{currency_two}'
    url = BASE_URL + endpoint

    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Raise an exception if the request was unsuccessful        
        response.raise_for_status()

        # Parse the JSON response to get the conversion rate
        data = response.json()['conversion_rate']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    return data

def rate(data, currency_one):
    # Check if data is available
    if data:
        for currency, rate in data:
            print(f"1 {currency} == {rate} {currency_one}")
    else:
        print("No data available.")


def main():
    print(f'Welcome to the currency converter!\n'
          f' * List - lists the different currencies;\n'
          f' * Convert - convert from one currency to another;\n'
          f' * Rate - get the exchange rate of two currencies')
    print()  # separator

    while True:
        command = input('Enter a command (q to quit): ').lower()

        if command == 'q':
            break
        elif command == 'list':
            currency_one = first_currency()  # Get the base currency from the user
            data = get_currencies(currency_one)  # Get the list of available currencies and their conversion rates
            rate(data, currency_one)  # Print the conversion rates
        elif command == 'convert':
            currency_one = first_currency()
            second_currency = input('Please enter second (target) currency:').upper()  # Get the target currency from the user
            amount = int(input(f'Choose amount to convert from {currency_one} to {second_currency}: '))  # Get the amount to convert
            conversion_rate = convert(currency_one, second_currency)  # Get the conversion rate between the base and target currencies
            if conversion_rate:
                # Print the converted amount if the conversion rate is available
                print(f'{amount} {currency_one} == {conversion_rate * amount:.2f} {second_currency}')
        elif command == 'rate':
            currency_one = first_currency()  
            second_currency = input('Please enter second (target) currency:').upper() 
            conversion_rate = convert(currency_one, second_currency)  
            if conversion_rate:
                print(f'1 {currency_one} == {conversion_rate:.2f} {second_currency}')
        else:
            # Print an error message if the command is not recognized
            print('Unrecognized command!')

if __name__ == "__main__":
    main()


