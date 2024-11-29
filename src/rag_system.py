from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_nomic.embeddings import NomicEmbeddings
from langchain_community.vectorstores import SKLearnVectorStore
from langchain.schema import Document

class RAGSystem:
    def __init__(self):
        """
        Initializes the RAG system with an in-memory vector store and retriever.
        """
        # Initialize an empty vector store
        self.vectorstore = SKLearnVectorStore(
            embedding=NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local")
        )

        self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=250, chunk_overlap=0
        )

        self.retriever = self.vectorstore.as_retriever(k=1)

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

    
rag_instance = RAGSystem()
