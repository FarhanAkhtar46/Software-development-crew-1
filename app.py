import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from crewai import Agent, Crew
from task import SoftwareDevelopmentTasks
from agents import SoftwareDevelopmentAgents

# Initialize tasks and agents
tasks = SoftwareDevelopmentTasks()
agents = SoftwareDevelopmentAgents()

# Streamlit UI
st.title("Software Development Crew")
st.subheader("Welcome to the Software Development Crew")

software_idea = st.text_input("Enter the software idea:", "school management system")

def save_to_file(content, filename):
    """Save content to a file."""
    with open(filename, 'w') as file:
        file.write(content)

def create_and_run_crew(agents, tasks, crew_name):
    """Create and run a crew with the given agents and tasks."""
    st.write(f"Starting {crew_name}...")
    crew = Crew(agents=agents, tasks=tasks, verbose=True)
    results = crew.kickoff()
    st.write(f"{crew_name} completed.")
    return results

if st.button("Run Crew"):
    st.write("Running the Software Development Crew...")

    # Define agents
    project_manager_agent = agents.project_manager_agent()
    architect_agent = agents.architect_agent()
    developer_agent = agents.software_developer_agent()
    tester_agent = agents.tester_agent()

    # Define tasks
    documentation_creation = tasks.documentation_creation(project_manager_agent, software_idea)
    architecture_design = tasks.architecture_design(architect_agent, software_idea)
    code_development = tasks.code_development(developer_agent, software_idea)
    unit_testing = tasks.unit_testing(tester_agent, software_idea)

    # Run Documentation and Architecture Crews
    doc_results = create_and_run_crew(
        agents=[project_manager_agent],
        tasks=[documentation_creation],
        crew_name="Documentation Crew"
    )
    arch_results = create_and_run_crew(
        agents=[architect_agent],
        tasks=[architecture_design],
        crew_name="Architecture Crew"
    )

    # Save Documentation and Architecture outputs
    if doc_results and arch_results:
        save_to_file(doc_results, 'SRS_documentation.txt')
        save_to_file(arch_results, 'High_level_design_documentation.txt')
    else:
        st.error("Error: Incomplete results from Documentation and Architecture Crew")

    # Run Development and Testing Crews
    dev_results = create_and_run_crew(
        agents=[developer_agent],
        tasks=[code_development],
        crew_name="Development Crew"
    )
    test_results = create_and_run_crew(
        agents=[tester_agent],
        tasks=[unit_testing],
        crew_name="Testing Crew"
    )

    # Save Development and Testing outputs
    if dev_results and test_results:
        save_to_file(dev_results, 'ok.txt')
        save_to_file(test_results, 'Test_results.txt')
    else:
        st.error("Error: Incomplete results from Development and Testing Crew")

    st.success('Files saved successfully!')