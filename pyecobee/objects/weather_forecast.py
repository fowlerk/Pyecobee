"""
This module is home to the WeatherForecast class
"""
from pyecobee.ecobee_object import EcobeeObject


class WeatherForecast(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/WeatherForecast.shtml

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
        '_weather_symbol',
        '_date_time',
        '_condition',
        '_temperature',
        '_pressure',
        '_relative_humidity',
        '_dewpoint',
        '_visibility',
        '_wind_speed',
        '_wind_gust',
        '_wind_direction',
        '_wind_bearing',
        '_pop',
        '_temp_high',
        '_temp_low',
        '_sky',
    ]

    attribute_name_map = {
        'weather_symbol': 'weatherSymbol',
        'weatherSymbol': 'weather_symbol',
        'date_time': 'dateTime',
        'dateTime': 'date_time',
        'condition': 'condition',
        'temperature': 'temperature',
        'pressure': 'pressure',
        'relative_humidity': 'relativeHumidity',
        'relativeHumidity': 'relative_humidity',
        'dewpoint': 'dewpoint',
        'visibility': 'visibility',
        'wind_speed': 'windSpeed',
        'windSpeed': 'wind_speed',
        'wind_gust': 'windGust',
        'windGust': 'wind_gust',
        'wind_direction': 'windDirection',
        'windDirection': 'wind_direction',
        'wind_bearing': 'windBearing',
        'windBearing': 'wind_bearing',
        'pop': 'pop',
        'temp_high': 'tempHigh',
        'tempHigh': 'temp_high',
        'temp_low': 'tempLow',
        'tempLow': 'temp_low',
        'sky': 'sky',
    }

    attribute_type_map = {
        'weather_symbol': 'int',
        'date_time': 'six.text_type',
        'condition': 'six.text_type',
        'temperature': 'int',
        'pressure': 'int',
        'relative_humidity': 'int',
        'dewpoint': 'int',
        'visibility': 'int',
        'wind_speed': 'int',
        'wind_gust': 'int',
        'wind_direction': 'six.text_type',
        'wind_bearing': 'int',
        'pop': 'int',
        'temp_high': 'int',
        'temp_low': 'int',
        'sky': 'int',
    }

    def __init__(
        self,
        weather_symbol=None,
        date_time=None,
        condition=None,
        temperature=None,
        pressure=None,
        relative_humidity=None,
        dewpoint=None,
        visibility=None,
        wind_speed=None,
        wind_gust=None,
        wind_direction=None,
        wind_bearing=None,
        pop=None,
        temp_high=None,
        temp_low=None,
        sky=None,
    ):
        """
        Construct a WeatherForecast instance
        """
        self._weather_symbol = weather_symbol
        self._date_time = date_time
        self._condition = condition
        self._temperature = temperature
        self._pressure = pressure
        self._relative_humidity = relative_humidity
        self._dewpoint = dewpoint
        self._visibility = visibility
        self._wind_speed = wind_speed
        self._wind_gust = wind_gust
        self._wind_direction = wind_direction
        self._wind_bearing = wind_bearing
        self._pop = pop
        self._temp_high = temp_high
        self._temp_low = temp_low
        self._sky = sky

    @property
    def weather_symbol(self):
        """
        Gets the weather_symbol attribute of this WeatherForecast
        instance.

        :return: The value of the weather_symbol attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._weather_symbol

    @property
    def date_time(self):
        """
        Gets the date_time attribute of this WeatherForecast instance.

        :return: The value of the date_time attribute of this
        WeatherForecast instance.
        :rtype: six.text_type
        """

        return self._date_time

    @property
    def condition(self):
        """
        Gets the condition attribute of this WeatherForecast instance.

        :return: The value of the condition attribute of this
        WeatherForecast instance.
        :rtype: six.text_type
        """

        return self._condition

    @property
    def temperature(self):
        """
        Gets the temperature attribute of this WeatherForecast instance.

        :return: The value of the temperature attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._temperature

    @property
    def pressure(self):
        """
        Gets the pressure attribute of this WeatherForecast instance.

        :return: The value of the pressure attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._pressure

    @property
    def relative_humidity(self):
        """
        Gets the relative_humidity attribute of this WeatherForecast
        instance.

        :return: The value of the relative_humidity attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._relative_humidity

    @property
    def dewpoint(self):
        """
        Gets the dewpoint attribute of this WeatherForecast instance.

        :return: The value of the dewpoint attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._dewpoint

    @property
    def visibility(self):
        """
        Gets the visibility attribute of this WeatherForecast instance.

        :return: The value of the visibility attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._visibility

    @property
    def wind_speed(self):
        """
        Gets the wind_speed attribute of this WeatherForecast instance.

        :return: The value of the wind_speed attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._wind_speed

    @property
    def wind_gust(self):
        """
        Gets the wind_gust attribute of this WeatherForecast instance.

        :return: The value of the wind_gust attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._wind_gust

    @property
    def wind_direction(self):
        """
        Gets the wind_direction attribute of this WeatherForecast
        instance.

        :return: The value of the wind_direction attribute of this
        WeatherForecast instance.
        :rtype: six.text_type
        """

        return self._wind_direction

    @property
    def wind_bearing(self):
        """
        Gets the wind_bearing attribute of this WeatherForecast
        instance.

        :return: The value of the wind_bearing attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._wind_bearing

    @property
    def pop(self):
        """
        Gets the pop attribute of this WeatherForecast instance.

        :return: The value of the pop attribute of this WeatherForecast
        instance.
        :rtype: int
        """

        return self._pop

    @property
    def temp_high(self):
        """
        Gets the temp_high attribute of this WeatherForecast instance.

        :return: The value of the temp_high attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._temp_high

    @property
    def temp_low(self):
        """
        Gets the temp_low attribute of this WeatherForecast instance.

        :return: The value of the temp_low attribute of this
        WeatherForecast instance.
        :rtype: int
        """

        return self._temp_low

    @property
    def sky(self):
        """
        Gets the sky attribute of this WeatherForecast instance.

        :return: The value of the sky attribute of this WeatherForecast
        instance.
        :rtype: int
        """

        return self._sky
