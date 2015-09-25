import random
import sys
import os

print("Hey, I'm Betty.")
name = input("What is your name? ")
print("Hi there " + name + "!")
print("Let's get started!\n")

ws = input('Pick a mode. Type "w" for weights and "s" for scheduling. ')

# Program pre-checking definitions
invalid = True
comma = ","
dash = "-"

# Start of Weights
if ws == "w":

    # Start of Vertices
    vertices = input('Type in the vertices of the graph. For example, "A,B,C,D"... ')
    if comma in vertices:
        print("Awesome.")
        print(vertices.split(',')) #.append() produces extra brackets that seem like another set of lists []
    else:
        print('You have your vertices in the wrong format. Try adding a comma. For example "A,B,C,D" instead of', vertices)
        sys.exit("Error.")

    edges = input("Now type in the edges of the graph.\n"
                  'For example, "A-B,B-C,C-D"... ')

    # Start of Edges
    if dash in edges:
        print("Awesome.")
        print(edges.split(','))
    else:
        print('You have your vertices in the wrong format. Try adding a dash. For example "A-B,B-C,C-D" instead of', edges)
        sys.exit("Error.")

    # Start of Weights
    e_weights_yn = input('Are there any weights for the edges? Type "y" for yes and "n" for no... ')
    if e_weights_yn == "n":
        print("Got it. I'll find an Euler circuit for you.")
        print("Here's what I got...")
        print(edges, ",", edges[-1:], "-", edges[0])
    elif e_weights_yn == "y":
        list_e_weights = []
        e_weights = input('Please specify the weights. For example, "A-B=1,B-C=5,C-D=3,D-E=10"... ')
        print("Here's the cheapest tour I have for you:")
        sort_e_weights = ','.join(sorted(e_weights.split(','), key = lambda m: int(m.split('=')[1])))
        print(sort_e_weights)
    else:
        print("This is not a valid function.")

    # Display Final Results
    print("\n\n")
    print("The final results are:")
    print("Vertices: ", vertices.split(','))
    print("Edges: ", edges)
    if e_weights_yn == "y":
        print("Weights: ", sort_e_weights)
    else:
        print(edges, ",", edges[-1:], "-", edges[0])

elif ws == "s":
    # Start Scheduling
    task_list = []
    tasks = input('List your tasks in the following format. For example, "A=2,B=5,C=1,D=9"... ')
    sort_e_weights = ','.join(sorted(tasks.split(','), key = lambda m: int(m.split('=')[1])))
    task_list.append(tasks)
    t_places = input('Type in your task paths. For example: "A-D,B-D,C-E"... ')
    t_list = []
    t_list.append(t_places.split(','))
    z_t_places = t_list[::2]
    o_t_places = t_list[1::2]
    print("With two processors, using the Decreasing Time algorithm, here are the results:")
    print("P1: ", z_t_places)
    print("P2: ", o_t_places)

else:
    print("Sorry, the command was not found.")
    sys.exit("Program closed.")
