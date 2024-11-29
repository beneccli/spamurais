from src.rag_system import rag_instance
from .models import StartEmailAnalysisPayload
from .prompts.rag_keywords_chain import rag_keywords_chain
from .prompts.final_answer_chain import final_answer_chain
from src.llm import llm
from langchain_core.output_parsers import StrOutputParser


def run_email_analysis(payload: StartEmailAnalysisPayload) -> str:
    recipient_email = payload.email
    email_content = payload.content

    retriever = rag_instance.retriever

    # question = "What is the name of the user?"
    question = email_content
    # documents = retriever.invoke(question)

    # rag_keywords_chain = rag_keywords_prompt | llm | StrOutputParser()
    rag_keywords_llm_output = rag_keywords_chain.invoke({"user_input": question})
    rag_keywords_list = rag_keywords_llm_output.split('|')

    documents = []

    for keywords in rag_keywords_list:
        documents.extend(retriever.invoke(keywords))

    doc_texts = "\\n".join([doc.page_content for doc in documents])
    answer = final_answer_chain.invoke({"question": question, "documents": doc_texts})

    return {answer}
