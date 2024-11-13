from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go

# Initialize the Dash app
app = Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Line Plot with User-Selected Slope", style={'textAlign': 'center', 'color': '#333'}),
    
    # Dropdown for selecting slope
    html.Label("Select Slope:", style={'fontSize': '16px', 'color': '#555'}),
    dcc.Dropdown(
        id='slope-dropdown',
        options=[{'label': f'Slope = {s}', 'value': s} for s in range(-5, 6) if s != 0],  # Options from -5 to 5, excluding 0
        placeholder="Choose a slope",
        style={'width': '150px', 'margin': '0 auto', 'fontSize': '16px'}
    ),
    
    # Output graph area
    dcc.Graph(id="output-graph", style={'margin-top': '20px', 'height': '300px'})
])

# Callback to update the graph based on user selection
@app.callback(
    Output("output-graph", "figure"),
    Input("slope-dropdown", "value")
)
def update_graph(selected_slope):
    # Default figure with an empty plot if no slope is selected
    fig = go.Figure()

    if selected_slope is not None:
        # Define x and y values based on the selected slope
        x_values = list(range(-10, 11))  # Range from -10 to 10 for a balanced line
        y_values = [selected_slope * x for x in x_values]  # y = slope * x

        # Create the line plot
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name=f'y = {selected_slope}x',
                                 line=dict(color='blue', width=2)))

    # Update layout for the graph
    fig.update_layout(
        title=f"Line Plot with Slope {selected_slope if selected_slope is not None else ''}",
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        plot_bgcolor="#f9f9f9",
        margin=dict(l=40, r=40, t=80, b=40),
        showlegend=False,
        height=500,
        width=500
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
