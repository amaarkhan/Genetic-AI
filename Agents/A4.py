'''
Section 4: Implement using BDI (Believe, Desire, Intention) 
Agent purpose: 
Create an agent that takes user preference based on weather like sunny or rainy and tells the user about places to visit. 
Objective: 
Build an agent that: 
Believe: Extracts and stores key facts from user input to form the agent's beliefs 
Desires: Highlights what the user wants and sends it to the ‘intend’ function. 
Intends: Executes tool (suggest places depend on user specified weather)  

Outputs: list of places according to the weather conditions specified. 
'''
import string

class BDI:
    def __init__(self):
        pass

    def believe(self, weather):
        if "rain" in weather:
            return "rainy"
        elif "sun" in weather:
            return "sunny"
        elif "snow" in weather:
            return "snowy"
        else:
            return "unknown"

    def desire(self, weather_condition):
        if weather_condition == "rainy":
            print("User prefers indoor activities due to rain.")
        elif weather_condition == "sunny":
            print("User prefers outdoor activities due to sun.")
        elif weather_condition == "snowy":
            print("User prefers snowy activities.")
        else:
            print("User has no specific weather preference.")
        return weather_condition

    def intend(self, weather_condition):
        if weather_condition == "rainy":
            return ["Visit a museum", "Go to a cafe", "Watch a movie"]
        elif weather_condition == "sunny":
            return ["Visit the beach", "Go hiking", "Have a picnic"]
        elif weather_condition == "snowy":
            return ["Go skiing", "Build a snowman", "Enjoy hot chocolate"]
        else:
            return ["No specific places available for this weather condition"]

bdi = BDI()
a=input("Enter the weather condition (e.g., 'rainy', 'sunny', 'snowy'): ")
b = bdi.believe(a)
c = bdi.desire(b)
d = bdi.intend(c)
print(f"Recommended places for {c} weather: {', '.join(d)}")