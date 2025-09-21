# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
import re

st.set_page_config(layout="wide", page_title="CORD-19 Data Explorer")

@st.cache_data
def load_data(path="metadata_cleaned_sample.csv", fallback="metadata.csv", nrows=None):
    # prefer cleaned sample saved by notebook; fallback to full metadata.csv
    if os.path.exists(path):
        return pd.read_csv(path, parse_dates=['publish_time'], low_memory=False)
    elif os.path.exists(fallback):
        # read only a subset if file huge
        if nrows:
            return pd.read_csv(fallback, nrows=nrows, parse_dates=['publish_time'], low_memory=False)
        else:
            return pd.read_csv(fallback, parse_dates=['publish_time'], low_memory=False)
    else:
        raise FileNotFoundError("No metadata_cleaned_sample.csv or metadata.csv found. Place CSV in this folder.")

import os
data_path = "metadata_cleaned_sample.csv"
# allow user to choose to read sample or full (careful with full)
if st.sidebar.checkbox("Use local cleaned sample (recommended)", value=True):
    df = load_data(path=data_path)
else:
    st.sidebar.write("Attempting to load metadata.csv (may be large)")
    df = load_data(path=data_path, fallback="metadata.csv", nrows=20000)  # read top 20k by default

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of the CORD-19 metadata (titles, abstracts, dates, journals).")

# Basic info
col1, col2, col3 = st.columns(3)
col1.metric("Total papers", len(df))
col2.metric("First year", int(df['year'].dropna().min()) if 'year' in df.columns and df['year'].dropna().size>0 else "N/A")
col3.metric("Last year", int(df['year'].dropna().max()) if 'year' in df.columns and df['year'].dropna().size>0 else "N/A")

# Filters
st.sidebar.header("Filters")
min_year = int(df['year'].dropna().min()) if 'year' in df.columns and df['year'].dropna().size>0 else 2019
max_year = int(df['year'].dropna().max()) if 'year' in df.columns and df['year'].dropna().size>0 else 2022
year_range = st.sidebar.slider("Select year range", min_year, max_year, (min_year, max_year))

journal_options = list(df['journal'].fillna("Unknown").value_counts().head(50).index)
selected_journal = st.sidebar.selectbox("Top journals (quick filter)", ["All"] + journal_options)

# Apply filters
df_filtered = df.copy()
if 'year' in df.columns:
    df_filtered = df_filtered[(df_filtered['year'] >= year_range[0]) & (df_filtered['year'] <= year_range[1])]
if selected_journal != "All":
    df_filtered = df_filtered[df_filtered['journal'].fillna("Unknown") == selected_journal]

st.subheader("Publications over Time")
if 'year' in df_filtered.columns:
    year_counts = df_filtered['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    year_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of papers")
    st.pyplot(fig)
else:
    st.write("Year data not available.")

st.subheader("Top Journals")
if 'journal' in df.columns:
    top_j = df_filtered['journal'].fillna("Unknown").value_counts().head(20)
    fig, ax = plt.subplots()
    sns.barplot(x=top_j.values, y=top_j.index, ax=ax)
    ax.set_xlabel("Count")
    st.pyplot(fig)
else:
    st.write("Journal column missing.")

st.subheader("Top Words in Titles (simple frequency)")
def simple_tokenize(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = text.split()
    return [t for t in tokens if len(t) > 2]

title_counter = Counter()
for t in df_filtered['title'].dropna().astype(str):
    title_counter.update(simple_tokenize(t))
most_common = title_counter.most_common(20)
words, counts = zip(*most_common) if len(most_common) > 0 else ([], [])
fig, ax = plt.subplots()
sns.barplot(x=list(counts), y=list(words), ax=ax)
ax.set_xlabel("Count")
st.pyplot(fig)

st.subheader("Sample of Papers")
n_show = st.slider("How many rows to show", 5, 200, 20)
st.dataframe(df_filtered.head(n_show))

st.write("### Notes")
st.write("- If the file is large, use the cleaned sample created by the notebook or check the 'Use local cleaned sample' box.")
st.write("- Word cloud requires additional libraries; this app shows a simple frequency bar chart instead.")
