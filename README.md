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
4. Create a `.env` file in the root directory and add your ExchangeRate-API key:
    ```env
    API_KEY=your_api_key_here
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
