import pandas as pd

# Open the errors.csv file
errors = pd.read_csv('errors.csv')

# Open the Data_Analyst_Sample.csv file
data = pd.read_csv('Data_Analyst_Sample.csv')

# Create a dictionary of the errors and corrected names
error_dict = dict(zip(errors['Campaign error name'], errors['Campaign correct']))

# Count the number of errors in the dataset
error_count = 0
for name in data[pd.notna(data['Campaign Name'])]['Campaign Name']:
    for error, correct in error_dict.items():
        if error in name:
            error_count += 1
print(f'Number of errors in the dataset: {error_count}')

# Correct the errors
data['Campaign Name'] = data['Campaign Name'].replace(error_dict)

# Verify the errors have been corrected
error_count = 0
for name in data[pd.notna(data['Campaign Name'])]['Campaign Name']:
    for error, correct in error_dict.items():
        if error in name:
            error_count += 1
if error_count == 0:
    print('All errors have been corrected.')
else:
    print(f'{error_count} errors remain in the dataset.')
