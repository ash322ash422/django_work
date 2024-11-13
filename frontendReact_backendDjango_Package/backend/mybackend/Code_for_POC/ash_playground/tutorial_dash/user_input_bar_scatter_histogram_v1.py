from dash import Dash, html, dcc, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objs as go

# Initialize the Dash app
app = Dash(__name__)

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values_1 = [10, 15, 13, 17, 19]
y_values_2 = [5, 9, 7, 10, 12]

# Layout of the app
app.layout = html.Div([
    html.H1("Dynamic Subplots with User Selection", style={'textAlign': 'center', 'color': '#333'}),

    # Dropdowns for selecting plot types
    html.Div([
        html.Label("Select Plot Type for Subplot 1:", style={'fontSize': '14px', 'color': '#555'}),
        dcc.Dropdown(
            id='dropdown-plot-1',
            options=[
                {'label': 'Line Plot', 'value': 'line'},
                {'label': 'Bar Plot', 'value': 'bar'},
                {'label': 'Scatter Plot', 'value': 'scatter'}
            ],
            value='line',  # Default value
            style={'width': '150px', 'margin': '0 auto', 'fontSize': '14px'}
        ),
    ], style={'display': 'inline-block', 'margin-right': '40px'}),

    html.Div([
        html.Label("Select Plot Type for Subplot 2:", style={'fontSize': '14px', 'color': '#555'}),
        dcc.Dropdown(
            id='dropdown-plot-2',
            options=[
                {'label': 'Line Plot', 'value': 'line'},
                {'label': 'Bar Plot', 'value': 'bar'},
                {'label': 'Scatter Plot', 'value': 'scatter'}
            ],
            value='bar',  # Default value
            style={'width': '150px', 'margin': '0 auto', 'fontSize': '14px'}
        ),
    ], style={'display': 'inline-block'}),

    # Output graph area
    dcc.Graph(id="output-graph", style={'margin-top': '20px', 'height': '500px'})
])

# Callback to update the graph based on user selection
@app.callback(
    Output("output-graph", "figure"),
    Input("dropdown-plot-1", "value"),
    Input("dropdown-plot-2", "value")
)

def update_graph(plot_type_1, plot_type_2):
    
    print(f"Selected plot type for Subplot 1: {plot_type_1}")
    print(f"Selected plot type for Subplot 2: {plot_type_2}")
    
    # Create subplots with two rows
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Subplot 1", "Subplot 2"))
    # fig = ppp_fig(config,data)
    
    # Add trace to subplot 1
    if plot_type_1 == 'line':
        fig.add_trace(go.Scatter(x=x_values, y=y_values_1, mode='lines', name='Line Plot 1'), row=1, col=1)
    elif plot_type_1 == 'bar':
        fig.add_trace(go.Bar(x=x_values, y=y_values_1, name='Bar Plot 1'), row=1, col=1)
    elif plot_type_1 == 'scatter':
        fig.add_trace(go.Scatter(x=x_values, y=y_values_1, mode='markers', name='Scatter Plot 1'), row=1, col=1)

    # Add trace to subplot 2
    if plot_type_2 == 'line':
        fig.add_trace(go.Scatter(x=x_values, y=y_values_2, mode='lines', name='Line Plot 2'), row=1, col=2)
    elif plot_type_2 == 'bar':
        fig.add_trace(go.Bar(x=x_values, y=y_values_2, name='Bar Plot 2'), row=1, col=2)
    elif plot_type_2 == 'scatter':
        fig.add_trace(go.Scatter(x=x_values, y=y_values_2, mode='markers', name='Scatter Plot 2'), row=1, col=2)

    # Update layout for the graph
    fig.update_layout(
        title="User-Selected Subplots",
        title_font_size=20,
        title_font_color="#333",
        title_x=0.5,
        plot_bgcolor="#f9f9f9",
        margin=dict(l=40, r=40, t=80, b=40),
        showlegend=False
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
