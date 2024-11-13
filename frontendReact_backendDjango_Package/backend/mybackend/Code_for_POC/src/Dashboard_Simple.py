import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from main_Dummy_AW import *
# import main_Dummy_AW
# from flask_caching import Cache

# Create a Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory',
# })

# Define the layout of the dashboard
app.layout = html.Div(
    children=[
        dbc.Navbar(
            children=[
                dbc.NavbarBrand(
                    html.H1(
                        "Sample Geomechanics Project",
                        className="navbar-brand",
                        style={"font-size": "28px", "text-align": "center"},
                    )
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(
                        children=[
                            dbc.NavItem(
                                dcc.Dropdown(
                                    id="well-dropdown",
                                    options=[
                                        {"label": "Well ABC", "value": "Well_1"},
                                        {"label": "Well XYZ", "value": "Well_2"},
                                        {"label": "Well 3", "value": "Well_3"},
                                        {"label": "Well 4", "value": "Well_4"},
                                        {"label": "Well 5", "value": "Well_5"},
                                    ],
                                    value="Well_1",
                                    clearable=False,
                                    style={"width": "200px", "margin-left": "auto"},
                                ),
                                className="nav-item",
                                style={"margin-left": "auto"},
                            )
                        ],
                        navbar=True,
                        className="ml-auto",
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ],
            color="teal",
            dark=True,
        ),
        dcc.Tabs(
            id="tabs",
            value="tab-well-info",
            children=[
                dcc.Tab(label="Well Information", value="tab-well-info"),
                dcc.Tab(label="Drilling Analysis", value="tab-drilling-analysis"),
                dcc.Tab(label="Input Logs", value="tab-input-logs"),
                dcc.Tab(label="Rock Properties", value="tab-rock-properties"),
                dcc.Tab(label="PPP", value="tab-ppp"),
                dcc.Tab(label="MEM+WBS", value="tab-mem-wbs"),
                dcc.Tab(label="MW Window", value="tab-mw-window"),
                dcc.Tab(label="SPP", value="tab-spp"),
                dcc.Tab(label="Extra", value="tab-extra"),
            ],
            style={
                "width": "100%",
                "margin": "0px",
                "padding": "0px",
            },  # full screen width
            className="container-fluid",
        ),
        html.Div(
            id="tab-content",
            className="container-fluid",
            style={"padding": "10px", "height": "calc(100vh - 120px)"},
        ),  # height of the entire viewport minus navbar height
    ]
)


# Map the well objects to the dropdown values
well_objects = {
    "Well_1": Well_1,
    "Well_2": Well_2,
    # "Well_3": Well_3,
    # "Well_4": Well_4,
    # "Well_5": Well_5,
}


# Define the common style
common_graph_style = {
    "width": "100%",
    "height": "100%",
}


@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "value"), Input("well-dropdown", "value")],
)
# @cache.memoize(timeout=3600)
def render_tab_content(tab_value, well_value):
    # Get the selected well object based on the well value
    selected_well = well_objects[well_value]

    if tab_value == "tab-well-info":
        return html.Div(
            children=[
                dcc.Graph(
                    id="field-layout-plot",
                    figure={},
                    style={"width": "30%", "float": "left", "display": "inline"},
                ),
                dcc.Graph(
                    id="well-3d-plot",
                    figure={},
                    style={"width": "70%", "float": "right", "display": "inline"},
                ),
            ],
            className="row",
            # className="container-fluid", style={"padding": "10px"}
            # )
        )
    elif tab_value == "tab-drilling-analysis":
        return html.Div(
            children=[
                dcc.Graph(
                    id="well-schematic-plot",
                    figure={},
                    style={"width": "30%", "float": "left", "display": "inline"},
                ),
                dcc.Graph(
                    id="formation-tops-plot",
                    figure={},
                    style={"width": "30%", "float": "center", "display": "inline"},
                ),
                dcc.Graph(
                    id="ddr-analysis-plot",
                    figure={},
                    style={"width": "30%", "float": "right", "display": "inline"},
                ),
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )
    elif tab_value == "tab-input-logs":
        return html.Div(
            children=[
                dcc.Graph(
                    id="input-logs-plot",
                    figure=selected_well.fig_input_logs(),
                    style=common_graph_style,
                )
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )
    elif tab_value == "tab-rock-properties":
        return html.Div(
            children=[
                dcc.Graph(
                    id="rock-properties-plot",
                    figure=selected_well.fig_rock_properties(),
                    style=common_graph_style,
                )
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )
    elif tab_value == "tab-ppp":
        return html.Div(
            children=[
                dcc.Graph(
                    id="ppp-plot",
                    figure=selected_well.fig_ppp_log2(),
                    style=common_graph_style,
                ),
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )
    elif tab_value == "tab-mem-wbs":
        return html.Div(
            children=[
                dcc.Graph(
                    id="mem-wbs-plot",
                    figure=selected_well.fig_wbs_log(),
                    style=common_graph_style,
                ),
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )
    elif tab_value == "tab-mw-window":
        return html.Div(
            children=[
                dcc.Graph(
                    id="mw-window-plot",
                    figure=selected_well.fig_mud_window(),
                    style={"width": "30%", "float": "left", "display": "inline"},
                ),
                dcc.Graph(id="stereonet-plot", figure={}),
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )
    elif tab_value == "tab-spp":
        return html.Div(
            children=[
                dcc.Graph(
                    id="spp-plot",
                    figure=selected_well.fig_spp_log(),
                    style=common_graph_style,
                ),
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )
    elif tab_value == "tab-extra":
        return html.Div(
            children=[
                html.H4("Extra Content"),
            ],
            style={
                "height": "100%"
            },  # set the height of the Div containing the graph to 100%
        )


# Run the Dash application
if __name__ == "__main__":
    app.run_server(port=2001, debug=True)
