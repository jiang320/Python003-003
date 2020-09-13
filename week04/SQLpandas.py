import pandas as pd


filename = 'input.csv'
# with open(filename, "r", encoding='utf-8') as f:
#     for line in f:
#         print(line)

data=pd.read_csv(filename,header=None)
data.columns = ['id','type', 'number', 'publishtime']
#1. SELECT * FROM data;
print(data)
# 2. SELECT * FROM data LIMIT 10;
print(data[:10])
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data.id)
# 4. SELECT COUNT(id) FROM data;
print(data.id.count())
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data.id<1000)&(data.publishtime>1988)])
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(data.groupby('id')['type'].unique)
print("----------------------------------------------")
filename2 = 'input2.csv'
data2=pd.read_csv(filename2,header=None)
data2.columns = ['id','type', 'number', 'publishtime']
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(data,data2,on='id',how='inner'))
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([data,data2]).drop_duplicates())
# 9. DELETE FROM table1 WHERE id=10;
print(data[data.id!=4])
# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(data.drop('number',axis=1))