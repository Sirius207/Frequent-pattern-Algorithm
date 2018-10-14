from algorithm.fpGrowth import FPGrowth


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
    args = parser.parse_args()

    with open(args.input, 'r') as input_file, open(args.output, 'w') as output:
        data_list = strToList(input_file)
        results = FPGrowth(data_list)
