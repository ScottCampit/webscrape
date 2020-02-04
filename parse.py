"""

"""

from metapub import PubMedFetcher

fetch = PubMedFetch()

pmids = getch.pmids_for_query(query='13C glucose flux histone PTM metabolism',
                              since=None,
                              until=None,
                              retmax=1000)

print(pmids)
