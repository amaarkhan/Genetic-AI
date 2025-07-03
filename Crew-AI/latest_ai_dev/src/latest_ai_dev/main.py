#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from latest_ai_dev.crew import LatestAiDev

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    user_input= input("Enter the info you want to send an email about: ")


    inputs = {
        'email_context': user_input,  
        'current_year': str(datetime.now().year)
    }
    
    try:
        LatestAiDev().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

