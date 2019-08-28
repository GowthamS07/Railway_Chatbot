# Railway_Chatbot
TCS HumAIn Competition

---

## Contents
The file contains the following files and folder:
  - config_spacy.json
  - rail_domain.yml
  - data (folder)
  
---

### data
 - This folder consists of the training data `data.json` , It is the collection of possible dialogues so as to train the RASA NLU with the intent and the entities in the context/sentence that a user provides.
 
 - The old versions of RASA were using `.json` file format and the newer versions use `.md` format but since to train this high level model I used `.json` format because I utilized the convinience of `npm trainer`, it uses GUI to get the context, Intent and entities from the developer and add it to the file.
 
 - Instead of downloading that file you can use the link below to create your data and download the `.json` file.
    <https://rasahq.github.io/rasa-nlu-trainer/> this is helpful in creating your training data for the chatbot.
    
 - To train the file use the following syntax in your command line:
    `python -m rasa_nlu.train -c config_spacy.json --data data/data.json -o models --fixed_model_name nlu --project current --verbose`
   
 - This will Train your model.
 
 ---
 
 ### config_spacy.json
  - This was present in the older version will be upgraded
  - This is the main file that contains the `pipeline`, here the pipeline used is `spacy_sklearn`, spacy_sklearn is used because this contains pretrained word model that is useful since there are less than 1000 training data for word vectors.
  - This has to be downloaded first using the following syntax:
      `python -m spacy download en` , this downloads the English model and thus helps the chatbot to make conversation easily.
  - Since this is a high level model I am using spacy, I will try to implement `tensorflow_embedding` and experiment with results and then give out the final model.

---

### rail_domain.yml
  - This `.yml` file consists of the templates of some words that the chatbot could use to speak to the user.
  - It also contains all the Intents and Entities that are present for the chatbot to detect and perform respective actions.
