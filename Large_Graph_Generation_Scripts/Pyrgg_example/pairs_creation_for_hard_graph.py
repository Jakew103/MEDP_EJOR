#this script will create the pairs file for the specified graph file.
#This file will create desired_prop * |V| for each cluster specified + 2 pairs for each inter cluster.

import random
import sys


#used to calculate the number of intercluster edges created for the graphs
def recursive_count(number):
    if number == 1:
        return 1
    else:
        return number + recursive_count(number -1)


def create_pairs_file(desired_prop, number_clusters, cluster_size, output_pairs_folder):

    total_pair_count = 0
    node_pair_map = dict()
    required_pairs_cluster = desired_prop * cluster_size
    required_intercluster_pairs = 5
    total_required_pairs = int((desired_prop * number_clusters * cluster_size) + (recursive_count(number_clusters - 1) * required_intercluster_pairs))
    
    
    with open(output_pairs_folder + "/" + "pairs_file_" + str(total_required_pairs) + ".rpairs", 'w') as output_file_object:

        #generate pairs for each intracluster
        for cluster_idx in range(0,number_clusters):

            intra_cluster_pair_count = 0
            while intra_cluster_pair_count < required_pairs_cluster:

                origin_node = random.randint((cluster_idx * cluster_size) + 1, (cluster_idx * cluster_size) + cluster_size)
                dest_node = random.randint((cluster_idx * cluster_size) + 1, (cluster_idx * cluster_size) + cluster_size)
                #origin node and destination node must be different
                if (origin_node != dest_node):

                    orig_to_dest_tuple = (origin_node, dest_node)
                    dest_to_orig_tuple = (dest_node, origin_node)

                    #the node pair can't already exist, in either permutation
                    if ((orig_to_dest_tuple not in node_pair_map.keys()) and (dest_to_orig_tuple not in node_pair_map.keys())):
                        node_pair_map[orig_to_dest_tuple] = True
                        node_pair_map[dest_to_orig_tuple] = True
                        output_file_object.write(str(origin_node) + " " + str(dest_node) + '\n')
                        intra_cluster_pair_count += 1
                        total_pair_count += 1

        #generate pairs for each intercluster
        for outgoing_cluster_idx in range(0,number_clusters):
            for incoming_cluster_idx in range(outgoing_cluster_idx + 1, number_clusters):
                inter_cluster_pair_count = 0
                #generate five pairs for intercluster
                while inter_cluster_pair_count < required_intercluster_pairs:
                    origin_node = random.randint((outgoing_cluster_idx * cluster_size) + 1,
                                                 (outgoing_cluster_idx * cluster_size) + cluster_size)
                    dest_node = random.randint((incoming_cluster_idx * cluster_size) + 1,
                                               (incoming_cluster_idx * cluster_size) + cluster_size)
                    # origin node and destination node must be different
                    if (origin_node != dest_node):

                        orig_to_dest_tuple = (origin_node, dest_node)
                        dest_to_orig_tuple = (dest_node, origin_node)

                        # the node pair can't already exist, in either permutation
                        if ((orig_to_dest_tuple not in node_pair_map.keys()) and (
                                dest_to_orig_tuple not in node_pair_map.keys())):
                            node_pair_map[orig_to_dest_tuple] = True
                            node_pair_map[dest_to_orig_tuple] = True
                            output_file_object.write(str(origin_node) + " " + str(dest_node) + '\n')
                            inter_cluster_pair_count += 1
                            total_pair_count += 1

    print(total_pair_count)
def main():

    desired_prop = float(sys.argv[1])
    output_folder = sys.argv[2]
    number_clusters = int(sys.argv[3])
    cluster_size = int(sys.argv[4])

    create_pairs_file(desired_prop, number_clusters, cluster_size, output_folder)


if __name__ == "__main__":

    main()
