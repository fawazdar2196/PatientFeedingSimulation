import csv
from itertools import product

# Differentiating factors and their possible values
graphs = ['random', 'scale-free']
dags = [True, False]
confoundings = [True, False]
densities = [0.1, 0.5]  # Example values, replace with actual density values
effects = [0.1, 0.5]  # Example values, replace with actual effect values
interventions = [True, False]

# Methods to compare
methods = ['inspre', 'inspre_DAG', 'LLCB']

# Generate all 64 possible combinations of the six differentiating factors
data_combinations = list(product(graphs, dags, confoundings, densities, effects, interventions))

# Define a function to simulate results for each method (replace with actual computations if needed)
def simulate_result(method, graph, dag, confounding, density, effect, intervention):
    # Placeholder for actual method result computation
    return {
        'method': method,
        'result': f"Simulated_{method}_{graph}_{dag}_{confounding}_{density}_{effect}_{intervention}"
    }

# Prepare CSV header
header = ['graph', 'DAG', 'confounding', 'density', 'effects', 'intervention', 'method', 'result']

# Write to CSV file
with open('results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    
    for data in data_combinations:
        graph, dag, confounding, density, effect, intervention = data
        
        # For each dataset, run all three methods and store results
        for method in methods:
            result = simulate_result(method, graph, dag, confounding, density, effect, intervention)
            # Append the result row
            writer.writerow([graph, dag, confounding, density, effect, intervention, method, result['result']])

print("CSV generation complete. Check 'results.csv' for output.")
