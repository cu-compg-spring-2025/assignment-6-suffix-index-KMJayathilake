import time
import random
import matplotlib.pyplot as plt
import suffix_trie
import suffix_tree
import suffix_array


def generate_random_dna(length):
    return ''.join(random.choices("ACGT", k=length))


def measure_build_time(build_function, text):
    start_time = time.time()
    structure = build_function(text)
    end_time = time.time()
    return structure, end_time - start_time


def measure_search_time(search_function, structure, queries):
    times = []
    for query in queries:
        start_time = time.time()
        search_function(structure, query)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


def run_experiment():
    text_length = 1000  
    num_queries = 100  
    query_lengths = [10, 20, 30, 40, 50]  

    dna_sequence = generate_random_dna(text_length)

    
    trie, trie_build_time = measure_build_time(suffix_trie.build_suffix_trie, dna_sequence)
    tree, tree_build_time = measure_build_time(suffix_tree.build_suffix_tree, dna_sequence)
    array, array_build_time = measure_build_time(suffix_array.build_suffix_array, dna_sequence)

    build_times = {
        "Suffix Trie": trie_build_time,
        "Suffix Tree": tree_build_time,
        "Suffix Array": array_build_time,
    }

    
    queries = [generate_random_dna(length) for length in query_lengths]

    
    trie_search_times = measure_search_time(suffix_trie.search_trie, trie, queries)
    tree_search_times = measure_search_time(suffix_tree.search_tree, tree, queries)
    array_search_times = measure_search_time(lambda structure, q: suffix_array.search_array(dna_sequence, structure, q), array, queries)




 
    plt.figure(figsize=(10, 5))
    plt.bar(build_times.keys(), build_times.values(), color=["blue", "green", "red"])
    plt.xlabel("Data Structure")
    plt.ylabel("Time (seconds)")
    plt.title("Build Time Comparison")
    plt.show()

    
    plt.figure(figsize=(10, 5))
    plt.plot(query_lengths, trie_search_times, label="Suffix Trie", marker="o")
    plt.plot(query_lengths, tree_search_times, label="Suffix Tree", marker="s")
    plt.plot(query_lengths, array_search_times, label="Suffix Array", marker="^")
    plt.xlabel("Query Length")
    plt.ylabel("Time (seconds)")
    plt.title("Search Time Comparison")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_experiment()
