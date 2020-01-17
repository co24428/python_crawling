import pandas as pd
import glob

path = r'C:/Users/admin/Desktop/python_crawling/python_crawling/project/resources' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, encoding="euc-kr")
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print(frame)