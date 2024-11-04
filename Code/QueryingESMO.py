from owlready2 import *

# Load the ontology from a file (you can also load from a URL)
onto = get_ontology("ESMO.rdf").load()

# Optional: Run the reasoner to infer new relationships
with onto:
    sync_reasoner()  # This uses the HermiT reasoner by default

## CQ: What do ecosystem processes output?
# Access the classes and object property
ecosystem_process_class = onto.search_one(iri="*Ecosystem_process")
has_output_property = onto.search_one(iri="*has_output")

# Querying for the outputs of the `Ecosystem_process` class itself
if has_output_property:
    # Check if the class itself has any output property restrictions
    for restriction in ecosystem_process_class.is_a:
        if isinstance(restriction, Restriction) and restriction.property == has_output_property:
            # Print the class that is the output of `ecosystem_process_class`
            print(f"Class {ecosystem_process_class} has output class {restriction.value}")
else:
    print("The property `bfo:has_output` was not found.")


## CQ: What value does an ecosystem have?
# Access the classes and object property
ecosystem_class = onto.search_one(iri="*Ecosystem")
has_quality_property = onto.search_one(iri="*has_quality")
value_class = onto.search_one(iri="*#Value")

# Querying for the outputs of the `Ecosystem_process` class itself
if has_quality_property:
    # Check if the class itself has any output property restrictions
    for restriction in ecosystem_class.is_a:
        if isinstance(restriction, Restriction) and restriction.property == has_quality_property:
            output_class = restriction.value
            # Check if the output class is a subclass of `Value`
            if value_class in output_class.ancestors():
                print(f"Class {ecosystem_class.name} has value {output_class.name}")
            else:
                print(f"Class {output_class.name} is not a subclass of `Value`.")
else:
    print("Either `has_quality` property or `Value` class was not found.")


## CQ: What ES does the epipelagic ocean provide?
# Access the Epipelagic_ocean class
Epipelagic_ocean = onto.search_one(iri="*Epipelagic_ocean")

# Find the classes in the environs of Epipelagic_ocean
environ_classes = Epipelagic_ocean.BFO_0000183
# Find services realized by these classes
realized_services = set()
for env_class in environ_classes:
    if hasattr(env_class, 'BFO_0000055'):
        realized_services.update(env_class.BFO_0000055)

# Print results
for service in realized_services:
    print(service.name)


## CQ: What type of ecosystem service is water quality regulation?
# Retrieve the Water_quality_regulation_service class
water_quality_regulation_service_class = onto.search_one(iri="*Water_quality_regulation_service")

# Retrieve and print the superclasses
if water_quality_regulation_service_class:
    for superclass in water_quality_regulation_service_class.is_a:
        # Check if the superclass is a class
        if isinstance(superclass, owlready2.entity.EntityClass):
            print(superclass.name)
else:
    print("Class Water_quality_regulation_service not found.")


## CQ: What are the benefits of wild fish provisioning services for commercial fishers?
# Access the classes and object property
commercial_fisher_class = onto.search_one(iri="*Commercial_fisher")
benefits_from_property = onto.search_one(iri="*benefits_from")

#checks what is commercial fisher benefits from
if benefits_from_property:
    # Check if the class itself has any output property restrictions
    for restriction in commercial_fisher_class.is_a:
        if isinstance(restriction, Restriction) and restriction.property == benefits_from_property:
            # Print the class that is the output of `commercial_fisher_class`
            print(f"Class {commercial_fisher_class} benefits from class {restriction.value}")
else:
    print("The property `esmo:benefits_from` was not found.")



## CQ: What ecosystem good does whale watching depend on?
# Access the classes
whale_watching_class = onto.search_one(iri="*Whale_watching")
ecosystem_good_aggregate_class = onto.search_one(iri="*Ecosystem_good_aggregate")

# Check if the property 'participates_in' exists
participates_in_property = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000056")

# Function to find subclasses of a given class
def get_subclasses(base_class):
    return [cls for cls in onto.classes() if base_class in cls.ancestors()]

# Find subclasses of Ecosystem_good_aggregate
subclasses = get_subclasses(ecosystem_good_aggregate_class)

# Find subclasses that participate in Whale_watching
participating_subclasses = []
if participates_in_property and whale_watching_class:
    for subclass in subclasses:
        # Check if the subclass has any restrictions involving the participates_in property
        for restriction in subclass.is_a:
            if isinstance(restriction, Restriction) and restriction.property == participates_in_property:
                if restriction.value == whale_watching_class:
                    participating_subclasses.append(subclass)

