'''
Section 3: Implement using the OODA Loop (Observe-Orient-Decide-Act) 
Agent Purpose (Travel Itinerary Planner Agent): 
This AI agent helps users plan a day of travel by: 
Fetching tourist attractions in a given city. 
Checking local weather to adjust recommendations. 
Suggesting indoor/outdoor activities based on weather. 
Estimating time required for each activity. 

Agent Workflow: 
Input: User query (e.g., "Plan a day in Barcelona"). 

Tools: 
attractions_tool(location) → Returns ["Sagrada Familia", "Park Güell"]. 
weather_tool(location) → Returns {"condition": "rainy", "temp": 16}. 
time_estimator(activity) → Returns {"Sagrada Familia": "2 hours"}. 
Output: Structured itinerary with weather-adjusted activities and time estimates. 

Task: 
Build the agent using the OODA framework, where: 
Observe: Parse user input (e.g., "Plan a day in Berlin" → {"location": "berlin", "intent": "itinerary"}). 

Orient: 
Check if the user specified weather constraints (e.g., "if it rains"). 
Prioritize indoor activities for bad weather. 

Decide: Decide which action to take. Like, take out activities according to the weather conditions and estimated time. 

Act: Execute tools and compile results. 
Example Output: 
{ 
 "location": "berlin", 
 "weather": {"condition": "sunny", "temp": 22}, 
 "itinerary": [ 
  {"activity": "Museum Island", "time": "3 hours", "type": "indoor"} 
 ] 
} 
'''

import string
class Agent:
    def __init__(self):
        self.parse_input = None
        self.weather_data = None
        self.attractions = None
        self.time_estimates = None
        self.itinerary = []

    def perceive(self, input_text):
        # Lowercase and remove punctuation
        words = input_text.lower().translate(str.maketrans('', '', string.punctuation)).split()
        location = None
        intent = None

        if "plan" in words or "itinerary" in words:
            intent = "itinerary"
        else:
            intent = "weather"

        # Assume location is the last word that is not a stopword
        stopwords = {"what", "should", "i", "for", "pack", "packing", "weather", "in", "the"}
        location_candidates = [word for word in words if word not in stopwords]
        if location_candidates:
            location = location_candidates[-1]
        self.parse_input = {"location": location, "intent": intent}
        return self.parse_input
    
    def think(self):
        if self.parse_input["intent"] == "itinerary":
            self.weather_data = self.weather_tool(self.parse_input["location"])
            self.attractions = self.attractions_tool(self.parse_input["location"])
            for attraction in self.attractions:
                time_estimate = self.time_estimator(attraction)
                if self.weather_data["condition"] == "rainy" and time_estimate:
                    # Prioritize indoor activities
                    self.itinerary.append({
                        "activity": attraction,
                        "time": time_estimate,
                        "type": "indoor"
                    })
                else:
                    self.itinerary.append({
                        "activity": attraction,
                        "time": time_estimate,
                        "type": "outdoor"
                    })
        else:
            self.weather_data = self.weather_tool(self.parse_input["location"])

    def weather_tool(self, location):
        # Mock weather data
        mock_weather_data = {
            "berlin": {"condition": "sunny", "temp": 22},
            "paris": {"condition": "rainy", "temp": 16},
            "barcelona": {"condition": "cloudy", "temp": 20}
        }
        return mock_weather_data.get(location.lower(), {"condition": "unknown", "temp": 0})
    
    def attractions_tool(self, location):
        # Mock attractions data
        mock_attractions = {
            "berlin": ["Museum Island", "Brandenburg Gate", "Berlin Wall"],
            "paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
            "barcelona": ["Sagrada Familia", "Park Güell", "Gothic Quarter"]
        }
        return mock_attractions.get(location.lower(), [])
    
    def time_estimator(self, activity):
        # Mock time estimates
        mock_time_estimates = {
            "Museum Island": "3 hours",
            "Brandenburg Gate": "1 hour",
            "Berlin Wall": "2 hours",
            "Eiffel Tower": "2 hours",
            "Louvre Museum": "4 hours",
            "Notre-Dame Cathedral": "1.5 hours",
            "Sagrada Familia": "2 hours",
            "Park Güell": "1.5 hours",
            "Gothic Quarter": "2 hours"
        }
        return mock_time_estimates.get(activity, None)
    
    def goal(self):
        if self.parse_input["intent"] == "itinerary":
            return {
                "location": self.parse_input["location"],
                "weather": self.weather_data,
                "itinerary": self.itinerary
            }
        else:
            return {
                "location": self.parse_input["location"],
                "weather": self.weather_data
            }
        
agent = Agent()
input_text = "Plan a day in Barcelona"
agent.perceive(input_text)
agent.think()
result = agent.goal()
print(result)