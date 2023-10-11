import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set_style('darkgrid')


def create_df_year(data):
  year_df = data.groupby('yr').instant.nunique().reset_index()
  year_df.rename(
    columns={
      'instant': 'sum'
    }, inplace=True
  )

  return year_df


def create_df_season(data):
  df_season = data.groupby('season').instant.nunique().reset_index()
  df_season.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_season


def create_df_weathersit(data):
  df_weathersit = data.groupby('weathersit').instant.nunique().reset_index()
  df_weathersit.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_weathersit

def year(data):
  st.subheader('Year')

  fig, ax = plt.subplots(figsize=(10, 5))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=data.sort_values(by='yr', ascending=False),
    x='sum',
    y='yr',
    orient='h',
    ax=ax,
  )
  ax.set_title(
    'Jumlah Bike Sharing Per Tahun',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Tahun', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def month(data):
  st.subheader('Bulan')

  fig, ax = plt.subplots(figsize=(20, 12))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=data.sort_values(by='mnth', ascending=False),
    x='cnt',
    y='mnth',
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Per Bulan',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Bulan', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def hour(data):
  st.subheader('Jam')

  fig, ax = plt.subplots(figsize=(20, 12))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=data.sort_values(by='hr', ascending=False),
    x='cnt',
    y='hr',
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Per Jam',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Jam', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=24, padding=20)
  st.pyplot(fig)


def season(data):
  st.subheader('Musim')

  fig, ax = plt.subplots(figsize=(20, 10))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=data.sort_values(by='season', ascending=False),
    x='sum',
    y='season',
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Berdasarkan Musim',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Musim', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def weathersit(data):
  st.subheader('Cuaca')

  fig, ax = plt.subplots(figsize=(20, 10))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=data.sort_values(by='weathersit', ascending=False),
    x='sum',
    y='weathersit',
    orient='h',
    ax=ax,
  )
  
  ax.set_title(
    'Jumlah Bike Sharing Berdasarkan Cuaca',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Cuaca', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)

def sidebar(data):
  data['dteday'] = pd.to_datetime(data['dteday'])
  min_date = data['dteday'].min()
  max_date = data['dteday'].max()

  with st.sidebar:
    st.image('bicycle.png', width=150)

    def on_change():
      st.session_state.date = date

    date = st.date_input(
      label='Rentang Waktu',
      value=[min_date, max_date],
      min_value=min_date,
      max_value=max_date,
      on_change=on_change
    )

    return date
# Load Cleaned Data
day_df = pd.read_csv('../data/day_clean.csv')
hour_df = pd.read_csv('../data/hour_clean.csv')

# Sidebar
date = sidebar(day_df)
if len(date) == 2:
  df_main = day_df[
    (day_df["dteday"] >= str(date[0])) & (day_df["dteday"] <= str(date[1]))
  ]
else:
  df_main = day_df[
    (day_df["dteday"] >= str(st.session_state.date[0])) & (
      day_df["dteday"] <= str(st.session_state.date[1])
    )
  ]

with st.container():
  st.subheader('Statistik Berdasarkan Waktu')
  tab_year, tab_month, tab_hour = st.tabs(['Tahun', 'Bulan', 'Jam'])
  df_year = create_df_year(df_main)

  with tab_year:
    year(df_year)

  with tab_month:
    month(df_main)

  with tab_hour:
    hour(hour_df)


with st.container():
  df_weathersit = create_df_weathersit(df_main)
  weathersit(df_weathersit)

  with st.expander('Keterangan'):
    st.write(
      """
      `Mist + Cloudy`: Berkabut dan berawan  
      `Light Snow`: Sedikit bersalju  
      `Clear`: Cuaca cerah
      """
    )


with st.container():
  df_season = create_df_season(df_main)
  season(df_season)

  with st.expander('Keterangan'):
    st.write(
      """
      `Winter`: Musim Dingin  
      `Summer`: Musim Panas  
      `Springer`: Musim Semi  
      `Fall`: Musim Gugur
      """
    )