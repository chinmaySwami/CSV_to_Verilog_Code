import pandas as pd

# Removeing starting spaces in notepad++
#      Find : ^\s+
# Search mode -- tick regular expression

# Enter csv file name
csv_file_name = 'DT_MDL4.csv'

# Verilog File name
verilog_file_name = 'dummy_test.v'

df = pd.read_csv(csv_file_name, index_col=False,
                 names=["ID", "p_if/class", "p_condition", "p_then", "p_node",
                                       "c_ID", "c_elif", "c_condition", "c_then", "c_node", "cc_ID",
                                       "cc_else","f_val"])

# print(df.columns)
# print(df)


df["ID"] = df["ID"].astype('float32')

df = df.astype(str)
df = df.replace({'p_then': {'then': 'begin'}, 'c_then':{'then': 'begin'}, 'c_elif':{'elseif': 'else if'}})

df['p_if/class'] = df['p_if/class'] + " ("+df['p_condition']+") "+df['p_then']

df['c_elif'] = df['c_elif'] + " ("+df['c_condition']+") "+df['c_then']

# df = df.replace({'p_if/class': r'^class.*$'}, {'p_if/class': 'class'}, regex=True)

ndf = df[['ID', 'p_if/class', 'c_ID', 'c_elif', 'cc_ID', 'cc_else', 'f_val']]

condition_dict = {}
for index, row in ndf.iterrows():
    condition_dict[row[0]] = [row[1], row[2]]

code = ""
for index, row in ndf.iterrows():
    if index == 0:
        code += row[1] + "\n "+ "$*"+str(row[2])+"*$"+" \n"+"end \n"
        code += row[3] + "\n" + "$*" + str(row[4]) + "*$" + "\n" + "end \n"
    else:
        if not 'class' in row[1]:
            strs1 =  row[1] + "\n"+ "$*"+str(row[2])+"*$"+"\n"+"end \n"
            strs2 = row[3] + "\n" + "$*" + str(row[4]) + "*$" + "\n" + "end \n"

            code = code.replace("$*"+str(row[0])+"*$", strs1+strs2)
        else:
            strs = row[1].replace('(=)', '=') + ';'
            code = code.replace("$*" + str(row[0]) + "*$", strs)


code += "\n "+ "end \n"+ "endmodule"
print(code)

# Writing the code to file
with open(verilog_file_name, "a") as f:
    f.write(code)
