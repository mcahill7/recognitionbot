# recognitionbot
## Install Dependencies:

1. pip install django

2. pip install djangorestframework

3. pip install slackclient

4. pip install slackeventsapi


## Run the App:
python manage.py runserver 0.0.0.0:8000

Then start ngrok:
ngrok http 8000

Creating Pipeline
To create the pipeline run the following aws cloudformation create-stack --stack-name recognition-pipeline --template-body file://pipeline/pipeline.yaml --capabilities CAPABILITY_NAMED_IAM

To update the pipeline run the following aws cloudformation update-stack --stack-name recognition-pipeline --template-body file://pipeline/pipeline.yaml --capabilities CAPABILITY_NAMED_IAM