from dash import Dash, html, dcc, Input, Output, State
import plotly.graph_objs as go

# Initialize the Dash app
app = Dash(__name__)

# Sample data for the graph
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 17, 19]

# Layout of the app
app.layout = html.Div([
    html.H1("Interactive Graph with Point Selection", style={'textAlign': 'center', 'color': '#333'}),

    # Row for dropdowns
    html.Div([
        html.Div([
            html.Label("Select X Value:", style={'fontSize': '14px', 'color': '#555'}),
            dcc.Dropdown(
                id='dropdown-x',
                options=[{'label': f'X = {x}', 'value': x} for x in x_values],
                placeholder="X Value",
                style={'width': '120px', 'fontSize': '14px'}
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),

        html.Div([
            html.Label("Select Y Value:", style={'fontSize': '14px', 'color': '#555'}),
            dcc.Dropdown(
                id='dropdown-y',
                options=[{'label': f'Y = {y}', 'value': y} for y in y_values],
                placeholder="Y Value",
                style={'width': '120px', 'fontSize': '14px'}
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),

        html.Button("Submit", id="submit-button", n_clicks=0,
                    style={'margin-top': '20px', 'padding': '8px 16px', 'fontSize': '14px', 'color': 'white', 'backgroundColor': '#4CAF50'}),
    ], style={'textAlign': 'center', 'padding': '10px'}),

    # Output graph area
    dcc.Graph(id="output-graph", style={'margin-top': '20px', 'height': '500px'})
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
    fig = go.Figure(data=go.Scatter(
        x=x_values, y=y_values,
        mode='lines+markers',
        line=dict(color='royalblue', width=3),
        marker=dict(size=8, color='orange'),
        name='Sample Data'
    ))

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
        title_font_size=20,
        title_font_color="#333",
        title_x=0.5,
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        plot_bgcolor="#f9f9f9",
        margin=dict(l=40, r=40, t=80, b=40)
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
