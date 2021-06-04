# First Project - Data Analysis

This project is centered around exploratory data 
analysis [(EDA)](EDA_Checklist.pdf) techniques and statistical analysis, 
as well as modeling data using linear regression.

## Content

The project uses the dataset [us_bank_wages](/us_bank_wages/us_bank_wages.txt).

The EDA is dived into 9 parts:

1. [Loading the data](EDA_0_Load_Data.ipynb)

2. [Plotting the data](EDA_1_Plot.ipynb)

3. [Start a linear regression model with all features](EDA_2_LinReg_all_var.ipynb)

4. [Start a linear regression model with only 3 features](EDA_3_LinReg_3_best_var.ipynb)

5. [Start a linear regression model with only 1 feature](EDA_4_LinReg_best_var.ipynb)

6. [Discussion about sociodemographic features](EDA_5_groupBy_SocioDemogr.ipynb)

7. [Try a linear regression model with the sociodemographic features](EDA_6_LinReg_SocioDemogr.ipynb)

8. [A mode of removing outliners](EDA_7_Clean_Data.ipynb)

9. [Summary of the EDA](EDA_8_Insights.ipynb)

## Python Script

To get the the values of the linear regression model automatically you also can run the python EDA [Script](EDA_script.py) in your terminal:

```bash
python EDA_script.py
```

The required packages can be found and loaded via `requirements.txt`