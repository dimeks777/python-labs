import os

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from numpy import sqrt, sin
import pandas as pd

from app_logger import get_logger

logger = get_logger(__name__)


def matplotlib_math_plot(path):
    x = np.linspace(0, 5, 1000)
    plt.plot(x, sqrt(x) * sin(10 * x), label='y = sqrt(x) * sin(10x)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Simple Plot")
    plt.legend()
    res_path = os.path.join(path, 'math')
    if not os.path.exists(res_path):
        os.makedirs(res_path)
    plt.savefig(os.path.join(res_path, 'math_plot1.png'), bbox_inches='tight')


def plotly_math_plot(path):
    x = np.linspace(0, 4, 1000)
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=[5 * sin(10 * x1) * sin(3 * x1) for x1 in x],
        name="y=5sin(10x)sin(3x)"
    ))

    fig.update_layout(
        title="Plotly demo",
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        legend_title="Functions",
        showlegend=True,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    res_path = os.path.join(path, 'math')
    if not os.path.exists(res_path):
        os.makedirs(res_path)
    os.path.join(res_path, 'math_plot2.html')
    fig.write_image(os.path.join(res_path, 'math_plot2.pdf'), format='pdf')


def plotly_finance_plot(path):
    data = pd.read_csv(os.path.join(path, 'finances.csv')).to_dict()

    fig2 = go.Figure()
    fig3 = go.Figure()
    fig2.add_trace(go.Bar(
        x=[x for x in data['Name'].values()],
        y=[y for y in data['Gross Profit'].values()],
        name='Gross Profit'
    ))
    fig2.add_trace(go.Bar(
        x=[x for x in data['Name'].values()],
        y=[y for y in data['Return on Assets'].values()],
        name='Return on Assets(%)'
    ))
    fig3.add_trace(go.Bar(
        x=[x for x in data['Name'].values()],
        y=[y for y in data['Book Value Per Share'].values()],
        name='Book Value Per Share'
    ))
    fig3.add_trace(go.Bar(
        x=[x for x in data['Name'].values()],
        y=[y for y in data['Return on Assets'].values()],
        name='Return on Assets(%)'
    ))

    fig2.update_layout(
        title="Yahoo finance analysis",
        xaxis_title="Companies",
        yaxis_title="Gross Profit",
        legend_title="Legend",
        showlegend=True,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    fig3.update_layout(
        title="Yahoo finance analysis",
        xaxis_title="Companies",
        yaxis_title="Book Value Per Share",
        legend_title="Legend",
        showlegend=True,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

    fig2.write_image(os.path.join(path, 'finance_1.pdf'), format='pdf')
    fig3.write_image(os.path.join(path, 'finance_2.pdf'), format='pdf')


def do_draw(path_to_finances, path_to_math):
    logger.info("Starting draw script")
    matplotlib_math_plot(path_to_math)
    plotly_math_plot(path_to_math)
    plotly_finance_plot(path_to_finances)
    logger.info("Draw script finished")
