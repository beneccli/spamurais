from src.rag_system import rag_instance

def initialize_rag_email_analysis():
    rag_instance.feed_email("User's name is Benoit Eccli.")
    rag_instance.feed_email("User's is 32 years old.")
    rag_instance.feed_email("User's nationality is French.")
    rag_instance.feed_email("User is an expat living in Hong Kong.")
    rag_instance.feed_email("User has a girlfriend called Vaishnavi.")
