import time

from algorithm.fpGrowth import FPGrowth
from algorithm.apriori import Apriori

def str_to_list(input_data):
    data_list = [
        data.replace(',\n', '').split(',')
        for data in input_data
    ]
    return data_list

def get_results(func, data_list, minsup):
    start_time = time.time()
    fp_results = func(data_list, minsup)
    end_time = time.time()
    duration = end_time - start_time

    return (duration, fp_results)

algorithm_list = {
    'fp': FPGrowth,
    'ap': Apriori
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                       default='data/sample.txt',
                       help='input data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    parser.add_argument('--minsup',
                       default=0.3,
                       help='input minsup')
    parser.add_argument('--algorithm',
                       default='fp',
                       help='frequent pattern algorithm')

    args = parser.parse_args()

    with open(args.input, 'r') as input_file, open(args.output, 'w') as output:
        # Part: 1
        # find frequent patterns
        #
        output.write('pattern,counts\n')

        data_list = str_to_list(input_file)

        fp_algorithm = algorithm_list[args.algorithm]
        minsup = int( float(args.minsup) * len(data_list) )
        (fp_duration, fp_results) = get_results(fp_algorithm, data_list, minsup)

        for key in fp_results.fp_dict:
            output.write(str(key) + ',' + str(fp_results.fp_dict[key]))
            output.write('\n')

        print(fp_duration)
