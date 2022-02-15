import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
from collections import defaultdict
import plotly.graph_objs as go
import plotly.plotly as py
from statsmodels.tsa.holtwinters import ExponentialSmoothing, Holt

app = dash.Dash()

#read data
#----------------------------------------------
df = pd.read_csv('data.csv',parse_dates=["Month"])
df3 = pd.read_csv('data.csv',parse_dates=["Month"],index_col='Month')
#data cleanin (restructure).
#----------------------------------------------
df2 = df.copy()
df['Net Profit'] = df['Revenue'] - df['Cost']
df['Customer conversion rate'] = (df['No of transactions'] / df['Customer Traffic']) * 100
# df['Sales']
# df = df.drop(['Cost','Revenue', 'No of transactions', 'Customer Traffic'], axis=1)
restructure = pd.melt(df, id_vars=['Month'], var_name="Indicators", value_name="Val")
restructure2 = pd.melt(df3, id_vars=['Month'], var_name="Indicators", value_name="Val")
restructure2.index.freq = 'MS'
#----------------------------------------------

colnames = ['Revenue','Cost','Av. Customers gained per month',
            'Av. Customers lost per mont','Av. Sales per customer',
            'No of transactions','Customer Traffic','Net Profit','Customer conversion rate']

def col_corr(index):
    return [df[colnames[index]].corr(df[colnames[0]]),
        df[colnames[index]].corr(df[colnames[1]]),
        df[colnames[index]].corr(df[colnames[2]]),
        df[colnames[index]].corr(df[colnames[3]]),
        df[colnames[index]].corr(df[colnames[4]]),
        df[colnames[index]].corr(df[colnames[5]]),
        df[colnames[index]].corr(df[colnames[6]]),
        df[colnames[index]].corr(df[colnames[7]]),
        df[colnames[index]].corr(df[colnames[8]])]

rev = col_corr(0)
cos = col_corr(1)
av1 = col_corr(2)
av2 = col_corr(3)
av3 = col_corr(4)
not1 = col_corr(5)
ct = col_corr(6)
np = col_corr(7)
ccr = col_corr(8)
# -----------------
#Charts Layout
app.layout = html.Div(children=[
    html.H2('Descriptive Analytics'),
    dcc.Dropdown(
        id = 'my-dropdown',
        options=[{'label': i, 'value': i} for i in restructure.Indicators.unique()],
        value = restructure.Indicators[0]
        ),
    dcc.Graph(
        id = 'my-graph'
        ),
    dcc.Graph(id = 'corrm',
            figure = {
                'data': [
                    go.Heatmap(z=[rev,cos,av1,av2,av3,not1,ct,np,ccr],
                               x=colnames,
                               y=colnames)
                ]
            }),
    html.Div([
        dash_table.DataTable(
        id = "stats-table",

        columns=[
            {'name': 'Statistical Metric', 'id': 'statmet'},
            {'name': 'Value', 'id': 'val'}
        ],
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        html.H3("Interpretations"),   
        html.P("Mean: Mean is the average you're used to, where you add up all the numbers and then divide by the number of numbers. It tries to show the average value (distribution) in a list of values."),
        html.P("Standard Error of Mean: Standard error of the mean measures how far the sample mean of the data is likely to be from the true population mean"),
        html.P("Median: Median is the middle value in the vector of numbers."),
        html.P("Mode: Mode is the value that occurs most often. If no number in the vector is repeated, then there is no mode for the vector"),
        html.P("Standard Deviation: Standard deviation measures the amount of variability or dispersion for a subject set of data from the mean"),
        html.P("Variance: Variance is a measurement of the span of numbers in a data set. The variance measures the distance each number in the set is from the mean."),
        html.P("Kurtosis: Kurtosis measures the degree of outlier-prone a data is (whether the data are less outlier-prone or more outlier-prone than the normal distribution).\
             Data sets with high kurtosis are more prone to outliers which implies occasional wild values and vice versa."),
        html.P("Skewness: Skewness describes the degree a set of data varies from the normal distribution in a set of statistical data"),
        html.P("Range: Range of a list a numbers is the difference between the largest and smallest values"),
        html.P("Minimum: Minimum refers to the least value in the series"),
        html.P("Maximum: Maximum refers to the highest value in the series"),
        html.P("Sum: Sum refers to an aggregation (addition) of the values in a series"),
        html.P("Count: Count refers to the number of values in a series"),
        html.P("Lower Quartile: The lower quartile is the number below which lies the 25 percent of the bottom data."),
        html.P("Upper Quartile: The upper quartile has 75 percent of the data below it and the top 25 percent of the data above it."),
        html.P("IQR: IQR short for Interquartile range is the difference between the lower quartile and the upper quartile. It is usually unaffected by extreme values."),

    ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),

        html.Div([
            html.H2("Predictive Analytics"),
            dcc.Dropdown(
                    id = 'pred-dropdown',
                    options=[{'label': i, 'value': i} for i in restructure.Indicators.unique()],
                    value = restructure.Indicators[0]
                    ),
            dcc.Graph(
                    id = 'pred-graph'
                    ),
        ])
])

@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    dff = restructure[restructure['Indicators'] == selected_dropdown_value]
    return {
        'data': [{
            'x': dff.Month,
            'y': dff.Val,
            'line': {
                'width': 3,
                'shape': 'spline'
            }
        }]
    }

@app.callback(Output('stats-table', 'data'),
              [Input('my-dropdown', 'value')])
def update_columns(selected_dropdown_value):
    return generate_stats_dict(df[selected_dropdown_value])

def generate_stats_dict(df_column):
    result = {
        'Arithmetic Mean': df_column.mean(),
        'Standard Error of Mean': df_column.sem(),
        'Median': df_column.median(),
        # 'Mode': df_column.mode(),
        'Standard Deviation': df_column.std(),
        'Variance': df_column.var(),
        'Kurtosis': df_column.kurtosis(),
        'Skewness': df_column.skew(),
        'Range': df_column.max() - df_column.min(),
        'Minimum': df_column.min(),
        'Maximum': df_column.max(),
        'Sum': df_column.sum(),
        'Count': df_column.count(),
        'Lower quartile': df_column.quantile([0.25]),
        'Upper quartile': df_column.quantile([0.75]),
        'IQR': df_column.quantile([0.75]) - df_column.quantile([0.25]),
        'Lower limit': 0.0,
        'Upper limit': 0.0,
    }
    return [ {'statmet': k, 'val': v} for k, v in result.items() ]

@app.callback(Output('pred-graph', 'figure'),
              [Input('pred-dropdown', 'value')])
def update_pred_graph(selected_dropdown_value):
    d3f = restructure[restructure['Indicators'] == selected_dropdown_value]
    train, test = d3f.iloc[:130, 0], d3f.iloc[130:, 0]
    model = ExponentialSmoothing(train, seasonal='add', seasonal_periods=12, trend='add').fit()
    pred = model.predict(start=test.index[0], end=test.index[-1]+12)
    return {
        'data': [
            {
            'x': d3f.Month,
            'y': d3f.Val,
            'line': {
                'width': 3,
                'shape': 'spline'
                }
            },
            {
            'x': pred.index,
            'y': pred,
            'line': {
                'width': 3,
                'shape': 'spline'
                }
            }
        ]
    }

if __name__ == '__main__':
    app.run_server(debug=True)