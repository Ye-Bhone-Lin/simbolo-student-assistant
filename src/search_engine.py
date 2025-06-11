from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import os
import json
from groq import Groq
import streamlit as st 

es = st.secrets['ELASTIC_SEARCH_API_KEY']
gr = st.secrets['GROQ_API_KEY']

#load_dotenv()

class SearchEngine:
    @classmethod
    def retrieve_information(cls, user_input: str):
        client = Elasticsearch(
            "https://608291f321b44714a3d68daf7c09ca10.us-central1.gcp.cloud.es.io:443",
            api_key=os.getenv("ELASTIC_SEARCH_API_KEY")
        )

        index_name = "search-simbolo"

        try:
            with open("Simbolo_Information.json", "rt") as file:
                simbolo_file = json.load(file)
                actions = [
                    {
                        "_index": index_name,
                        "_source": item
                    }
                    for item in simbolo_file
                ]
                helpers.bulk(client, actions)
        except Exception as e:
            print(f"Error indexing data: {e}")

        # Search query
        query = {
            "query": {
                "match": {
                    "Questions": user_input
                },
            }
        }

        try:
            response = client.search(index=index_name, body=query, size=35)
            results = response["hits"]["hits"]

            if not results:
                print("No results found.")

            template_for_prompt = []
            for result in results:
                #print(result["_source"])
                template_for_prompt.append(result["_source"])

            prompt_template = [{
                "question": [item["Questions"] for item in template_for_prompt],
                "answer": [item["Answers"] for item in template_for_prompt]
            }]

            prompt_template_for_llm = """
            You are a helpful assistant trained to answer questions about Simbolo, a training school.

            You have access to the following knowledge base of Questions and Answers:

            {question}
            {answer}

            When a user asks a question, provide the most accurate answer based on the knowledge base above.

            If the question cannot be answered from the knowledge base, reply: "I'm sorry, I do not have enough information to answer that question."
            """

            questions_text = "\n\n---\n\n".join(prompt_template[0]["question"])
            answers_text = "\n\n---\n\n".join(prompt_template[0]["answer"])

            final_prompt = prompt_template_for_llm.format(
                question=questions_text,
                answer=answers_text
            )

            return final_prompt
        except Exception as e:
            print(f"Error retrieving data from Elasticsearch: {e}")
            return "I'm sorry, I do not have enough information to answer that question."

class GenerateOutput:
    @classmethod
    def model_generate(cls, user_input: str):
        model = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

        try:
            chat_completion = model.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": SearchEngine.retrieve_information(user_input)
                    },
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )

            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error generating output: {e}")
            return "I'm sorry, I cannot generate an answer at this time."
