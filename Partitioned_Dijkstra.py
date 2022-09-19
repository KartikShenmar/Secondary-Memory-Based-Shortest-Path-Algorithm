from os import openpty, path, read, write
import math
from decimal import Decimal
import itertools
import numpy as np
from collections import defaultdict
import heapq as h

k = int(input("Enter value of k : "))
B = int(input("Enter value of B : "))
print("\n\n")
ov = 0

#Function to get Cell-ID of a given node
def cell(x, y, x_min, y_min):
    i = int((int(x) - x_min) / int(k))
    j = int((int(y) - y_min) / int(k))
    cellid = [i,j]
    return cellid

#Function to write nodes in the file
def writenodes(id, x, y, i, records, overflow_files, ov):
    x_ind = id[0]
    y_ind = id[1]
    if(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] == 0):
        name = str(id[0])+","+str(id[1])+".txt"
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
    elif(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] > 0):
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
        name = str(id[0])+","+str(id[1])+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
    else:
        if(records[x_ind][y_ind] == B):
            records[x_ind][y_ind] = 1
            overflow_files[x_ind][y_ind]+=1
            name = str(id[0])+","+str(id[1])+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
            file = open(str(id[0])+","+str(id[1])+".txt", "a")
            file.write("?? {}".format(str(id[0])+","+str(id[1])+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"))
            file.close()
            file = open(name, "a")
            file.write("?? {}".format(str(id[0])+","+str(id[1])+".txt"))
            file.write("\n")
            file.close()
            
            
    file = open(name,"a")
    file.write(str(i)+" "+str(x)+" "+str(y))
    file.write("\n")
    file.close()
     
#Function to write edges in the file
def writeedges(node1, node2, edge_length, records, overflow_files, writehash, nodeid):
    x_ind = nodeid[0]
    y_ind = nodeid[1]
    if(writehash[x_ind][y_ind] == 0):
        writehash[x_ind][y_ind] = 1
        if(overflow_files[x_ind][y_ind] > 0):
            name1 = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
        else:
            name1 = str(x_ind)+","+str(y_ind)+".txt"
        file = open(name1,"a")
        file.write("##")
        file.write("\n")
        file.close()
    if(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] == 0):
        name = str(x_ind)+","+str(y_ind)+".txt"
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
    elif(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] > 0):
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
        name = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
    else:
        if(records[x_ind][y_ind] == B):
            records[x_ind][y_ind] = 1
            overflow_files[x_ind][y_ind]+=1
            name = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
            file = open(str(x_ind)+","+str(y_ind)+".txt", "a")
            file.write("?? {}".format(str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"))
            file.close()
            file = open(name, "a")
            file.write("?? {}".format(str(x_ind)+","+str(y_ind)+".txt"))
            file.write("\n")
            file.close()

    file = open(name,"a")
    file.write(str(node1)+" "+str(node2)+" "+str(edge_length))
    file.write("\n")
    file.close()

#Function to write boundary nodes in the file
def write_boundarynodes(node, nodeid, xnode, ynode, records, overflow_files, writestar, writehash):
    x_ind = nodeid[0]
    y_ind = nodeid[1]
    if(writestar[x_ind][y_ind] == 0):
        writestar[x_ind][y_ind] = 1
        if(overflow_files[x_ind][y_ind] > 0):
            name1 = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
        else:
            name1 = str(x_ind)+","+str(y_ind)+".txt"
        
        if(writehash[x_ind][y_ind] == 0):
            name2 = ""
            if(overflow_files[x_ind][y_ind] == 0):
                name2 = str(x_ind)+","+str(y_ind)+".txt"
            else:
                name2 = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
            file = open(name2, "a")
            file.write("##")
            file.write("\n")
            file.close()
        
        file = open(name1, "a")
        file.write("**")
        file.write("\n")
        file.close()
    if(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] == 0):
        name = str(x_ind)+","+str(y_ind)+".txt"
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
    elif(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] > 0):
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
        name = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
    else:
        if(records[x_ind][y_ind] == B):
            records[x_ind][y_ind] = 1
            overflow_files[x_ind][y_ind]+=1
            name = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
            file = open(str(x_ind)+","+str(y_ind)+".txt", "a")
            file.write("?? {}".format(str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"))
            file.close()
            file = open(name, "a")
            file.write("?? {}".format(str(x_ind)+","+str(y_ind)+".txt"))
            file.write("\n")
            file.close()

    file = open(name, "a")
    file.write(str(node)+" "+str(xnode)+" "+str(ynode))
    file.write("\n")
    file.close()

#Function to write boundary edges in the file
def write_boundaryedges(node1, node2, edge_length, nodeid, records, overflow_files, writepercent, temparray, writestar):
    x_ind = nodeid[0]
    y_ind = nodeid[1]
    if(writepercent[x_ind][y_ind] == 0):
        writepercent[x_ind][y_ind] = 1
        if(overflow_files[x_ind][y_ind] > 0):
            name1 = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
        else:
            name1 = str(x_ind)+","+str(y_ind)+".txt"

        if(writestar[x_ind][y_ind] == 0):
            name2 = ""
            if(overflow_files[x_ind][y_ind] == 0):
                name2 = str(x_ind)+","+str(y_ind)+".txt"
            else:
                name2 = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
            file = open(name2, "a")
            file.write("**")
            file.write("\n")
            file.close()
        file = open(name1,"a")
        file.write("%%")
        file.write("\n")
        file.close()

    if(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] == 0):
        name = str(x_ind)+","+str(y_ind)+".txt"
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
    elif(records[x_ind][y_ind] < B and overflow_files[x_ind][y_ind] > 0):
        records[x_ind][y_ind] = records[x_ind][y_ind] + 1
        name = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
    else:
        if(records[x_ind][y_ind] == B):
            records[x_ind][y_ind] = 1
            overflow_files[x_ind][y_ind]+=1
            name = str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"
            file = open(str(x_ind)+","+str(y_ind)+".txt", "a")
            file.write("?? {}".format(str(x_ind)+","+str(y_ind)+"ov"+str(int(overflow_files[x_ind][y_ind]))+".txt"))
            file.close()
            file = open(name, "a")
            file.write("?? {}".format(str(x_ind)+","+str(y_ind)+".txt"))
            file.write("\n")
            file.close()

    file = open(name,"a")
    file.write(str(node1)+" "+str(node2)+" "+str(edge_length))
    file.write("\n")
    file.close()

#Creating a list that stores information of nodes.txt
readfile = open("nodes.txt", "r")
readlist1 = []
for line in readfile:
    line = line.strip()
    line_list = line.split()
    readlist1.append(line_list)

#Creating 3 lists for node, x, y present in the nodes.txt   
node, x, y = [], [], []
for i in readlist1:
    node.append(int(i[0]))
    x.append(Decimal(i[1]))
    y.append(Decimal(i[2]))

#Calculating minimum and maximum coordinates
x_min = min(x)
y_min = min(y)
x_max = max(x)
y_max = max(y)

#Updating x_max and y_max depending on value of k
x_max = x_max + math.ceil(x_max - x_min) % k
y_max = y_max + math.ceil(y_max - y_min) % k

#row length and column length of some arrays used for special purpose
x_size = int((x_max - x_min) / k)
y_size = int((y_max - y_min) / k)

#Special arrays created to store metadata of our program
records = np.zeros((x_size + 10, y_size + 10))
overflow_files = np.zeros((x_size + 10, y_size + 10))
writehash = np.zeros((x_size + 10, y_size + 10))
edge_redundancy = np.zeros((60000, 60000))
writestar = np.zeros((x_size + 10, y_size + 10))
writepercent = np.zeros((x_size + 10, y_size + 10))
temparray = np.zeros((60000, 60000))
redundat_node = np.zeros((60000, 60000))
disk_blocks_checker = np.zeros((x_size + 10, y_size + 10))
path_node = np.zeros(60000)
path_node_partitiondj = np.zeros(60000)
#path_node = {}

for i in range(len(readlist1)):
    x1 = x[i]
    y1 = y[i]
    id = cell(x1, y1, x_min, y_min)
    writenodes(id, x1, y1, i, records, overflow_files, ov)

readfile = open("edges.txt", "r")
readlist2 = []
for line in readfile:
    line = line.strip()
    line_list = line.split()
    readlist2.append(line_list)

#Creating 3 lists for node1, node2, edge length present in the edges.txt 
node1, node2, edge_length = [], [], []
for i in readlist2:
    if(edge_redundancy[int(i[0])][int(i[1])] == 0):     #Removing redundant edges and storing data in the respective lists
        edge_redundancy[int(i[0])][int(i[1])] = 1
        node1.append(int(i[0]))
        node2.append(int(i[1]))
        edge_length.append(Decimal(i[2]))

#Fetching Cell-IDs of nodes in the first column of edges.txt
node1_id = []
for i in range(len(node1)): 
    x1 = x[node1[i]]
    y1 = y[node1[i]]
    id1 = cell(x1, y1, x_min, y_min)
    node1_id.append(id1)

#Fetching Cell-IDs of nodes in the second column of edges.txt
node2_id = []
for i in range(len(node2)): 
    x2 = x[node2[i]]
    y2 = y[node2[i]]
    id2 = cell(x2, y2, x_min, y_min)
    node2_id.append(id2)

for i in range(len(node1_id)):
    if(node1_id[i] == node2_id[i]):
        writeedges(node1[i], node2[i], edge_length[i], records, overflow_files, writehash, node1_id[i])

redundancy_removal = defaultdict(list)
for i in range(len(node1_id)):
    if(node1_id[i] != node2_id[i]):
        redundancy_removal[tuple(node1_id[i])].append(node2[i])
        redundancy_removal[tuple(node2_id[i])].append(node1[i])
       
Total_keys = redundancy_removal.keys()
for i in Total_keys:
    temp = redundancy_removal[i]
    temp = set(temp)
    temp = list(temp)
    for j in range(len(temp)):
        write_boundarynodes(temp[j], list(i), x[temp[j]], y[temp[j]], records, overflow_files, writestar, writehash)

for i in range(len(node1_id)):
    if(node1_id[i] != node2_id[i]):
        write_boundaryedges(node1[i], node2[i], edge_length[i], node1_id[i], records, overflow_files, writepercent, temparray, writestar)
        write_boundaryedges(node1[i], node2[i], edge_length[i], node2_id[i], records, overflow_files, writepercent, temparray, writestar)


#Djikstra Implementation

#Required input taken from user and desired output displayed for simple djikstra algorithm.
print("SIMPLE DJIKSTRA ALGORITHM\n")
source_nodeid = int(input("Enter value of source node : "))
destination_nodeid = int(input("Enter value of destination node : "))
source_node_x_coordinate = x[source_nodeid]
source_node_y_coordinate = y[source_nodeid]
source_node_cell_id = cell(source_node_x_coordinate, source_node_y_coordinate, x_min, y_min)
destination_node_x_coordinate = x[destination_nodeid]
destination_node_y_coordinate = y[destination_nodeid]
destination_node_cell_id = cell(destination_node_x_coordinate, destination_node_y_coordinate, x_min, y_min)

Graph = {}          #Empty graph created for Simple Djikstra algorithm. 
Graph_Seen = {}     #Empty graph created for Partitioned Djikstra algorithm.

#Function of Simple Djikstra Algorithm
def djikstra(Graph, source_node, destination_node):
    visited_nodes = set()
    cost_repository = {vertex: float('infinity') for vertex in Graph}
    cost_repository[source_node] = 0
    min_heap = []
    h.heappush(min_heap, (0, source_node))
    while len(min_heap) > 0:
        min_dist, min_vertex = h.heappop(min_heap)

        if(min_dist <= cost_repository[min_vertex]):
            for adjacent_node, cost in Graph[min_vertex].items():
                if(adjacent_node in visited_nodes):
                    continue
                updated_distance = min_dist + cost

                if updated_distance < cost_repository[adjacent_node]:
                    cost_repository[adjacent_node] = updated_distance
                    path_node[int(adjacent_node)] = int(min_vertex)
                    h.heappush(min_heap, (updated_distance, adjacent_node))
        else:
            continue

        if(min_vertex == destination_node):
            break

    return cost_repository

#Stack helping to store the shortest path from source to destination in correct order.      
helper_stack = []

#Function that prints the shortest path for Simple Djikstra algorithm.
def path_print():
    final_path = np.zeros(len(helper_stack))
    i = 0

    while(helper_stack):
        final_path[i] = helper_stack.pop()
        i = i + 1

    print("Shortest path achieved is : ")

    j = 0
    while(j < len(final_path)):
        print("{} ->".format(final_path[j]), end = " ")
        j = j + 1

#Fucntion that keeps track of shortest path and displays it.
def path_identification(source_nodeid, destination_nodeid):
    node = int(destination_nodeid)
    helper_stack.append(node)

    while(node != int(source_nodeid)):
       helper_stack.append(int(path_node[node]))
       node = int(path_node[node])

    path_print()

#Functions for adding vertices and edges in the adjacency list of Graph of Simple Djikstra implementation.
def Vertex_Graph(v):
  if v not in Graph:
    Graph[v] = {}

def Edge_Graph(v1, v2, e):
  Graph[v1][v2] = e
    
#Adding vertices as keys in the dictionary Graph   
for i in node:
    Vertex_Graph(i)

#Adding edges ad values correspoding to their keys
for i in range(len(edge_length)):
    Edge_Graph(node1[i], node2[i], edge_length[i])

#Calculating shortest distance between source and destination node.
shortest_distance_dj = djikstra(Graph, source_nodeid, destination_nodeid)
print("Distance between {} and {} in djikstra algorithm is {}.".format(source_nodeid, destination_nodeid, shortest_distance_dj[destination_nodeid]))
path_identification(source_nodeid, destination_nodeid)

#Functions for adding vertices and edges dynamically in the adjacency list of Graph of Partiotined Djikstra implementation.
def Vertex_Graph_Grid(v):
  global No_of_vertices
  if v not in Graph_Seen:
    Graph_Seen[v] = {}

def Edge_Graph_Grid(v1, v2, e):
  Graph_Seen[v1][v2] = e

Edge_start = '##'
Boundary_edge = '**'
Boundary_node = '%%'
File_Alias = '??'
def check(file_list):
    if(file_list[0] == Edge_start or file_list[0] == Boundary_edge or file_list[0] == Boundary_node or file_list[0] == File_Alias):
        return 'F'
    else:
        return 'T'

file_holder = {}    #Dictionary that keeps check of the files that were opened and are in main memory.
disk_blocks = 0     #Calculates the no. of disk blocks loaded into main memory.
def  Create_Dynamic_Graph(current_vertex_id, file_count):
    global disk_blocks
    set_flag = 'F'
    set_flag1 = 'T'
    overflow_counter = 1
    temp = tuple(current_vertex_id)

    if(temp in file_holder.keys()):
        return

    file_holder[temp] = 1
    disk_blocks+=file_count + 1
    name =''
    fcount = file_count + 1

    for i in range(fcount):
        if(i == 0):
            name = str(current_vertex_id[0])+","+str(current_vertex_id[1])+".txt"
        else:
            name = str(current_vertex_id[0])+","+str(current_vertex_id[1])+"ov"+str(overflow_counter)+".txt"
            overflow_counter = overflow_counter + 1

        file = open(name, "r")

        for line in file:
            line = line.strip()
            file_list = line.split()
            if(file_list[0] == Edge_start or file_list[0] == Boundary_node):
                set_flag = 'T'
                Marker1 = True
                continue
            elif(file_list[0] == Boundary_edge):
                set_flag = 'F'
                Marker2 = False
                continue
            
            if(set_flag == 'T' and check(file_list) == 'T'):
                if(set_flag1 == 'T'):
                    Vertex_Graph_Grid(int(file_list[0]))
                    Edge_Graph_Grid(int(file_list[0]), int(file_list[1]), Decimal(file_list[2]))

        file.close()

    overflow_counter = 1
        
#Function of Partitioned Djikstra Algorithm
def djikstra_partitioned(source_node, destination_node):
    visited_nodes = set()
    cost_repository = {v: Decimal('infinity') for v in Graph}
    cost_repository[source_node] = 0
    min_heap = []
    h.heappush(min_heap, (0, source_node))
    while(len(min_heap) > 0 or h.heappop(min_heap) != destination_nodeid):
        min_dist, min_vertex = h.heappop(min_heap)
        visited_nodes.add(min_vertex)
        min_vertex_id = cell(x[min_vertex], y[min_vertex], x_min, y_min)            #Finding cell id of vertex popped.
        file_count = int(overflow_files[min_vertex_id[0]][min_vertex_id[1]])    #Keeps check of no. of overflow files a main file has.
        Create_Dynamic_Graph(min_vertex_id, file_count)             #Dynamically make the graph, i.e., keep updating Graph_Seen
    
        if(min_dist <= cost_repository[min_vertex]):
            for adjacent_node, cost in Graph_Seen[min_vertex].items():
                if(adjacent_node in visited_nodes):
                    continue
                updated_distance = min_dist + cost

                if updated_distance < cost_repository[adjacent_node]:
                    cost_repository[adjacent_node] = updated_distance
                    path_node_partitiondj[int(adjacent_node)] = int(min_vertex)
                    h.heappush(min_heap, (updated_distance, adjacent_node))
        else:
            continue

        if(min_vertex == destination_node):
            break   

    return cost_repository
        
#Stack helping to store the shortest path from source to destination in correct order.      
helper_stack_partitiondj = []

#Function that prints the shortest path for Partitioned Djikstra algorithm.
def path_print_partitiondj():
    final_path = np.zeros(len(helper_stack_partitiondj))
    i = 0

    while(helper_stack_partitiondj):
        final_path[i] = helper_stack_partitiondj.pop()
        i = i + 1

    print("Shortest path achieved is : ")

    j = 0
    while(j < len(final_path)):
        print("{} ->".format(final_path[j]), end = " ")
        j = j + 1

#Fucntion that keeps track of shortest path and displays it.
def path_identification_partitondj(source_nodeid, destination_nodeid):
    node = int(destination_nodeid)
    helper_stack_partitiondj.append(node)

    while(node != int(source_nodeid)):
       helper_stack_partitiondj.append(int(path_node_partitiondj[node]))
       node = int(path_node_partitiondj[node])

    path_print_partitiondj()

#Required input taken from user and desired output displayed for partitioned djikstra algorithm.
print("\n")
print("PARTITIONED DJIKSTRA ALGORITHM\n")
source_nodeid = int(input("Enter value of source node of new graph: "))
destination_nodeid = int(input("Enter value of destination node of new graph: "))
source_node_x_coordinate = x[source_nodeid]
source_node_y_coordinate = y[source_nodeid]
source_node_cell_id = cell(source_node_x_coordinate, source_node_y_coordinate, x_min, y_min)
destination_node_x_coordinate = x[destination_nodeid]
destination_node_y_coordinate = y[destination_nodeid]
destination_node_cell_id = cell(destination_node_x_coordinate, destination_node_y_coordinate, x_min, y_min)
shortest_distance_djp = djikstra_partitioned(source_nodeid, destination_nodeid)
print("Distance between {} and {} in optimised djikstra algorithm is {}.".format(source_nodeid, destination_nodeid, shortest_distance_djp[destination_nodeid]))
print("Disk blocks = {}".format(disk_blocks))
path_identification_partitondj(source_nodeid, destination_nodeid)