# Map Coloring Problem using Backtracking (CSP)

# Define the map as a dictionary where keys are regions and values are neighbors
map_graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # Tasmania has no borders
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Function to check if the current color assignment is valid
def is_valid(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking CSP solver
def backtrack(assignment, graph, colors):
    # If all regions are assigned, return the assignment
    if len(assignment) == len(graph):
        return assignment

    # Select an unassigned region (no heuristics used here)
    unassigned = [r for r in graph if r not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment, graph):
            assignment[unassigned] = color  # Make assignment
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[unassigned]  # Backtrack

    return None  # No valid assignment fou
