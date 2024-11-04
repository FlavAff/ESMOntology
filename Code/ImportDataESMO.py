import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF

# Load ontology
g = Graph()
g.parse("ESMO.rdf", format="xml")

# Define namespaces
EX = Namespace("http://purl.obolibrary.org/obo/esmo.owl#")

# Read the CSV file
dataFish = pd.read_csv('/Users/flavio/Documents/McGill/PhD/Chapter 1/Data/ChinookDatOnto.csv')
dataWater = pd.read_csv('/Users/flavio/Documents/McGill/PhD/Chapter 1/Data/WQInstances.csv')
dataOrca = pd.read_csv('/Users/flavio/Documents/McGill/PhD/Chapter 1/Data/OrcaInstances.csv')

# Iterate through the rows in the CSV for water
for index, row in dataWater.iterrows():
    # Create URIs for wildcaught_fish and wholesale_value instances
    water_instance_uri = URIRef(EX[row['Water']])
    
    # Add triples for wildcaught_fish
    g.add((water_instance_uri, RDF.type, EX.Clean_freshwater))
    g.add((water_instance_uri, EX.hasConcentration, Literal(row['TotalP'])))
    g.add((water_instance_uri, EX.hasYear, Literal(row['Year'])))


# Iterate through the rows in the CSV for fish
for index, row in dataFish.iterrows():
    # Create URIs for wildcaught_fish and wholesale_value instances
    fish_instance_uri = URIRef(EX[row['Fish_population']])
    catch_instance_uri = URIRef(EX[row['Wildcaugh_fish']])
    fleet_instance_uri = URIRef(EX[row['Fishing_fleet']])
    value_instance_uri = URIRef(EX[row['Wholesale_value']])
    
    # Add triples for fish_population
    g.add((fish_instance_uri, RDF.type, EX.Fish_population))
    g.add((fish_instance_uri, EX.hasAbundance, Literal(row['Abundance'])))
    g.add((fish_instance_uri, EX.hasYear, Literal(row['Year'])))

    # Add triples for wildcaught_fish
    g.add((catch_instance_uri, RDF.type, EX.Wildcaught_fish))
    g.add((catch_instance_uri, EX.hasCount, Literal(row['Catch'])))
    g.add((catch_instance_uri, EX.hasYear, Literal(row['Year'])))

    # Add triples for fishing_fleet
    g.add((fleet_instance_uri, RDF.type, EX.Fishing_fleet))
    g.add((fleet_instance_uri, EX.hasCount, Literal(row['Vessel'])))
    g.add((fleet_instance_uri, EX.hasYear, Literal(row['Year'])))

    # Add triples for wholesale_value
    g.add((value_instance_uri, RDF.type, EX.Wholesale_value))
    g.add((value_instance_uri, EX.hasWholesaleValue, Literal(row['Wholesale'])))
    g.add((value_instance_uri, EX.hasYear, Literal(row['Year'])))
    
    # Link the wildcaught_fish to wholesale_value
    g.add((catch_instance_uri, EX.has_quality, value_instance_uri))


# Iterate through the rows in the CSV for orca
for index, row in dataOrca.iterrows():
    # Create URIs for wildcaught_fish and wholesale_value instances
    orca_instance_uri = URIRef(EX[row['Whales']])
    
    # Add triples for wildcaught_fish
    g.add((orca_instance_uri, RDF.type, EX.Whale_population))
    g.add((orca_instance_uri, EX.hasAbundance, Literal(row['Abundance'])))
    g.add((orca_instance_uri, EX.hasYear, Literal(row['Year'])))



# Save the updated ontology
g.serialize(destination='updated_ontology.owl', format='xml')
