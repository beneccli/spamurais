# Spamurais

## How to install

1. Install ollama: https://ollama.com
2. Start Ollama server: `ollama serve`
3. Install python and pip if not done yet
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment: `source venv/bin/activate` (linux) or `venv\Scripts\activate` (windows)
6. Install dependencies: `pip install -r requirements.txt`

Notes:
- If you get an error during pip install, try install setuptools: `pip install --upgrade setuptools`
- If you get any error during the run of the script, try adding this module: `pip install "nomic[local]"`
- Current setup has been tested with python 3.12.2 and pip 24.3.1

## How to run

Execute command: `python run.py`
