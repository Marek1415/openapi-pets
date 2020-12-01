# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Pet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, status: str=None):  # noqa: E501
        """Pet - a model defined in Swagger

        :param id: The id of this Pet.  # noqa: E501
        :type id: int
        :param name: The name of this Pet.  # noqa: E501
        :type name: str
        :param status: The status of this Pet.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'status': 'status'
        }

        self._id = id
        self._name = name
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Pet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pet of this Pet.  # noqa: E501
        :rtype: Pet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Pet.


        :return: The id of this Pet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Pet.


        :param id: The id of this Pet.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Pet.


        :return: The name of this Pet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Pet.


        :param name: The name of this Pet.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self) -> str:
        """Gets the status of this Pet.

        pet status in the store  # noqa: E501

        :return: The status of this Pet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Pet.

        pet status in the store  # noqa: E501

        :param status: The status of this Pet.
        :type status: str
        """
        allowed_values = ["available", "pending", "sold"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
        ***REMOVED***

        self._status = status
