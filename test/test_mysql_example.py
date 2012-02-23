# # -*- coding: utf-8 -*-

# import rdflib
# from rdflib.graph import ConjunctiveGraph
# from rdflib import plugin
# from rdflib.store import Store, VALID_STORE
# from rdflib import URIRef

# rdflib.plugin.register('MySQL', Store,'rdflib_mysql.MySQL', 'MySQL')
# default_graph_uri = "http://example.com/rdfstore"
# configString = "host=localhost,user=gjh,password=50uthf0rk,db=test"

# # Get the mysql plugin. You may have to install the python mysql libraries
# store = plugin.get('MySQL', Store)('rdfstore')

# def test():
#     # Attempt to open previously created store
#     rt = store.open(configString, create=False)
#     if rt == 0:
#         # There is no underlying MySQL infrastructure, create it
#         store.open(configString,create=True)
#     else:
#         assert rt == VALID_STORE, "There underlying store is corrupted"
#     # create a graph, with the opened store bound at constructor arg
#     graph = ConjunctiveGraph(store, identifier = URIRef(default_graph_uri))

#     # Bind some namespaces
#     graph.bind("dc", "http://http://purl.org/dc/elements/1.1/")
#     graph.bind("foaf", "http://xmlns.com/foaf/0.1/")
#     graph.bind("fb", "http://rdf.freebase.com/ns/")

#     graph.parse("http://rdf.freebase.com/rdf/en.nikola_tesla", format="xml")
#     graph.parse("http://rdf.freebase.com/rdf/en.johann_wolfgang_goethe", format="xml")
#     # Add the information into the database
#     graph.commit()

#     assert len(graph.serialize(format="nt")) > 12, graph.serialize(format="nt")

# if __name__ == '__main__':
#     test()

