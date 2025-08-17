from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph


class ChatAgent:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if ChatAgent._instance is not None:
            raise RuntimeError('Use instance() instead of constructor')
        self.model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
        self.workflow = StateGraph(state_schema=MessagesState)
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self._call_model)
        memory = MemorySaver()
        self.app = self.workflow.compile(checkpointer=memory)

    def chat(self, message: str, session_key: str, stream: bool = False):
        input_messages = [HumanMessage(message)]
        config = {'configurable': {'thread_id': session_key}}
        if stream:
            for chunk, metadata in self.app.stream({"messages": input_messages}, config, stream_mode="messages"):
                if isinstance(chunk, AIMessage):
                    print(chunk.content, end="|", flush=True)
            return
        output = self.app.invoke({"messages": input_messages}, config)
        return output["messages"][-1].content

    def _call_model(self, state: MessagesState):
        response = self.model.invoke(state["messages"])
        return {"messages": response}


if __name__ == '__main__':
    agent = ChatAgent.instance()
    agent.chat("Tell me a fun fact about pandas", 'test', stream=True)
