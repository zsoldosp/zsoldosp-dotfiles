from django.views import debug
import os
CUSTOM_TECHNICAL_500_TEMPLATE_PATH = os.path.join(TEMPLATE_DIRECTORY, 'technical_500.html')
#with open(CUSTOM_TECHNICAL_500_TEMPLATE_PATH, 'w+') as f:
#    f.write(debug.TECHNICAL_500_TEMPLATE)
CUSTOM_TECHNICAL_500_TEMPLATE_CONTENT = None
with open(CUSTOM_TECHNICAL_500_TEMPLATE_PATH, 'r') as f:
    CUSTOM_TECHNICAL_500_TEMPLATE_CONTENT = f.read()
#CUSTOM_TECHNICAL_500_TEMPLATE_CONTENT = 'Hello World, this is how you can overwrite template content'
debug.TECHNICAL_500_TEMPLATE = CUSTOM_TECHNICAL_500_TEMPLATE_CONTENT
