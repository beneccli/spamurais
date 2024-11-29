from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import llm

def generate_rag_keywords_chain():
    # Don't add any additional information other than the one asked in the question.
    # Answer the question directly, don't mention that you used documents to answer.
    prompt = PromptTemplate(
        template="""You are an expert at extracting concise and relevant keywords from a user’s question to query a knowledge base. Your task is to output only the extracted keywords as a single string, separated by pipes (|). Ensure each keyword or phrase is complete and self-contained, repeating any necessary context to make each keyword meaningful on its own.

Examples:
	1.	User’s question: “What is the user’s name and age?”
Output: user name|user age
	2.	User’s question: “What are the advantages of solar energy?”
Output: solar energy advantages
	3.	User’s question: “What is the user’s size and gender?”
Output: user size|user gender
	4.	User’s question: “How do plants perform photosynthesis?”
Output: plants photosynthesis

Now, extract keywords for the following user’s question:

User’s question: “{user_input}”

Output:
        """,
        input_variables=["user_input"],
    )
    return prompt | llm | StrOutputParser()

rag_keywords_chain = generate_rag_keywords_chain()
