import datetime

import dash_bootstrap_components as dbc
from dash import html, dcc


def input_field(header, id, placeholder, options, size=2, offset=0, text_align='center',value = 0):
    input = dbc.Col([html.Header(header),
                     dcc.Dropdown(id=id, multi=False, value=value, placeholder=placeholder, optionHeight=20,
                                  options=options,
                                  style={'color': 'black', 'background': 'white'}),
                     ], xl={'size':2,'offset':1},lg={'size':2,'offset':1},md={'size':2,'offset':1},
                    sm={'size':6,'offset':1},xs={'size':6,'offset':1}, style={'text-align': text_align})
    return input


def time_select(hour_id, min_id,value=0,value2=0):
    time = dbc.Row([
        dbc.Col([
            dcc.Dropdown([x for x in range(0, 24)], placeholder="Hour", id=hour_id, style={'text-align': 'start'},
                         className='text-black',value=value),
        ]),
        dbc.Col([
            dcc.Dropdown([x for x in range(0, 60)], placeholder="Minute", id=min_id, style={'text-align': 'start'},
                         className='text-black',value=value2),
        ])
    ])
    return time


def airlines(x=0):
    """
    get the list of all airlines 0 value for all except one selected
    :param x: input value
    :return:
    """
    airline = ['Air India', 'GoAir', 'IndiGo',
               'Jet Airways', 'Multiple carriers', 'Other',
               'SpiceJet', 'Vistara']

    airline_val = [0, 0, 0, 0, 0, 0, 0, 0]
    if x in airline:
        a = airline.index(x)
        airline_val[a] = 1
    return airline_val

def source(x=0):
    source = ['Chennai','Delhi','Kolkata','Mumbai']
    src_val = [0, 0, 0, 0]
    if x in source:
        a = source.index(x)
        src_val[a] = 1
    return src_val


def destination(x=0):

    destination = ['Cochin', 'Delhi', 'Hyderabad','Kolkata','New Delhi']
    dest_val = [0, 0, 0, 0,0]
    if x in destination:
        a = destination.index(x)
        dest_val[a] = 1
    return dest_val




def date_month_wk(x):
    import datetime
    input = x
    format = '%Y-%m-%d'
    datetime = datetime.datetime.strptime(input, format)
    return [datetime.date().day, datetime.date().month, datetime.date().isocalendar().week]