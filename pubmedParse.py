"""

"""

from Bio import Entrez
import requests
Entrez.email = "scampit@umich.edu"
entrezURL = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

def search(query):
    """
    """

    handle = Entrez.esearch(
        db='pubmed',
        sort='relevance',
        retmode='xml',
        term=query)
    results = Entrez.read(handle)
    return results