# Output results
if participating_subclasses:
    print(f"Subclasses of Ecosystem_good_aggregate that participate in Whale_watching:")
    for participating_class in participating_subclasses:
        print(participating_class.name)
else:
    print(f"No subclasses of Ecosystem_good_aggregate participate in Whale_watching.")



## CQ: What ecosystem functions realise provisioning ecosystem services?
# Access the necessary classes and properties
provisioning_service_class = onto.search_one(iri="*Provisioning_ecosystem_service")
has_realisation_property = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000054")
ecosystem_function_class = onto.search_one(iri="*Ecosystem_function")

# Initialize the list to store the results
related_classes = []

if provisioning_service_class and has_realisation_property and ecosystem_function_class:
    # Find all subclasses of Provisioning_ecosystem_service
    for subclass in provisioning_service_class.subclasses():
        # Check if the subclass has any `has_realisation` property restrictions
        for restriction in subclass.is_a:
            if isinstance(restriction, Restriction) and restriction.property == has_realisation_property:
                # Get the class that is connected via `has_realisation`
                related_class = restriction.value
                # Check if the related class is part of Ecosystem_function (subclass of it)
                if ecosystem_function_class in related_class.ancestors():
                    related_classes.append((subclass, related_class))
    
    # Output the results
    if related_classes:
        print(f"Classes related to subclasses of {provisioning_service_class.name} via has_realisation and part of Ecosystem_function:")
        for subclass, related_class in related_classes:
            print(f"{subclass.name} has_realisation {related_class.name} (subclass of Ecosystem_function)")
    else:
        print(f"No subclasses of {provisioning_service_class.name} are connected via has_realisation to classes that are part of Ecosystem_function.")
else:
    print("The required class or property was not found.")


## CQ: Who benefits from food value?
# Access the necessary classes and object property
food_value_class = onto.search_one(iri="*Food_value")
benefits_from_property = onto.search_one(iri="*benefits_from")

# Initialize the list to store the results
related_classes = []

if food_value_class and benefits_from_property:
    # Find all classes that have any `benefits_from` property restrictions
    for cls in onto.classes():
        for restriction in cls.is_a:
            if isinstance(restriction, Restriction) and restriction.property == benefits_from_property:
                # Check if the restriction value is connected to `Food_value`
                if restriction.value == food_value_class:
                    related_classes.append(cls)
    
    # Output the results
    if related_classes:
        print(f"Classes connected to {food_value_class.name} via benefits_from:")
        for related_class in related_classes:
            print(f"{related_class.name} benefits_from {food_value_class.name}")
    else:
        print(f"No classes are connected to {food_value_class.name} via benefits_from.")
else:
    print("The required class or property was not found.")



## CQ: What is necessary to realise the wild fish provisioning service?
# Step 1: Retrieve the Wild_fish_provisioning_service class
wild_fish_provisioning_service_class = onto.search_one(iri="*Wild_fish_provisioning_service")

# Step 2: Retrieve the has_realization property
realize_property = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000055")

# Step 3: Query for classes that realize Wild_fish_provisioning_service
realizing_classes = []

if wild_fish_provisioning_service_class and realize_property:
    for cls in onto.classes():
        for restriction in cls.is_a:
            if isinstance(restriction, Restriction) and restriction.property == realize_property:
                if restriction.value == wild_fish_provisioning_service_class:
                    realizing_classes.append(cls)

# Output the results
if realizing_classes:
    print("Classes that realize Wild_fish_provisioning_service:")
    for realizing_class in realizing_classes:
        print(realizing_class.name)
else:
    print("No classes found that realize Wild_fish_provisioning_service.")



## CQ: What causes exploitation
# Access the necessary class and object property
exploitation_class = onto.search_one(iri="*Exploitation")
causally_upstream_property = onto.search_one(iri="*causally_upstream_of")

# Initialize the list to store the results
upstream_classes = []

if exploitation_class and causally_upstream_property:
    # Iterate over all classes in the ontology
    for cls in onto.classes():
        for restriction in cls.is_a:
            if isinstance(restriction, Restriction) and restriction.property == causally_upstream_property:
                # Check if the restriction value points to the Exploitation class
                if restriction.value == exploitation_class:
                    upstream_classes.append(cls)
    
    # Output the results
    if upstream_classes:
        print(f"Classes that are causally upstream of {exploitation_class.name}:")
        for upstream_class in upstream_classes:
            print(upstream_class.name)
    else:
        print(f"No classes are causally upstream of {exploitation_class.name}.")
else:
    print("The required class or property was not found.")


