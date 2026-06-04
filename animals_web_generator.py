import json


def load_data(file_path: str) -> list:
    """
    Loads and parses a JSON file.

    :param file_path: The path to the JSON file.
    :return: A parsed list of dictionaries containing animal data.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_file(file_path: str) -> str:
    """
    Reads the content of a text file.

    :param file_path: The path to the text file.
    :return: The content of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_file(file_path: str, content: str) -> None:
    """
    Writes a string to a file.

    :param file_path: The path to the output file.
    :param content: The string content to be written.
    """
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def generate_animals_string(animals_data: list) -> str:
    """
    Iterates through the animal data and generates a single formatted string.
    Fields are only included if they exist in the data.

    :param animals_data: A list of dictionaries representing animals.
    :return: A string containing the formatted animal information.
    """
    output = ""
    for animal in animals_data:
        name = animal.get("name")
        if name:
            output += f"Name: {name}\n"

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        if diet:
            output += f"Diet: {diet}\n"

        # Locations, only need the first item
        locations = animal.get("locations")
        if locations and len(locations) > 0:
            output += f"Location: {locations[0]}\n"

        animal_type = characteristics.get("type")
        if animal_type:
            output += f"Type: {animal_type}\n"

        # Empty line to separate animals
        output += "\n"

    return output


def main() -> None:
    """
    Main entry point of the script.
    Orchestrates reading data, generating the HTML string, and writing the output file.
    """
    # 1. Load the animal data
    animals_data = load_data("animals_data.json")

    # 2. Generate the formatted string
    animals_info_string = generate_animals_string(animals_data)

    # 3. Read the HTML template
    html_template = read_file("animals_template.html")

    # 4. Replace the placeholder with the generated string
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

    # 5. Write the final HTML content to a new file
    write_file("animals.html", final_html)


if __name__ == "__main__":
    main()