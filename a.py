from langgraph.graph import StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    input: str

def process_input(state: AgentState):
    from langchain_community.llms import Ollama
    llm = Ollama(model="deepseek-r1:1.5b", base_url="http://localhost:11434")
    return {"processed_output": llm.invoke(state["input"])}

graph_builder = StateGraph(AgentState)
graph_builder.add_node("process_input", process_input)
graph_builder.set_entry_point("process_input")
graph_builder.set_finish_point("process_input")