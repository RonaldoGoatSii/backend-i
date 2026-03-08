# Contact Manager CLI

## Purpose
The **Contact Manager CLI** is a modular Python utility designed to bridge the gap between structured data and human-readable documentation. It solves the problem of local contact management by providing:
* **Data Redundancy**: Saving detailed contact information into individual Markdown files for easy previewing in any text editor.
* **Search Optimization**: Maintaining a centralized JSON index to allow instantaneous searches without parsing multiple files.
* **Input Validation**: Ensuring data integrity by strictly enforcing numeric-only phone numbers and alphabetic-only names.

**Tutorial**
Commands:
```bash
mkdir contacts
cd contacts
git init
uv venv
source .venv/bin/activate
uv pip install typer
mkdir -p app
touch app/__init__.py

## Project Structure
The application follows a strict three-layer architecture to ensure maintainability and clear separation of concerns:

* **CLI Layer (`src/main.py`)**: Handles user interaction, command-line arguments, and output formatting using the `typer` library.
* **Logic Layer (`src/services/numbers.py`)**: Contains business rules, specifically the validation logic for names and phone numbers.
* **Data Layer (`src/services/database.py`)**: Manages the persistence of data, handling both the file system (Markdown) and the search index (JSON).

## Installation
This project uses `uv` for modern, fast dependency management.

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd backend-i