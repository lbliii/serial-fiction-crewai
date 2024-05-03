import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(model="gpt-3.5-turbo")

# Load YAML configuration
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


@CrewBase
class SerialFictionCrew():
    """SerialFictionCrew crew"""
    agents_config_file = 'config/agents.yaml'
    tasks_config_file = 'config/tasks.yaml'
 
    def __init__(self) -> None:
        self.model = llm
        self.agents_config = load_yaml(self.agents_config_file)
        self.tasks_config = load_yaml(self.tasks_config_file)
    
    @agent
    def concept_researcher(self):
        return Agent(
            config = self.agents_config['concept_researcher'],
            llm = self.model
        )
        
    @agent
    def world_builder(self):
        return Agent(
            config = self.agents_config['world_builder'],
            llm = self.model
        )
        
    @agent
    def plot_planner(self):
        return Agent(
            config = self.agents_config['plot_planner'],
            llm = self.model
        )
        
    @agent
    def character_designer(self):
        return Agent(
            config = self.agents_config['character_designer'],
            llm = self.model
        )
    
    @agent
    def episode_writer(self):
        return Agent(
            config = self.agents_config['episode_writer'],
            llm = self.model
        )
        
    @agent
    def story_editor(self):
        return Agent(
            config = self.agents_config['story_editor'],
            llm = self.model
        )
    
    @agent
    def lore_keeper(self):
        return Agent(
            config = self.agents_config['lore_keeper'],
            llm = self.model
        )
        
    @agent
    def timeline_keeper(self):
        return Agent(
            config = self.agents_config['timeline_keeper'],
            llm = self.model
        )
        
    @task 
    def research_story_concept(self) -> Task:
        return Task(
            config = self.tasks_config['research_story_concept'],
            agent = self.concept_researcher()
        )
        
    @task
    def build_story_world(self) -> Task:
        return Task(
            config = self.tasks_config['build_story_world'],
            agent = self.world_builder()
        )
    
    @task
    def plan_story_plot(self) -> Task:
        return Task(
            config = self.tasks_config['plan_story_plot'],
            agent = self.plot_planner()
        )
        
    @task
    def design_story_characters(self) -> Task:
        return Task(
            config = self.tasks_config['design_story_characters'],
            agent = self.character_designer()
        )
        
    @task
    def write_story_episode(self) -> Task:
        return Task(
            config = self.tasks_config['write_story_episode'],
            agent = self.episode_writer()
        )
        
    @task
    def edit_story(self) -> Task:
        return Task(
            config = self.tasks_config['edit_story'],
            agent = self.story_editor()
        )
        
    @task
    def update_story_lore(self) -> Task:
        return Task(
            config = self.tasks_config['update_story_lore'],
            agent = self.lore_keeper()
        )
        
    @task
    def update_story_timeline(self) -> Task:
        return Task(
            config = self.tasks_config['update_story_timeline'],
            agent = self.timeline_keeper()
        )
        
    @task
    def consult_with_keepers(self) -> Task:
        return Task(
            config = self.tasks_config['consult_with_keepers'],
            agent = self.lore_keeper()
        )
        
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_llm=self.model
        )
        

    