#This script will create the collated graph for the hard problem consisting of n subgraphs and the newly created edges between them

import sys
import random
import csv
import os
from graph_statistics_calculator import getGraphStatistics

def main():

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    number_clusters = int(sys.argv[3])
    cluster_size = int(sys.argv[4])

    total_edges_before_collation = 0
    generated_edges = 0
    # copy all of the connections within each graph into the collated graph as well as a newly created edge between the different clusters
    # finally, the collated graph must have the number of nodes and number of edges given as the first 2 lines.

    output_file_path = output_folder + "/collated_graph_" + str(int(number_clusters * cluster_size)) + ".bb"
    with open(output_file_path, "w") as collated_graph_output_object:
        cluster_idx = -1
        for filename in os.listdir(input_folder):
            if ".csv" in filename:
                #copy in each edge from the other graphs, but add cluster_idx * cluster_size to the node number for each cluster considered

                cluster_idx += 1

                with open(input_folder + "/" + filename, "r" ) as cluster_file_object:
                    cluster_file_csvreader = csv.reader(cluster_file_object, delimiter=',')
                    for line_split in cluster_file_csvreader:
                        outgoing_node = int(line_split[0])
                        incoming_node = int(line_split[1])

                        #change the node numbers based on the cluster idx
                        outgoing_node += (cluster_idx * cluster_size)
                        incoming_node += (cluster_idx * cluster_size)

                        collated_graph_output_object.write(str(outgoing_node) + " " + str(incoming_node) + " " + "1" + "\n")
                        total_edges_before_collation += 1

                    #generate random edges between current cluster and all clusters still remaining
                    for i in range(cluster_idx + 1, number_clusters):
                        new_outgoing_node = random.randint((cluster_idx * cluster_size) + 1, (cluster_idx * cluster_size) + cluster_size)
                        new_incoming_node = random.randint((i * cluster_size) + 1, (i * cluster_size) + cluster_size)
                        collated_graph_output_object.write(str(new_outgoing_node) + " " + str(new_incoming_node) + " " + "1" + "\n")
                        generated_edges += 1

        print("total edges generated between clusters is " + str(generated_edges))
    print("total edges before collation is " + str(total_edges_before_collation))

    #change the created graph file to add in the number of nodes and number of edges at the top

    edge_count, node_count, dummy1, dummmy2 = getGraphStatistics(output_file_path)

    #create a temporary new filename with the new collated graph
    temp_object_path = output_file_path + ".temp"
    with open(temp_object_path , "w") as temp_output_file_object:
        temp_output_file_object.write(str(node_count) + "\n")
        temp_output_file_object.write(str(edge_count) + "\n")
        with open(output_file_path, "r") as original_collated_file_object:
            for line in original_collated_file_object:
                temp_output_file_object.write(line)


    os.remove(output_file_path)
    os.rename(temp_object_path, output_file_path)




if __name__ == "__main__":

    main()

