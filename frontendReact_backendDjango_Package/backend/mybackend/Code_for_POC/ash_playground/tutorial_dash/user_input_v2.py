from dash import Dash, html, dcc, Input, Output, State
import plotly.graph_objs as go

# Initialize the Dash app
app = Dash(__name__)

# Sample data for the graph
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 17, 19]

# Layout of the app
app.layout = html.Div([
    html.H1("Interactive Graph with Point Selection"),

    # Dropdown for selecting X and Y values
    html.Label("Select X Value:"),
    dcc.Dropdown(
        id='dropdown-x',
        options=[{'label': f'X = {x}', 'value': x} for x in x_values],
        placeholder="Select an X value"
    ),

    html.Label("Select Y Value:"),
    dcc.Dropdown(
        id='dropdown-y',
        options=[{'label': f'Y = {y}', 'value': y} for y in y_values],
        placeholder="Select a Y value"
    ),
    
    # Submit button
    html.Button("Submit", id="submit-button", n_clicks=0, style={'margin-top': '10px'}),

    # Output graph area
    dcc.Graph(id="output-graph", style={'margin-top': '20px'})
])

# Callback to update the graph based on user selection
@app.callback(
    Output("output-graph", "figure"),
    Input("submit-button", "n_clicks"),
    State("dropdown-x", "value"),
    State("dropdown-y", "value")
)
def update_graph(n_clicks, selected_x, selected_y):
    # Create a basic line plot
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Sample Data'))

    # Check if the submit button was clicked and values were provided
    if n_clicks > 0 and selected_x is not None and selected_y is not None:
        # Display the selected point as an annotation on the graph
        fig.add_annotation(
            x=selected_x,
            y=selected_y,
            text=f"({selected_x}, {selected_y})",
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-40,
            font=dict(size=12, color="red"),
            bgcolor="yellow",
            bordercolor="black"
        )

    # Update layout for the graph
    fig.update_layout(
        title="Sample Graph with Selected Point Annotation",
        xaxis_title="X Axis",
        yaxis_title="Y Axis"
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
