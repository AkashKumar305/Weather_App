# Weather Data Retrieval

This Python script retrieves current weather data for a specified city using the WeatherAPI. It allows users to input a city name, fetches the current weather data from the API, and displays it to the user.

## Usage

1. Clone the repository or download the Python script (`app.py`).
2. Ensure you have Python installed on your system.
3. Install the `requests` library if you haven't already:

    ```
    pip install requests
    ```

4. Obtain an API key from [WeatherAPI](https://www.weatherapi.com/) and replace `'key'` in the `main()` function with your API key.
5. Run the script:

    ```
    python weather.py
    ```

6. Enter the name of the city when prompted.
7. The script will then retrieve and display the current weather data for the specified city.

## Dependencies

- Python 3.x
- `requests` library

## Notes

- This script uses the WeatherAPI to fetch weather data. Make sure you comply with their terms of use and API usage guidelines.
- Error handling is implemented to deal with cases where the API request fails or incomplete data is received.

