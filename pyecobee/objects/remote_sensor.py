"""
This module is home to the RemoteSensor class
"""
from pyecobee.ecobee_object import EcobeeObject


class RemoteSensor(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/RemoteSensor.shtml

    Attribute names have been generated by converting ecobee property
    names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value
    of READONLY is "no".

    An __init__ argument without a default value has been generated if
    the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated
    if the value of REQUIRED is "no".
    """

    __slots__ = ['_id', '_name', '_type', '_code', '_in_use', '_capability']

    attribute_name_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'code': 'code',
        'in_use': 'inUse',
        'inUse': 'in_use',
        'capability': 'capability',
    }

    attribute_type_map = {
        'id': 'six.text_type',
        'name': 'six.text_type',
        'type': 'six.text_type',
        'code': 'six.text_type',
        'in_use': 'bool',
        'capability': 'List[RemoteSensorCapability]',
    }

    def __init__(
        self, id_=None, name=None, type_=None, code=None, in_use=None, capability=None
    ):
        """
        Construct a RemoteSensor instance
        """
        self._id = id_
        self._name = name
        self._type = type_
        self._code = code
        self._in_use = in_use
        self._capability = capability

    @property
    def id(self):
        """
        Gets the id attribute of this RemoteSensor instance.

        :return: The value of the id attribute of this RemoteSensor
        instance.
        :rtype: six.text_type
        """

        return self._id

    @property
    def name(self):
        """
        Gets the name attribute of this RemoteSensor instance.

        :return: The value of the name attribute of this RemoteSensor
        instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def type(self):
        """
        Gets the type attribute of this RemoteSensor instance.

        :return: The value of the type attribute of this RemoteSensor
        instance.
        :rtype: six.text_type
        """

        return self._type

    @property
    def code(self):
        """
        Gets the code attribute of this RemoteSensor instance.

        :return: The value of the code attribute of this RemoteSensor
        instance.
        :rtype: six.text_type
        """

        return self._code

    @property
    def in_use(self):
        """
        Gets the in_use attribute of this RemoteSensor instance.

        :return: The value of the in_use attribute of this RemoteSensor
        instance.
        :rtype: bool
        """

        return self._in_use

    @property
    def capability(self):
        """
        Gets the capability attribute of this RemoteSensor instance.

        :return: The value of the capability attribute of this
        RemoteSensor instance.
        :rtype: List[RemoteSensorCapability]
        """

        return self._capability