## CQ: Who participates in whale watching?
# Access the necessary classes and object properties
whale_watching_class = onto.search_one(iri="*Whale_watching")
participate_in_property = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000056")
act_in_property = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000166")
actor_class = onto.search_one(iri="*Actor")

# Initialize the list to store the results
participating_classes = []

if whale_watching_class:
    # Check for classes that participate_in Whale_watching
    if participate_in_property:
        for cls in onto.classes():
            for restriction in cls.is_a:
                if isinstance(restriction, Restriction) and restriction.property == participate_in_property:
                    if restriction.value == whale_watching_class:
                        participating_classes.append(cls)

    # Check for classes that act_in Whale_watching
    if act_in_property:
        for cls in onto.classes():
            for restriction in cls.is_a:
                if isinstance(restriction, Restriction) and restriction.property == act_in_property:
                    if restriction.value == whale_watching_class:
                        participating_classes.append(cls)

    # Filter for subclasses of Actor
    actor_participating_classes = [
        cls for cls in set(participating_classes)
        if actor_class in cls.ancestors()  # Check if Actor is in the class hierarchy
    ]

    # Output the results
    if actor_participating_classes:
        print(f"Classes that participate_in or act_in {whale_watching_class.name} and are subclasses of Actor:")
        for actor_class in actor_participating_classes:
            print(actor_class.name)
    else:
        print(f"No classes that participate_in or act_in {whale_watching_class.name} are subclasses of Actor.")
else:
    print("The class `Whale_watching` was not found.")


## CQ: Which ecosystem provides freshwater supply?
# Access the class Freshwater_supply and Ecosystem
freshwater_supply_class = onto.search_one(iri="*Clean_freshwater")
ecosystem_class = onto.search_one(iri="*Ecosystem")

# Function to check if a class is connected to the target class
def is_connected(start_class, target_class, visited=None):
    """Recursively check if there's a path from `start_class` to `target_class`."""
    if visited is None:
        visited = set()
    
    if start_class in visited:
        return False
    visited.add(start_class)

    # Check if the current class is the target class
    if start_class == target_class:
        return True

    # Check all restrictions for the current class
    for restriction in start_class.is_a:
        if isinstance(restriction, Restriction):
            related_class = restriction.value
            if is_connected(related_class, target_class, visited):
                return True

    return False

# Find subclasses of Ecosystem
if ecosystem_class:
    subclasses = [cls for cls in onto.classes() if ecosystem_class in cls.ancestors()]

    # Check each subclass for connection to Freshwater_supply
    connected_subclasses = []
    for subclass in subclasses:
        if is_connected(subclass, freshwater_supply_class):
            connected_subclasses.append(subclass)

    # Output results
    if connected_subclasses:
        print(f"Subclasses of Ecosystem that are indirectly connected to Freshwater_supply:")
        for connected_class in connected_subclasses:
            print(connected_class.name)
    else:
        print(f"No subclasses of Ecosystem are indirectly connected to Freshwater_supply.")
else:
    print("The class `Ecosystem` or `Freshwater_supply` was not found.")



## CQ: Which ecosystem service is linked to a commodity?
# Access the classes
ecosystem_service_class = onto.search_one(iri="*Ecosystem_service")
commodity_aggregate_class = onto.search_one(iri="*Commodity_aggregate")

# Function to check if there is an indirect connection
def is_indirectly_connected(start_class, target_class, visited=None):
    """Recursively check for an indirect connection from `start_class` to `target_class`."""
    if visited is None:
        visited = set()
    
    if start_class in visited:
        return False
    visited.add(start_class)

    # Check if the current class is the target class
    if start_class == target_class:
        return True

    # Check all restrictions for the current class
    for restriction in start_class.is_a:
        if isinstance(restriction, Restriction):
            related_class = restriction.value
            if is_indirectly_connected(related_class, target_class, visited):
                return True

    return False

# Find subclasses of Ecosystem_service
if ecosystem_service_class:
    subclasses_of_ecosystem_service = [cls for cls in onto.classes() if ecosystem_service_class in cls.ancestors()]

    # Find subclasses of Commodity_aggregate
    subclasses_of_commodity_aggregate = [cls for cls in onto.classes() if commodity_aggregate_class in cls.ancestors()]

    # Check for indirect connections
    connected_subclasses = []
    for subclass in subclasses_of_ecosystem_service:
        for target_class in subclasses_of_commodity_aggregate:
            if is_indirectly_connected(subclass, target_class):
                connected_subclasses.append(subclass)
                break  # No need to check further for this subclass

    # Output results
    if connected_subclasses:
        print(f"Subclasses of Ecosystem_service that are indirectly connected to any subclass of Commodity_aggregate:")
        for connected_class in connected_subclasses:
            print(connected_class.name)
    else:
        print(f"No subclasses of Ecosystem_service are indirectly connected to any subclass of Commodity_aggregate.")
