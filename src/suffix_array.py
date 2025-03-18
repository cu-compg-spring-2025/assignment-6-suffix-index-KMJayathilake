import argparse
import utils
import suffix_tree

SUB = 0
CHILDREN = 1

def build_suffix_array(T):
  
    tree = suffix_tree.build_suffix_tree(T)
    suffix_array = []
    stack = [(0, "")] 
    
    while stack:
        node_idx, suffix = stack.pop()
        
        if not tree[node_idx][CHILDREN]:  
            suffix_array.append(len(T) - len(suffix))
        
        for child in sorted(tree[node_idx][CHILDREN]):
            child_idx = tree[node_idx][CHILDREN][child]
            stack.append((child_idx, suffix + tree[child_idx][SUB]))
    
    return sorted(suffix_array)

def search_array(T, suffix_array, q):
   
    lo, hi = 0, len(suffix_array)
    
    while lo < hi:
        mid = (lo + hi) // 2
        suffix = T[suffix_array[mid]:]
        
        if suffix.startswith(q):
            return len(q)
        elif suffix < q:
            lo = mid + 1
        else:
            hi = mid
    
    return len(q) if q in T else 0

if __name__ == '__main__':
    def get_args():
        parser = argparse.ArgumentParser(description='Suffix Array')
        
        parser.add_argument('--reference',
                            help='Reference sequence file',
                            type=str)
        
        parser.add_argument('--string',
                            help='Reference sequence',
                            type=str)
        
        parser.add_argument('--query',
                            help='Query sequences',
                            nargs='+',
                            type=str)
        
        return parser.parse_args()
    
    def main():
        args = get_args()
        
        T = None
        if args.string:
            T = args.string
        elif args.reference:
            reference = utils.read_fasta(args.reference)
            T = reference[0][1]
        
        array = build_suffix_array(T)
        
        if args.query:
            for query in args.query:
                match_len = search_array(T, array, query)
                print(f'{query} : {match_len}')
    
    main()
