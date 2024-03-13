#!/bin/zsh

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 test_size"
    exit 1
fi

# Get the test size from the argument
test_size=$1

# Run the command 16 times
for i in {1..16}
do
   ./reverse_engineer.native $test_size
done
