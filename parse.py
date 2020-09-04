"""
Parse PubMed 
@Author: Scott Campit
"""

from metapub import PubMedFetcher
import pandas as pd
import sys

fetch = PubMedFetcher()

# Get PMIDs using query
pmids = fetch.pmids_for_query(query=sys.argv[1],
                              since=None,
                              until=None,
                              retmax=1000)
print("Number of PMIDs with search query: " + str(len(pmids)))
#print("Example PMID Queried: " + str(pmids[4]))
# Get abstracts based on keyword search
abstracts = {}
for id in pmids:
    article = fetch.article_by_pmid(id)
    abstracts[id] = [article.title, article.abstract, article.journal, article.year, article.authors]
    #print(abstracts[id])
df = pd.DataFrame.from_dict(abstracts,
                            orient='index',
                            columns=['Title', 'Abstract', 'Journal', 'Year', 'Authors'])
df.index.name = 'PMID'
df.to_csv(sys.argv[2]+'.csv')
