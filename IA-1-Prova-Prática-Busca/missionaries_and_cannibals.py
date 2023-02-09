# Initial Situation
#
# Position initial_state[0] -> 3 Missionaries on the left side
# Position initial_state[1] -> 3 Canibals on the left side
# Position initial_state[2] -> 0 Missionaries on the right side
# Position initial_state[3] -> 0 Canibals on the right side
# Position initial_state[4] -> Canoe side: 0 -> Left, 1 - > Right

initial_state = [3,3,0,0,0]

# Operators Definition
# ordered pair containing the number o missionaries and canibals
# (1,0) - Cross a missionary in the canoe
# (2,0) - Cross two missionaries in the canoe
# (1,1) - Cross a cannibal and a missionary in the canoe
# (0,2) - Cross two cannibals in the canoe
# (0,1) - Cross a cannibal in the canoe
operators = [(1,0),(1,1),(2,0),(0,2)]

frontier = []
visited_nodes = []

def move_canoe(n_state,n_missionaries=0, n_cannibals=0):
    # control
    if n_missionaries + n_cannibals > 2:
        return 

    # canoe on the left side
    if n_state[-1] == 0:
        origin_missionaries = 0
        origin_cannibals = 1
        destiny_missionaries = 2
        destiny_cannibals = 3
    # canoe on the right side
    else:
        origin_missionaries = 2
        origin_cannibals = 3
        destiny_missionaries = 0
        destiny_cannibals = 1
    # se não há o que transportar...
    if n_state[origin_missionaries] == 0 and n_state[origin_cannibals] == 0:
        return
    
    ## atualizando a posição da canoa
    n_state[-1] = 1 - n_state[-1]
    #transportando os missionários.
    #missionarios na origem
    for i in range(min(n_missionaries, n_state[origin_missionaries])):
        n_state[origin_missionaries] -= 1
        n_state[destiny_missionaries] += 1
    #transportando os canibais
    for i in range(min(n_cannibals, n_state[origin_cannibals])):
        n_state[origin_cannibals] -=1
        n_state[destiny_cannibals] += 1
    #pronto
    return n_state    

def sucessors(state):
    sucessors = []
    for (i,j) in operators:
        s = move_canoe(state[:],i,j)
        if s== None: continue
        if (s[0]<s[1] and s[0]>0) or s[2]<s[3] and s[2]>0: continue
        if s in visited_nodes: continue
        sucessors.append(s)
    return sucessors 

# print(sucessors(initial_state))

def get_unvisited_adjacent_node(element_to_analyze):
    l = sucessors(element_to_analyze)
    if len(l) > 0:
        return l[0]
    else:
        return -1

def test_objective(state):
    if state[2] >= 3 and state[3] >= 3:
        return True
    else:
        return False    

# Depth-First search
def dfs(initial_state):
    frontier.append(initial_state)
    while len(frontier) != 0:
        element_to_analyze = frontier[len(frontier)-1] 
        if test_objective(element_to_analyze):break
        v = get_unvisited_adjacent_node(element_to_analyze)
        if v == -1:
            frontier.pop()
        else: 
            visited_nodes.append(v)
            frontier.append(v)
    else:
        print("Path not found. Unsuccessful search")
    return frontier

sol = dfs(initial_state)
# print(sol)

for i in range(1, len(sol)):
    destiny_missionaries = abs(sol[i][0] - sol[i-1][0])
    destiny_cannibals = abs(sol[i][1] - sol[i-1][1])
    canoe = sol[i][4]-sol[i-1][4]
    if canoe == 1:
        s = "->"
    else:
        s = "<-"
    print(sol[i-1],"({},{},{})".format(destiny_missionaries,destiny_cannibals,s))


