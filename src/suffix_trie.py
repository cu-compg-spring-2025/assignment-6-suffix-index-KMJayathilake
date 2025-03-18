import argparse
import utils

def get_args():
    parser = argparse.ArgumentParser(description='Suffix Trie')

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

class SuffixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class SuffixTrie:
    def __init__(self, text):
        self.root = SuffixTrieNode()
        self.build_suffix_trie(text)
    
    def build_suffix_trie(self, s):
        """Constructs a suffix trie for the given string."""
        for i in range(len(s)):
            current_node = self.root
            for char in s[i:]:
                if char not in current_node.children:
                    current_node.children[char] = SuffixTrieNode()
                current_node = current_node.children[char]
            current_node.is_end_of_word = True
    
    def search_trie(self, pattern):
        """Searches for a pattern in the suffix trie and returns the prefix overlap length."""
        current_node = self.root
        match_length = 0
        
        for char in pattern:
            if char in current_node.children:
                current_node = current_node.children[char]
                match_length += 1
            else:
                break
        
        return match_length

def build_suffix_trie(s):
    return SuffixTrie(s)

def search_trie(trie, pattern):
    return trie.search_trie(pattern)

if __name__ == '__main__':
    import argparse
    import utils

    def get_args():
        parser = argparse.ArgumentParser(description='Suffix Trie')

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

        trie = build_suffix_trie(T)

        if args.query:
            for query in args.query:
                match_len = search_trie(trie, query)
                print(f'{query} : {match_len}')

    main()
