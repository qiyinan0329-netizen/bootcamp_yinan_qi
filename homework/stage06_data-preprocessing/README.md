## Data Cleaning Strategy

The sample dataset contains missing values and mixed data types.  
To ensure the dataset is ready for analysis, the following cleaning steps were applied:

1. **Fill Missing Numeric Values**  
   - Numeric columns (`age`, `income`, `score`, `extra_data`) were filled using the **median** of each column.  
   - This preserves the central tendency without being affected by outliers.

2. **Handle Missing Non-Numeric Values**  
   - Categorical columns (`city`, `zipcode`) were filled with `'Unknown'` or `'00000'`.  
   - This ensures all rows have values and avoids errors in later processing.

3. **Drop Remaining Missing Rows (Optional)**  
   - Rows with missing values in critical columns can be removed to ensure data integrity.  
   - This step is optional depending on analysis needs.

4. **Normalize Numeric Columns**  
   - Numeric columns were scaled using **Min-Max normalization** (values between 0 and 1).  
   - This ensures that features are on the same scale, which is important for many machine learning models.

5. **Saving Cleaned Data**  
   - Cleaned datasets are saved in `data/processed/` for further analysis or modeling.  
   - Both CSV and Parquet formats are supported.