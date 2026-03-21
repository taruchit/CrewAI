from crewai import Agent, Crew, Process, Task
from crewai import CrewBase, agent, crew, task
import os

@CrewBase
class BlogWritingWithCrewAI:
    # Dynamically locate the config folder relative to this file
    base_path = os.path.dirname(__file__)
    agents_config = os.path.join(base_path, 'config/agents.yaml')
    tasks_config = os.path.join(base_path, 'config/tasks.yaml')

    @agent
    def report_generator(self) -> Agent:
        return Agent(config=self.agents_config['report_generator'])

    @agent
    def blog_writer(self) -> Agent:
        return Agent(config=self.agents_config['blog_writer'])

    @task
    def report_task(self) -> Task:
        return Task(config=self.tasks_config['report_task'])

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_writing_task'],
            output_file=os.path.join(self.base_path, '/content/blog_writing_project/blogs/blog.md')
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
