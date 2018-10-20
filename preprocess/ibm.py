
file_configs = [
    ['1','5','5'],
    ['10','5','5'],
    ['10','5','10'],
    ['10','5','15'],
    ['10','5','20'],
    ['10','5','25'],
    ['10','5','30'],
    ['20','5','30'],
]

for file_config in file_configs:

    file_name = 't{}_l{}_n{}.data'.format(file_config[0], file_config[1], file_config[2])

    base_path = '../data/IBM'
    input_file_path = base_path + '/raw/' + file_name
    output_file_path = base_path + '/proccessed/' + file_name

    with open(input_file_path, 'r') as input, open(output_file_path, 'w') as output:
        line_index = '1'
        for line in input.readlines():
            line_data = list(filter(None, line.split(' ')))
            current_line_index = line_data[0]
            line_value = line_data[2].replace('\n', '')
            if line_index == current_line_index:
                output.write(line_value + ',')
            else:
                output.write('\n')
                output.write(line_value + ',')
                line_index = current_line_index


