# import streamlit as st
# from Bio_Epidemiology_NER.bio_recognizer import ner_prediction
# from neo4j import GraphDatabase

# def fetch_symptom_related_nodes(symptoms):
#     symptoms=symptoms+" "
#     # Define the Neo4j connection parameters
#     uri = "neo4j+s://71041f2d.databases.neo4j.io"  # Replace with your Neo4j server URI
#     username = "neo4j"
#     password = "d7NBKR45Nrx8wMrKsUYwHTAsKv7xDVF1UNmaKUH_i74"
    
#     # Define the Cypher query
#     query = (
#         "MATCH (s:Symptom {name: $symptoms})-[:IS_SYMPTOM_OF]->(d:Disease) "
#         "RETURN  s, d"
#     )
    
#     # Establish a connection to the database and execute the query
#     with GraphDatabase.driver(uri, auth=(username, password)) as driver:
#         with driver.session() as session:
#             result = session.run(query, symptoms=symptoms)
#             # Collect the results into a list of dictionaries
#             results = [record.data() for record in result]
    

#     return results


# def main():
#     st.title("Doc-aid- A Hybrid graph transformer for medical recommendations")

#     # Get user input
#     st.header("Enter a medical text:")
#     user_input = st.text_area("", "")

#     if st.button("Process Text"):
#         # Perform NER prediction on user input
#         ner_df = ner_prediction(corpus=user_input, compute='cpu')
#         st.write(ner_df)

#         # Extract symptom information from the NER results
#         symptoms = ner_df[ner_df["entity_group"] == "Sign_symptom"]

#         if not symptoms.empty:
#     # Get the corresponding value
#            sign_symptom_value = symptoms.iloc[0]['value']
#            st.write(sign_symptom_value.tolist())
#         if sign_symptom_value:
#             st.markdown("Extracted Symptoms:")
#             st.write(sign_symptom_value)
#             st.write("-----------------------------------------------------------------------")

#             # Query the Neo4j database for related diseases
#             results = fetch_symptom_related_nodes(sign_symptom_value)
#             unique_disease_nodes=set()
#             for result in results:
#                 disease_node=result['d']
#                 unique_disease_nodes.add(disease_node['name'])


#             if unique_disease_nodes:
#                 st.markdown("Related Diseases:")
#                 for disease_name in unique_disease_nodes:
#                     st.write(f"Disease Name: {disease_name}")
#             else:
#                 st.warning("No related diseases found.")
#         else:
#             st.warning("No symptoms extracted from the text.")

# if __name__ == "__main__":
#     main()

import streamlit as st
from Bio_Epidemiology_NER.bio_recognizer import ner_prediction
from neo4j import GraphDatabase

def fetch_symptom_related_nodes(symptom):
    symptom = symptom + " "
    # Define the Neo4j connection parameters
    uri = "neo4j+s://71041f2d.databases.neo4j.io"  # Replace with your Neo4j server URI
    username = "neo4j"
    password = "d7NBKR45Nrx8wMrKsUYwHTAsKv7xDVF1UNmaKUH_i74"
    
    # Define the Cypher query
    query = (
        "MATCH (s:Symptom {name: $symptom})-[:IS_SYMPTOM_OF]->(d:Disease) "
        "RETURN  s, d"
    )
    
    # Establish a connection to the database and execute the query
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            result = session.run(query, symptom=symptom)
            # Collect the results into a list of dictionaries
            results = [record.data() for record in result]
    
    return results

def main():
    st.title("Doc-aid- A Hybrid graph transformer for medical recommendations")

    # Get user input
    st.header("Enter a medical text:")
    user_input = st.text_area("", "")

    if st.button("Process Text"):
        # Perform NER prediction on user input
        ner_df = ner_prediction(corpus=user_input, compute='cpu')
        st.write(ner_df)

        # Extract symptom information from the NER results
        symptoms_df = ner_df[ner_df["entity_group"] == "Sign_symptom"]

        if not symptoms_df.empty:
            # Get the list of unique symptoms
            unique_symptoms = symptoms_df["value"].unique()

            # Loop through each symptom
            for symptom in unique_symptoms:
                st.write("-----------------------------------------------------------------------")

                st.markdown(f"Extracted Symptom: {symptom}")
                st.write("-----------------------------------------------------------------------")

                # Query the Neo4j database for related diseases for the current symptom
                results = fetch_symptom_related_nodes(symptom)
                unique_disease_nodes = set()
                for result in results:
                    disease_node = result['d']
                    unique_disease_nodes.add(disease_node['name'])

                if unique_disease_nodes:
                    st.markdown("Related Diseases:")
                    for disease_name in unique_disease_nodes:
                        st.write(f"Disease Name: {disease_name}")
                else:
                    st.warning("No related diseases found for this symptom.")
        else:
            st.warning("No symptoms extracted from the text.")

if __name__ == "__main__":
    main()
