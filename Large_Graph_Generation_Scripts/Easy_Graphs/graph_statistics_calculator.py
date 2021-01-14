import csv
import os
import sys

#take in dict as parameter
def getMinMaxDegree(outgoing_edges):

    min_edge_deg = 99999999999999
    max_edge_deg = -1

    for key, value in outgoing_edges.items():

        if value < min_edge_deg:
            min_edge_deg = value
        if value > max_edge_deg:
            max_edge_deg = value


    return min_edge_deg, max_edge_deg





#return edge count, node count, min degree, max degree

def getGraphStatistics(filename):
    #count number of edges
    source_node_idx = 0
    dest_node_idx = 1
    edge_weight = 2

    outgoing_edges = dict()
    node_set = set()

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        edge_count = 0
        for data in csvreader:
            #need to check if the graph file has nodes and edges given as the first 2 lines
            if len(data) == 1:
                continue
            edge_count += 1
            if data[source_node_idx] != "":
                source_node = int(data[source_node_idx])
                node_set.add(source_node)
                if not source_node in outgoing_edges:
                    outgoing_edges[source_node] = 1
                else:
                    outgoing_edges[source_node] += 1



    min_edge_degree, max_edge_degree = getMinMaxDegree(outgoing_edges)

    return edge_count, len(node_set), min_edge_degree, max_edge_degree



# generate statistics for each graph in specified folder
def main():


    input_root_path = sys.argv[1]

    for input_filename in os.listdir(input_root_path):


        edge_count, node_count, min_edge_degree, max_edge_degree = getGraphStatistics(
            input_root_path + "/" + input_filename)

        print("For filename " , input_filename)
        print("Total number of edges is:", edge_count)
        print("Total number of nodes is:", node_count)
        print("Min Edge Degree is: ", min_edge_degree)
        print("Max Edge Degree is: ", max_edge_degree)
        print("Average Edge Degree is: ", (edge_count / node_count))

#input filenames
if __name__ == "__main__":
    main()




#generate random commodity pairs
