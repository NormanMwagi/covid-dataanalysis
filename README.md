# CORD-19 Data Explorer

This project is a beginner-friendly data analysis and visualization of the **CORD-19 research dataset** (metadata only).  
It guides you through loading, cleaning, analyzing, and presenting COVID-19 research data using **Pandas, Matplotlib, Seaborn, and Streamlit**.

---

## 📌 Project Overview

- Load and explore the `metadata.csv` file from the CORD-19 dataset.
- Perform **basic data cleaning** (missing values, date conversion, new features).
- Analyze and visualize research trends:
  - Publications per year
  - Top journals
  - Word frequency in titles
- Build a **Streamlit app** to make the analysis interactive.

---

## 🛠️ Tools and Libraries

- **Python 3.7+**
- [Pandas](https://pandas.pydata.org/) – data manipulation
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) – visualization
- [Streamlit](https://streamlit.io/) – web application
- [WordCloud](https://github.com/amueller/word_cloud) – generate word cloud

---

## 📂 Dataset

We use the **metadata.csv** file from the CORD-19 dataset, available on [Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

For practice, you can also work with a **sample of the dataset** (e.g., first 5,000 rows).

---

## 🚀 How to Run

### 1. Clone this repo

```bash
git clone https://github.com/your-username/cord19-explorer.git
cd cord19-explorer

2. Create and activate a virtual environment

On Windows (Git Bash):

python -m venv venv
source venv/Scripts/activate


On Linux/Mac:

python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run Jupyter Notebook (optional, for exploration)
jupyter notebook

5. Run Streamlit app
streamlit run app.py

📊 Example Visualizations

Publications per year

Top publishing journals

Word cloud of paper titles

Distribution by source

✅ Expected Outcomes

By completing this project, you will:

Understand the basic data science workflow (load → clean → analyze → visualize → present).

Build a simple interactive Streamlit app.

Practice with a real-world dataset.

```
