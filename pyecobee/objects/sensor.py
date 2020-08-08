"""
This module is home to the Sensor class
"""
from pyecobee.ecobee_object import EcobeeObject


class Sensor(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Sensor.shtml

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

    __slots__ = [
        '_name',
        '_manufacturer',
        '_model',
        '_zone',
        '_sensor_id',
        '_type',
        '_usage',
        '_number_of_bits',
        '_bconstant',
        '_thermistor_size',
        '_temp_correction',
        '_gain',
        '_max_voltage',
        '_multiplier',
        '_states',
    ]

    attribute_name_map = {
        'name': 'name',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'zone': 'zone',
        'sensor_id': 'sensorId',
        'sensorId': 'sensor_id',
        'type': 'type',
        'usage': 'usage',
        'number_of_bits': 'numberOfBits',
        'numberOfBits': 'number_of_bits',
        'bconstant': 'bconstant',
        'thermistor_size': 'thermistorSize',
        'thermistorSize': 'thermistor_size',
        'temp_correction': 'tempCorrection',
        'tempCorrection': 'temp_correction',
        'gain': 'gain',
        'max_voltage': 'maxVoltage',
        'maxVoltage': 'max_voltage',
        'multiplier': 'multiplier',
        'states': 'states',
    }

    attribute_type_map = {
        'name': 'six.text_type',
        'manufacturer': 'six.text_type',
        'model': 'six.text_type',
        'zone': 'int',
        'sensor_id': 'int',
        'type': 'six.text_type',
        'usage': 'six.text_type',
        'number_of_bits': 'int',
        'bconstant': 'int',
        'thermistor_size': 'int',
        'temp_correction': 'int',
        'gain': 'int',
        'max_voltage': 'int',
        'multiplier': 'int',
        'states': 'List[State]',
    }

    def __init__(
        self,
        name=None,
        manufacturer=None,
        model=None,
        zone=None,
        sensor_id=None,
        type_=None,
        usage=None,
        number_of_bits=None,
        bconstant=None,
        thermistor_size=None,
        temp_correction=None,
        gain=None,
        max_voltage=None,
        multiplier=None,
        states=None,
    ):
        """
        Construct a Sensor instance
        """
        self._name = name
        self._manufacturer = manufacturer
        self._model = model
        self._zone = zone
        self._sensor_id = sensor_id
        self._type = type_
        self._usage = usage
        self._number_of_bits = number_of_bits
        self._bconstant = bconstant
        self._thermistor_size = thermistor_size
        self._temp_correction = temp_correction
        self._gain = gain
        self._max_voltage = max_voltage
        self._multiplier = multiplier
        self._states = states

    @property
    def name(self):
        """
        Gets the name attribute of this Sensor instance.

        :return: The value of the name attribute of this Sensor
        instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def manufacturer(self):
        """
        Gets the manufacturer attribute of this Sensor instance.

        :return: The value of the manufacturer attribute of this Sensor
        instance.
        :rtype: six.text_type
        """

        return self._manufacturer

    @property
    def model(self):
        """
        Gets the model attribute of this Sensor instance.

        :return: The value of the model attribute of this Sensor
        instance.
        :rtype: six.text_type
        """

        return self._model

    @property
    def zone(self):
        """
        Gets the zone attribute of this Sensor instance.

        :return: The value of the zone attribute of this Sensor
        instance.
        :rtype: int
        """

        return self._zone

    @property
    def sensor_id(self):
        """
        Gets the sensor_id attribute of this Sensor instance.

        :return: The value of the sensor_id attribute of this Sensor
        instance.
        :rtype: int
        """

        return self._sensor_id

    @property
    def type(self):
        """
        Gets the type attribute of this Sensor instance.

        :return: The value of the type attribute of this Sensor
        instance.
        :rtype: six.text_type
        """

        return self._type

    @property
    def usage(self):
        """
        Gets the usage attribute of this Sensor instance.

        :return: The value of the usage attribute of this Sensor
        instance.
        :rtype: six.text_type
        """

        return self._usage

    @property
    def number_of_bits(self):
        """
        Gets the number_of_bits attribute of this Sensor instance.

        :return: The value of the number_of_bits attribute of this
        Sensor instance.
        :rtype: int
        """

        return self._number_of_bits

    @property
    def bconstant(self):
        """
        Gets the bconstant attribute of this Sensor instance.

        :return: The value of the bconstant attribute of this Sensor
        instance.
        :rtype: int
        """

        return self._bconstant

    @property
    def thermistor_size(self):
        """
        Gets the thermistor_size attribute of this Sensor instance.

        :return: The value of the thermistor_size attribute of this
        Sensor instance.
        :rtype: int
        """

        return self._thermistor_size

    @property
    def temp_correction(self):
        """
        Gets the temp_correction attribute of this Sensor instance.

        :return: The value of the temp_correction attribute of this
        Sensor instance.
        :rtype: int
        """

        return self._temp_correction

    @property
    def gain(self):
        """
        Gets the gain attribute of this Sensor instance.

        :return: The value of the gain attribute of this Sensor
        instance.
        :rtype: int
        """

        return self._gain

    @property
    def max_voltage(self):
        """
        Gets the max_voltage attribute of this Sensor instance.

        :return: The value of the max_voltage attribute of this Sensor
        instance.
        :rtype: int
        """

        return self._max_voltage

    @property
    def multiplier(self):
        """
        Gets the multiplier attribute of this Sensor instance.

        :return: The value of the multiplier attribute of this Sensor
        instance.
        :rtype: int
        """

        return self._multiplier

    @property
    def states(self):
        """
        Gets the states attribute of this Sensor instance.

        :return: The value of the states attribute of this Sensor
        instance.
        :rtype: List[State]
        """

        return self._states
