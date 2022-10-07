import pandas as pd
import plotly.express as px
import datetime as dt
import streamlit as st
import requests

@st.cache
def load_dataframe():
    url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
    df = pd.read_csv(url)

    #remove time in data
    df['data'] = pd.to_datetime(df['data']).dt.date
    return df

def main():
    # set layout to wide y default
    st.set_page_config(layout='wide')

    # load datafame from url
    df = load_dataframe()

    # sidebar with date filters
    data_inizio = st.sidebar.date_input(
        'data inizio',
        min(df['data']),
        min_value=min(df['data']),
        max_value=max(df['data']),
        )
    data_fine = st.sidebar.date_input(
        'data fine',
        max(df['data']),
        min_value=min(df['data']),
        max_value=max(df['data']),
        )

    # sidebar regioni selector
    regioni_filters = st.sidebar.multiselect(
        'Seleziona regioni',
        df['denominazione_regione'].unique(),
        df['denominazione_regione'].unique()
    )

    # filter dates in dataframe
    df = df[(df['data'] >= data_inizio) & (df['data'] <= data_fine)]

    # filter regioni 
    df = df[df['denominazione_regione'].isin(regioni_filters)]

    # display dataframe in ST
    st.title('Dataframe contagi covid-19 :syringe:')
    st.dataframe(df)

    # 2 columns
    col1, col2 = st.columns(2, gap='small')

    #First column
    col1.title('Grafico totale casi')
    fig1 = px.line(
        df,
        x='data',
        y='totale_casi',
        color='denominazione_regione'
    )
    col1.plotly_chart(fig1)
    col2.title('Grafico dimessi guariti')
    fig2 = px.line(
        df,
        x='data',
        y='dimessi_guariti',
        color='denominazione_regione'
    )
    col2.plotly_chart(fig2)

if __name__ == '__main__':
    main()