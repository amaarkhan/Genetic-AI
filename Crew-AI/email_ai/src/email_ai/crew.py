from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class EmailAi():
    """EmailAi crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def document_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['document_reader'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def email_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['email_writer'], # type: ignore[index]
            verbose=True
        )
    
    @task
    def document_reader_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_reader_task'], # type: ignore[index]
        )

    @task
    def email_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['email_writer_task'], # type: ignore[index]
            output_file='generated_email.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the EmailAi crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
