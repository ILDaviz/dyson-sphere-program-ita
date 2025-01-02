# Dyson sphere program translation tool!

A tool for translating the Dyson Sphere Program game into Italian or other languages.  
This tool is designed to translate the text into any configured language.  
Currently, the only completed translation is in Italian

- Italian V0.2 Alpha

# How to install the mod?
1. Go to the game's Steam folder.
2. Locate the `Locale` folder inside the game directory.
3. Inside `Locale` create a new folder called `1055`.
4. Copy the contents of `translated/it` into the `1055` folder (remove demo.txt).
5. Add this line `"1055,Italiano,itIT,it,2052,0"` in `Header.txt` under the line `"1033,English,enUS,en,2052,0"`.
6. Launch the game and change the language :D
7. If you find any translation errors, open an issue report or update the file yourself and request a merge request.

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
5. Run the `update` script to update the tests: TODO!
   ```bash
   python update.py
   ```
6. Translated files will be saved in the `translated/it/` directory.

## Additional Notes
- **Configuration files**: Use the `.env` file for specific configurations.
- **License**: This project is licensed under the Apache 2.0 license.

## Contributions
Contributions are welcome! Open an `issue` or submit a `pull request` for improvements or fixes.

## Disclaimer

This tool is an **open-source** project developed independently to translate the texts of the video game **Dyson Sphere Program**. This project is **not affiliated with**, **supported by**, or **approved by** **Youthcat Studio** or **Gamera Games**.

All rights related to the video game and its content are owned by their respective rights holders. The use of this tool is entirely at the user's discretion and risk. We provide no **warranties** regarding the accuracy, completeness, or functionality of the generated translations.

This project is created exclusively for **non-commercial** purposes and aims to enhance the gaming experience for the Italian-speaking community or other language communities. Any misuse, unauthorized distribution, or violation of the original video game's terms of service is solely the responsibility of the user.

Please always respect the **terms of use** and **policies** established by the video game developer. For more information or clarification, it is recommended to consult the official resources provided directly by **Youthcat Studio** or **Gamera Games**.