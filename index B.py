# ========= Imports ============ #
import dash_bootstrap_components as dbc
from dash import html
import dash

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN])
server = app.server

card_content = [
    dbc.CardHeader("Jogador"),
    dbc.CardBody(
        [
            html.H5("Dohmann", className="card-title"),
            html.P(
                "Nome Completo: Gustavo Abreu Dohmann",
                className="card-text",
            ),
        ]
    ),
]

 
# =========  Layout  =========== #
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(card_content, color="primary", inverse=True, style = {"height":"80vh","margin":"10px"})], sm=4),
        dbc.Col([
            dbc.Row([dbc.Card(card_content, color="secondary", inverse=False)]),
            dbc.Row([dbc.Card(card_content, color="info", inverse=True)]),

                ],sm = 4),
            ]),
])


# =========  Callbacks  =========== #



# =========  Run Server  =========== #
if __name__ == "__main__":
    app.run_server(port=8051, debug=True)