# Motor Vehicle Collision Analysis

## Overview

This project analyzes motor vehicle collision data to uncover patterns and insights related to crashes. Using Python and libraries like `pandas`, `matplotlib`, and `seaborn`, the project explores trends in crash locations, times, and contributing factors.

---

## Dataset

The dataset used in this analysis is [`Motor_Vehicle_Collisions_-_Crashes.csv`](https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes). It includes information about motor vehicle collisions, such as:

- Crash date and time
- Borough and ZIP code
- Latitude and longitude
- Street names involved in the collisions
- Contributing factors for vehicles involved
- Types of vehicles involved

The data is cleaned and processed to handle missing values and prepare it for analysis.

---

## Tools and Technologies

- **Python Libraries**:
  - `pandas` for data manipulation and analysis
  - `matplotlib` and `seaborn` for data visualization
- Jupyter Notebook for code execution and visualization
- Dash and Plotly for building an interactive dashboard

---

## Methodology

1. **Data Cleaning**:
   - Load the dataset and handle missing values (`na_values` set for blank spaces).
   - Examine the attributes using exploratory techniques like `df.head()`.

2. **Exploratory Data Analysis (EDA)**:
   - Visualize crash trends over time and by location.
   - Analyze contributing factors and vehicle types involved.

3. **Visualization**:
   - Create plots to highlight key insights using `matplotlib` and `seaborn`.

4. **Interactive Dashboard**:
   - Develop a dashboard with Dash to provide dynamic visualizations and user interactivity.

---

## Interactive Dashboard

As part of this project, an interactive dashboard was created using Dash to explore motor vehicle collision data dynamically. The dashboard includes the following features:

1. **Year Range Slider**:
   - Allows users to filter data for specific years between 2017 and 2021.
   - Updates all visualizations dynamically based on the selected year range.

2. **Visualizations**:
   - **Pie Chart (Collisions by Season)**:
     - Displays the distribution of collisions across seasons.
   - **Pie Chart (Collisions by Day/Night)**:
     - Shows the proportion of collisions occurring during the day versus night.
   - **Bar Chart (Collisions by Borough)**:
     - Highlights the total number of collisions in each NYC borough.

3. **Technology Stack**:
   - **Dash**: For building the dashboard and handling interactivity.
   - **Plotly Express**: For creating visually appealing and dynamic plots.
   - **Pandas**: For data manipulation and filtering.

---

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/illelias/stjohns_625.git
   cd stjohns_625/main
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas matplotlib seaborn dash plotly
   ```

3. **Prepare the Dataset**:
   - Ensure the `Motor_Vehicle_Collisions_-_Crashes.csv` and `cleaned_df.csv` files are in the appropriate directory.

4. **Run the Jupyter Notebook**:
   ```bash
   jupyter notebook Elias\ Illescas\ Final\ Project.ipynb
   ```
   - Open the notebook in your browser and execute the cells to reproduce the analysis.

5. **Run the Dashboard**:
   ```bash
   python Final\ Project\ Dash.py
   ```
   - Open the provided URL in your web browser to interact with the dashboard.

---

## Visualizations

- Static and interactive charts created with `matplotlib`, `seaborn`, and Dash.
- Examples include time-series plots of crashes and interactive pie/bar charts in the dashboard.

---

## Next Steps

- Extend the analysis to include temporal patterns (e.g., by hour or day).
- Integrate machine learning models to predict collision severity.
- Deploy an interactive dashboard for real-time data exploration.

---

## Acknowledgments

- Data sourced from public records: [`Motor_Vehicle_Collisions_-_Crashes.csv`](https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes)
- Python libraries and Jupyter Notebook for enabling analysis.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

