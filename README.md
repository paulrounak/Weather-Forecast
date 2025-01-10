# Weather Forecasting Tool 

## Problem Statement 

Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage the OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can assist with API usage, data parsing, and error handling.


---


## Resources Used 
 
- **Python Version** : 3.10.12
 
- **GitHub Copilot** : 1.84.0.1
 
- **OpenWeatherMap API** : 3.0
 
- **IDE** : Visual Studio Code (Version: 1.79.2)


---


## Architecture Flow Diagram 
![Architecture](https://github.com/rpaulwastaken/WeatherForecast/assets/136478346/22184d41-e3eb-44cd-80c5-67dfc0ccd3f6) 


---


## Working Model 

The command-line tool provides current and future weather conditions for a given city. The video below demonstrates the working of the tool and showcases its ability to handle exceptional conditions:


https://github.com/user-attachments/assets/13c31f15-d774-4d74-89d8-d0fe3ec14b93


---


## Installation and Usage 

For easy installation, the tool comes as a single Python script using functional programming.

### Steps to Install: 

1. Download or clone the repository.
   
   ```
   git clone https://github.com/paulrounak/Weather-Forecast.git
   ```
2. Copy the `weathermap.py` file to your working directory.

### Usage: 
 
Open a terminal and run the following command to get weather conditions for a given city:


 ```
 python weathermap.py <city_name>
 ```

Example:


 ```
 python weathermap.py Hawaii
 ```

### CLI Syntax 

#### Usage: 


```
weathermap.py [-c|-f|-C|-F] <city_name>
```

#### Options: 
 
- `-c`: Get current weather in **metric units** .
 
- `-f`: Get a **5-day forecast**  in **metric units** .
 
- `-C`: Get current weather in **imperial units** .
 
- `-F`: Get a **5-day forecast**  in **imperial units** .
 
- `-h`: Display the help message.

#### Note: 
For city names with spaces, enclose the name in double quotes.
Example: `"Vatican City"`.

---


## GitHub Copilot Usage 

GitHub Copilot was installed as an extension in Visual Studio Code. It was utilized to enhance productivity through the following features:

- Generating code from comments.

- Using auto-suggest to improve code efficiency.

- Creating help statements and documentation.
---


## License 

This project is open-source. Feel free to fork, modify, and contribute to the project.


---
