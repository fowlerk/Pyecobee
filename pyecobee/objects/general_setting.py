"""
This module is home to the GeneralSetting class
"""
from pyecobee.ecobee_object import EcobeeObject


class GeneralSetting(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/GeneralSetting.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_type', '_enabled', '_remind_technician']

    attribute_name_map = {'type': 'type', 'enabled': 'enabled', 'remind_technician': 'remindTechnician',
                          'remindTechnician': 'remind_technician'}

    attribute_type_map = {'type': 'six.text_type', 'enabled': 'bool', 'remind_technician': 'bool'}

    def __init__(self, type, enabled=None, remind_technician=None):
        """
        Construct a GeneralSetting instance
        """
        self._type = type
        self._enabled = enabled
        self._remind_technician = remind_technician

    @property
    def type(self):
        """
        Gets the type attribute of this GeneralSetting instance.

        :return: The value of the type attribute of this GeneralSetting instance.
        :rtype: six.text_type
        """

        return self._type

    @property
    def enabled(self):
        """
        Gets the enabled attribute of this GeneralSetting instance.

        :return: The value of the enabled attribute of this GeneralSetting instance.
        :rtype: bool
        """

        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled attribute of this GeneralSetting instance.

        :param enabled: The enabled value to set for the enabled attribute of this GeneralSetting instance.
        :type: bool
        """

        self._enabled = enabled

    @property
    def remind_technician(self):
        """
        Gets the remind_technician attribute of this GeneralSetting instance.

        :return: The value of the remind_technician attribute of this GeneralSetting instance.
        :rtype: bool
        """

        return self._remind_technician

    @remind_technician.setter
    def remind_technician(self, remind_technician):
        """
        Sets the remind_technician attribute of this GeneralSetting instance.

        :param remind_technician: The remind_technician value to set for the remind_technician attribute of this GeneralSetting instance.
        :type: bool
        """

        self._remind_technician = remind_technician
