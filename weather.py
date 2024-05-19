import requests
import json


try:
    with open('weather_data.json', 'r') as f:
        weather_data_all = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    weather_data_all = {}

while True:

    see_old_data = input("Do you want to see old data? (yes/no): ")
    if see_old_data.lower() == "yes":

        print("Available cities:")
        for city in weather_data_all.keys():
            print(city)
        city_name = input("Enter the name of the city from the list above: ".lower())
        if city_name not in weather_data_all:
            print("Data for the selected city is not available.")
            city_name = input("Enter the name of a new city: ")
    else:
        city_name = input("Enter the name of a new city: ".lower())

    if city_name not in weather_data_all:
        url = f"https://open-weather13.p.rapidapi.com/city/{city_name}/EN"

        headers = {
         "X-RapidAPI-Key": "YOUR_API_KEY",
         "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        weather_data = response.json()

        weather_data_all[city_name] = weather_data

        with open('weather_data.json', 'w') as f:
            json.dump(weather_data_all, f)

        print("Weather data saved to weather_data.json")
    else:
        weather_data = weather_data_all[city_name]

    while True:
        print("What information would you like to display?")
        print("1. Coordinates")
        print("2. Weather")
        print("3. Base")
        print("4. Main")
        print("5. Visibility")
        print("6. Wind")
        print("7. Clouds")
        print("8. Timezone")
        print("9. ID")
        print("10. Name")

        choice = input("Enter the number of your choice: ")

        key_map = {
            "1": "coord",
            "2": "weather",
            "3": "base",
            "4": "main",
            "5": "visibility",
            "6": "wind",
            "7": "clouds",
            "8": "timezone",
            "9": "id",
            "10": "name"
        }

        selected_key = key_map.get(choice)

        if selected_key in weather_data:
            print(weather_data[selected_key])
        else:
            print("Invalid choice.")

        continue_same_city = input("Do you want to continue with the same city? (yes/no): ")
        if continue_same_city.lower() != "yes":
            break

    continue_new_city = input("Do you want to continue with a new city? (yes/no): ")
    if continue_new_city.lower() != "yes":
        break