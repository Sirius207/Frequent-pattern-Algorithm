import pandas as pd
import time

from algorithm.fpGrowth import FPGrowth
from algorithm.apriori import Apriori


MINSUP_DICT = {
    't1_l5_n5': [0.005, 0.006, 0.007, 0.008, 0.009],
    't10_l5_n5': [0.005, 0.006, 0.007, 0.008, 0.009],
    't10_l5_n30': [0.002, 0.003, 0.004, 0.005],
    't20_l5_n30': [0.002, 0.003, 0.004, 0.005],
}
EXP_TIMES = 2


algorithm_dict = {
    'fpg': FPGrowth,
    'apr': Apriori
}

ibm_file_configs = [
    ['1', '5', '5'],
    ['10', '5', '5'],
    ['10', '5', '30'],
    ['20', '5', '30']
]

output_file_path = './results/ibm.csv'


def str_to_list(input_data):
    data_list = [
        data.replace(',\n', '').split(',')
        for data in input_data
    ]
    return data_list


def count_time(func, data_list, minsup):
    duration = 0
    for count in range(EXP_TIMES):
        start_time = time.time()
        fp_results = func(data_list, minsup)
        end_time = time.time()
        duration += (end_time - start_time)
    duration /= EXP_TIMES

    fp_num = len(fp_results.fp_dict.keys())

    return (duration, fp_num)


with open(output_file_path, 'w') as output:
    output.write('data,minsup,fp_num,algorithm,time\n')

    for file_config in ibm_file_configs:

        file_name = 't{}_l{}_n{}'.format(
            file_config[0], file_config[1], file_config[2])
        base_path = './data/IBM/proccessed/'
        input_file_path = base_path + file_name + '.data'

        with open(input_file_path, 'r') as input_file:

            data_list = str_to_list(input_file)
            data_length = len(data_list)

            for key in algorithm_dict:
                for current_minsup in MINSUP_DICT[file_name]:
                    (fp_duration, fp_num) = count_time(
                        algorithm_dict[key], data_list, int(current_minsup*data_length))
                    data = [file_name, str(current_minsup), str(
                        fp_num), key, str(fp_duration)]
                    print(data)

                    output.write(','.join(data))
                    output.write('\n')
