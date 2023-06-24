# Fastest_Coder_First_Hackathon
Problem statement : Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

## Resources Used
  python version 3.10.12 <br/>
  github copilot 1.84.0.1 <br/>
  OpenWeatherMap API 3.0 <br/>
  Visual Studio Code(IDE) 1.79.2 <br/>

## An architecture flow diagram shown below.

![Architecture](https://github.com/Fastest-Coder-First/Fastest_Coder_First_Hackathon/assets/136478346/66ff3c45-0422-4c8f-b6c7-f9969646acd9)



## Working Model
The working of the command line tool for producing current and future weather conditions for a given city is shown in the video below. The video also highlights few exception conditions and the tool capability to handle exceptional conditions.


[weather.webm](https://github.com/Fastest-Coder-First/Fastest_Coder_First_Hackathon/assets/136478346/cdcf9caf-7ddb-48e0-a9ad-dc45b89faefb)




## Installation and Usage
  To maximize ease of installation, I have kept a single file with the python script using Functional Programming.
  
  1. Install or copy the file weathermap.py into your working directory.
  2. Open a terminal and run the following command to get weather conditions for a given city.

     _python weathermap.py Hawaii_

## CLI Syntax

#### Usage: weathermap.py [-c|-f|-C|-F] city <br/>

Options: <br/>
        -c: for Current Weather in metric units, <br/>
        -f: for 5-day Forecast in metric units, <br/>
        -C: for Current Weather in imperial units, <br/>
        -F: for 5-day Forecast in imperial units, <br/>
        -h: for help <br/>
        <br/>
#### For Help <br/>
Usage: weathermap.py -h <br/>
        
#### Note: For City names with spaces, enclose within "" (double quotes). For Example "Vatican City".
<br/>

## Github Copilot Usage
Github Copilot was installed as an extension in the VS Code IDE. Its usage was maximized by <br/>
  -generating code from comments, <br/>
  -using its code autosuggest feature. <br/>
  -generating help statements.<br/>
  
## An example of github copilot usage for code generation is given below:

[gitcopilot.webm](https://github.com/Fastest-Coder-First/Fastest_Coder_First_Hackathon/assets/136478346/81f9882c-83f3-42ce-88f8-7e91637d4fab)

