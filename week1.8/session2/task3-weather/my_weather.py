import sys
import httpx
import pandas as pd
import matplotlib.pyplot as plt

api_key="U6KXJTZC2E8VGH39PD7UMG4BZ"   # your API key

city="Leeds"     # city location
country="UK"     # country location

elements = "include=days&elements=tempmax,tempmin,temp"   # request history of temperature data for Leeds

# URL location of the API for time history forecasts
base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# construct the URL string for the API call
url = base + city + "," + country + "?key=" + api_key + "&" + elements

# http request
response = httpx.get(url)

# check the status code and stop if the request failed
print("Status code:", response.status_code)
if response.status_code != 200:
    print("Error: request failed:", response.text)
    sys.exit(1)

# status code (should be checked)
print(response.status_code)

# json data
data = response.json()

# raw data output
print(data)

# extract the temperature data as lists from the JSON dictionary
temp_data = data['days']

# extract the daily data (a list of dictionaries, one per day)
temp_data = data["days"]
print(temp_data)

print(temp_data)

# use pandas to convert data to  dataframe

df = pd.DataFrame(temp_data)

# convert to a pandas DataFrame, using the date as  x-axis
df = pd.DataFrame(temp_data)
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.set_index("datetime")
print(df)

# using matplotlib plot the 3 data sets: (tempmin,temp,tempmax) as line graphs

df.plot()

plt.show()

# annotate the graph with axis labels

# note that temperature is in Farenheit (F)
for col in ["tempmin", "temp", "tempmax"]:
    df[col] = (df[col] - 32) * 5 / 9
print(df.round(1))
# convert to Celcius before plotting 

# using the documentation explore other data, eg. rainfall  
df["precip_mm"] = df["precip"] * 25.4
rain = df["precip_mm"]
rain.index = rain.index.strftime("%d %b")   # short date labels for the bars
plt.figure()                                # start a new, separate graph
ax = rain.plot(kind="bar", color="steelblue")
ax.set_title(f"Daily rainfall forecast for {city}")
ax.set_xlabel("Date")
ax.set_ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("rainfall.png")
plt.show()