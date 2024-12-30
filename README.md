# dyson-sphere-program-ita

A tool for translating the Dyson Sphere Program game into Italian or other languages.  
This tool is designed to translate the text into any configured language.  
Currently, the only completed translation is in Italian V0.1.

# How to install the mod?
1. Go to the game's Steam folder.
2. Locate the `Locale` folder inside the game directory.
3. Create a new folder called `1055`.
4. Copy the contents of `translated/it` into the `1055` folder.
5. Add this line `"1055,Italiano,itIT,it,2052,0"` in `Header.txt` under the line `"1033,English,enUS,en,2052,0"`.
6. Launch the game and change the language :D

## For Developers

### Set up the environment
```bash
python3 -m venv venv
```

#### Activate the environment on Mac
```bash
source venv/bin/activate
```

#### Activate the environment on Windows
```bash
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure
```
DYSON-SPHERE-PROGRAM-ITA/
├── original/
│       ├── base.txt
│       └── ...
├── translated/
│   └── it/
│       ├── base.txt
│       └── ...
├── venv/
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Running the project
1. Place the files to be translated in the `original/` folder.
2. Activate the virtual environment:
   - **Mac/Linux**: `source venv/bin/activate`
   - **Windows**: `venv\Scripts\activate`
3. Install the dependencies with `pip install -r requirements.txt`.
4. Run the `make` script to create files:
   ```bash
   python make.py
   ```
5. Run the `update` script to update the tests:
   ```bash
   python update.py
   ```
6. Translated files will be saved in the `translated/it/` directory.

## Additional Notes
- **Configuration files**: Use the `.env` file for specific configurations.
- **License**: This project is licensed under the Apache 2.0 license.

## Contributions
Contributions are welcome! Open an `issue` or submit a `pull request` for improvements or fixes.
