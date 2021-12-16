from django.apps import AppConfig
from django.conf import settings
import pickle
import os


class EndpointsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EndPoints'

    # create path to models
    path = os.path.join(settings.MODELS, 'models.p')
 
    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
       data = pickle.load(pickled)

    regressor = data['regressor']
    vectorizer = data['vectorizer']
