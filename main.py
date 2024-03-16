import subprocess
import glob

# Ścieżka do folderu wejściowego zawierającego pliki danych
input_folder = 'input/datasource1/*'
# Ścieżka do pliku wyjściowego
output_file = 'output.txt'

# Lista wszystkich plików w folderze 'input/datasource'
input_files = glob.glob(input_folder)

# Otwarcie pliku wyjściowego do zapisu
with open(output_file, 'w') as outfile:
    for input_file in input_files:
        # Uruchomienie mapper.py dla każdego pliku i przechwycenie jego wyjścia
        mapper_cmd = ['python', 'mapper.py']
        mapper_process = subprocess.Popen(mapper_cmd, stdin=open(input_file, 'r'), stdout=subprocess.PIPE, text=True)

        # Uruchomienie combiner.py na wyjściu z mapper.py
        combiner_cmd = ['python', 'combiner.py']
        combiner_process = subprocess.Popen(combiner_cmd, stdin=mapper_process.stdout, stdout=subprocess.PIPE, text=True)
        mapper_process.stdout.close()  # Pozwala combiner_process na odbieranie EOF

        # Sortowanie wyników z combiner.py
        sorted_combiner_output = sorted(combiner_process.stdout)

        # Emulacja przekazania wyników z combiner.py do reducer.py
        reducer_input = "".join(sorted_combiner_output)
        reducer_cmd = ['python', 'reducer.py']
        reducer_output = subprocess.check_output(reducer_cmd, input=reducer_input, text=True)

        # Zapisanie wyniku działania reducer.py do pliku wyjściowego
        outfile.write(reducer_output)
