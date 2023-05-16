# entailment-awareness-text-summarization
This is the github repository of our ECE-GY 7123 Deep Learning Spring 2023 Final Project

### Team Members:
Brijendra Kumar Asthana (bka2022)

Karan Joglekar (kaj9196)

Shashakt Jha (ssj2580)



### Prerequisite: 
Please install the packages in the ``requirements.txt`` file

## Running the code
To run the code, configure the parameters in the ``constants.py`` file
The description of each parameter is appropriately mentioned in the file as follows:
```
# CONSTANTS
DEV_TEST = False #For Development
SUBSET = True #Use Subset of Dataset set as 25000
USE_TRAINED = True # Use a previously trained checkpoint model
trained_model_name = "results/checkpoint-15500/"
USE_RL = True #Use entailment
REGULARIZE = True #Use Regularization
reward_type = "entailment_max" # Reward type For ENT: "entailment_mean", For ENT+: "entailment_max"
EVAL_ONLY = True #Evaluate the model only
encoder_max_length = 512 # Encoder Max Length
decoder_max_length = 32 # Decoder Max length
NUM_EPOCHS = 5 # Num Epochs to Train
WARMUP_STEPS = 500 # Warmup-steps
TEST_SAMPLES = 15 # Number of Output Samples to be evaluated
```

To run the training(or fine-tuning) and evaluation process set ``EVAL_ONLY`` to ``False`` and use the following command
```
python3 main.py
```
You can configure other params in ``constants.py`` as per your experiment.
The model will be saved in the ``results`` folder, output log events in ``logs``

To evaluate a trained model on any number of samples set ``EVAL_ONLY`` to ``True`` and mention the ``trained_model_name`` path in the ``constants.py`` file.
Run the ``main.py`` to evaluate and produce output summaries.


