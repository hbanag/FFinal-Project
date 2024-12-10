##Import Statements
import argparse
import json 
import relationships
import sys
from collections import deque



## Person class 
class Person:
    """

    Attributes:
        name (str): The name of the person.
        gender (str): The gender of the person ('f' for female, 'm' for male, 'n' for nonbinary).
        parents (list): A list of Person instances representing the person's parents.
        spouse (Person or None): The spouse of the person, if applicable.

    Methods:
        __init__(name, gender):
            Initializes a new Person instance with the given name and gender.
            
        add_parent(parent):
            Adds a parent to the person’s list of parents if the parent is a valid Person instance.
            
        set_spouse(spouse):
            Sets the spouse attribute to the provided Person instance.

        connections():
            Finds and returns a dictionary of connected individuals and paths, where each key is
            a Person instance reachable from self via parent or spouse relationships, and each 
            value is a string path ("P" or "S") indicating the shortest path from self to that person.
            Side effects: Adds Person instances to a queue for tracking connections and paths.

        relation_to(other):
            Determines the kinship relationship from self to another person, if a defined relationship exists.

            Args:
                other (Person): Another Person instance to find a relationship to.

            Returns:
                str: The relationship term, or "distant relative" if no specific term is found.
                None: If no relationship exists between self and other.

            Side effects: None.
    """
    #__init__()
    def __init__(self, name, gender):
        """
        Initializes a new Person instance with the given name and gender.

        Args:
            name (str): The person's name.
            gender (str): The person's gender ('f', 'm', or 'n').

        Side effects: 
            initiates 'name' attribute to the provided name
            Initiates 'gender' attribute with the provided gender
            Initalizes 'parens' attribute will be an empty list
            Initializes 'spouse' attribute as None

        """
        self.name = name
        self.gender = gender
        self.parents = []
        self.spouse = None


    #add_parent()
    def add_parent(self, parent):
        """
        Adds a parent to the person’s list of parents if the parent is a valid Person instance.

        Args:
            parent (Person): The Person instance to add as a parent.

        Raises:
            TypeError: If the parent argument is not an instance of Person.

        Side effects:
            Modifies the parents attribute by appending a new Person instance.
        """
        if isinstance(parent, Person):
            self.parents.append(parent)
        else:
            raise TypeError("The parent must be an instance of Person.")




    #set_spouse()
    def set_spouse(self, spouse):
        """
        Sets the spouse attribute to the provided Person instance.

        Args:
            spouse (Person): The Person instance to set as the spouse.

        Raises:
            TypeError: If the spouse argument is not an instance of Person.

        Side effects:
            Modifies the spouse attribute by setting it to a new Person instance.
        """
        if isinstance(spouse, Person):
            self.spouse = spouse
        else:
            raise TypeError("Spouse must be an isntance of Person.")


    #connections

    # build a queue to help us keep track of individuals whose parents and spouses we need to 
    # We will use a list as our queue; we’ll use the append() method to add something, and pop(0) whenever we remove something (the 0 tells Python to remove the item at index 0).

    def connections(self):
        """
        Finds and returns a dictionary of connections (cdict) for self. Each key in the
        dictionary is a Person instance reachable from self via parent and/or spouse
        relationships, and each value is a path string indicating the shortest connections path.

        Returns:
            dict: Dictionary with connected Person instances as keys and path strings as values.

        Side effects:
            Uses a queue to keep track of and modify the list of Person instances to visit
            while finding connections.
        """
        cdict = {self: ""}
        queue = deque([self])

        while queue:
            person = queue.popleft()
            personpath = cdict[person]

            for parent in person.parents:
                if parent not in cdict:
                    cdict[parent] = personpath+ "P"
                    queue.append(parent)

            if "S" not in personpath and person.spouse and person.spouse not in cdict:
                cdict[person.spouse] = personpath + "S"
                queue.append(person.spouse)
       
        return cdict
                
    #relation_to() - utilize the min function ("HINTS") to keep it concise
    def relation_to(self, other):

        """
        Determines the relationship between self and another person.

        Args:
            other (Person): The other Person instance to find the relationship to.

        Returns:
            str: The kinship term describing self's relationship to the other person,
                 or "distant relative" if no specific term is found.
        """
        if not isinstance(other, Person):
            raise TypeError("Expected a Person instance for 'other'.")

        self_connections = self.connections()
        other_connections = other.connections()

        shared_relatives = set(self_connections).intersection(other_connections)
        if not shared_relatives:
            return None  # No relation if no shared relatives

        shortest_path = min(
            (self_connections[relative] + ":" + other_connections[relative] for relative in shared_relatives),
            key=len
        )

        if shortest_path in relationships.relationships:
            return relationships.relationships[shortest_path].get(self.gender, "distant relative")

        return "distant relative"


