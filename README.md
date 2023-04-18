
# Dataset Converter

This project allows users to convert datasets between csv, parquet and xlsx formats.

# Website

You can access the website through here: https://datasetconverter.streamlit.app/

# Supported Extensions

- xlsx
- csv
- parquet


# Env File

Env file contains relevant extension data. You must create a .env file in order to use the project. And your `.env` file content should look like this:

```bash
ALLOWED_FILE_EXTENSIONS="csv,xlsx,parquet"
DEFAULT_FROM_FILE_EXTENSION="csv"
DEFAULT_TO_FILE_EXTENSION="parquet"
```

- `ALLOWED_FILE_EXTENSIONS` is the extensions that is being allowed to conversion
- `DEFAULT_FROM_FILE_EXTENSION` is the extension type that will be selected when the program is started or auto-selected when the same type has chosen for input and output extensions
- `DEFAULT_TO_FILE_EXTENSION` is the extension type that will be selected when the program is started or auto-selected when the same type has chosen for input and output extensions

# Support

You can always open a Pull Request or an issue when you see the opportunity of improving the project. Every help and advice will be welcomed.

