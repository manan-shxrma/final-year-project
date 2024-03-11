import os
import pandas as pd

df1 = pd.read_csv("train_test_sets/1/split_3585_642_1016.csv")
df1.columns = ['set', 'label', 'video_frame']

df2 = pd.read_csv("train_test_sets/1/split_4252_642_987.csv")
df2.columns = ['set', 'label', 'video_frame']

df3 = pd.read_csv("train_test_sets/1/split_4527_642_978.csv")
df3.columns = ['set', 'label', 'video_frame']

df4 = pd.read_csv("train_test_sets/1/split_4550_642_940.csv")
df4.columns = ['set', 'label', 'video_frame']

df5 = pd.read_csv("train_test_sets/1/split_4686_642_972.csv")
df5.columns = ['set', 'label', 'video_frame']

df_combined1 = pd.concat([df1, df2, df3, df4, df5], ignore_index = True)

print(df_combined1.head())
print(df_combined1.info())

df6 = pd.read_csv("train_test_sets/2/split_3394_642_987.csv")
df6.columns = ['set', 'label', 'video_frame']

df7 = pd.read_csv("train_test_sets/2/split_4469_642_993.csv")
df7.columns = ['set', 'label', 'video_frame']

df8 = pd.read_csv("train_test_sets/2/split_4594_642_964.csv")
df8.columns = ['set', 'label', 'video_frame']

df9 = pd.read_csv("train_test_sets/2/split_4766_642_999.csv")
df9.columns = ['set', 'label', 'video_frame']

df10 = pd.read_csv("train_test_sets/2/split_4789_642_976.csv")
df10.columns = ['set', 'label', 'video_frame']

df_combined2 = pd.concat([df6, df7, df8, df9, df10], ignore_index = True)

print(df_combined2.head())
print(df_combined2.info())


df11 = pd.read_csv("train_test_sets/3/split_3307_642_1027.csv")
df11.columns = ['set', 'label', 'video_frame']

df12 = pd.read_csv("train_test_sets/3/split_4491_642_962.csv")
df12.columns = ['set', 'label', 'video_frame']

df13 = pd.read_csv("train_test_sets/3/split_4632_642_1054.csv")
df13.columns = ['set', 'label', 'video_frame']

df14 = pd.read_csv("train_test_sets/3/split_4734_642_950.csv")
df14.columns = ['set', 'label', 'video_frame']

df15 = pd.read_csv("train_test_sets/3/split_4783_642_963.csv")
df15.columns = ['set', 'label', 'video_frame']

df_combined3 = pd.concat([df11, df12, df13, df14, df15], ignore_index = True)

print(df_combined3.head())
print(df_combined3.info())

df16 = pd.read_csv("train_test_sets/4/split_3239_642_1007.csv")
df16.columns = ['set', 'label', 'video_frame']

df17 = pd.read_csv("train_test_sets/4/split_4206_642_1020.csv")
df17.columns = ['set', 'label', 'video_frame']

df18 = pd.read_csv("train_test_sets/4/split_4395_642_963.csv")
df18.columns = ['set', 'label', 'video_frame']

df19 = pd.read_csv("train_test_sets/4/split_4489_642_977.csv")
df19.columns = ['set', 'label', 'video_frame']

df20 = pd.read_csv("train_test_sets/4/split_4749_642_1012.csv")
df20.columns = ['set', 'label', 'video_frame']

df_combined4 = pd.concat([df16, df17, df18, df19, df20], ignore_index = True)

print(df_combined4.head())
print(df_combined4.info())


df = pd.concat([df_combined1, df_combined2], ignore_index=True)
print(df.head())
print(df.info())

dataset = 'dataset.csv'
df.to_csv(dataset, index=False)