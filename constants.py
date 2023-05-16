
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
