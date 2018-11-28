import numpy as np
import time

from plotly.graph_objs import Data

from stats import xtile, median

import_time_start_matplotlib = time.time()
import matplotlib
import matplotlib.pyplot as plt
import_time_stop_matplotlib = time.time()

import_time_start_plotly = time.time()
import plotly
plotly.offline.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import_time_stop_plotly = time.time()



NUM_OF_SIN_CURVES = 1
SCREEN_SIZE = [(20, 15), (12, 9), (4, 3)]
LOOP_TIMES = 2
render_time = []

def convert_inch_to_pixel(inch_list):
    pixel_list = []
    i = []
    j = []
    for x,y in inch_list:
        i.append(96 * x)
        j.append(96 * y)
    pixel_list += zip(i, j)
    return pixel_list


def test_plotly_barchat(loop_times=LOOP_TIMES):
    SCREEN_PIXEL = convert_inch_to_pixel(SCREEN_SIZE)
    render_time = []
    all_render_time_np = []
    for (i, j) in SCREEN_PIXEL:
        print("Screen Size: ", (i, j))
        for x in range(loop_times):
            objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
            y_pos = np.arange(len(objects))
            performance = [10, 8, 6, 4, 2, 1]

            layout = go.Layout(
                autosize=False,
                width=i,
                height=j,
                margin=go.layout.Margin(
                    l=50,
                    r=50,
                    b=100,
                    t=100,
                    pad=4
                ),
                paper_bgcolor='#7f7f7f',
                plot_bgcolor='#c7c7c7'
            )

            tstart = time.time()
            data = [go.Bar(x=objects, y=performance)]
            fig = go.Figure(data=data, layout=layout)

            plotly.offline.plot(fig, filename='basic-bar')

            tend = time.time()
            render_time.append(tend - tstart)
            print(6, "Bar Chart Draw Time: ", tend - tstart)
        render_time_np = np.array(render_time)
        all_render_time_np.append(render_time_np)
        print("Mean Render Time: ", render_time_np.mean())
        print("Median Render Time: ", median(render_time_np))
        print()
    print("Xtiles:")
    for np_arr in all_render_time_np:
        print(xtile(np_arr, lo=0, hi=2))


