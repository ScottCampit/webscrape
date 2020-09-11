# PubMed Webscraper
**Author:** Scott Campit

## Summary
This software uses the `PubMedFetcher` API (see documentation [here](https://pypi.org/project/metapub/)) for extracting a table containing useful summary data. The fields are shown in the table below:

|  |  |  |  |  |  |
|--|--|--|--|--|--|
|PMID|Article Title|Abstract|Journal|Year|Authors|

## Usage
The script that performs all of the action is the `parse.py` script. The syntax is shown below. Note that you should substitute your keyword in the <INSERT KEYWORD> argument below.

``` bash
# Syntax
python3 parse.py <INSERT KEYWORD>

# Example to query 'H3K9 acetylation'
python3 parse.py 'H3K9 acetylation'
```

To parse multiple keywords, they must be formatted into a Python list. An example is shown below:

``` bash
python3 parse.py ['Acetylation', 'Methylation', 'Cancer', 'Metabolism']
```

## Dependencies
To get started, you will need to make an account with NCBI and set up an API key. The instructions can be found [here](https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/).

**Notes**
To ensure your OS recognizes the NCBI API Key, you will need to type in the command, variable name, and API key using the following syntax. You must use `NCBI_API_KEY` as the variable name.

```bash
export NCBI_API_KEY="API KEY GOES HERE"
``` 
