# Weather API Program

The Weather API Program is a Python application that utilizes the OpenWeather API to provide weather information for a specified city. It allows users to either input their OpenWeather API key or use a default key to fetch and display the current weather details.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [API Key](#api-key)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Weather API Program is designed to fetch and display current weather data for a given city using the OpenWeather API. It includes a simple user interface for entering the API key and the desired city.

## Features

- Fetches real-time weather data from the OpenWeather API.
- Allows users to enter their OpenWeather API key or use a default key.
- Displays temperature, weather description, and the time zone of the specified city.

## Requirements
- Requires request package
- API Key for OpenWeather

## Installations

1. **Clone Repository**

   ```bash
   https://github.com/FinesserULTRA/API-Implementation.git
   ```
2. **Get Requests**

   ```bash
   pip install requests
   ```

3. **Change directory**

   ```bash
   cd API-Implementation
   ```

## Usage

1. **Run the program:**

    ```bash
    python main.py
    ```

2. **Follow on-screen instructions:**

    - Choose whether to enter your API key or use the default key.
    - Enter the city for which you want to check the weather.

## API Key

- If you choose option 1 (Enter API Key), you will be prompted to provide your OpenWeather API key.
- If you choose option 2 (Use Default API Key), a default API key will be used (for demonstration purposes).

## Functions

### `WeatherApiClient`

- Constructor: Initializes the WeatherApiClient object with the provided API key.
- `getWeather(city)`: Requests weather data from the OpenWeather API for the specified city.
- `showData(data)`: Displays temperature, weather description, and time zone based on the received data.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the [GNU v3 License](LICENSE).

---

*Note: Further enhancements and improvements may be added, and any contributions toward improvement are highly appreciated.*
