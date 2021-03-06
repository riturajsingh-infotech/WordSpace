# ###################################################
# Explore the direct inked entities between keywords
# Here direct linked entities states the one edge link
# between the two set of Keywords
# Input : Two keywords
# Output : Set of Linked Edges between the two keywords
#          The linked edges are the properties between the
#          two keywords.
# @ Author : Rituraj Singh
#            rituraj.singh@irisa.fr
# Created Time : 18 July 2018, 17 : 45 (GMT + 2)
#         At: INRIA/IRISA, Rennes, France
####################################################
from SPARQLWrapper import SPARQLWrapper, JSON
import numpy as np
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

#print(query_str)
#Q1 : dbpedia:India dcterms:subject ?super
#q2 : dbpedia:New_Delhi rdf:type ?super
#q4 : dbpedia:New_Delhi (owl:sameAs|^owl:sameAs)* ?super
#q3 : dbpedia:Hindi ?super dbpedia:India
#q5: dbpedia: """ +first_keyword + """ ?super dbpedia: """ + Second_keyword + """

def planet_link(planet_one, planet_two):
    query_str = """
        PREFIX dbpedia: <http://dbpedia.org/resource/>
        select distinct ?super 
        where 
        {
            dbpedia:""" + planet_one + """ ?super dbpedia:""" + planet_two + """
        }"""
    sparql.setQuery(query_str);
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    # print(results);
    my_key = [];
    for result in results['results']['bindings']:
        #   print(result['super']['value'])
        my_key.append(result['super']['value'])

    my_keywords = np.array(my_key)
    return my_keywords;