##Family class
class Family:
        #__init__() - utilize family.json
    """
    This represents a family tree and controls parent-child and spouse relationships.

    Attributes:
        family: describes the Family object created form the JSON data
        relationship: Matches the relationship or None will appear if there is no match

    Args:
        data (dict): A dictionary containing family data which consist of 'indiviauals' (dict),
            'parents' (dict), and 'couples' (list[list])
    
    """
    def __init__(self, data):
        """
        Initializes a Family instance.

        Args:
            data (dict): Dictionary containing keys "individuals", "parents", and "couples".
                         - "individuals" is a dictionary with names as keys and genders as values.
                         - "parents" is a dictionary with names as keys and lists of parent names as values.
                         - "couples" is a list of lists, where each inner list contains two names of married people.
        
        Side effects:
            Creates Person instancesand stores data in the 'self.people' dict
            'parents' attributes creates the parent-child relationship
            'spouse' attribute creates the spouse relationship
            'self.people' stores all of Person instances by names
        """
        self.people = {}

        for name, gender in data["individuals"].items():
            self.people[name] = Person(name, gender)

        for person_name, parent_names in data["parents"].items():
            person = self.people[person_name]
            for parent_name in parent_names:
                parent = self.people[parent_name]
                person.add_parent(parent)

        for spouse1_name, spouse2_name in data["couples"]:
            spouse1 = self.people[spouse1_name]
            spouse2 = self.people[spouse2_name]
            spouse1.set_spouse(spouse2)
            spouse2.set_spouse(spouse1)


    #relation() - similar to relation_to()
    def relation(self, name1, name2):
        """
        Finds the relationship between two people given their names.

        Args:
            name1 (str): The name of the first person.
            name2 (str): The name of the second person.

        Returns:
            str: The relationship term between the two people, or None if not related.
        """
        if name1 not in self.people or name2 not in self.people:
            return None  # One or both people not found in family

        person1 = self.people[name1]
        person2 = self.people[name2]
        return person1.relation_to(person2)





##main function
def main(filepath, name1, name2):
    """
    Determines the relationship between two people in a family defined by a JSON file.

    Args:
        filepath (str): Path to the JSON file containing family data.
        name1 (str): The name of the first person.
        name2 (str): The name of the second person.

    Side effects:
        Reads and loads data from JSON file
        Prints the relationsihp between two people
        Error will appear if relatiosnhip is not a match
    """
    with open(filepath, "r", encoding="utf-8") as f:
        family_data = json.load(f)

    family = Family(family_data)

    relationship = family.relation(name1, name2)

    if relationship is None:
        print(f"{name1} is not related to {name2}")
    else:
        print(f"{name1} is {name2}'s {relationship}")


##parse_args function
def parse_args(args):
    """
    Parses command-line arguments.

    Args:
        args (list): List of command-line arguments.

    Returns:
        Namespace: Parsed arguments with attributes filepath, name1, and name2.
    """
    parser = argparse.ArgumentParser(description="Determine the relationship between two people in a family.")

    parser.add_argument("filepath", help="Path to the JSON file containing family data.")
    parser.add_argument("name1", help="The name of the first person.")
    parser.add_argument("name2", help="The name of the second person.")

    return parser.parse_args(args)


#if __name__ == "__main__" statement 
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    main(args.filepath, args.name1, args.name2)