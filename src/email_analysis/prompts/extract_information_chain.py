from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import llm

def generate_extract_information_chain():
    # Don't add any additional information other than the one asked in the question.
    # Answer the question directly, don't mention that you used documents to answer.
    prompt = PromptTemplate(
        template="""Extract all meaningful information and relationships from the following email. Summarize each piece of information concisely in the format “Entity Action Object” or similar. Separate multiple pieces of information with pipes ("|"). Do not include any explanations, headers, comments, or extra text—output only the summarized information as a single line separated by pipes.

Here is the email:
{email_content}

Expected Output (and nothing else):
Pierre password will expire | Celine is now working on the project Arrakis | The report is due by Friday | The meeting will take place at 3 PM in Room 402
""",
        input_variables=["email_content"],
    )
    return prompt | llm | StrOutputParser()

extract_information_chain = generate_extract_information_chain()



