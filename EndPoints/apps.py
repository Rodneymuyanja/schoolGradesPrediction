from django.apps import AppConfig
from django.conf import settings
import pickle
import os


class EndpointsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EndPoints'

    # create path to models
    path = os.path.join(settings.MODELS, '77model.pickle')
 
    #loading the model 
    with open(path, 'rb') as pickled:
       model = pickle.load(pickled)


