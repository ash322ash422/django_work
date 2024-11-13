from dash import Dash, html, dcc, Input, Output, State

# Initialize the Dash app
app = Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Input Form Example"),

    # Input fields for sw_max, phit_offset, vpvs_min
    html.Label("Enter sw_max:"),
    dcc.Input(id='input-sw-max', type='text', placeholder="Enter sw_max", style={'margin-right': '10px'}),
    
    html.Label("Enter phit_offset:"),
    dcc.Input(id='input-phit-offset', type='text', placeholder="Enter phit_offset", style={'margin-right': '10px'}),
    
    html.Label("Enter vpvs_min:"),
    dcc.Input(id='input-vpvs-min', type='text', placeholder="Enter vpvs_min", style={'margin-right': '10px'}),
    
    # Submit button
    html.Button("Submit", id="submit-button", n_clicks=0, style={'margin-top': '10px'}),
    
    # Output area
    html.Div(id="output", style={'margin-top': '20px', 'font-size': '18px'})
])

# Callback to update the output based on user input
@app.callback(
    Output("output", "children"),
    Input("submit-button", "n_clicks"),
    State("input-sw-max", "value"),
    State("input-phit-offset", "value"),
    State("input-vpvs-min", "value")
)
def display_values(n_clicks, sw_max, phit_offset, vpvs_min):
    if n_clicks > 0:
        return f"sw_max: {sw_max}, phit_offset: {phit_offset}, vpvs_min: {vpvs_min}"
    return "Enter values and click Submit"

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
