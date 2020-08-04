# COLABot NLP Service

This repo contains a Dockerfile to create and run a container that:
- Builds a NLP model based on the contents of file colabot_commands.yaml
- Runs a webserver that receives text from the "text" field in the body of a POST request
    and returns best match for COLABot from a list of available commands along with the confidence score.
    

To run locally:
- python build_model.py
- python app.py
