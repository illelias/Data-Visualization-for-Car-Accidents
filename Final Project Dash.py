#Elias Illescas Python Dashboard
#Importing necessary packages
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('cleaned_df.csv') #Loading dataset
app = dash.Dash(__name__) #Creating the dashboard
app.layout = html.Div([ #Creating the layout for the dashboard

html.H1("NYC Collisions Analysis (2017-2021)", style={'textAlign': 'center'}), #Title at the top
  
     html.Div(
        dcc.RangeSlider( #Slider that will control the years on the plot
            id='year-slider', #Slider id used in input callback
            min=df['YEAR'].min(), #Starting at 2017
            max=df['YEAR'].max(), #Ending at 2021
            step=1, #Moves the slider one year(step) at a time
            value=[df['YEAR'].min(), df['YEAR'].max()], #Defines the default range
            marks={year: str(year) for year in range(df['YEAR'].min(), df['YEAR'].max() + 1)} #Makes string for each year to label the slider accordingly
        ),
        style={'width': '80%', 'margin': '20px auto'}
    ),
    html.Div([ #Layout for the plots that will be displayed
        html.Div(dcc.Graph(id='season-pie-chart'), style={'width': '33%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='day-night-pie-chart'), style={'width': '33%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id='borough-bar-chart')], style={'width': '33%', 'display': 'inline-block'}),
    ]),
    html.Div(
        children=[ #Create text below the plots
            html.P("For my dashboard, I decided to use Dash to create the interactivity with my visuals. "
                   "I created the original file in RStudio, but then used PyCharm to finish it. Using the slider "
                   "to allow the user to input which years between 2017 and 2021 they would like to see, the plots are "
                   "updated to show the total occurrences of motor vehicle collisions between the inputted years. "
                   "For the plots I choose the pie charts and the bar chart. The pie charts give the total amount of "
                   "motor collisions in a given season and also if it took place during day or night based on the criteria "
                   "I created. The bar chart gives the total collisions by each borough."),
        ],
        style={'textAlign': 'left', 'margin': '20px', 'fontSize': '20px'}
    ),

])


@app.callback(
    [Output('season-pie-chart', 'figure'), #The output of the plots that will be returned
     Output('day-night-pie-chart', 'figure'),
     Output('borough-bar-chart', 'figure')],
    [Input('year-slider', 'value')] #The input of the slider that the user can change to update the plots
)
def update_charts(selected_year_range): #Creating a function that will update the plots based on the range selected by the user
    start_year, end_year = selected_year_range #Assigning two variables to the variable that will be applied to the function
    filtered_df = df[(df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)] #Creating variable that filters the data based on user inputs

    season_data = ( #Creating a variable that will group the data by season and count up the instances each season appears.
        filtered_df.groupby('SEASON')
        .size()
        .reset_index(name='Total Collisions')
    )
    season_fig = px.pie( #Creating pie chart that will be outputted using season data.
        season_data,
        names='SEASON',
        values='Total Collisions',
        title=f'Collisions by Season'
    )

    day_night_data = ( #Creating a variable that will group the data by day/night and count up the instances each day or night appears.
        filtered_df.groupby('DAY/NIGHT')
        .size()
        .reset_index(name='Total Collisions')
    )
    day_night_fig = px.pie( #Creating a pie chart that will be outputted using day/night data.
        day_night_data,
        names='DAY/NIGHT',
        values='Total Collisions',
        title=f'Collisions by Day/Night'
    )
    borough_data = ( #Creating a variable that will group the data by borough and count up the instances each borough appears
        filtered_df.groupby('BOROUGH')
        .size()
        .reset_index(name='Total Collisions')
    )
    borough_bar_fig = px.bar( #Creatig a bar chart that will be outputted using borough data.
        borough_data,
        x='BOROUGH',
        y='Total Collisions',
        title=f'Collisions by Borough',
        labels={'BOROUGH': 'Borough', 'Total Collisions': 'Total Collisions'}
    )

    return season_fig, day_night_fig, borough_bar_fig #Returns all plots to be outputted

if __name__ == '__main__':
    app.run_server(debug=True) #Runs the dashboard.
