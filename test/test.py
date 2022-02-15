import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
# from statsmodels.tsa.holtwinters import ExponentialSmoothing
# from random import random

df = pd.read_csv('dest/data.csv')
df2 = df.copy()
df['Net Profit'] = df['Revenue'] - df['Cost']
df['Customer conversion rate'] = (df['No of transactions'] / df['Customer Traffic']) * 100
# df3 = df.copy()
# df3 = df3.drop(['Month'])
# # df['Sales']
# df = df.drop(['Cost','Revenue', 'No of transactions', 'Customer Traffic'], axis=1)
restructure = pd.melt(df, id_vars=['Month'], var_name="Indicators", value_name="Value")



help(df.iloc)


# colnames = ['Revenue','Cost','Av. Customers gained per month','Av. Customers lost per mont','Av. Sales per customer','No of transactions','Customer Traffic','Net Profit','Customer conversion rate']

# def col_corr(index):
#     return [df[colnames[index]].corr(df[colnames[0]]),
#         df[colnames[index]].corr(df[colnames[1]]),
#         df[colnames[index]].corr(df[colnames[2]]),
#         df[colnames[index]].corr(df[colnames[3]]),
#         df[colnames[index]].corr(df[colnames[4]]),
#         df[colnames[index]].corr(df[colnames[5]]),
#         df[colnames[index]].corr(df[colnames[6]]),
#         df[colnames[index]].corr(df[colnames[7]]),
#         df[colnames[index]].corr(df[colnames[8]])]

# rev = col_corr(0)
# cos = col_corr(1)
# av1 = col_corr(2)
# av2 = col_corr(3)
# av3 = col_corr(4)
# not1 = col_corr(5)
# ct = col_corr(6)
# np = col_corr(7)
# ccr = col_corr(8)

# trace = go.Heatmap(z=[rev,cos,av1,av2,av3,not1,ct,np,ccr],
#                    x=colnames,
#                    y=colnames)
# data=[trace]
# py.plot(data, filename='labelled-heatmap')

# print(df.corr())

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

    # dcc.Graph(id = 'my-graph',
    #     figure = {
    #         'data' : [
    #         {'x': df['Year'],'y':df['Revenue'],'type':'line'} 
    #         ]
    #     }


# @app.callback(Output('stats-table', 'data'),
#               [Input('my-dropdown', 'value')])

# def update_columns(rows):
#     # dff = restructure[restructure['Indicators'] == selected_dropdown_value]
#     for row in rows:
#         row['val'] = float(1)
#     return rows

# @app.callback(
#     Output('stats-table', 'data'),
#     [Input('stats-table', 'data_timestamp')],
#     [State('stats-table', 'data')])
# def update_columns(timestamp, rows):
#     for i in header:
#         for row in rows:
#                 row['val'] = float(i) ** 2
#     return rows

# if __name__ == '__main__':
#     app.run_server(debug=True)