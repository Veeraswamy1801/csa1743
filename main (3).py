from collections import dequedef vacuum_world(initial_state):
    state = list(initial_state)
    actions = []

    print("Initial State:", state)

    while state[1] == "Dirty" or state[2] == "Dirty":
        location = state[0]

        if location == "A":
            if state[1] == "Dirty":
                actions.append("Suck")
                state[1] = "Clean"
                print("Action: Suck | Location: A | Room A cleaned.")
            else:
                actions.append("Move Right")
                state[0] = "B"
                print("Action: Move Right | Vacuum moved to Room B.")
        elif location == "B":
            if state[2] == "Dirty":
                actions.append("Suck")
                state[2] = "Clean"
                print("Action: Suck | Location: B | Room B cleaned.")
            else:
                actions.append("Move Left")
                state[0] = "A"
                print("Action: Move Left | Vacuum moved to Room A.")

    print("\nFinal State:", state)
    print("Actions Taken:", actions)

# Example initial state: Vacuum at A,


# State: (missionaries_left, cannibals_left, boat_position, missionaries_right, cannibals_right)
# boat_position: 0 = left side, 1 = right side

def is_valid(state):
    m_left, c_left, _, m_right, c_right = state
    # Check for negative numbers
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    # Missionaries eaten on left side
    if m_left > 0 and m_left < c_left:
        return False
    # Missionaries eaten on right side
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_successors(state):
    m_left, c_left, boat, m_right, c_right = state
    successors = []
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # Possible boat moves

    for m, c in moves:
        if boat == 0:  # Boat on left side
            new_state = (m_left - m, c_left - c, 1, m_right + m, c_right + c)
        else:  # Boat on right side
            new_state = (m_left + m, c_left + c, 0, m_right - m, c_right - c)

        if is_valid(new_state):
            successors.append((new_state, (m, c)))

    return successors

def bfs():
    start = (3, 3, 0, 0, 0)  # All on left side
    goal = (0, 0, 1, 3, 3)   # All on right side
    visited = set()
    queue = deque()
    queue.append((start, []))

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state == goal:
            return path + [current_state]

        for successor, move in get_successors(current_state):
            queue.append((successor, path + [current_state]))

    return None

def print_solution(solution):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    if not solution:
        print("No solution found.")
        return

    print("Solution found in {} steps:\n".format(len(solution) - 1))
    for i, state in enumerate(solution):
        m_left, c_left, boat, m_right, c_right = state
        boat_side = "Left" if boat == 0 else "Right"
        print(f"Step {i}:")
        print(f"  Left Side  -> Missionaries: {m_left}, Cannibals: {c_left}")
        print(f"  Right Side -> Missionaries: {m_right}, Cannibals: {c_right}")
        print(f"  Boat is on the {boat_side} side.\n")

# Run the program
solution = bfs()
print_solution(solution)
