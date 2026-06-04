import json


def load_data(file_path: str) -> list:
    """
    Loads and parses a JSON file.

    :param file_path: The path to the JSON file.
    :return: A parsed list of dictionaries containing animal data.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the JSON content is malformed.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_file(file_path: str) -> str:
    """
    Reads the content of a text file.

    :param file_path: The path to the text file.
    :return: The content of the file as a string.
    :raises FileNotFoundError: If the file does not exist.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_file(file_path: str, content: str) -> None:
    """
    Writes a string to a file.

    :param file_path: The path to the output file.
    :param content: The string content to be written.
    :raises OSError: If the file cannot be written.
    """
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def serialize_animal(animal_obj: dict) -> str:
    """
    Serializes a single animal dictionary into an HTML list item.

    :param animal_obj: A dictionary containing animal data.
    :return: An HTML formatted string representing the animal card.
    """
    output = '<li class="cards__item">\n'

    name = animal_obj.get("name")
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")

    locations = animal_obj.get("locations")
    first_location = locations[0] if locations and len(locations) > 0 else None

    animal_type = characteristics.get("type")

    # Only create the paragraph if at least one detail exists
    if diet or first_location or animal_type:
        output += '  <p class="card__text">\n'

        if diet:
            output += f"      <strong>Diet:</strong> {diet}<br/>\n"

        if first_location:
            output += f"      <strong>Location:</strong> {first_location}<br/>\n"

        if animal_type:
            output += f"      <strong>Type:</strong> {animal_type}<br/>\n"

        output += "  </p>\n"

    output += "</li>\n"

    return output


def generate_animals_string(animals_data: list) -> str:
    """
    Iterates through the animal data and generates a combined HTML string.

    :param animals_data: A list of dictionaries representing animals.
    :return: A string containing the combined HTML formatted animal information.
    """
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main() -> None:
    """
    Main entry point of the script.
    Orchestrates reading data, generating the HTML string, and writing the output file.
    Handles potential file and data parsing errors gracefully.
    """
    try:
        # 1. Load the animal data
        animals_data = load_data("animals_data.json")

        # 2. Generate the formatted HTML string
        animals_info_string = generate_animals_string(animals_data)

        # 3. Read the HTML template
        html_template = read_file("animals_template.html")

        # 4. Replace the placeholder with the generated string
        final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

        # 5. Write the final HTML content to a new file
        write_file("animals.html", final_html)
        print("Website successfully generated in 'animals.html'.")

    except FileNotFoundError as error:
        print(f"Error: Required file not found - {error.filename}")
    except json.JSONDecodeError as error:
        print(f"Error: Failed to parse JSON data. Malformed syntax at line {error.lineno}.")
    except OSError as error:
        print(f"Error: An I/O error occurred while handling files - {error.strerror}")


if __name__ == "__main__":
    main()