else:
    print("The classes `Ecosystem_service` or `Commodity_aggregate` were not found.")



## CQ: What is an example of anthropogenic contribution for wildlife viewing services? 
# Step 1: Retrieve the relevant classes and properties
eesv_anthropogenic_contribution_class = onto.search_one(iri="*EESV_anthropogenic_contribution")
wildlife_viewing_service_class = onto.search_one(iri="*Wildlife_viewing_service")
measure_of_property = onto.search_one(iri="*measure_of")

# Step 2: Function to check indirect connection
def is_indirectly_related(start_class, target_class, visited=None):
    if visited is None:
        visited = set()
    if start_class in visited:
        return False
    visited.add(start_class)

    # If the start_class is the target class, we found a connection
    if start_class == target_class:
        return True

    # Check for all related classes through restrictions
    for restriction in start_class.is_a:
        if isinstance(restriction, Restriction):
            related_classes = [restriction.value]  # Gather related classes
            for related_class in related_classes:
                if is_indirectly_related(related_class, target_class, visited):
                    return True
    return False

# Step 3: Query classes that are a measure_of EESV_anthropogenic_contribution
measure_of_classes = []

if eesv_anthropogenic_contribution_class and measure_of_property:
    for cls in onto.classes():
        for restriction in cls.is_a:
            if isinstance(restriction, Restriction) and restriction.property == measure_of_property:
                if restriction.value == eesv_anthropogenic_contribution_class:
                    measure_of_classes.append(cls)

# Step 4: Filter classes that are indirectly related to Wildlife_viewing_service
indirectly_related_classes = []

for cls in measure_of_classes:
    if is_indirectly_related(cls, wildlife_viewing_service_class):
        indirectly_related_classes.append(cls)

# Output the results
if indirectly_related_classes:
    print("Classes that are a measure_of EESV_anthropogenic_contribution and indirectly related to Wildlife_viewing_services:")
    for cls in indirectly_related_classes:
        print(cls.name)
else:
    print("No classes found that match the criteria.")



## CQ: What is a measure of ecological supply for a provisioning service?
# Step 1: Retrieve all descendants of Provisioning_ecosystem_service
provisioning_ecosystem_service_class = onto.search_one(iri="*Provisioning_ecosystem_service")
provisioning_descendants = set()

if provisioning_ecosystem_service_class:
    provisioning_descendants = provisioning_ecosystem_service_class.descendants()

# Step 2: Retrieve all classes related to EESV_ecological_supply via the measure_of property
measure_of_property = onto.search_one(iri="*measure_of")
eesv_ecological_supply_class = onto.search_one(iri="*EESV_ecological_supply")
measure_related_classes = []

if measure_of_property and eesv_ecological_supply_class:
    for cls in onto.classes():
        for restriction in cls.is_a:
            if isinstance(restriction, Restriction) and restriction.property == measure_of_property:
                if restriction.value == eesv_ecological_supply_class:
                    measure_related_classes.append(cls)

# Step 3: Check if the classes from step 2 are indirectly related to descendants of Provisioning_ecosystem_service
def is_indirectly_related(start_class, target_classes):
    """Recursively check if a class is indirectly related to any class in `target_classes`."""
    visited = set()
    queue = [start_class]
    
    while queue:
        current_class = queue.pop(0)
        
        if current_class in visited:
            continue
        visited.add(current_class)
        
        # Check if the current class is in the target classes (descendants)
        if current_class in target_classes:
            return True
        
        # Check all the restrictions of the current class
        for restriction in current_class.is_a:
            if isinstance(restriction, Restriction):
                queue.append(restriction.value)
    
    return False

# Step 4: Check which of the measure-related classes are indirectly related to Provisioning_ecosystem_service descendants
indirectly_related_classes = []

for cls in measure_related_classes:
    if is_indirectly_related(cls, provisioning_descendants):
        indirectly_related_classes.append(cls)

# Output the results
if indirectly_related_classes:
    print("Classes related to EESV_ecological_supply and indirectly related to descendants of Provisioning_ecosystem_service:")
    for related_class in indirectly_related_classes:
        print(related_class.name)
else:
    print("No classes found that meet the criteria.")


## CQ: What is a measure of EESV use in wild fish provisioning?
# Access the classes EESV_use and Wild_fish_provisioning_service
eesv_use_class = onto.search_one(iri="*EESV_use")
wild_fish_provisioning_service_class = onto.search_one(iri="*Wild_fish_provisioning_service")

