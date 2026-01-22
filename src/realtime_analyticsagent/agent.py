from typing import List, Tuple

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_anthropic import ChatAnthropic
from langchain_community.tools import TavilySearchResults
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from .config import validate_config

def build_agent():

    validate_config()


    llm = ChatAnthropic(
    model = "claude-haiku-4-5-20251001",
    temperature = 0.2,
    streaming = True,
    )

    #Search_tool

    search_tool = TavilySearchResults( 
       max_results = 5,
    include_answer = True
    ) 

#code tool

    code_tool = PythonREPLTool()


    tools = [search_tool, code_tool]


    agent = create_agent(
        model = llm,
        tools = tools
    )
    return agent


 #def extract_tool_names(conversation: dict) -> List[str]
#TODO : Add system prompts and tools descriptions as prompts

def run_agent(query :str) -> Tuple[List[List],str]:
    

    
    print("-------------------------")
    agent = build_agent()
    # result = agent.invoke(
    #     {
    #         "message" : [
    #             {"role" : "user" , "content" : query}
    #         ]
    #     }
    # )
    result = agent.invoke(
        {
            "messages" : [HumanMessage("Give me three fun facts about SADM, Give me short response with in 300 charcters ")]
        }
    )
    #print(result)

    tools_used : List[str] = []

    #last_message = " +++++++++++++++++++=Testing +++++++++++++++++++++"
    last_message =  result['messages'][-1].content
    #print("++++++++++++++++++++++++")
    #print(last_message)


    if isinstance(last_message,str):
        answer_text = last_message
    elif isinstance(last_message,List):
        parts = []
        for part in last_message:
            if isinstance(part, dict) and part.get("type") == "text":
                parts.append(part.get('text', ""))
            elif isinstance(part, str):
                parts.append(part)
        answer_text = "".join(parts)
    else:
        answer_text = str(last_message)
    
    return tools_used, answer_text 




if __name__ == "__main__":

    q = "Give me three fun facts about SADM, Give me short response with in 300 charcters "

    tools, answer = run_agent(q)
    print("Tools used are : ", tools )    # Add tools here later
    print("LLMs output : ", answer)


