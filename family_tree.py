# Example family tree structure
person = {
    "name": "John",
    "children": [
        {
            "name": "Jim",
            "children": [
                {"name": "Liam", "children": []},
                {"name": "Ella", "children": []}
            ]
        },
        {
            "name": "Zoe",
            "children": []
        }
    ]
}

# TASK:
# Complete the following function to collect all names 
# of children in the family tree using recursion

def get_all_children_names(person):
    names = []
    
    # Loop through each child in person's children
    for child in person["children"]:
        names.append(child["name"])
        
        # To do: Use recursion to get names of all descendants of this child
        # and add them to the 'names' list
    
    return names

# Example usage:
print(get_all_children_names(person))  # print all children's and grandchildren's names
