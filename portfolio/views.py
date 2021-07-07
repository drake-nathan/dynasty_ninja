from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import plotly.express as px
from .portfolio_function import portfolio_function


def home(request):
    return render(request, 'portfolio/home.html')

@login_required
def portfolio(request):

    # Call main function
    portfolio, league_count, league_names, total_num_of_players, highest_count = portfolio_function(request.user.username)

    # Make string with list of league names
    pretty_string = f"Dynasty Ninja found {league_count} dynasty leagues with your username:"
    for league in league_names:
        pretty_string +=  " " + league + ","
    pretty_string = pretty_string[:-1] + "."

    graph_height = total_num_of_players * 18

    tick_number = range(highest_count + 1)

    # Make graph, output to html div
    fig = px.bar(
        portfolio, x="Count",
        y="Name",
        orientation='h',
        height=graph_height,
        width=800
    )
    fig.update_layout(
        xaxis = {'side': 'top'},
        font = dict(
            size=12
    ))
    context_graph = fig.to_html(include_plotlyjs='cdn', full_html=False)

    # pass context to django template
    context = {
        'graph': context_graph,
        'league_string': pretty_string,
        'total_num_of_players': total_num_of_players
    }
    return render(request, 'portfolio/portfolio.html', context)

def about(request):
    pass