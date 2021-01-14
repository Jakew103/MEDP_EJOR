#edges::

#format is

#num edges
#num nodes
#node1 node2 weight
# .
# .
# .
#to generate the graph_file (.bb), just calculate num edges, nodes and then copy the rest of the graph file

import os
from new_graph_generation.graph_statistics_calculator import getGraphStatistics
import random
import sys


#all nodes are indexed from 1

#Steps -
#1 create new output file,
#2 randomly select pairs from (1 - node_count) without duplicates
#3  write pairs in the output file.
#INPUTS - desired proportion of nodes to form pairs, total nodes in the graph, output folder for the pairs, output filename for pairs file
#OUTPUT - None
def create_pairs_file(desired_prop, node_count, output_pairs_folder, output_filename):

    node_pair_map = dict()
    with open(output_pairs_folder + "/" + output_filename, 'w') as output_file_object:
        pair_count = 0
        while pair_count < (desired_prop * node_count):
            origin_node = random.randint(1, node_count)
            dest_node = random.randint(1, node_count)
            #origin node and destination node must be different
            if (origin_node != dest_node):

                orig_to_dest_tuple = (origin_node, dest_node)
                dest_to_orig_tuple = (dest_node, origin_node)

                #the node pair can't already exist, in either permutation
                if ((orig_to_dest_tuple not in node_pair_map.keys()) and (dest_to_orig_tuple not in node_pair_map.keys())):
                    node_pair_map[orig_to_dest_tuple] = True
                    node_pair_map[dest_to_orig_tuple] = True
                    output_file_object.write(str(origin_node) + " " + str(dest_node) + '\n')
                    pair_count += 1




# desired proportions=  0.40 |V|
# read in each graph and insert node count and edge count at the top of the file.
# for each graph type, create 0.4 |V| pairs file

def create_graphs_pairs_files(graph_input_filename_folder, output_graphs_folder, output_pairs_folder):


    desired_props = [0.4]

    for filename in os.listdir(graph_input_filename_folder):
        if ".csv" in filename:
            edge_count, node_count, dummy1, dummmy2 = getGraphStatistics(graph_input_filename_folder + "/" + filename)
            filename_copy = filename
            output_filename = filename_copy.replace(".csv",".bb")
            with open(output_graphs_folder + "/" + output_filename, 'w') as graph_output_fileobject:
                #insert node count and edge count at the top of the file.
                graph_output_fileobject.write(str(node_count) + "\n")
                graph_output_fileobject.write(str(edge_count) + "\n")
                with open(graph_input_filename_folder + "/" + filename, 'r') as graph_input_fileobject:
                    #copy line by line from input to output file
                    for line in graph_input_fileobject:
                        line = line.replace("," , " ")
                        graph_output_fileobject.write(line)

            #create the pairs files
            for desired_prop in desired_props:
                pairs_filename = output_filename.replace(".bb", "")
                pairs_filename += ("_" + str(desired_prop) + ".rpairs")
                create_pairs_file(desired_prop, node_count, output_pairs_folder, pairs_filename)

def main():


    output_graphs_folder = sys.argv[1]
    output_pairs_folder = sys.argv[2]
    graph_input_filename_folder = sys.argv[3]
    #these are the generated graphs from the pyrgg software
    create_graphs_pairs_files(graph_input_filename_folder, output_graphs_folder, output_pairs_folder)



if __name__ == "__main__":
    main()
