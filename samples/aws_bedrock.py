import os
from redlite import run, load_dataset
from redlite.model.aws_bedrock_model import AwsBedrockModel
from redlite.metric import MatchMetric


model = AwsBedrockModel(
    model_id="amazon.titan-text-agile-v1",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)
dataset = load_dataset("hf:innodatalabs/rt-gsm8k-gaia")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)
