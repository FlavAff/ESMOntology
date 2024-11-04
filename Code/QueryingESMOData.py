from owlready2 import *

# Load the ontology from a file (you can also load from a URL)
onto = get_ontology("ESMOdata.rdf").load()

# Optional: Run the reasoner to infer new relationships
with onto:
    sync_reasoner()  # This uses the HermiT reasoner by default


## CQ: What was the economic value of chinook salmon provisioning in 2002?
# Access the class Wholesale_value
wholesale_value_class = onto.search_one(iri="*Wholesale_value")

# Check if the class exists
if wholesale_value_class:
    # Query for instances of Wholesale_value
    instances = list(wholesale_value_class.instances())
    
    # Check if there are any instances
    if instances:
        print(f"Found {len(instances)} instances of Wholesale_value:")
        
        # Initialize a variable to hold the desired instance
        target_instance = None
        
        # Iterate through instances to find the one with hasYear = 2002
        for instance in instances:
            year_values = getattr(instance, 'hasYear', None)
            if year_values is not None:
                # Check if year_values is a list and iterate through it
                if isinstance(year_values, IndividualValueList):
                    for year_value in year_values:
                        try:
                            float_year_value = float(year_value)
                            if float_year_value == 2002:
                                target_instance = instance
                                break  # Exit the loop once the target is found
                        except ValueError:
                            continue
                else:
                    # Handle case where it's a single value
                    try:
                        float_year_value = float(year_values)
                        if float_year_value == 2002:
                            target_instance = instance
                            break
                    except ValueError:
                        continue

        # Check if the target instance was found
        if target_instance:
            print(f"Target instance found: {target_instance.name}")
            # Now retrieve the hasWholesaleValue property
            wholesale_values = getattr(target_instance, 'hasWholesaleValue', None)

            # Check if the hasWholesaleValue property is defined
            if wholesale_values is not None:
                # Print the wholesale value(s)
                if isinstance(wholesale_values, IndividualValueList):
                    for value in wholesale_values:
                        try:
                            print(f"  hasWholesaleValue = {float(value)}")
                        except ValueError:
                            print(f"  hasWholesaleValue value is not a number: {value}")
                else:
                    try:
                        print(f"  hasWholesaleValue = {float(wholesale_values)}")
                    except ValueError:
                        print(f"  hasWholesaleValue value is not a number: {wholesale_values}")
            else:
                print("  hasWholesaleValue property is not defined for this instance.")
        else:
            print("No instance of Wholesale_value with hasYear = 2002 was found.")
    else:
        print("No instances of Wholesale_value were found.")
else:
    print("The class `Wholesale_value` was not found.")


## CQ: How many times was chinook catch higher than 100000 units?
# Access the class Wildcaught_fish
wildcaught_fish_class = onto.search_one(iri="*Wildcaught_fish")

# Check if the class exists
if wildcaught_fish_class:
    # Query for instances of Wildcaught_fish
    instances = list(wildcaught_fish_class.instances())
    
    # Check if there are any instances
    if instances:
        print(f"Found {len(instances)} instances of Wildcaught_fish:")
        
        # Initialize a counter for hasCount over 100000
        count_over_100000 = 0
        
        # Iterate through instances and print their properties
        for instance in instances:
            print(f"Instance: {instance.name}")
            # Attempt to get the hasCount property
            catch_values = getattr(instance, 'hasCount', None)

            # Check if the hasCount property is defined and not None
            if catch_values is not None:
                # Ensure catch_values is a list and iterate through it
                if isinstance(catch_values, IndividualValueList):
                    for value in catch_values:
                        try:
                            float_value = float(value)
                            print(f"  hasCount = {float_value}")
                            # Check if the catch value is over 100000
                            if float_value > 100000:
                                count_over_100000 += 1
                                print(f"  hasCount is over 100000: {float_value}")
                        except ValueError:
                            print(f"  hasCount value is not a number: {value}")
                else:
                    # Handle case where it's a single value
                    try:
                        float_value = float(catch_values)
                        print(f"  hasCount = {float_value}")
                        if float_value > 100000:
                            count_over_100000 += 1
                            print(f"  hasCount is over 100000: {float_value}")
                    except ValueError:
                        print(f"  hasCount value is not a number: {catch_values}")
            else:
                print("  hasCount property is not defined for this instance.")
        
        # Print the total count of hasCount values over 100000
        print(f"\nTotal number of times hasCount was over 100000: {count_over_100000}")
    else:
        print("No instances of Wildcaught_fish were found.")
else:
    print("The class `Wildcaught_fish` was not found.")



## CQ: What was the measure of EESV ecological supply for water quality regulation in 2020?
# Access the class Clean_freshwater
clean_freshwater_class = onto.search_one(iri="*Clean_freshwater")

