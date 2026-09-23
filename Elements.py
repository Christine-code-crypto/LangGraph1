### STATE:
# A shared data structure that stores the current information or context
# of the entire application.
#
# Think of it like the application's memory.
# It keeps track of variables and data that different nodes can access
# and modify while they are running.

#State = shared memory
#Nodes = functions/workers that read or update that memory

### NODE
# Nodes:
# Nodes are functions that perform specific tasks in the graph.
#
# Each node usually receives the current state,
# does some work with it,
# and returns new information or an updated state.

###GRAPH
# A graph is the overall structure that connects different nodes together.
#
# It controls the order in which nodes run
# and decides which path the program should follow.
#
# Think of it as the workflow or roadmap of the application.
#State = the shared memory/data
# = the workers/functions
#Graph = the map showing which worker runs next

###EDGE
# Edges are the connections between nodes in a graph.
#
# They decide which node should run next
# after the current node finishes its task.
#
# Think of edges like train tracks:
# nodes are the stations,
# and edges are the tracks connecting the stations.
#State = the data being remembered
#Node  = the function doing the work
#Edge  = the connection/path between nodes
#Graph = the whole workflow containing everything

### Conditional Edges:
# Conditional edges choose the next node based on a condition.
#
# They check the current state,
# make a decision,
# and then send the graph to the correct next node.
#
# Think of them like traffic lights:
# the condition decides which direction to go next.

### START:
# START is the virtual entry point of a LangGraph workflow.
#
# It marks where the graph begins.
# START does not perform any task itself.
# It simply tells LangGraph which node should run first.
#
# Think of it like the starting line of a race.

### END:
# END is the virtual finishing point of a LangGraph workflow.
#
# It tells LangGraph that the graph has finished running.
# Once execution reaches END, no more nodes are executed.
#
# Think of it like the finish line of a race.

#### Tools:
# Tools are special functions or utilities that nodes can use
# to perform specific tasks.
#
# For example, a tool can:
# fetch data from an API,
# search for information,
# query a database,
# or perform calculations.
#
# Nodes are part of the graph itself,
# while tools are extra abilities that nodes can use.
#
# Think of tools like items in a toolbox:
# each tool has a specific job.
#Tool = something a node uses to get a job done.
#A node can exist in the graph, while a tool is usually something the node calls when it needs extra capability.
#For instance a user wants to know the weather in Nairobi,
#The node will use weather API tool to Gets weather data


### ToolNode:
# A ToolNode is a special node whose main job is to run a tool.
#
# Example:
# If the user asks for the weather,
# the AI may decide that it needs the weather tool.
#
# The ToolNode runs the weather tool/API,
# gets the weather data,
# and puts the result back into the State.
#
# Other nodes can then use that weather information.
#
# Example flow:
# AI Node -> ToolNode -> Weather Tool -> Weather Data -> State
#Weather API/tool = knows HOW to fetch weather data
#ToolNode          = runs/calls that tool when requested

###### API = a way for different software systems to communicate with each other.
###### An API is a way for one program to talk to another program and ask it for something.

############# StateGraph:
# StateGraph is the main structure used to build a LangGraph workflow.
#
# It brings together:
# - the State
# - the Nodes
# - the Edges
# - the Conditional Edges
#
# It defines how all these parts are connected
# and how data moves through the workflow.
#
# Think of StateGraph like a building blueprint:
# it shows how all parts of the workflow fit together.
# StateGraph = the structure where you build your whole LangGraph workflow.
# StateGraph = the LangGraph class/tool you use to build that workflow around a shared State


##### Runnable:
# A Runnable is something that can be executed to perform a task.
#
# It usually takes some input,
# does some work,
# and produces an output.
#
# Runnables can be combined together
# to build larger AI workflows.
#
# Think of a Runnable like a LEGO brick:
# each brick does one part,
# and many bricks can be connected together.
# Runnable = something that can be run.
# Runnable = an executable component that can be used as part of a workflow, including inside nodes or other chains
###A NODE CAN BE A RUNNABLE

########### Messages:
# Messages represent the different kinds of information
# exchanged between the user, AI model, and tools.
#
# HumanMessage:
# A message coming from the user.
#
# SystemMessage:
# Instructions or context given to the AI model.
#
# AIMessage:
# A response produced by the AI model.
#
# ToolMessage:
# The result returned after a tool has been used.
#
# FunctionMessage:
# An older message type used to represent results from function calls.
# In modern LangChain/LangGraph tool calling, ToolMessage is commonly used instead.

'''
SystemMessage:
"You are a helpful weather assistant."

        ↓

HumanMessage:
"What's the weather in Nairobi?"

        ↓

AIMessage:
"I need to use the weather tool."

        ↓

Tool runs...

        ↓

ToolMessage:
"Temperature: 24°C, Cloudy"

        ↓

AIMessage:
"It's 24°C and cloudy in Nairobi."
'''