from algorithm.fpGrowth import FPGrowth
from algorithm.apriori import Apriori

# Constants
MINSUP = 2

def strToList(input_data):
    data_list = [
        data.replace('\n', '').split(',')
        for data in input_data
    ]
    return data_list


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
        data_list = strToList(input_file)

        fp_results = FPGrowth(data_list, MINSUP)
        ap_results = Apriori(data_list, MINSUP)
