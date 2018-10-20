import time

from algorithm.fpGrowth import FPGrowth
from algorithm.apriori import Apriori

# Constants
MINSUP = 2

def str_to_list(input_data):
    data_list = [
        data.replace(',\n', '').split(',')
        for data in input_data
    ]
    return data_list

def count_time(func):
    start_time = time.time()
    fp_results = func(data_list, MINSUP)
    end_time = time.time()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                       default='data/sample.txt',
                       help='input data file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    parser.add_argument('--minsup',
                       default=2,
                       help='input minsup')
    args = parser.parse_args()

    with open(args.input, 'r') as input_file, open(args.output, 'w') as output:
        data_list = str_to_list(input_file)
        print(data_list)

        time_list = []

        start_time = time.time()
        fp_results = FPGrowth(data_list, MINSUP)
        end_time = time.time()
        duration = end_time - start_time
        time_list.append(duration)

        start_time = time.time()
        ap_results = Apriori(data_list, MINSUP)
        end_time = time.time()
        duration = end_time - start_time
        time_list.append(duration)

        print(time_list)