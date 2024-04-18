import subprocess
import glob

input_folder = 'input/datasource1/*'
output_file = 'output.csv'

input_files = glob.glob(input_folder)

with open(output_file, 'w') as outfile:
    for input_file in input_files:
        mapper_cmd = ['python', 'mapper.py']
        mapper_process = subprocess.Popen(mapper_cmd, stdin=open(input_file, 'r'), stdout=subprocess.PIPE, text=True)

        combiner_cmd = ['python', 'combiner.py']
        combiner_process = subprocess.Popen(combiner_cmd, stdin=mapper_process.stdout, stdout=subprocess.PIPE, text=True)
        mapper_process.stdout.close()

        sorted_combiner_output = sorted(combiner_process.stdout)

        reducer_input = "".join(sorted_combiner_output)
        reducer_cmd = ['python', 'reducer.py']
        reducer_output = subprocess.check_output(reducer_cmd, input=reducer_input, text=True)

        outfile.write(reducer_output)
