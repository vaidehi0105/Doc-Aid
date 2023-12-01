![s1](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/a5eb0b42-462b-4bff-9500-85789136d2f0)# Doc-Aid
Doc-Aid : A Medical Recommendation Application

DocAid, where users can track diseases, predict illnesses, and store healthcare information, which will  be significant and impactful endeavor.....

Problem Statement : Current healthcare diagnostics face challenges in accuracy and real-time adaptability. Traditional methods may not provide precise insights into health conditions. Our project tackles this by introducing an innovative medical diagnosis system. 

#Motivation
1.Accessibility and Affordibility : Many existing healthcare platforms, especially sophisticated ones, are often costly and not easily accessible to the general public.
2.Preventive Healthcare : Early disease prediction and healthcare tracking can significantly contribute to preventive healthcare
3.Empowering Patients: A platform which  will empowers patients by giving them more control over their health data and insights into their health conditions
4.Integration of AI and healthcare : The integration of AI in healthcare is still in its early stages in many regions . A platform with effecirntly uses AI for disease prediction and health tracking can be a game-changer

# Objective:
1. Compare and Analyse Different Disease Prediction Models :
    1. Naive Bayes
    2. Bayesian Model
    3. Baysian Model + ANN
    4. Naive Bayes + ANN
Out of these models fusion of Naive Bayes and ANN gave excellent results with accuracy of 95.06% and loss of 0.08 %

![hybridmodel drawio](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/a3a373bd-04e9-42ea-b0a9-069cc1dd9adb)

# Fusion Model 
Firstly we trained Naive Bayes model with our pre-processed dataset to generate initial probability estimates for each disease based on the input symptoms and their weights. It helps to capture the probabilistic relationship between symptoms and diseases.
Then we used these output probabilities from the Naive Bayes model to feed into our ANN model . The ANN model learns the complex patterns and interactions in the data that Naive Bayes might have missed.

2. Construction of Knowledge graph : I constructed weighted knowledge graph with the help of neo4j.
   
![construction_knowledge_graph drawio](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/c209a0cc-e8ca-4962-8db5-911db70234e6=250x250)

Why Knowledge graph?

![whyknowledge drawio](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/45baa296-c9da-40cc-9c89-3933c54edea7=250x250)

I created weighted knowledge graph using neo4j graph database where we have two nodes which are Disease node and Symptom node and Relationship between them  as “IS_SYMPTOM_OF” where we have severity of symptom incorporated in the relationship between each symptom and disease node

Sample of knowledge graph 

![graph (2)](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/e1f88821-9740-4110-87b5-f0d73f8f5156=250x250=250x250)


# How does User Interface works?

![user_inputs drawio](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/a3d126d6-00f5-41f8-a922-eb323ed7d459=250x250)

#Web interface 

![s2](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/03928c43-67c6-4a56-9ac4-3a6e5e68adf3=250x250)
![s3](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/e16995ec-3b52-4a44-a1b2-ea4befe33208=250x250)
![s4](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/3fa45920-fe6e-485b-8fdd-d0051418abc0=250x250)
![s6](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/14ad5499-522a-4b82-beb1-bc0ed19dc2e1=250x250)
![s7](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/d454f972-43d3-41e2-bfcc-ae4151451880=250x250)
![s8](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/75a2b9c5-940c-4036-97b5-d01e2b08649d=250x250)
![s9](https://github.com/vaidehi0105/Doc-Aid/assets/72137592/6293ceb8-907c-4ced-b647-b66eea619578=250x250)


# Code explaination :
### Web app files
Complete web app files. Have a run 

### Capstone-ner.ipynb file

1. PDF PARSING
   Discharge PDF parsing
2. HEALTHCARE GOOGLE API Output

3. Dataset consisting 1657 text rows and google healthcare api output

### -------------------------------------------------------------------------

### Capstone.ipynb
Model for entity-group segreagation and using neo4j testing

### Knowledge-graph_data.ipynb

Creating knowledge graph data in neo4j


## app.py 

streamlit app 

   
