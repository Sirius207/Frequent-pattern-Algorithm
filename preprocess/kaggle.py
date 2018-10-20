
with open('../data/Kaggle/cart_dataset.txt', 'r') as input, open('../data/Kaggle/cart_dataset_v2.txt', 'w') as output:
    for transaction_str in input:
        transaction = transaction_str.split(',')
        transaction.pop()
        for item in set(transaction):
            if item[0] == ' ':
                new_item = item.replace(' ', '', 1)
                output.write(new_item + ',')
            else:
                output.write(item + ',')
        output.write('\n')