# Check if the class exists
if clean_freshwater_class:
    # Query for instances of Clean_freshwater
    instances = list(clean_freshwater_class.instances())
    
    # Check if there are any instances
    if instances:
        print(f"Found {len(instances)} instances of Clean_freshwater:")
        
        # Initialize a variable to hold the desired instance
        target_instance = None
        
        # Iterate through instances to find the one with hasYear = 2020
        for instance in instances:
            year_values = getattr(instance, 'hasYear', None)
            if year_values is not None:
                # Check if year_values is a list and iterate through it
                if isinstance(year_values, IndividualValueList):
                    for year_value in year_values:
                        try:
                            float_year_value = float(year_value)
                            if float_year_value == 2020:
                                target_instance = instance
                                break  # Exit the loop once the target is found
                        except ValueError:
                            continue
                else:
                    # Handle case where it's a single value
                    try:
                        float_year_value = float(year_values)
                        if float_year_value == 2020:
                            target_instance = instance
                            break
                    except ValueError:
                        continue

        # Check if the target instance was found
        if target_instance:
            print(f"Target instance found: {target_instance.name}")
            # Now retrieve the hasConcentration property
            concentration_values = getattr(target_instance, 'hasConcentration', None)

            # Check if the hasConcentration property is defined
            if concentration_values is not None:
                # Print the concentration value(s)
                if isinstance(concentration_values, IndividualValueList):
                    for value in concentration_values:
                        try:
                            print(f"  hasConcentration = {float(value)}")
                        except ValueError:
                            print(f"  hasConcentration value is not a number: {value}")
                else:
                    try:
                        print(f"  hasConcentration = {float(concentration_values)}")
                    except ValueError:
                        print(f"  hasConcentration value is not a number: {concentration_values}")
            else:
                print("  hasConcentration property is not defined for this instance.")
        else:
            print("No instance of Clean_freshwater with hasYear = 2020 was found.")
    else:
        print("No instances of Clean_freshwater were found.")
else:
    print("The class `Clean_freshwater` was not found.")


## CQ: When did commercial fishers earn more than 20 million from wholesale?
# Access the class Wholesale_value
wholesale_value_class = onto.search_one(iri="*Wholesale_value")

# Check if the class exists
if wholesale_value_class:
    # Query for instances of Wholesale_value
    instances = list(wholesale_value_class.instances())

    # Initialize a variable to keep track of results
    results = []

    # Iterate through instances to check for hasWholesaleValue > 20
    for instance in instances:
        wholesale_values = getattr(instance, 'hasWholesaleValue', None)
        if wholesale_values is not None:
            # Check if wholesale_values is a list and iterate through it
            if isinstance(wholesale_values, IndividualValueList):
                for value in wholesale_values:
                    try:
                        if float(value) > 20:
                            # Get the hasYear property for this instance
                            year_values = getattr(instance, 'hasYear', None)
                            if year_values is not None:
                                # Collect the year values
                                if isinstance(year_values, IndividualValueList):
                                    for year in year_values:
                                        results.append(year)
                                else:
                                    results.append(year_values)  # Single value case
                    except ValueError:
                        continue
            else:
                # Handle case where it's a single value
                try:
                    if float(wholesale_values) > 20:
                        # Get the hasYear property for this instance
                        year_values = getattr(instance, 'hasYear', None)
                        if year_values is not None:
                            results.append(year_values)
                except ValueError:
                    continue

    # Output results
    if results:
        print("Years of instances of Wholesale_value where hasWholesaleValue > 5:")
        for year in results:
            print(year)
    else:
        print("No instances of Wholesale_value found with hasWholesaleValue > 5.")
else:
    print("The class `Wholesale_value` was not found.")

## CQ: In what years was the measure of EESV anthropogenic contribution for chinook salmon provisioning higher than 3000 but less than 4000?
# Access the class Fishing_fleet
fishing_fleet_class = onto.search_one(iri="*Fishing_fleet")

# Check if the class exists
if fishing_fleet_class:
    # Query for instances of Fishing_fleet
    instances = list(fishing_fleet_class.instances())

    # Initialize a variable to keep track of results
    results = []

    # Iterate through instances to check for hasCount > 3000 and < 4000
    for instance in instances:
        count_value = getattr(instance, 'hasCount', None)
        if count_value is not None:
            # Check if count_value is a list and iterate through it
            if isinstance(count_value, IndividualValueList):
                for value in count_value:
                    try:
                        if 3000 < float(value) < 4000:
                            # Get the hasYear property for this instance
                            year_values = getattr(instance, 'hasYear', None)
                            if year_values is not None:
                                # Collect the year values
                                if isinstance(year_values, IndividualValueList):
                                    for year in year_values:
                                        results.append(year)
                                else:
                                    results.append(year_values)  # Single value case
                    except ValueError:
                        continue
            else:
                # Handle case where it's a single value
                try:
                    if 3000 < float(count_value) < 4000:
                        # Get the hasYear property for this instance
                        year_values = getattr(instance, 'hasYear', None)
                        if year_values is not None:
                            results.append(year_values)
                except ValueError:
                    continue

    # Output results
    if results:
        print("Years of instances of Fishing_fleet where hasCount > 3000 and < 4000:")
        for year in results:
            print(year)
    else:
        print("No instances of Fishing_fleet found with hasCount > 3000 and < 4000.")
else:
    print("The class `Fishing_fleet` was not found.")


# CQ: How many killer whales were there in 2003, 2008 and 2012?
# Find the Whale_population class in the ontology
whale_population_class = onto.search_one(iri="*Whale_population")

# Years of interest
target_years = {2003, 2008, 2017}

# Dictionary to store abundance values by year
abundance_by_year = {year: [] for year in target_years}

# Iterate through instances of Whale_population
for instance in whale_population_class.instances():
    # Retrieve the values for hasYear and hasAbundance for each instance
    year = getattr(instance, "hasYear", [None])[0]
    abundance = getattr(instance, "hasAbundance", [None])[0]
    
    # Check if the year is one of the target years
    if year in target_years:
        abundance_by_year[year].append(abundance)

# Output the results
for year, abundances in abundance_by_year.items():
    print(f"Abundance values for the year {year}: {abundances if abundances else 'No data found'}")
