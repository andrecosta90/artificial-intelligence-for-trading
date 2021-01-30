# import helper
import plotly.graph_objs as go
import plotly.offline as offline_py
offline_py.init_notebook_mode(connected=True)


def _generate_stock_trace(prices):
    return go.Scatter(
        name='Index',
        x=prices.index,
        y=prices,
        
    )


def _generate_traces(name_df_color_data):
    traces = []

    for name, df, color in name_df_color_data:
        traces.append(go.Scatter(
            name=name,
            x=df.index,
            y=df,
            mode='line',
            line={'color': color}))

    return traces


def plot_stock(prices, title):

    layout = go.Layout(title=title)

    stock_trace = _generate_stock_trace(prices)

    offline_py.iplot({'data': [stock_trace], 'layout': layout})


def print_dataframe(df, n_rows=10, n_columns=3):
    missing_val_str = '...'


    formatted_df = df.iloc[:n_rows, :n_columns]
    formatted_df = formatted_df.applymap('{:.3f}'.format)

    if len(df.columns) > n_columns:
        formatted_df[missing_val_str] = [missing_val_str]*len(formatted_df.index)
    if len(df.index) > n_rows:
        formatted_df.loc[missing_val_str] = [missing_val_str]*len(formatted_df.columns)

    trace = go.Table(
        type='table',
        columnwidth=[1, 3],
        header={
            'values': [''] + list(formatted_df.columns.values),
            
            'font': {'size': 13}},
        cells={
            'values': formatted_df.reset_index().values.T,
            
            
            'font': {'size': 13}})

    offline_py.iplot([trace])


def plot_resampled_prices(df_resampled, df, title):
   
    layout = go.Layout(title=title)

    traces = _generate_traces([
        ('Monthly Close', df_resampled),
        ('Close', df)])

    offline_py.iplot({'data': traces, 'layout': layout})


def plot_returns(returns, title):
    
    layout = go.Layout(title=title)

    traces = _generate_traces([
        ('Returns', returns)])

    offline_py.iplot({'data': traces, 'layout': layout})


def plot_shifted_returns(df_shited, df, title):
    
    layout = go.Layout(title=title)

    traces = _generate_traces([
        ('Shifted Returns', df_shited),
        ('Returns', df)])

    offline_py.iplot({'data': traces, 'layout': layout})


def print_top(df, name, top_n=10):
    print('{} Most {}:'.format(top_n, name))
    print(', '.join(df.sum().sort_values(ascending=False).index[:top_n].values.tolist()))
