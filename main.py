import pandas as pd
from pyeda.inter import exprvars, truthtable
from pyeda.boolalg.bdd import expr2bdd, bdd2expr

# === CONFIG ===
excel_file = 'dummy_truth_table.xlsx'  # Your Excel file
input_cols = [f'x{i}' for i in range(10)]  # x0 to x9

# === STEP 1: Load Excel File ===
df = pd.read_excel(excel_file)

# === STEP 2: Ensure all inputs/outputs are integers ===
df[input_cols + ['out']] = df[input_cols + ['out']].astype(int)

# Print the first few rows of the dataframe to ensure it's loaded correctly
print("First few rows of the truth table:")
print(df.head())

# === STEP 3: Sort rows to match binary counting order (required for pyeda) ===
df['input_tuple'] = df[input_cols].apply(tuple, axis=1)
df = df.sort_values('input_tuple')
df = df.drop(columns='input_tuple')

# === STEP 4: Extract outputs and define variables ===
outputs = df['out'].tolist()
vars = exprvars('x', 10)  # x[0], x[1], ..., x[9]

# === STEP 5: Build Truth Table ===
tt = truthtable(vars, outputs)

# === STEP 6: Convert Truth Table to Binary Decision Diagram (BDD) ===
bdd = expr2bdd(tt)  # Create Binary Decision Diagram (BDD)

# === STEP 7: Convert BDD to Boolean Expression (Using bdd2expr) ===
expr = bdd2expr(bdd)  # Convert the BDD to a Boolean expression

# === STEP 8: Print Result ===
print("✅ Simplified Boolean Expression:")
print(expr)  # Prints the Boolean expression
