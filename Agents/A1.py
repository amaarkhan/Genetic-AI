'''
Section 1: Simple Agent Scenario: Build a Packing List Advisor Agent AI agent that: Checks weather forecasts for a destination Recommends packing 
items based on weather conditions Suggests indoor/outdoor activities depending on rain/sun Agents perceive the input and then decide which tool to
 use, either 'weather tool' or 'packing advisor tool'. Based on the weather conditions in the specified location, it recommends a packing list, 
 or the user can also only ask for weather in a specific location. You should be implementing a class Agent with 5 functions:
   perceive which accepts the input and parses it to be sent to think function think which decides which tool to use 2 functions for tools:
     weather tool and packing advisor tool goal which outputs the result Task: Implement an Agent class with the following specifications: 
     Perceive Function: Extracts location and intent from user input Example input: "What should I pack for Paris?" 
     → {"location": "paris", "intent": "packing"} Think Function: Decides which tools to use If intent is "packing" → use both weather 
     and packing tools Else → use only weather tool Tools: weather_tool(location): Returns mock data like {"condition": "rainy", "temp": 14}
       packing_advisor(weather_condition): Returns items like ["umbrella", "jacket"] Goal Function: Returns structured output Example output for
         packing request: { "location": "paris", "weather": {"condition": "rainy", "temp": 14}, "packing_list": ["umbrella", "jacket"] }
'''
import string

class Agent:
    def __init__ (self):
        self.parse_input = None
        self.weather_data = None
        self.packing_list = None

    

    def perceive(self, input_text):
        # Lowercase and remove punctuation
        words = input_text.lower().translate(str.maketrans('', '', string.punctuation)).split()
        location = None
        intent = None

        if "pack" in words or "packing" in words:
            intent = "packing"
        else:
            intent = "weather"
        
        # Assume location is the last word that is not a stopword
        stopwords = {"what", "should", "i", "for", "pack", "packing", "weather", "in", "the"}
        location_candidates = [word for word in words if word not in stopwords]
        if location_candidates:
            location = location_candidates[-1]  # Get last possible location word

        self.parse_input = {"location": location, "intent": intent}
        return self.parse_input

    
    def think(self):
        if self.parse_input["intent"] == "packing":
            self.weather_data = self.weather_tool(self.parse_input["location"])
            self.packing_list = self.packing_advisor_tool(self.weather_data["condition"])
        else:
            self.weather_data = self.weather_tool(self.parse_input["location"])

    def weather_tool(self, location):
        # Mock weather data
        mock_weather_data = {
            "paris": {"condition": "rainy", "temp": 14},
            "london": {"condition": "cloudy", "temp": 10},
            "new york": {"condition": "sunny", "temp": 25}
        }
        return mock_weather_data.get(location.lower(), {"condition": "unknown", "temp": 0})
    
    def packing_advisor_tool(self, weather_condition):
        # Mock packing list based on weather condition
        packing_advice = {
            "rainy": ["umbrella", "jacket", "waterproof shoes"],
            "cloudy": ["light jacket", "sweater"],
            "sunny": ["sunglasses", "hat", "light clothing"]
        }
        return packing_advice.get(weather_condition, [])
    
    def goal(self):
        if self.parse_input["intent"] == "packing":
            return {
                "location": self.parse_input["location"],
                "weather": self.weather_data,
                "packing_list": self.packing_list
            }
        else:
            return {
                "location": self.parse_input["location"],
                "weather": self.weather_data
            }
        

agent = Agent()

input_text = "What is weather in Paris "
agent.perceive(input_text)
agent.think()
result = agent.goal()
print(result)