# Check if both classes exist
if eesv_use_class and wild_fish_provisioning_service_class:
    # Find all classes that have the measure_of property pointing to EESV_use
    measure_of_eesv_use_classes = [
        cls for cls in onto.classes()
        if hasattr(cls, "measure_of") and eesv_use_class in cls.measure_of
    ]

    # Function to check if a class is indirectly related to Wild_fish_provisioning_service
    def is_indirectly_related(start_class, target_class, visited=None):
        if visited is None:
            visited = set()

        if start_class in visited:
            return False
        visited.add(start_class)

        # Check if the current class is the target class
        if start_class == target_class:
            return True

        # Check all restrictions for the current class
        for restriction in start_class.is_a:
            if isinstance(restriction, Restriction):
                related_class = restriction.value
                if is_indirectly_related(related_class, target_class, visited):
                    return True

        return False

    # Check if any of the measure_of classes are indirectly related to Wild_fish_provisioning_service
    related_classes = []
    for measure_class in measure_of_eesv_use_classes:
        if is_indirectly_related(measure_class, wild_fish_provisioning_service_class):
            related_classes.append(measure_class)

    # Output results
    if related_classes:
        print("Classes that are a measure_of EESV_use and are indirectly related to Wild_fish_provisioning_service:")
        for related_class in related_classes:
            print(related_class.name)
    else:
        print("No classes that are a measure_of EESV_use are indirectly related to Wild_fish_provisioning_service.")
else:
    print("One or both classes (`EESV_use` or `Wild_fish_provisioning_service`) were not found.")


# CQ: What driver affects killer whale populations?
# Find the Whale_population, Direct_driver, and Indirect_driver classes
whale_population_class = onto.search_one(iri="*Whale_population")
direct_driver_class = onto.search_one(iri="*Direct_driver")
indirect_driver_class = onto.search_one(iri="*Indirect_driver")

# Check if the classes are found in the ontology
if not whale_population_class or not direct_driver_class or not indirect_driver_class:
    print("One or more required classes were not found in the ontology.")
else:
    # List to hold the classes that meet the conditions
    influencing_classes = []

    # Search for all classes in the ontology
    for cls in onto.classes():
        # Check if the class belongs to Direct_driver or Indirect_driver
        if direct_driver_class in cls.ancestors() or indirect_driver_class in cls.ancestors():
            # Check if the class causally_influences Whale_population
            for restriction in cls.is_a:
                if (
                    isinstance(restriction, Restriction) and
                    restriction.property.name == "causally_influences" and
                    restriction.value == whale_population_class
                ):
                    influencing_classes.append(cls)

    # Output results
    if influencing_classes:
        print("Classes that causally influence Whale_population and are a Direct or Indirect driver:")
        for influencing_class in influencing_classes:
            print(influencing_class.name)
    else:
        print("No classes meet the specified conditions.")


# CQ: Where are whales found?
# Find the Ecosystem and Whale_population classes
ecosystem_class = onto.search_one(iri="*Ecosystem")
whale_population_class = onto.search_one(iri="*Whale_population")

# Check if the classes are found in the ontology
if not ecosystem_class or not whale_population_class:
    print("The Ecosystem or Whale_population class was not found.")
else:
    # List to hold the subclasses of Ecosystem that are indirectly connected to Whale_population
    indirectly_connected_classes = []

    # Define a recursive function to check for indirect connection
    def is_indirectly_connected(start_class, target_class, visited=None):
        if visited is None:
            visited = set()
        if start_class in visited:
            return False
        visited.add(start_class)

        # Check direct relationships in start_class
        for restriction in start_class.is_a:
            if isinstance(restriction, Restriction) and restriction.value == target_class:
                return True
            elif isinstance(restriction, Restriction):
                # Recursively check if restriction.value is indirectly connected to target_class
                if is_indirectly_connected(restriction.value, target_class, visited):
                    return True
        return False

    # Find subclasses of Ecosystem
    for subclass in ecosystem_class.subclasses():
        # Check if each subclass is indirectly connected to Whale_population
        if is_indirectly_connected(subclass, whale_population_class):
            indirectly_connected_classes.append(subclass)

    # Output results
    if indirectly_connected_classes:
        print("Subclasses of Ecosystem that are indirectly connected to Whale_population:")
        for cls in indirectly_connected_classes:
            print(cls.name)
    else:
        print("No subclasses of Ecosystem are indirectly connected to Whale_population.")
