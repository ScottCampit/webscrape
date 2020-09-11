"""
parse.py contains functions to help query PubMed programmically. 

UPDATES 09/11/2020:
  * Created `keyword_query` function to encapsulate the keyword search function
  * Updated some inline comments and variable names to make code more readable

@author: Scott Campit
"""

from metapub import PubMedFetcher
import pandas as pd
import sys

def keyword_query(keywords=sys.argv[1], savepath=sys.argv[2],
	              start_date=None, end_date=None, 
	              num_of_articles=1000):
	"""
	keyword_query takes in a keyword string or list of keywords, and outputs 
	PMIDs that have a match of those keywords.

	:param keywords:         A string or a list of keywords to query.
	:param savepath:         A string denoting the full path to save the file in.
	:param start_date:       A string denoting the start date.
	:param end_date:         A string denoting the end date.
	:param num_of_articles:  An integer denoting the maximum number of articles.

	:return df:              A pandas dataframe of the query.
	"""
	
	fetch = PubMedFetcher()

	# Get PMIDs using query
	pmids = fetch.pmids_for_query(query=keywords,
	                              since=start_date,
	                              until=end_date,
	                              retmax=num_of_articles)
	print("Number of PMIDs with search query: " + str(len(pmids)))

	# Get abstracts based on keyword search. 
	# The query saves to a dictionary, using the PMID as the key.
	abstracts = {}
	for id in pmids:
	    article = fetch.article_by_pmid(id)
	    abstracts[id] = [article.title, article.abstract, 
	                     article.journal, article.year, 
	                     article.authors]

	# Save the dictionary as a dataframe   
	df = pd.DataFrame.from_dict(abstracts,
	                            orient='index',
	                            columns=['Title', 'Abstract', 
	                                     'Journal', 'Year', 
	                                     'Authors'])

	# Save the dataframe
	df.index.name = 'PMID'
	df.to_csv(savepath)

	return df

if __name__ == "__main__":
	keyword_query(keywords=sys.argv[1], savepath=sys.argv[2])
