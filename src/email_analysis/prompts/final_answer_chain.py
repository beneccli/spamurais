from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import llm


        # template="""You are an assistant for question-answering tasks.
        # Use the following documents to answer the question.
        # If you don't know the answer, just say that you don't know.
        # Use three sentences maximum and keep the answer concise.
        # Answer only with required information, no additional information.
        # Question: {question}
        # Documents: {documents}
        # Answer:
        # """,

def generate_final_answer_chain():
    # Don't add any additional information other than the one asked in the question.
    # Answer the question directly, don't mention that you used documents to answer.
    prompt = PromptTemplate(
        template="""You are an advanced assistant designed to analyze emails for their importance. Use the email content and the contextual information provided to decide if the email warrants the user's attention. If the email is not important, respond with “NO." If the email is important, provide a concise summary written as a direct reminder or actionable note for the user.

Inputs:

	1.	Email Content: {email_content}

	2.	Contextual Information (from relevant documents): {rag_documents}

Task:

	1.	Analyze the email content in conjunction with the contextual information.
	2.	Respond:
	-	If the email is NOT important, reply with exactly “NO" (no further explanation).
	-	If the email IS important, provide a concise, actionable summary written directly to the user. Use a tone that emphasizes action or a reminder, like:
	-	“Don't forget that the project is expected to be delivered by August 23rd."
	-	“You should review the updated budget proposal mentioned in the email."

Guidelines:

	-	The summary must directly address the user and communicate the key takeaway or required action.
	-	Use the contextual information to enhance your judgment but avoid overly verbose explanations.
	-	Ensure the output is strictly formatted as either “NO" or a one-sentence actionable summary.

Example Outputs:

	1.	“NO"
	2.	“Don't forget to confirm your attendance for the meeting scheduled on September 15th."
	3.	“You should review the revised terms in the attached contract."

Now, analyze the inputs and respond accordingly.
        """,
        input_variables=["email_content", "rag_documents"],
    )
    return prompt | llm | StrOutputParser()

final_answer_chain = generate_final_answer_chain()
