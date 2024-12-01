from src.rag_system import rag_instance
from .models import StartEmailAnalysisPayload
from .prompts.rag_keywords_chain import rag_keywords_chain
from .prompts.final_answer_chain import final_answer_chain
from .prompts.extract_information_chain import extract_information_chain
from .prompts.consolidate_information_chain import consolidate_information_chain
from .prompts.keep_only_relevant_info_chain import keep_only_relevant_info_chain
import re

def run_email_analysis(payload: StartEmailAnalysisPayload) -> str:
    retriever = rag_instance.retriever
    user_info = "My name is Alan MELIER. I am software engineer. I am part of the team ABC/DEF/XRP. I am working on the project SGIA."

    # Step 1 - Extract information from email
    extract_information_output = extract_information_chain.invoke({"email_content": payload.content})
    consolidated_infos = consolidate_information_chain.invoke({"email_infos": extract_information_output})
    relevant_infos = keep_only_relevant_info_chain.invoke({"summarised_info": consolidated_infos, "user_info": user_info})

    pattern = r"<START_FINAL_RESULT>(.*?)<END_FINAL_RESULT>"
    match = re.search(pattern, relevant_infos)

    if match:
        relevant_infos = match.group(1)

    information_brut = relevant_infos.split(" | ")

    print(extract_information_output)
    print(consolidated_infos)

    rag_keywords_llm_output = rag_keywords_chain.invoke({"user_input": payload.content})
    rag_keywords_list = rag_keywords_llm_output.split('|')

    documents = []

    for keywords in rag_keywords_list:
        documents.extend(retriever.invoke(keywords))

    doc_texts = "\\n".join([doc.page_content for doc in documents])
    answer = final_answer_chain.invoke({"email_content": payload.content, 
                                        "rag_documents": doc_texts})

    return {relevant_infos}
