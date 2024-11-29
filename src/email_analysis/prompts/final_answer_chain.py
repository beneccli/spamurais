from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import llm

def generate_final_answer_chain():
    # Don't add any additional information other than the one asked in the question.
    # Answer the question directly, don't mention that you used documents to answer.
    prompt = PromptTemplate(
        template="""You are an assistant for question-answering tasks.
        Use the following documents to answer the question.
        If you don't know the answer, just say that you don't know.
        Use three sentences maximum and keep the answer concise.
        Answer only with required information, no additional information.
        Question: {question}
        Documents: {documents}
        Answer:
        """,
        input_variables=["question", "documents"],
    )
    return prompt | llm | StrOutputParser()

final_answer_chain = generate_final_answer_chain()
