#Variables
temperature = 0.7 #float
max_tokens = 1024 #int
is_streaming =False #boolean
content_box = None #None
# Type Hints
model_name:str ="gemini-2.0-flash"
temperature:float =0.7 #float
max_tokens: int =1024 #int
is_streaming:bool= False #boolean
content_box:str| None=None #None
print(type(model_name))

# Strings: immutable | string formatting
#old version
name = "LLM"
score = 97.3
print("score %.1f"%score)
print("Hello %s"%name)

#f strings (py 3,6+)
print(f"Hello:{name}")
print(f"score:{score:.1f}")


#Expression inside f- strings
word_limit = 200
print(f"{'over'if word_limit > 150 else 'under'}limit")
data = {"topic":"RAG"}
print(f"topic:{data['topic']}")

# Format specifiers
pi = 3.141592
print(f"pi:{pi:.2f}")

#Debugging
temp=0.7
print(f"{temp=}")

#multi-line f-string formatting
user_input = "what is Langchain?"
context_text = "Langchain is a framework for building applications with LLMs."
system_prompt = f"""you are a helpful assistant.
context provided: {context_text}
student question: {user_input}
Instructions:
-answer based only on the context above 
-if the answer is not in the context, say "I don't know"
-keep your answers under 3 sentences
""".strip() # remove leading and trailing whitespace
print(system_prompt)


lists: ordered, mutable, heterogeneous sequence of elements
# In Gen AI:Chat history, chunks of retrieved documents, embeddings, etc. are stored in lists
# Token sequence 
chat_history:list[dict]=[
    {"role":"user","content":"what is an LLM?"},
    {"role":"assistant","content":"A LLM is a neural network model trained on large amounts of text."}, 
]
# Acess
first_msg = chat_history[0]
print(first_msg) 
print(chat_history[-1]['content']) # last element in the list


python --version