def test_plotly_sign_curve(loop_times=LOOP_TIMES):
    #TODO
    x = np.arange(0, 2 * np.pi, 0.01)
    y = np.sin(x)
    trace1 = {
        "x": x,
        "y": y,
        "line": {
            "color": "rgb(0,113.985,188.955)",
            "dash": "solid",
            "width": 0.5
        },
        "marker": {
            "color": "rgb(0,113.985,188.955)",
            "line": {"width": 0.5},
            "size": 6
        },
        "mode": "lines",
        "name": "",
        "showlegend": True,
        "type": "scatter",
        "visible": True,
        "xaxis": "x1",
        "yaxis": "y1"
    }
    data = Data([trace1])
    SCREEN_PIXEL = convert_inch_to_pixel(SCREEN_SIZE)
    render_time = []
    all_render_time_np = []

    for (i, j) in SCREEN_PIXEL:
        print("Screen Size: ", (i, j))
        for k in range(loop_times):
            tstart = time.time()
            layout = {
                "annotations": [
                    {
                        "x": 0.5175,
                        "y": 0.935,
                        "align": "center",
                        "bordercolor": "rgba(0,0,0,0)",
                        "borderpad": 3,
                        "borderwidth": 0.5,
                        "font": {
                            "color": "rgb(0,0,0)",
                            "family": "Arial, sans-serif",
                            "size": 11
                        },
                        "showarrow": False,
                        "text": "<b>Sine curve</b>",
                        "textangle": 0,
                        "xanchor": "center",
                        "xref": "paper",
                        "yanchor": "bottom",
                        "yref": "paper"
                    },
                    {
                        "x": 0.5175,
                        "y": 0.461162790698,
                        "align": "center",
                        "bordercolor": "rgba(0,0,0,0)",
                        "borderpad": 3,
                        "borderwidth": 0.5,
                        "font": {
                            "color": "rgb(0,0,0)",
                            "family": "Arial, sans-serif",
                            "size": 11
                        },
                        "showarrow": False,
                        "text": "<b>Cosine curve</b>",
                        "textangle": 0,
                        "xanchor": "center",
                        "xref": "paper",
                        "yanchor": "bottom",
                        "yref": "paper"
                    }
                ],
                "autosize": False,
                "height": i,
                "hovermode": "closest",
                "margin": {
                    "r": 0,
                    "t": 0,
                    "b": 0,
                    "l": 0,
                    "pad": 0
                },
                "paper_bgcolor": "rgb(255,255,255)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "showlegend": False,
                "title": "<b>Sine curve</b>",
                "titlefont": {"color": "rgba(0,0,0,0)"},
                "width": j,
                "xaxis1": {
                    "anchor": "y1",
                    "autorange": False,
                    "domain": [0.13, 0.905],
                    "exponentformat": "none",
                    "gridcolor": "rgb(38.25,38.25,38.25)",
                    "gridwidth": 1,
                    "linecolor": "rgb(38.25,38.25,38.25)",
                    "linewidth": 1,
                    "mirror": "ticks",
                    "nticks": 9,
                    "range": [0, 7],
                    "showgrid": False,
                    "showline": True,
                    "side": "bottom",
                    "tickcolor": "rgb(38.25,38.25,38.25)",
                    "tickfont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 10
                    },
                    "ticklen": 6.51,
                    "ticks": "inside",
                    "tickwidth": 1,
                    "titlefont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 11
                    },
                    "type": "linear",
                    "zeroline": False
                },
                "xaxis2": {
                    "anchor": "y2",
                    "autorange": False,
                    "domain": [0.13, 0.905],
                    "exponentformat": "none",
                    "gridcolor": "rgb(38.25,38.25,38.25)",
                    "gridwidth": 1,
                    "linecolor": "rgb(38.25,38.25,38.25)",
                    "linewidth": 1,
                    "mirror": "ticks",
                    "nticks": 9,
                    "range": [0, 7],
                    "showgrid": False,
                    "showline": True,
                    "side": "bottom",
                    "tickcolor": "rgb(38.25,38.25,38.25)",
                    "tickfont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 10
                    },
                    "ticklen": 6.51,
                    "ticks": "inside",
                    "tickwidth": 1,
                    "titlefont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 11
                    },
                    "type": "linear",
                    "zeroline": False
                },
                "yaxis1": {
                    "anchor": "x1",
                    "autorange": False,
                    "domain": [0.583837209302, 0.925],
                    "exponentformat": "none",
                    "gridcolor": "rgb(38.25,38.25,38.25)",
                    "gridwidth": 1,
                    "linecolor": "rgb(38.25,38.25,38.25)",
                    "linewidth": 1,
                    "mirror": "ticks",
                    "nticks": 6,
                    "range": [-1, 1],
                    "showgrid": False,
                    "showline": True,
                    "showticklabels": True,
                    "side": "left",
                    "tickcolor": "rgb(38.25,38.25,38.25)",
                    "tickfont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 10
                    },
                    "ticklen": 6.51,
                    "ticks": "inside",
                    "tickwidth": 1,
                    "titlefont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 11
                    },
                    "type": "linear",
                    "zeroline": False
                },
                "yaxis2": {
                    "anchor": "x2",
                    "autorange": False,
                    "domain": [0.11, 0.451162790698],
                    "exponentformat": "none",
                    "gridcolor": "rgb(38.25,38.25,38.25)",
                    "gridwidth": 1,
                    "linecolor": "rgb(38.25,38.25,38.25)",
                    "linewidth": 1,
                    "mirror": "ticks",
                    "nticks": 6,
                    "range": [-1, 1],
                    "showgrid": False,
                    "showline": True,
                    "showticklabels": True,
                    "side": "left",
                    "tickcolor": "rgb(38.25,38.25,38.25)",
                    "tickfont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 10
                    },
                    "ticklen": 6.51,
                    "ticks": "inside",
                    "tickwidth": 1,
                    "titlefont": {
                        "color": "rgb(38.25,38.25,38.25)",
                        "family": "Arial, sans-serif",
                        "size": 11
                    },
                    "type": "linear",
                    "zeroline": False
                }
            }

            fig = go.Figure(data=data, layout=layout)
            plot_url = plotly.offline.plot(fig)
            tend = time.time()
            render_time.append(tend - tstart)
            print(NUM_OF_SIN_CURVES, "Sine Curve Draw Time: ", tend - tstart)
        render_time_np = np.array(render_time)
        all_render_time_np.append(render_time_np)
        print("Mean Render Time: ", render_time_np.mean())
        print("Median Render Time: ", median(render_time_np))
        print()
    print("Xtiles:")
    for np_arr in all_render_time_np:
        print(xtile(np_arr, lo=0, hi=2))


