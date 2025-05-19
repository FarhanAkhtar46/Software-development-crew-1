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
    try:
        with open(filename, 'w') as file:
            file.write(content)
        st.success(f"File saved: {filename}")
    except (OSError, IOError) as e:
        st.error(f"Error saving file {filename}: {e}")

def create_and_run_crew(agents, tasks, crew_name):
    """Create and run a crew with the given agents and tasks."""
    try:
        st.write(f"Starting {crew_name}...")
        crew = Crew(agents=agents, tasks=tasks, verbose=True)
        results = crew.kickoff()
        st.write(f"{crew_name} completed.")
        return results
    except Exception as e:
        st.error(f"Error running {crew_name}: {e}")
        return None

def handle_crew_results(results, filename, crew_name):
    """Handle the results of a crew and save them to a file."""
    if results:
        save_to_file(results, filename)
    else:
        st.error(f"Error: No results from {crew_name}")

if st.button("Run Crew"):
    st.write("Running the Software Development Crew...")

    # Define agents
    project_manager_agent = agents.project_manager_agent()
    architect_agent = agents.architect_agent()
    developer_agent = agents.software_developer_agent()
    tester_agent = agents.tester_agent()
    cost_estimator_agent = agents.cost_estimator_agent()  # New agent for cost estimation

    # Define tasks
    documentation_creation = tasks.documentation_creation(project_manager_agent, software_idea)
    architecture_design = tasks.architecture_design(architect_agent, software_idea)
    code_development = tasks.code_development(developer_agent, software_idea)
    unit_testing = tasks.unit_testing(tester_agent, software_idea)
    cost_estimation = tasks.cost_estimation(cost_estimator_agent, software_idea)  # New task for cost estimation

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
    handle_crew_results(doc_results, 'SRS_documentation.txt', "Documentation Crew")
    handle_crew_results(arch_results, 'High_level_design_documentation.txt', "Architecture Crew")

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
    handle_crew_results(dev_results, 'Developed_cdnjdndjdjode.txt', "Development Crew")
    handle_crew_results(test_results, 'Test_results.txt', "Testing Crew")

    # Run Cost Estimation Crew
    cost_results = create_and_run_crew(
        agents=[cost_estimator_agent],
        tasks=[cost_estimation],
        crew_name="Cost Estimation Crew"
    )

    # Save Cost Estimation output
    handle_crew_results(cost_results, 'Cost_ekkmation.txt', "Cost Estimation Crew")

    st.success('All  dddddnd d completed kdjkdessfully!')