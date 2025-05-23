import os
from textwrap import dedent
from crewai import Agent
# from tools.browser_tools import BrowserTools
# from tools import SearchTools
from langchain.llms import Ollama
from langchain_community.llms import Ollama

class SoftwareDevelopmentAgents:
    def __init__(self):
        self.llm = Ollama(model=os.environ['MODEL'])

    def project_manager_agent(self):
        return Agent(
            role="Project Manager",
            goal=dedent("""\
                Create comprehensive Software Requirements Specification (SRS) document
                for the given software idea."""),
            backstory=dedent("""\
                As the Project Manager, you are responsible for gathering requirements
                and creating the SRS document to guide the development process."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                #   SearchTools.search_internet
            ],
            allow_delegation=False,
            # llm=self.llm,
            verbose=True
        )

    def architect_agent(self):
        return Agent(
            role="Architect",
            goal=dedent("""\
                Design system architecture and create flow diagrams for the given software idea."""),
            backstory=dedent("""\
                As the Architect, you are tasked with designing the system architecture
                and creating flow diagrams based on the SRS document."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                #  SearchTools.search_internet
            ],
            # llm=self.llm,
            verbose=True
        )

    def software_developer_agent(self):
        return Agent(
            role="Software Developer",
            goal=dedent("""\
                Develop the software solution and write code based on the provided input."""),
            backstory=dedent("""\
                As the Software Developer, you are responsible for implementing the software
                solution based on the architecture and SRS document."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                #  SearchTools.search_internet
            ],
            # llm=self.llm,
            verbose=True
        )

    def tester_agent(self):
        return Agent(
            role="Tester",
            goal=dedent("""\
                Perform unit testing on the provided solution and code."""),
            backstory=dedent("""\
                As the Tester, you ensure the quality and functionality of the developed software
                by performing thorough unit testing."""),
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                #  SearchTools.search_internet
            ],
            allow_delegation=False,
            # llm=self.llm,
            verbose=True
        )
