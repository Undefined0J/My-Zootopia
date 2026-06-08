# Zootopia - Animal Web Generator

A Python-based application that dynamically fetches animal data from an external API and generates a beautifully styled, structured HTML webpage.

## Description

This project demonstrates a clean separation of concerns by splitting data retrieval and presentation logic. It fetches real-time animal information from the [API Ninjas - Animals API](https://api-ninjas.com/api/animals) and serializes the data into a responsive HTML card layout. 

Features include:
* Dynamic API integration using the `requests` library.
* Secure environment variable management for API keys via `python-dotenv`.
* Robust error handling for network timeouts, missing files, and non-existent animal queries.
* Modular architecture (`data_fetcher.py` for API calls, `animals_web_generator.py` for HTML serialization).

## Prerequisites

* Python 3.x
* An active API key from API Ninjas.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Undefined0J/My-Zootopia
2. Navigate into the project directory:
   ```bash
   cd My-Zootopia
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Create a .env file in the root directory and add your API key:
   ```bash
   API_NINJAS_KEY=your_actual_api_key_here

## Usage

1. Run the main script via the terminal:
   ```bash
   python animals_web_generator.py
2. You will be prompted to enter the name of an animal (e.g., Fox, Cheetah, Dog).
3. The script will fetch the data and generate an animals.html file in the root directory.
4. Open animals.html in any web browser to view the generated animal cards. If the animal does not exist, the HTML will display a corresponding error message.

## Have Fun!
### Best regards,   
#### Undefined0J
