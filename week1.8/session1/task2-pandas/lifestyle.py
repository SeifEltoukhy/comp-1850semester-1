import pandas

data = pandas.read_csv("lifestyle_data.csv")
print(type(data))
print("Total students:", len(data))
print("Average GPA:", data["GPA"].mean())
print("Sleep standard deviation:", data["Sleep_Hours_Per_Day"].std())
print("Maximum study hours:", data["Study_Hours_Per_Day"].max())
sorted_data = data.sort_values(by="Social_Hours_Per_Day")
print(sorted_data)
hours_columns = [col for col in data.columns if "Hours_Per_Day" in col]

data["Total_hours"] = data[hours_columns].sum(axis=1)

print(data["Total_hours"])

high_stress = data[data["Stress_Level"] == "High"]
print("High stress students:")
print(high_stress)

low_stress = data[data["Stress_Level"] == "Low"]
print("Low stress students:")
print(low_stress)

print("High  average GPA:", high_stress["GPA"].mean())
print("Low  average GPA:", low_stress["GPA"].mean())
# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students

# Find the mean average GPA of the students

# Find the standard deviation of how much sleep students get per day

# Find the maximum amount of study hours per day

# Sort the students by social hours per day ascending (lowest -> highest)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
