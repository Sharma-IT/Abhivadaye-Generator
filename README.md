# Abhivādaye Generator

A Python script that generates the traditional abhivādaye, a salutation used in Brahmin culture, in either Sanskrit or English formats.. This script provides the capability to generate abhivādaye salutations based on user inputs for names of prāvāra, sūtrakāra, vedaśākhā, and name. The generated salutations are saved to a text file.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Note](#note)
- [Disclaimer](#disclaimer)
- [Contact](#contact)
- [License](#license)

## Description

The abhivādaye is a traditional and Vedic salutation used by Hindu men but mainly Brahmin men, that includes information about the prāvāra, gotra, sūtra, vedaśākhā and name of the Brahmin. This script prompts the user to input the relevant information and then generates the abhivādaye in either Sanskrit or English-to-Sanskrit transliteration formats.

## Features

- Generate abhivādaye salutations in both Sanskrit and English.
- Save the generated abhivādaye to a text file.
- Load previously generated abhivādaye.

## Prerequisites

- Python 3.x installed.

## Usage

1. Clone the repository to your local machine:

```sh
git clone https://github.com/Sharma-IT/abhivadaye-generator.git
```

2. Navigate to the repository's directory:

```sh
cd abhivadaye-generator
```

3. Run the script:

```sh
python abhivadaye_generator.py
```

4. Choose an option from the menu:

- **Generate abhivādaye**: Input details and generate abhivādaye salutations.
- **Load and abhivādaye**: Load previously saved abhivādaye from a file.
- **Exit**: Terminate the program.

5. If you choose to generate an abhivādaye:
   
- Select 'S' for Sanskrit or 'E' for English.
- Input names of prāvāra, gotra, sūtrakāra, vedaśākhā, and your name.

6. The generated abhivādaye will be displayed on the console and saved to a text file named `abhivādaye_output.txt`.

7. If you choose to load an abhivādaye, it will load the last previously generated abhivādaye, and will print out the contents of the file (i.e. the abhivādaye) onto the console.

## Note

- Devanāgarī characters may not display correctly in some terminals. Consider copying and pasting the output into a text editor with Unicode support.

## Disclaimer

This script is intended to assist Brahmins interested in properly formulating the traditional abhivādaye salutation. Users should ensure they have received appropriate learning in this ritual etiquette (karma-ācāra) from their family, community or guru.

When using this tool, users must be fully aware of the precise details of their own lineage (vamśa-viśeṣa) including prāvāra, gotra, sūtrakāra and vedaśākhā. They are responsible for verifying the accuracy of these details before generating an abhivādaye.

This script is intended as an educational tool to assist Hindus and Brahmins interested in learning more about their heritage and traditions. I am proud of my heritage and I share this script in the spirit of promoting cultural awareness. Any harassment or defamation towards me will go against this spirit, and will not be tolerated.

## Contact

Shubham Sharma - [My LinkedIn](https://www.linkedin.com/in/sharma-it/) - shubhamsharma.emails@gmail.com.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details.
