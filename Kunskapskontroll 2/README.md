# Match this weeks offers with your own recipies

Consider that you do not wish to put time into planning your weekly grocery shoping. Instead, you are just fine with cooking with the same recipies. Wouldn't it be nice to match the offers at your local store with these recipies? This project gives an outline of how to code this tedious task.

This project constists of the following data pipeline:
1. loading data using API
2. Parsing and cleaning of data
3. Store offers in a table
4. Retrieve offers matching your recipies.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation
Installing libraries and modules are done using the 'pip install {package}' command.

## Usage
The code is primarily in english but there are some entries in swedish. This is because offers are given in swedish stores.
The required info given by you (the user) are:
1. You will need to specify a dictionary with recipies close to your heart in the form:
{
'pasta carbonara': ['ägg', 'pasta', 'bacon', 'parmesan', 'persilja', 'grädde'],

'köttbullar m. potatis': ['köttbullar', 'potatis', 'brunsås', 'lingonsylt'],
}

2. Locate your "store name" at https://ereklamblad.se/. Register on this site to recover an api-key.

The dictionary and key are inserted into recipe_matcher.py and fetch_key.py respectively. The "store name" goes into the main_with_recipies.py. 

## Contributing
Have ideas for further development or find room for improvements? Please open an issue or a pull request, I will be happy to hear from you!

## Authors
- Filip Holmberg - [GitHub Profile](https://github.com/FilipHolmbrg)
