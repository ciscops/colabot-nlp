import os
from jinja2 import Template

ENVIRONMENT = os.environ["ENVIRONMENT"]
envars = os.environ
env_dict = {}
for k, v in envars.items():
    env_dict[k] = v

with open(
    f"manifest/colabot-nlp-secrets-{ENVIRONMENT}.yaml.j2", "r", encoding="utf8"
) as f:
    template = Template(f.read())

with open(f"manifest/output-secrets-{ENVIRONMENT}.yaml", "w", encoding="utf8") as f:
    f.write(template.render(env_dict))

with open(
    f"manifest/colabot-nlp-manifest-{ENVIRONMENT}.yaml.j2", "r", encoding="utf8"
) as f:
    template = Template(f.read())

with open(f"manifest/output-manifest-{ENVIRONMENT}.yaml", "w", encoding="utf8") as f:
    f.write(template.render(env_dict))
