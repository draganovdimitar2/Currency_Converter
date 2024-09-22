from dotenv import load_dotenv
import os
import requests

load_dotenv()
BASE_URL = 'https://v6.exchangerate-api.com/v6/'
API_KEY = os.getenv('API_KEY')


def first_currency():
    currency_one = input('Please enter the first (base) currency:').upper()  # Choosing base currency
    return currency_one


def get_currencies(currency_one):
    endpoint = f'{API_KEY}/latest/' + currency_one
    url = BASE_URL + endpoint
    data = requests.get(url).json()['conversion_rates']
    data = list(data.items())
    data.sort()
    return data

def convert(currency_one, currency_two):
    endpoint = f'{API_KEY}/pair/{currency_one}/{currency_two}'
    url = BASE_URL + endpoint
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['conversion_rate']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    return data

def rate(data, currency_one):
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
            currency_one = first_currency()
            data = get_currencies(currency_one)
            rate(data, currency_one)
        elif command == 'convert':
            currency_one = first_currency()
            second_currency = input('Please enter second (target) currency:').upper()
            amount = int(input(f'Choose amount to convert from {currency_one} to {second_currency}: '))
            conversion_rate = convert(currency_one, second_currency)
            if conversion_rate:
                print(f'{amount} {currency_one} == {conversion_rate * amount:.2f} {second_currency}')
        elif command == 'rate':
            currency_one = first_currency()
            second_currency = input('Please enter second (target) currency:').upper()
            conversion_rate = convert(currency_one, second_currency)
            if conversion_rate:
                print(f'1 {currency_one} == {conversion_rate:.2f} {second_currency}')
        else:
            print('Unrecognized command!')

if __name__ == "__main__":
    main()


