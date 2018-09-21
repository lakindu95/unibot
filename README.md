# unibot
A simple chatbot using RASA NLU &amp; CORE

### Training the NLU model

``` python nlu_model.py ```

### Training the Rasa Core model
  
1. Start the custom action server by running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Open a new terminal and train the Rasa Core model by running:  

``` python dialogue_management_model.py```  
 
3. Talk to the chatbot once it's loaded.  

### Starting the online training session:

The process of running the online session is very similar to training the Rasa Core model:
1. Make sure the custom actions server is running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Start the online training session by running:  

``` python train_online.py ```  