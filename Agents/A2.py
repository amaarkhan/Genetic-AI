'''
Section 2: Multi-Agent System Build a Multi-Agent Travel Planning System that combines two specialized agents: Destination Recommender Agent that
 suggests travel destinations based on user preferences (beach, adventure, cultural trips) Weather Packing Agent (from Section 1) that generates 
 packing lists for the recommended destination The system coordinates between agents to provide complete travel planning assistance Task:
   The first agent perceives user preferences and recommends destinations using a 'destination recommender tool'.
     The second agent takes this recommendation, checks weather conditions, and provides a comprehensive packing list.
       The multi-agent system orchestrates the workflow between both agents to deliver a complete travel planning solution. 
       Final output should contain: Combines outputs from both agents Returns comprehensive travel planning response 
       Example output: json { "destination_recommendation": { "location": "Bali", "trip_type": "beach" }, 
       "weather_info": { "condition": "sunny", "temp": 28 }, "packing_list": ["sunscreen", "swimsuit", "sunglasses", "light_clothing"] } 
       Implement the destination recommender agent in the following way: Destination Recommender Agent Class: Perceive Function: 
       Extracts trip type from the user input Example input: "I want a beach vacation" → {"trip_type": "beach”} Think Function: 
       Decides to use destination recommender tool based on trip type Tools: destination_recommender_tool(trip_type): 
       Returns mock destinations like {"destination": "Bali", "type": "beach"} Goal Function: Returns structured destination recommendation 
       Example output: {"recommended_destination": "Bali", "trip_type": "beach"}
'''

class DestinationRecommenderAgent:
    def __init__(self):
        self.trip_type = None
        self.recommendation = None

    def perceive(self, input_text):
        words = input_text.lower().split()
        for word in words:
            if word in ["beach", "adventure", "cultural"]:
                self.trip_type = word
                break
        return {"trip_type": self.trip_type}

    def think(self):
        self.recommendation = self.destination_recommender_tool(self.trip_type)

    def destination_recommender_tool(self, trip_type):
        destinations = {
            "beach": {"destination": "Bali", "type": "beach"},
            "adventure": {"destination": "Nepal", "type": "adventure"},
            "cultural": {"destination": "Rome", "type": "cultural"}
        }
        return destinations.get(trip_type, {"destination": "unknown", "type": trip_type})

    def goal(self):
        return {
            "recommended_destination": self.recommendation["destination"],
            "trip_type": self.recommendation["type"]
        }




class PackingAgent:
    def __init__ (self):
        self.parse_input = None
        self.weather_data = None
        self.packing_list = None

    def perceive(self, location):
        self.parse_input = {"location": location, "intent": "packing"}
        return self.parse_input

    def think(self):
        if self.parse_input["intent"] == "packing":
            self.weather_data = self.weather_tool(self.parse_input["location"])
            self.packing_list = self.packing_advisor_tool(self.weather_data["condition"])
        else:
            self.weather_data = self.weather_tool(self.parse_input["location"])

    def weather_tool(self, location):
        mock_weather_data = {
            "bali": {"condition": "sunny", "temp": 28},
            "nepal": {"condition": "cloudy", "temp": 12},
            "rome": {"condition": "rainy", "temp": 16}
        }
        return mock_weather_data.get(location.lower(), {"condition": "unknown", "temp": 0})

    def packing_advisor_tool(self, condition):
        packing_advice = {
            "sunny": ["sunscreen", "swimsuit", "sunglasses", "light_clothing"],
            "cloudy": ["jacket", "boots"],
            "rainy": ["umbrella", "raincoat", "waterproof shoes"]
        }
        return packing_advice.get(condition, [])

    def goal(self):
        return {
            "weather_info": self.weather_data,
            "packing_list": self.packing_list
        }




class TravelPlannerSystem:
    def __init__(self):
        self.destination_agent = DestinationRecommenderAgent()
        self.packing_agent = PackingAgent()

    def run(self, user_input):
        # Step 1: Recommend Destination
        self.destination_agent.perceive(user_input)
        self.destination_agent.think()
        destination_result = self.destination_agent.goal()

        # Step 2: Packing Plan
        location = destination_result["recommended_destination"]
        self.packing_agent.perceive(location)
        self.packing_agent.think()
        packing_result = self.packing_agent.goal()

        # Step 3: Combine results
        return {
            "destination_recommendation": {
                "location": location,
                "trip_type": destination_result["trip_type"]
            },
            "weather_info": packing_result["weather_info"],
            "packing_list": packing_result["packing_list"]
        }



planner = TravelPlannerSystem()
user_input = "I want a beach vacation"
result = planner.run(user_input)
print(result)
