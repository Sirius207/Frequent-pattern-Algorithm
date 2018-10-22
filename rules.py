import csv
from algorithm.association_rules import find_rules


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # find association rules
    parser.add_argument('--minconfidence',
                       default=0.2,
                       help='minimum confidence')
    parser.add_argument('--input',
                       default='patterns.csv',
                       help='input file')
    parser.add_argument('--output',
                       default='rules.csv',
                       help='output file')
    args = parser.parse_args()

    with open(args.input, 'r') as input_file, open(args.output, 'w') as rules_output:

        reader = csv.DictReader(input_file)
        fp_dict = {
            row['pattern']: int(row['counts'])
            for row in reader
        }

        rules_output.write('rule,confidence,support\n')
        rules = find_rules(fp_dict, float(args.minconfidence))

        get_confidence = lambda rule: rule[1]
        rules.sort(key=get_confidence, reverse=True)

        for rule in rules:
            rule = map(str, rule)
            rules_output.write(','.join(rule))
            rules_output.write('\n')
