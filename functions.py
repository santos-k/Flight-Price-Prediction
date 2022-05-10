import datetime

import dash_bootstrap_components as dbc
from dash import html, dcc


def input_field(header, id, placeholder, options, size=2, offset=0, text_align='center',value = None):
    input = dbc.Col([html.Header(header),
                     dcc.Dropdown(id=id, multi=False, value=value, placeholder=placeholder, optionHeight=20,
                                  options=options,
                                  style={'color': 'black', 'background': 'white'}),
                     ], xl={'size':2,'offset':1},lg={'size':2,'offset':1},md={'size':2,'offset':1},
                    sm={'size':6,'offset':1},xs={'size':6,'offset':1}, style={'text-align': text_align})
    return input


def time_select(hour_id, min_id,value=None,value2=None):
    time = dbc.Row([
        dbc.Col([
            dcc.Input(id=hour_id, type='number', placeholder='Hour', min=0, max=23,value=value,style={'width':80}),
            dcc.Input(id=min_id, type='number', placeholder='Minute', min=0, max=59,value=value2,style={'width':80}),
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
    return [ datetime.date().month, datetime.date().day, datetime.date().isocalendar().week]


def flight_class(x):
    classs =  ['Business','First','Economy']
    if x == 'Business': return 2
    elif x == 'First': return 1
    else : return 0

def get_arrival_time(dep_h,dep_m,trav_h,trav_m):
    from datetime import datetime, timedelta
    datetime_original = datetime(2022, 6, 6, dep_h, dep_m)
    time_delta = timedelta(hours=trav_h, minutes=trav_m)
    datetime_new = datetime_original + time_delta
    arriv_hm = [datetime_new.hour,datetime_new.minute]
    return arriv_hm