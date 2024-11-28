from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_nomic.embeddings import NomicEmbeddings
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .models import StartEmailAnalysisPayload
from langchain.schema import Document

class RAGSystem:
    def __init__(self):
        """
        Initializes the RAG system with an in-memory vector store and retriever.
        """
        urls = [
            "https://lilianweng.github.io/posts/2023-06-23-agent",
            "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering",
            "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm",
        ]
        # Load documents from the URLs
        docs = [WebBaseLoader(url).load() for url in urls]
        docs_list = [item for sublist in docs for item in sublist]

        # # Initialize an empty vector store
        # self.vectorstore = SKLearnVectorStore(
        #     embedding=NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local")
        # )
        self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=250, chunk_overlap=0
        )
        doc_splits = self.text_splitter.split_documents(docs_list)
        # Create embeddings for documents and store them in a vector store
        self.vectorstore = SKLearnVectorStore.from_documents(
            documents=doc_splits,
            embedding=NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local"),
        )

    def feed_email(self, email_content: str):
        """
        Accepts email content as a string, processes it into chunks, and adds it to the RAG system.

        Args:
            email_content (str): The content of the email to be fed into the RAG.
        """
        # Create a Document from the email content
        document = Document(page_content=email_content)

        # Split the document into smaller chunks
        chunks = self.text_splitter.split_documents([document])

        # Add chunks to the vector store
        self.vectorstore.add_documents(chunks)

        return {"message": "Email content successfully added to the RAG system."}

    def get_retriever(self):
        """
        Returns the retriever object for querying the RAG system.
        """
        return self.vectorstore.as_retriever(k=4)

rag = RAGSystem()


class RAGApplication:
    def __init__(self, retriever, rag_chain):
        self.retriever = retriever
        self.rag_chain = rag_chain
    def run(self, question):
        # Retrieve relevant documents
        documents = self.retriever.invoke(question)
        # Extract content from retrieved documents
        doc_texts = "\\n".join([doc.page_content for doc in documents])
        # Get the answer from the language model
        answer = self.rag_chain.invoke({"question": question, "documents": doc_texts})
        return answer

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

rag_application = RAGApplication(rag.get_retriever(), generate_rag_chain())

def run_email_analysis(payload: StartEmailAnalysisPayload) -> str:
    recipient_email = payload.email
    email_content = payload.content

    question = "How can I integrate outlook api when my backend server"
    answer = rag_application.run(question)
    return {"message": f"Email sent to {recipient_email} with content analysis result: {answer}"}
