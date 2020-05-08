import pandas as pd

df = pd.read_csv('DT_MDL4.csv', index_col=False,
                 names=["ID", "p_if/class", "p_condition", "p_then", "p_node",
                                       "c_ID", "c_elif", "c_condition", "c_then", "c_node", "cc_ID",
                                       "cc_else","f_val"])


print(df.columns)
print(df)
df = df.astype(str)
df = df.replace({'p_then': {'then': 'begin'}, 'c_then':{'then': 'begin'}})

df['p_if/class'] = df['p_if/class'] + " ("+df['p_condition']+") "+df['p_then']

df['c_elif'] = df['c_elif'] + " ("+df['c_condition']+") "+df['c_then']

# df = df.replace({'p_if/class': r'^class.*$'}, {'p_if/class': 'class'}, regex=True)

print(df)

ndf = df[['ID', 'p_if/class', 'c_ID', 'c_elif', 'cc_ID', 'cc_else', 'f_val']]

print(ndf)

condition_dict = {}
for index, row in ndf:
    condition_dict[row[0]] = [row[1], row[2]]

print(condition_dict)