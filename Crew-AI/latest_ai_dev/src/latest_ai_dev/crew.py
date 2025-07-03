from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class LatestAiDev():
    """LatestAiDev crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

  
    @agent
    def email_writer(self)->Agent:
        return Agent(
            config=self.agents_config['email_writer'],
            verbose=True,
        )
    
    @task
    def email_task(self)-> Task:
        return Task(
            config=self.tasks_config['email_generation_task'],
            output_file='generated_email.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Email generator crew"""
 
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
