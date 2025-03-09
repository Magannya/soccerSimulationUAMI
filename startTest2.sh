#!/bin/bash

# Number of processes to launch
NUM_PROCESSES=10

# Command to run (replace with your actual command)
COMMAND="python3 t2-2.py"

# Launch processes in parallel
for ((i=1; i<=NUM_PROCESSES; i++)); do
    echo "Starting process $i..."
    $COMMAND &
done

# Wait for all background processes to finish
wait

echo "All processes completed."
