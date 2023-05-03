#!/bin/bash

# Define test cases
test_cases=(
"4\n1 2\n1 3\n1 4\n2 3\n" # Expected output: ['1', '2', '3']
"5\n1 2\n1 3\n2 3\n2 4\n3 4\n" # Expected output: ['1', '2', '3']
"6\n1 2\n1 3\n2 3\n2 4\n3 4\n4 5\n" # Expected output: ['2', '3', '4']
"1\n1 2\n" # Expected output: ['1', '2'] # Minimum input size
"2\n1 2\n3 4\n" # Expected output: ['1', '2'] # Multiple disconnected components
"3\n1 2\n1 3\n3 4\n" # Expected output: ['1'] # Maximal clique is smaller than largest connected component
"6\n1 2\n1 3\n2 3\n2 4\n3 4\n1 4\n" # Expected output: ['1', '2', '4'] # Maximal clique is larger than largest connected component
"7\n1 2\n1 3\n2 3\n2 4\n3 4\n4 5\n4 6\n" # Expected output: ['4'] 
"8\n1 2\n1 3\n1 4\n1 5\n1 6\n1 7\n2 3\n2 4\n" # Expected output: ['1'] # Maximal clique is the only clique
"10\n1 2\n1 3\n2 3\n2 4\n3 4\n4 5\n4 6\n5 6\n6 7\n7 5\n" # Expected output: ['4', '5', '6'] # Multiple maximal cliques
"11\n1 2\n1 3\n1 4\n1 5\n1 6\n2 3\n2 4\n2 5\n3 4\n3 5\n4 5\n" # Expected output: ['1', '2', '3', '4', '5'] # Maximal clique is the entire graph
"15\n1 2\n1 3\n2 3\n2 4\n3 4\n4 5\n5 6\n5 7\n6 7\n7 8\n8 9\n9 10\n10 11\n11 12\n12 10\n" # Expected output: ['5', '6', '7']
"8\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n4 5\n5 6\n" # Expected output: ['4'] 
)







# Run tests
for test_case in "${test_cases[@]}"; do
    echo "Running test: $test_case"
    echo -e "$test_case" | python3 ./cs412_maxclique_approx.py
    echo "======================================"
done

#!/bin/bash

# Run tests from input file
while read -r m; do
  echo "Running test with $m edges:"
  # Read the edges
  edges=""
  for i in $(seq 1 $m); do
    read -r edge
    edges+="$edge"$'\n'
  done

  # Measure start time
  start_time=$(date +%s)

  # Run the test
  echo -e "$m\n$edges" | python3 ./cs412_maxclique_approx.py

  # Measure end time
  end_time=$(date +%s)

  # Calculate and display runtime
  runtime=$((end_time - start_time))
  echo "Runtime: ${runtime}s"
  echo "======================================"
done < input_file.txt
