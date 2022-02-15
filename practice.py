import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import plotly.offline as py
# import plotly.graph_objs as go
from statsmodels.tsa.holtwinters import ExponentialSmoothing, Holt


df = pd.read_csv('dest/data.csv',parse_dates=['Month'])
# df['Month'].freq = 'MS'
# df.index.freq = 'MS'
train, test = df.iloc[:130, 0], df.iloc[130:, 0]
# print(train.index)
# print(test.index)
model = ExponentialSmoothing(train, seasonal='add', seasonal_periods=12, trend='add').fit()
pred = model.predict(start=test.Month[0], end=test.Month[-1]+12)

plt.plot(train.Month, train, label='Train')
plt.plot(test.Month, test, label='Test')
plt.plot(pred.Month, pred, label='Holt-Winters')
plt.legend(loc='best')
plt.show()

# df = pd.read_csv('dest/data.csv',parse_dates=['Month'],index_col='Month')
# # df['Month'].freq = 'MS'
# df.index.freq = 'MS'
# train, test = df.iloc[:130, 0], df.iloc[130:, 0]
# # print(train.index)
# # print(test.index)
# model = ExponentialSmoothing(train, seasonal='add', seasonal_periods=12, trend='add').fit()
# pred = model.predict(start=test.index[0], end=test.index[-1]+12)

# plt.plot(train.index, train, label='Train')
# plt.plot(test.index, test, label='Test')
# plt.plot(pred.index, pred, label='Holt-Winters')
# plt.legend(loc='best')
# plt.show()

# df = pd.read_csv('Iowa_Liquor_Sales.csv')
# df2 = df[100,]
# df2

# df = pd.read_csv('dest/data.csv')
# df2 = df.copy()
# df['Net Profit'] = df['Revenue'] - df['Cost']
# df['Customer conversion rate'] = (df['No of transactions'] / df['Customer Traffic']) * 100
# # df3 = df.copy()
# # df3 = df3.drop(['Month'])
# # # df['Sales']
# # df = df.drop(['Cost','Revenue', 'No of transactions', 'Customer Traffic'], axis=1)
# restructure = pd.melt(df, id_vars=['Month'], var_name="Indicators", value_name="Value")



#


# def plot_corr(df, size=10):
#     corr = df.corr()
#     # fig, ax = plt.subplots(figsize=(size, size))
#     plt.matshow(corr)
#     plt.xticks(range(len(corr.columns)), corr.columns)
#     plt.yticks(range(len(corr.columns)), corr.columns)
#     plt.show()

# plot_corr(df)

# data = [x + random() for x in range(1, 100)]

# model = ExponentialSmoothing(data)
# model_fit = model.fit()

# yhat = model_fit.predict(len(data), len(data))
# print(yhat)

# app.css.append_css({
#     "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
# })

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')
# plt.matshow(df.corr())


    # data = {}
    # data['data'] = result
    # return data
    # return result_pd.to_dict('records')

# trace = go.Heatmap(z=df.corr())
# data=[trace]
# py.iplot(data, filename='basic-heatmap')