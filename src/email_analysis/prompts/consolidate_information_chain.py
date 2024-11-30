from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import llm

def generate_consolidate_information_chain():
    # Don't add any additional information other than the one asked in the question.
    # Answer the question directly, don't mention that you used documents to answer.
    prompt = PromptTemplate(
        template="""Refine the following summarized information, which is separated by pipes ("|"), by merging only related or redundant pieces of information into a single, coherent summary. Consider two pieces of information related only if they involve the same person, entity, or project and describe closely connected actions or objects. Do not merge items based solely on shared dates, times, or general keywords unless they clearly refer to the same context or subject.

Output only the refined information as a single line of text, with each piece of information separated by pipes ("|"). Do not include any additional text, explanations, or headers—output only the refined information.

Here is the input:
{email_infos}

Example Input:
Q3 budget reconciliation report must be reviewed and submitted to Finance Department by Friday COB | Emma will coordinate final review with team members | Alan will prepare presentation slides for client pitch and share draft with team by Thursday | Sophia has transitioned to CyberSecurity Enhancement project | Monthly software updates will be rolled out this weekend | Raj needs to update inventory system logs by Thursday | Weekly brainstorming session is scheduled for Wednesday at 10:00 AM in Innovation Lab (Room 205)

Expected Output:
Q3 budget reconciliation report must be reviewed and submitted to Finance Department by Friday COB | Emma will coordinate final review with team members | Alan will prepare presentation slides for client pitch and share draft with team by Thursday | Sophia has transitioned to CyberSecurity Enhancement project | Monthly software updates will be rolled out this weekend | Raj needs to update inventory system logs by Thursday | Weekly brainstorming session is scheduled for Wednesday at 10:00 AM in Innovation Lab (Room 205)
""",
        input_variables=["email_infos"],
    )
    return prompt | llm | StrOutputParser()

consolidate_information_chain = generate_consolidate_information_chain()
