import marimo

__generated_with = "0.9.10"
app = marimo.App(
    width="medium",
    layout_file="layouts/presentation.slides.json",
    css_file="custom.css",
)


@app.cell
def __(mo):
    mo.md("#Situation")
    return


@app.cell
def __(mo):
    mo.md("#Obs")
    return


@app.cell
def __(mo):
    page = open("iframes/title.html", "r").read()
    mo.iframe(page, width="900px", height="100%").style(overflow= "hidden")
    return (page,)


@app.cell
def __(chart, mo):
    mo.vstack([chart, mo.ui.table(chart.value)])
    return


@app.cell
def __():
    import marimo as mo
    import time
    from marimo import Html
    import numpy as np

    import yfinance as yf
    import pandas as pd
    import altair as alt

    import pandas as pd
    import micropip
    import json
    import altair as alt
    import os
    return Html, alt, json, micropip, mo, np, os, pd, time, yf


@app.cell
def __(yf):
    # Test Data, Real Data Will Come Later
    tickers = ['MSFT', 'META', 'NVDA', 'AAPL', 'GOOG','XOM', 'PARR', 'CVX', 'COP', 'SLB',  'LLY', 'ROIV', 'PFE', 'JNJ', 'MRNA',  'T', 'KT', 'VZ', 'CMCSA', 'TMUS',  'CMBT', 'GE', 'BA', 'CAT', 'HON',  'BIPC', 'NEE', 'DUK', 'SO', 'AEP']
    data = yf.download(tickers, start="2019-01-01", end="2024-10-01")['Adj Close']

    data = data.reset_index()

    data['Date'] = data['Date'].dt.tz_localize(None)

    data_melted = data.melt(id_vars=['Date'], value_vars=tickers, var_name='Company', value_name='Stock Price')
    return data, data_melted, tickers


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


if __name__ == "__main__":
    app.run()
