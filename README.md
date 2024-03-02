# Invoices Generator

This is a simple Python script that generates a Word document (docx) using the `docxtpl` library. The script reads data from a text file (`myInfo.txt`) and prompts the user to input additional information. The generated document is saved in the `Generated` directory.

## Requirements

To run this script, you need to have the following Python libraries installed:

- `docxtpl`
- `python-docx`
- `python-docx-template`

You can install these libraries using pip:

```bash
pip install docxtpl python-docx python-docx-template
```

## Usage

1. Run the script:

```bash
python main.py
```

2. Follow the prompts to input the required information.

3. The generated document will be saved in the `Generated` directory.

## Structure

The script is divided into two main parts:

1. `main.py`: This is the main script that reads data from the text file, prompts the user to input additional information, and generates the Word document.
2. `readFromText.py`: This script reads data from the text file and stores it in a dictionary.

## Data

The data for the document is read from the `myInfo.txt` file. The file should be in the following format:

```
NAME=NewGen Sarl
ADDRESS=Belveder Rue N4
IF =64970210
TP =32667126
RC=640234
ICE =003235449300095
ZIP =20672
PHONE =+212 660 80 50 30
EMAIL =contact@example.ma
WEBSITE=www.example.ma
```

Each line should be in the format `KEY=VALUE`. The script will read the file and store the data in a dictionary.

## TODO

- Generate Pdf formats
- Logo and Digital signature
- Products details
- Host and back up the generated documents
- Activate switching languages
- Increment the invoices number
- Friendly UI instead of a CLI

Advanced milestones:

- Gathering the data and analyze it
- List the winning products
- Connect to a printers and print documents directly
