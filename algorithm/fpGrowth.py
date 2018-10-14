from algorithm.utility import FPTree


class FPGrowth:
    def __init__(self, input_data):
        self.item_counts = self._count_items(input_data)
        self.sorted_items = self._get_sorted_items(self.item_counts)
        self.sorted_data = self._sort_data(input_data)
        self.fp_tree = self._build_FPTree(self.sorted_data)

    #
    # Part 1: Basic Process
    #
    def _count_items(self, input_data):
        item_counts = {}
        for data in input_data:
            for item in data:
                if item not in item_counts:
                    item_counts[item] = 1
                else:
                    item_counts[item] += 1
        return item_counts

    def _sort_transaction(self, transaction, reverse=True):
        def sortByCounts(item):
            return self.item_counts[item]

        transaction.sort(key=sortByCounts, reverse=reverse)
        return transaction

    def _get_sorted_items(self, item_counts):
        return self._sort_transaction(list(item_counts.keys()), False)

    def _sort_data(self, input_data):
        return list(map(self._sort_transaction, input_data))

    def _build_FPTree(self, data_list):
        Root = FPTree()
        current_node = Root
        for transaction in data_list:
            # When combining suffix patterns, input type is string
            if isinstance(transaction, str):
                transaction = transaction.split(',')

            for item in transaction:
                current_node.insert_node(item)
                current_node = current_node.children[item]
            current_node = Root

        return Root

    #
    # Part 2: Frequent Patterns
    #

    def find_fp(self, minsup):
        def find_suffix_patterns(item, current_node, storage):
            for node_name in current_node.children:
                next_node = current_node.children[node_name]
                if node_name == item:
                    for i in range(next_node.counts):
                        storage['suffix_patterns'].append(','.join(storage['path_list']))
                elif next_node.children != None:
                    storage['path_list'].append(node_name)
                    find_suffix_patterns(item, next_node, storage)

            if storage['path_list']:
                storage['path_list'].pop()


        def find_single_fp(item, current_node, path_list, fp_dict):
            if current_node.children != None:
                for node_name in current_node.children:
                    next_node = current_node.children[node_name]
                    path_list.append(node_name)
                    current_path = ','.join(path_list)

                    if len(path_list) != 1:
                        full_path = node_name + ',' + item
                        if full_path not in fp_dict:
                            fp_dict[full_path] = next_node.counts
                        else:
                            fp_dict[full_path] += next_node.counts

                    if len(current_path) > 0:
                        full_path = current_path + ',' + item
                        if full_path not in fp_dict:
                            fp_dict[full_path] = next_node.counts
                        else:
                            fp_dict[full_path] += next_node.counts

                    find_single_fp(item, next_node, path_list, fp_dict)
                if path_list:
                    path_list.pop()
            else:
                path_list.pop()

        fp_dict = {}
        for item in self.sorted_items:
            # find suffix patterns
            storage = {
                'suffix_patterns': [],
                'path_list': [],
            }
            find_suffix_patterns(item, self.fp_tree, storage)
            # pattern combination
            combined_pattern = self._build_FPTree(storage['suffix_patterns'])
            find_single_fp(item, combined_pattern, [], fp_dict)

        # remove patterns that < minsup
        pop_list = []
        for key in self.item_counts:
            fp_dict[key] = self.item_counts[key]

        for key in fp_dict:
            if fp_dict[key] < minsup:
               pop_list.append(key)

        for key in pop_list:
            fp_dict.pop(key, 'None')

        print(fp_dict)
        return fp_dict

