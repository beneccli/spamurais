from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import llm

def generate_keep_only_relevant_info_chain():
    # Don't add any additional information other than the one asked in the question.
    # Answer the question directly, don't mention that you used documents to answer.
    prompt = PromptTemplate(
        template="""You are given:
	•	User Information:
{user_info}


	•	Summarized Information:
{summarised_info}



Your Task:

Filter the summarized information to retain only the pieces that are relevant to the user, based on their provided information.

Relevance Criteria:
	•	The information directly mentions the user's name.
	•	The information relates to the user's job title, role, projects, team, or department.
	•	The information describes major organizational changes that will significantly impact the user.

Do Not Include:
	•	Information about other people's tasks or roles, unless they directly involve or impact the user.
	•	General announcements or events that do not directly affect the user.

Instructions:
	1.	Do not modify any of the summarized information. Keep each piece exactly as it is written. Do not change names, roles, or any details within the sentences.
	2.	Only filter the information by removing or keeping entire pieces of summarized information (the text between the pipes).
	3.	Process each piece individually:
	•	For each piece of summarized information, determine if it meets any of the Relevance Criteria.
	•	If it does, include it in the output.
	•	If it does not, exclude it.
	4.	Output Format: Provide the filtered information only between the tags <START_FINAL_RESULT> and <END_FINAL_RESULT>. Inside these tags, list the filtered information as a single line of text, with each piece separated by pipes ("|").
	5.	Do not include any additional text, explanations, comments, or headers—output only the tags and the filtered relevant information between them.
	6.	Important: Any output outside the <START_FINAL_RESULT> and <END_FINAL_RESULT> tags will be discarded. Ensure all relevant information is within these tags.

Example Input:

User Information:

My name is Alan MELIER. I am a software engineer. I am part of the team ABC/DEF/XRP. I am working on the project SGIA.

Summarized Information:

Q3 budget reconciliation report must be reviewed and submitted to Finance Department by Friday COB | Emma will coordinate final review with team members | Alan will prepare presentation slides for client pitch and share draft with team by Thursday | Sophia has transitioned to CyberSecurity Enhancement project | Raj needs to update inventory system logs by Thursday | Weekly brainstorming session is scheduled for Wednesday at 10:00 AM in Innovation Lab (Room 205)

Expected Output:

<START_FINAL_RESULT>Alan will prepare presentation slides for client pitch and share draft with team by Thursday<END_FINAL_RESULT>

Notes:
	•	Do not include “Raj needs to update inventory system logs by Thursday" because it does not involve or impact the user.
	•	Do not include “Sophia has transitioned to CyberSecurity Enhancement project" unless the user is involved with that project.
	•	Only include information that directly involves or impacts the user.

This refined prompt explicitly instructs the model to:
	•	Only include information that is directly relevant to the user.
	•	Not include tasks of others unless they directly impact the user.
	•	Avoid modifying any of the summarized information.
	•	Output only the filtered information within the specified tags, with no additional text.
""",
        input_variables=["user_info", "summarised_info"],
    )
    return prompt | llm | StrOutputParser()

keep_only_relevant_info_chain = generate_keep_only_relevant_info_chain()

