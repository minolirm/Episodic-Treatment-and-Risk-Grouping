# 🏥 Episodic Treatment and Risk Grouping Analysis  

## 📘 Overview  
The goal of this project is to provide **insights for healthcare providers and payers** by analyzing episodic claims, grouping treatments, and assigning risk scores for patients.

---

## 🎯 Objectives  
- Transform healthcare claims data into **patient-level episodic treatment groups**.  
- Calculate **risk scores** for individual patients based on their treatment history.  
- Identify patterns in **hospitalization, treatment frequency, and costs**.  
- Demonstrate the effectiveness of **data analytics and visualization** in healthcare decision-making.  

---

## 📊 Dataset  
The dataset consists of **healthcare claims data** with the following fields:  

| Variable | Type | Description |
|----------|------|-------------|
| Patient ID | Categorical | Unique identifier for patients |
| Admission Date | Date | Hospital admission date |
| Discharge Date | Date | Hospital discharge date |
| Diagnosis Code | Categorical | ICD-9/ICD-10 diagnosis codes |
| Procedure Code | Categorical | CPT/HCPCS procedure codes |
| Cost | Continuous | Cost of treatment or hospital stay |
| Provider | Categorical | Hospital or healthcare provider name |

- Dataset includes multiple **hospital visits per patient**, allowing construction of **episodic treatment sequences**.  
- Sensitive patient information has been **anonymized** to maintain privacy.  

---

## ⚙️ Methodology  

### 🔹 Data Preprocessing  
- **Cleaned claims data** by handling missing and duplicate records.  
- Converted date fields to standard **datetime format**.  
- Aggregated multiple claims to form **episodic treatment sequences**.  
- Encoded categorical variables for analysis (e.g., diagnosis and procedure codes).  

### 🔹 Episodic Grouping and Risk Scoring  
- Grouped treatments into **episodes** per patient based on time intervals between claims.  
- Calculated **risk scores** based on frequency, severity, and cost of episodes.  
- Applied **visualizations** to identify high-risk patients and treatment patterns.  

### 🔹 Tools & Technologies  
- **Language:** Python, R  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `tidyverse`, `ggplot2`  
- **Environment:** Jupyter Notebook, RStudio  

---

## 📈 Results & Insights  
- Successfully **grouped patient treatments into episodes** and identified recurring patterns.  
- Risk scoring highlighted **high-cost and high-risk patients**, useful for proactive healthcare interventions.  
- Visualizations showed trends in **hospitalization, treatment types, and costs**.  

---

#### Create a virtual environment and install the packages in requirements.txt file

#### Follow the below steps for DDIG Process

1. Input following three csv files into ddi_input folder
    I) ClaimsToGroup file (csv)
   II) EnrollmentToGroup file (csv)
   III) MembersToGroup file (csv)
   
2. Input following three text files in the directory; "D:\ETG\output"
   
   I) ETGClaimsOutput file (txt)
   
   II) ETGConfinement file (txt)
   
   III) EtgSummary file (txt)
   
3. Run DDIG.py file
   
4. Following three Output file(s) and ControlReport will be saved in the ddi_output folder

   I) DDIGClaimOutput file (csv)
   
   II) DDIGConfinementOutput file (csv)
   
   III) DDIGSummaryOutput file (csv)
   
   IV) ControlReport file (text)

or 
#### For creating executable file, follow the below steps

1. In the terminal, run the below command.
   
   pyinstaller --onefile DDIG.py
   
2. After executable file creation process is successfully completed, in the DDIG project folder, 
   following output will be saved.
   - dist folder ---> Inside the dist folder, DDIG.exe file is created
   - build folder
   - DDIG.spec
   
3. Run the DDIG.exe file in the dist folder, 
   Following three Output file(s) and ControlReport will be saved in the ddi_output folder

   I) DDIGClaimOutput file (csv)
   
   II) DDIGConfinementOutput file (csv)
   
   III) DDIGSummaryOutput file (csv)
   
   IV) ControlReport file (text)
