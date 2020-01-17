import pandas as pd
# 구분자는 \t(탭) or , -> 확인 후 사용
df = pd.read_csv('C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\resources\\exam1.csv', delimiter=",")

df = df.dropna() # NaN제거 : 결측치 제거
# print(df)

list1 = df.values.tolist() # DataFrame > list
print(list1)
dict1 = df.to_dict() # DataFrame > Dictionary
print(dict1)