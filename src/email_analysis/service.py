from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.rag_system import rag_instance
from .models import StartEmailAnalysisPayload


def generate_rag_chain():
    prompt = PromptTemplate(
        template="""You are an assistant for question-answering tasks.
        Use the following documents to answer the question.
        If you don't know the answer, just say that you don't know.
        Use three sentences maximum and keep the answer concise:
        Question: {question}
        Documents: {documents}
        Answer:
        """,
        input_variables=["question", "documents"],
    )
    llm = ChatOllama(model="llama3.1", temperature=0)
    return prompt | llm | StrOutputParser()

def run_email_analysis(payload: StartEmailAnalysisPayload) -> str:
    recipient_email = payload.email
    email_content = payload.content

    retriever = rag_instance.retriever
    rag_chain = generate_rag_chain()

    question = "How can I integrate outlook api when my backend server"
    documents = retriever.invoke(question)
    doc_texts = "\\n".join([doc.page_content for doc in documents])
    answer = rag_chain.invoke({"question": question, "documents": doc_texts})
    
    return {"message": f"Email sent to {recipient_email} with content analysis result: {answer}"}
