# Game Collection App

A command-line application for managing a personal video game library with persistent storage.

This project is a Python-based CLI application that allows users to create, view, update, and delete entries in a personal game collection. Data is stored locally in JSON format to support persistence between sessions. I built this to strengthen my understanding of object-oriented design, CRUD systems, and persistent data storage in Python. This project was developed and tested using Bash in the Windows Subsystem for Linux (WSL) environment.

## Features

The application supports the following functionality:

- You can add new games with details such as title, platform, completion status, rating, and playtime
- View and search games in alphabetical order
- Edit existing game information
- Remove games from the collection
- Persistent storage using JSON files
- Input validation and error handling
- Automated unit tests with Pytest

## Tech Stack

- Python
- Pytest (unit testing)
- JSON (data persistence)

## Installation
(Commands below use Bash for Unix/Linux-based systems, including WSL)

1. Clone this repository into your desired directory:
   
   ```bash
   git clone https://github.com/NathanSchreiber/game-collection-app.git
   ```
   
2. Navigate to the project directory:
   
   ```bash
   cd game-collection-app
   ```
   
3. Create and activate a virtual environment:
   
  ```bash
   python3 -m venv env
   source env/bin/activate
  ```

4. Install dependencies:
 
   ```bash
   pip3 install -r requirements.txt
   ```
   
## How to run

Run the application from the project root:

```bash
python3 main.py
```

Follow the on-screen prompts to add, search, update, or remove games.

## Testing

Run the full test suite:

```bash
pytest
```

Run an individual test file:

```bash
pytest tests/test_main.py
```

## Project Structure

```
main.py
data.json
src/
  game.py     # Game object
  library.py  # Collection logic
  storage.py  # JSON persistence
tests/
  test_main.py
  test_library.py
  test_storage.py
```

## What I Learned

- Designing object-oriented systems in Python
- Implementing JSON-based data persistence
- Implementing CRUD functionality
- Writing automated tests using pytest
- Structuring multi-file Python applications

## Future Improvements

- Add a database (likely SQLite)
- Add filtering and sorting data with more precise control
- Add a GUI
