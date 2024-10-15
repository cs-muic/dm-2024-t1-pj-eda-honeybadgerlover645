import marimo

__generated_with = "0.9.9"
app = marimo.App(
    width="full",
    layout_file="layouts/viz_finance.slides.json",
    css_file="custom.css",
)


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.md(r"""# **Finance Visualization Test**""")
    return


@app.cell
def __():
    import yfinance as yf
    import pandas as pd
    import altair as alt

    import pandas as pd
    import micropip
    import json
    import altair as alt
    return alt, json, micropip, pd, yf


@app.cell
def __(yf):
    # Test Data, Real Data Will Come Later
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

    data = yf.download(tickers, start="2019-01-01", end="2024-10-01")['Adj Close']

    data = data.reset_index()

    data['Date'] = data['Date'].dt.tz_localize(None)

    data_melted = data.melt(id_vars=['Date'], value_vars=tickers, var_name='Company', value_name='Stock Price')
    return data, data_melted, tickers


@app.cell
def __(data):
    data
    return


@app.cell
def __(alt, data_melted, mo):
    brush = alt.selection_interval(encodings=["x"])

    _chart = (
        alt.Chart(data_melted)
            .mark_line()
            .encode(
            x='Date:T',
            y='Stock Price:Q',
            color='Company:N')
            .add_params(brush)
    )

    chart = mo.ui.altair_chart(
        _chart
    )
    return brush, chart


@app.cell
def __(chart, mo):
    mo.vstack([chart, mo.ui.table(chart.value)])
    return


if __name__ == "__main__":
    app.run()