def test_matplotlib_barchart(loop_times=LOOP_TIMES):
    render_time = []
    all_render_time_np = []
    for (i, j) in SCREEN_SIZE:
        print("Screen Size: ", (i, j))
        plt.rcParams["figure.figsize"] = (i, j)
        for x in range(loop_times):
            plt.ion()
            objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
            y_pos = np.arange(len(objects))
            performance = [10, 8, 6, 4, 2, 1]

            tstart = time.time()
            plt.bar(y_pos, performance, align='center', alpha=0.5)
            plt.xticks(y_pos, objects)
            plt.ylabel('Usage')
            plt.title('Programming language usage')

            plt.show()
            plt.close('all')
            tend = time.time()
            render_time.append(tend - tstart)
            print(6, "Bar Chart Draw Time: ", tend - tstart)
        render_time_np = np.array(render_time)
        all_render_time_np.append(render_time_np)
        print("Mean Render Time: ", render_time_np.mean())
        print("Median Render Time: ", median(render_time_np))
        print()
    print("Xtiles:")
    for np_arr in all_render_time_np:
        print(xtile(np_arr, lo=0, hi=2))


def test_matplotlib_sign(loop_times=LOOP_TIMES):
    render_time = []
    all_render_time_np = []
    for (i, j) in SCREEN_SIZE:
        print("Screen Size: ", (i, j))
        plt.rcParams["figure.figsize"] = (i, j)
        for k in range(loop_times):
            x = np.arange(0, 2 * np.pi, 0.01)
            y = np.sin(x)

            fig, axes = matplotlib.pyplot.subplots(nrows=6)

            styles = ['r-', 'g-', 'y-', 'm-', 'k-', 'c-']
            lines = [ax.plot(x, y, style)[0] for ax, style in zip(axes, styles)]

            tstart = time.time()
            for i in range(1, NUM_OF_SIN_CURVES):
                for j, line in enumerate(lines, start=1):
                    line.set_ydata(np.sin(j * x + i / 10.0))
                fig.canvas.draw()
            fig.show()
            plt.close(fig)
            tend = time.time()
            render_time.append(tend - tstart)
            print(NUM_OF_SIN_CURVES, "Sine Curve Draw Time: ", tend-tstart)
        render_time_np = np.array(render_time)
        all_render_time_np.append(render_time_np)
        print("Mean Render Time: ", render_time_np.mean())
        print("Median Render Time: ", median(render_time_np))
        print()
    print("Xtiles:")
    for np_arr in all_render_time_np:
        print(xtile(np_arr, lo=0, hi=2))


if __name__=="__main__":
    print("MATPLOTLIB: ")
    print("Import Time: ", import_time_stop_matplotlib - import_time_start_matplotlib)
    print()


    test_matplotlib_sign()
    test_matplotlib_barchart()

    print("PLOTLY: ")
    print("Import Time: ", import_time_stop_plotly - import_time_start_plotly)
    print()

    test_plotly_sign_curve()
    test_plotly_barchat()