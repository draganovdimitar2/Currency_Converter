# Currency Converter

A simple Python application to convert currencies using the ExchangeRate-API.

## Features

- Convert between different currencies.
- Fetch the latest exchange rates.
- User-friendly input for base and target currencies.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/draganovdimitar2/Currency_Converter
    ```
2. Navigate to the project directory:
    ```sh
    cd Currency_Converter
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. The `.env` file with the ExchangeRate-API key is already included in the repository. However, if you want to use your own API key, you can modify the `.env` file with your own key:
    ```sh
    echo "API_KEY=your_api_key_here" > .env
    ```

## Usage

1. Run the script:
    ```sh
    python Currency_Converter.py
    ```
2. Follow the prompts to enter the base and target currencies.

## Example

```sh
Please enter the first (base) currency: USD
Please enter the second (target) currency: EUR
