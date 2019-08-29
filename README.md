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
 - This file also consists of `stories.md` file.

  #### data.json
   - The old versions of RASA were using `.json` file format and the newer versions use `.md` format but since to train this high level model I used `.json` format because I utilized the convinience of `npm trainer`, it uses GUI to get the context, Intent and entities from the developer and add it to the file.

   - Instead of downloading that file you can use the link below to create your data and download the `.json` file.
      <https://rasahq.github.io/rasa-nlu-trainer/> this is helpful in creating your training data for the chatbot.

   - To train the file use the following syntax in your command line:
      `python -m rasa_nlu.train -c config_spacy.json --data data/data.json -o models --fixed_model_name nlu --project current --verbose`

   - This will Train your model.
  
  #### stories.md
   - This file consists of the storyline the chatbot follows, that is it consists of the conversational path that it should follow in order to have an engaging conversation.
   - For this higher model I have shown just few examples of the conversation path and trained it using simple syntax which will be shown in `policies.yml` file description.
    
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
  
---

### policies.yml
  - This `.yml` consists of the policies that the chatbot should follow, we have used:
      1. `Keras`  - to invoke LSTM
      2. `Memoization`    - for memory
      3. `FallBack`   - to fallback
  - **Note**: Full details are commented inside this file.
  - The syntax to train the model is given below:
      `python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml`
  - As mentioned in the `stories.md` description, the above syntax is used to train our model to converse.
  - I have not used the code due to plagiarism problems, This code gives the users control over the actions that are taken by the chatbot. This refines the chatbot's ability and action taken.
  - For now this works well

--- 

### actions.py
  - This file uses the API key that is obtained from <https://indianrailapi.com>, the API key is not in the code due to seurity reasons.
  - This file gets the train number or whatever relevant information that the user gives and then uses an API call to receive about the train status and other stuff, the code contains only train status to show how the model works.
  - The output comes in `.json` file format and each necessary values will be extracted from that.

---

### models.zip
  - This file is created when you train the model by the command given `data` section above.
  - since I couldn't upload the normal file due to size restriction I uploaded the `.zip` folder.
  - This folder contains the training data and the feature extractor as json files and also the intent classifier.
  - This was a result of the training and a core file for our chatbot.

---

### Slack

  - We integrate the chatbot into slack by logging on to slack API website and then creating a bot on your workspace (You should be needing a workspace in slack)
  - Then we use `ngork`,ngrok can serve local file system directories by using its own built-in fileserver, no separate server needed!
  - Those are form their website. Thus our files will pushed into Slack using ngork and the chatbot comes to life in Slack!
 **DISCLAIMER**
   - I haven't said many things in Slack integration, because the chatbot will be moved into Google Assistant through Dialog Flow.
   - My apologies for no code in here for Slack integration, since this is just the high level model I proposed this Idea of integration.
   
---

This is the complete Description of all the files and their working as a ChatBot..
