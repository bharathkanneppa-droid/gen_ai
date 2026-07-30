import pandas as pd
import numpy as np
import glob

# ============================================================
# 1. Data Cleaning - Handling missing values
# ============================================================
print("=" * 60)
print("1. DATA CLEANING - HANDLING MISSING VALUES")
print("=" * 60)

df1 = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
})
print("Original:")
print(df1)
print("\nFilled with column means:")
print(df1.fillna(df1.mean()))
print("\n")

# ============================================================
# 2. GroupBy - Aggregation
# ============================================================
print("=" * 60)
print("2. GROUPBY - AGGREGATION")
print("=" * 60)

df2 = pd.DataFrame({
    'Dept': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [100, 200, 150, 250, 300]
})
print(df2.groupby('Dept').agg({'Salary': ['mean', 'sum', 'count']}))
print("\n")

# ============================================================
# 3. Merging / Joining DataFrames
# ============================================================
print("=" * 60)
print("3. MERGING / JOINING DATAFRAMES")
print("=" * 60)

df3a = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df3b = pd.DataFrame({'ID': [2, 3, 4], 'Score': [85, 90, 95]})
print(pd.merge(df3a, df3b, on='ID', how='outer'))
print("\n")

# ============================================================
# 4. Time Series - Resampling
# ============================================================
print("=" * 60)
print("4. TIME SERIES - RESAMPLING")
print("=" * 60)

dates = pd.date_range('2024-01-01', periods=30, freq='D')
df4 = pd.DataFrame({'value': np.random.randn(30)}, index=dates)
print("Weekly mean:")
print(df4.resample('W').mean())
print("\n")

# ============================================================
# 5. Pivot Table
# ============================================================
print("=" * 60)
print("5. PIVOT TABLE")
print("=" * 60)

df5 = pd.DataFrame({
    'Date': ['Jan', 'Jan', 'Feb', 'Feb'],
    'City': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
})
print(pd.pivot_table(df5, values='Sales', index='Date', columns='City', aggfunc='sum'))
print("\n")

# ============================================================
# 6. Apply Custom Function
# ============================================================
print("=" * 60)
print("6. APPLY CUSTOM FUNCTION")
print("=" * 60)

df6 = pd.DataFrame({'Name': ['alice', 'bob', 'charlie'], 'Score': [75, 85, 95]})
df6['Grade'] = df6['Score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C')
print(df6)
print("\n")

# ============================================================
# 7. Filtering with Multiple Conditions
# ============================================================
print("=" * 60)
print("7. FILTERING WITH MULTIPLE CONDITIONS")
print("=" * 60)

df7 = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})
print(df7[(df7['Age'] > 28) & (df7['Salary'] < 75000)])
print("\n")

# ============================================================
# 8. Reading Multiple CSV Files & Concatenating
# ============================================================
print("=" * 60)
print("8. READING MULTIPLE CSV FILES & CONCATENATING")
print("=" * 60)

print("Example usage (uncomment if CSV files exist):")
print("# files = glob.glob('data/*.csv')")
print("# dfs = [pd.read_csv(f) for f in files]")
print("# combined = pd.concat(dfs, ignore_index=True)")
print("# print(combined.head())")
print()

# Demo with in-memory DataFrames
df8a = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df8b = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
combined = pd.concat([df8a, df8b], ignore_index=True)
print("Concatenated demo:")
print(combined)
print("\n")

# ============================================================
# 9. Rolling Window Statistics
# ============================================================
print("=" * 60)
print("9. ROLLING WINDOW STATISTICS")
print("=" * 60)

df9 = pd.DataFrame({'Sales': [100, 120, 130, 110, 150, 160, 140]})
df9['MA_3'] = df9['Sales'].rolling(window=3).mean()
print(df9)
print("\n")

# ============================================================
# 10. One-Hot Encoding (get_dummies)
# ============================================================
print("=" * 60)
print("10. ONE-HOT ENCODING (get_dummies)")
print("=" * 60)

df10 = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']})
encoded = pd.get_dummies(df10, columns=['Color'], prefix='', prefix_sep='')
print(encoded)
