import subprocess
import os
import sys

THRESHOLD = os.environ.get('THRESHOLD', 0.05)

# Check if the path argument was provided
if len(sys.argv) < 2:
    print("Please provide the path as an argument")
    sys.exit(1)

# Get the path from the arguments
path = sys.argv[1]

# Execute the bash command
command = f". ~/.bashrc && ENGINES=\"v8 jsc\" bash /Users/don/Desktop/wish-you-were-fast/wasm/compare-engines.bash {path}"
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
out, err = process.communicate()

out = out.decode('utf-8').replace('\x08', '')
lines = out.split('\n')

try:
    v8_line = lines[1]
    jsc_line = lines[2]
    # Split the values, convert them to float and calculate the average
    v8_values = [float(value) for value in v8_line.split(':')[1].split()]
    v8_average = sum(v8_values) / len(v8_values)

    jsc_values = [float(value) for value in jsc_line.split(':')[1].split()]
    jsc_average = sum(jsc_values) / len(jsc_values)

    # Calculate the difference and check if it's more than 10%
    difference = max(v8_average, jsc_average) / min(v8_average, jsc_average)
    print(f"V8: {v8_average}, JSC: {jsc_average}, Difference: {difference}", file=sys.stderr)
    interesting = difference > 1 + THRESHOLD
    if interesting:
        sys.exit(1)
    else:
        sys.exit(0)
except IndexError:
    print("Could not find values in the output")
    sys.exit(0)
