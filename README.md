#   EDUNET FOUNDATION ARTIFICIAL INTELLIGENCE WITH GREEN TECHNOLOGY 4-WEEKS VIRTUAL INTERNSHIP
Crop and Fertilizer Recommendation System A machine learning-based system to assist farmers and agricultural enthusiasts in making informed decisions about crop selection and fertilizer application based on soil and environmental conditions.

### **Crop Recommendation Dataset Analysis 🌾**

#### **Overview**
This script performs an exploratory data analysis (EDA) on the **Crop_recommendation.csv** dataset. The goal is to explore the dataset's structure, check for any issues like missing values or duplicates, and visualize how different features relate to the crop types.

#### **Steps Involved:**

1. **Data Import 📥**:
   - The dataset is loaded from the `Crop_recommendation.csv` file using `pandas.read_csv()`.

2. **Initial Exploration 🔍**:
   - We display the first few and last few rows of the dataset to get a quick overview.
   - Basic dataset info such as column types, non-null counts, and memory usage is retrieved using `info()`.

3. **Data Quality Checks ✅**:
   - We check for missing values in the dataset and identify any duplicates.

4. **Summary Statistics 📊**:
   - Descriptive statistics (mean, min, max, etc.) for numerical features are displayed to give a quick summary of the data.

5. **Feature Columns 📝**:
   - We extract and list the feature columns (everything except the target column `label`).

6. **Visualizations 📈**:
   - **Histograms** to see the distribution of each feature.
   - **Scatter Plots** to explore how each feature relates to the crop type.
   - **Box Plots** to detect outliers in the dataset.
   - **Correlation Heatmap** to visualize relationships between numerical features.

7. **Label Encoding 🔢**:
   - The `label` column, which contains crop types, is encoded as numeric values for easier analysis and visualization.

8. **Final DataFrame 📑**:
   - The original `label` column is dropped, leaving the features and the numeric encoding of the crop types for further analysis.

#### **Libraries Used** 
- `numpy`, `pandas`, `matplotlib`, and `seaborn` for data manipulation and visualization.

#### **Usage** 
- Install the required libraries, place the dataset file in the correct folder, and run the script to explore and visualize the data.

#### **What’s Next? 🔜**
This script will be updated next week with even more features and improvements, so stay tuned! 😊
