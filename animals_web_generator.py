import json


def load_data(file_path: str) -> list:
    """
    Loads and parses a JSON file.

    :param file_path: The path to the JSON file.
    :return: A parsed list of dictionaries containing animal data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals_data(animals_data: list) -> None:
    """
    Iterates through the animal data and prints specific details.
    Fields are only printed if they exist in the data.

    :param animals_data: A list of dictionaries representing animals.
    """
    for animal in animals_data:
        name = animal.get("name")
        if name:
            print(f"Name: {name}")

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        if diet:
            print(f"Diet: {diet}")

        # Locations, only need the first item
        locations = animal.get("locations")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")

        animal_type = characteristics.get("type")
        if animal_type:
            print(f"Type: {animal_type}")

        # Empty line to separate animals
        print()


def main() -> None:
    """
    Main entry point of the script.
    """
    # Load the data
    animals_data = load_data("animals_data.json")

    # Process and print the data
    print_animals_data(animals_data)


if __name__ == "__main__":
    main()