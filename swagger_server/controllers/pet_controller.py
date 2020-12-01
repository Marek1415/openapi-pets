import connexion
import six

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server import util
from swagger_server.controllers import database_controller

def add_pet(body):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    if database_controller.Database_connector.add_pet(body):
        return 'Pet added'
    else:
        return 'Pet couldn\'t be added'


def delete_pet(petId):  # noqa: E501
    """Deletes a pet

    # noqa: E501

    :param petId: Pet id to delete
    :type petId: int

    :rtype: None
    """
    if database_controller.Database_connector.delete_pet(body):
        return 'Pet deleted'
    else:
        return 'Pet couldn\'t be deleted'

def get_pet_by_id(petId):  # noqa: E501
    """Find pet by ID

    Returns a single pet # noqa: E501

    :param petId: ID of pet to return
    :type petId: int

    :rtype: Pet
    """
    result = database_controller.Database_connector.find_pet(petId)
    if result:
        return "Hello"
    else:
        return "Pet couldn't be found"


def update_pet(body):  # noqa: E501
    """Update an existing pet

    # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    if database_controller.Database_connector.update_pet(body):
        return 'Pet updated'
    else:
        return 'Pet couldn\'t be updated'
