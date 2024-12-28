# stjohns_625
Final Project for CUS 625 Data Visualization Programming
# Motor Vehicle Collision Analysis

## Overview

This project analyzes motor vehicle collision data to uncover patterns and insights related to crashes. Using Python and libraries like `pandas`, `matplotlib`, and `seaborn`, the project explores trends in crash locations, times, and contributing factors.

---

## Dataset

The dataset used in this analysis is `Motor_Vehicle_Collisions_-_Crashes.csv`. It includes information about motor vehicle collisions, such as:

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

---

## Key Insights

- Patterns in crash frequency by borough or ZIP code.
- Relationships between contributing factors and crash severity.
- Distribution of vehicle types involved in collisions.

---

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/illelias/stjohns_625.git
   cd stjohns_625/main
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. **Download the dataset**:
   - Ensure the `Motor_Vehicle_Collisions_-_Crashes.csv` file is in the same directory as the notebook.

4. **Run the Jupyter Notebook**:
   ```bash
   jupyter notebook Elias\ Illescas\ Final\ Project.ipynb
   ```
   - Open the notebook in your browser and execute the cells to reproduce the analysis.

---

## Visualizations

- Static and interactive charts created with `matplotlib` and `seaborn`.
- Examples include time-series plots of crashes and heatmaps of crash locations.

---

## Next Steps

- Extend the analysis to include temporal patterns (e.g., by hour or day).
- Integrate machine learning models to predict collision severity.
- Deploy an interactive dashboard for real-time data exploration.

---

## Acknowledgments

- Data sourced from public records: `Motor_Vehicle_Collisions_-_Crashes.csv`
- Python libraries and Jupyter Notebook for enabling analysis.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.



---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

