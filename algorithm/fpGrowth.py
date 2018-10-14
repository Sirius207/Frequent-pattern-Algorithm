from algorithm.utility import FPTree

class FPGrowth:
    def __init__(self, input_data):
        self.item_counts = self._count_items(input_data)
        self.sorted_data = self._sort_items(input_data)
        self.fp_tree = self._build_FPTree(self.sorted_data)

    def _count_items(self, input_data):
        item_counts = {}
        for data in input_data:
            for item in data:
                if item not in item_counts:
                    item_counts[item] = 1
                else:
                    item_counts[item] += 1
        return item_counts

    def _sort_items(self, input_data):
        def sortByCounts(item):
            return self.item_counts[item]

        def sort_transaction(transaction):
            transaction.sort(key=sortByCounts, reverse=True)
            return transaction

        return list(map(sort_transaction, input_data))


    def _build_FPTree(self, data_list):
        Root = FPTree()
        current_node = Root
        for transaction in data_list:
            for item in transaction:
                current_node.insert_node(item)
                current_node = current_node.children[item]
            current_node = Root

        return Root

    def _generate_fp(self, ):
        pass



