from agno.agent import Agent
from agno.models.azure import AzureOpenAI

from databricks_connector import DatabricksSQL

# Initialize the tool
db_tool = DatabricksSQL(
    server_hostname="",
    http_path="",
    access_token="",
)

query_db_agent = Agent(
    name="Databricks Search Agent",
    role=f"""You will get an sql query. 
    You need to run it on databricks with the tool you have and explain the result in natural languge with the data in table format.
    Also you need to generate the trend graph if you some data like that.""",
    model=AzureOpenAI(id=""),
    tools=[db_tool],
    show_tool_calls=True,
    markdown=True,
    add_history_to_messages=True,
    instructions=[
        "Return the data extracted in table format"
    ]
)

# Interactive Loop for Topic Input
while True:
    user_input = input("Enter the query (type 'exit' to quit): \n").strip()
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    query_db_agent.print_response(user_input)