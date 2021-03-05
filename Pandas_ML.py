import pandas as pd
from prettytable import PrettyTable
import datetime as dt

frame = pd.read_csv(r'C:\Admin\work\dataFrame.csv')

# print(frame.columns)
frame.drop([12,13], axis=0, inplace=True)
frame.rename(columns={'Local Times Activation Local Month':'month', 'Orders Number of Delivered Orders':'Orders',
                      'Orders Number of Active Couriers':'Couriers'}, inplace=True)
# print(frame.loc[[1, 2, 4, 5], ['Orders', 'Frequency']])
# frame['For NAs'] = ['Not NA']*8

frame.month = frame.month.apply(pd.to_datetime)

print(frame[(frame.Frequency >= 60)&(frame.month > dt.datetime(2020, 8, 1))])

pd.set_option('display.max_columns', 5)
print(frame)

# print(frame)