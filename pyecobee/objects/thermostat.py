"""
This module is home to the Thermostat class
"""
from pyecobee.ecobee_object import EcobeeObject


class Thermostat(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Thermostat.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_identifier', '_name', '_thermostat_rev', '_is_registered', '_model_number', '_brand', '_features',
                 '_last_modified', '_thermostat_time', '_utc_time', '_audio', '_alerts', '_reminders', '_settings',
                 '_runtime', '_extended_runtime', '_electricity', '_devices', '_location', '_energy', '_technician',
                 '_utility', '_management', '_weather', '_events', '_program', '_house_details', '_oem_cfg',
                 '_equipment_status', '_notification_settings', '_privacy', '_version', '_security_settings',
                 '_filter_subscription', '_remote_sensors']

    attribute_name_map = {'identifier': 'identifier', 'name': 'name', 'thermostat_rev': 'thermostatRev',
                          'thermostatRev': 'thermostat_rev', 'is_registered': 'isRegistered',
                          'isRegistered': 'is_registered', 'model_number': 'modelNumber', 'modelNumber': 'model_number',
                          'brand': 'brand', 'features': 'features', 'last_modified': 'lastModified',
                          'lastModified': 'last_modified', 'thermostat_time': 'thermostatTime',
                          'thermostatTime': 'thermostat_time', 'utc_time': 'utcTime', 'utcTime': 'utc_time',
                          'audio': 'audio', 'alerts': 'alerts', 'reminders': 'reminders', 'settings': 'settings',
                          'runtime': 'runtime', 'extended_runtime': 'extendedRuntime',
                          'extendedRuntime': 'extended_runtime', 'electricity': 'electricity', 'devices': 'devices',
                          'location': 'location', 'energy': 'energy', 'technician': 'technician', 'utility': 'utility',
                          'management': 'management', 'weather': 'weather', 'events': 'events', 'program': 'program',
                          'house_details': 'houseDetails', 'houseDetails': 'house_details', 'oem_cfg': 'oemCfg',
                          'oemCfg': 'oem_cfg', 'equipment_status': 'equipmentStatus',
                          'equipmentStatus': 'equipment_status', 'notification_settings': 'notificationSettings',
                          'notificationSettings': 'notification_settings', 'privacy': 'privacy', 'version': 'version',
                          'security_settings': 'securitySettings', 'securitySettings': 'security_settings',
                          'filter_subscription': 'filterSubscription', 'filterSubscription': 'filter_subscription',
                          'remote_sensors': 'remoteSensors', 'remoteSensors': 'remote_sensors'}

    attribute_type_map = {'identifier': 'six.text_type', 'name': 'six.text_type', 'thermostat_rev': 'six.text_type',
                          'is_registered': 'bool', 'model_number': 'six.text_type', 'brand': 'six.text_type',
                          'features': 'six.text_type', 'last_modified': 'six.text_type',
                          'thermostat_time': 'six.text_type', 'utc_time': 'six.text_type', 'audio': 'Audio',
                          'alerts': 'List[Alert]', 'reminders': 'List[ThermostatReminder2]', 'settings': 'Settings',
                          'runtime': 'Runtime', 'extended_runtime': 'ExtendedRuntime', 'electricity': 'Electricity',
                          'devices': 'List[Device]', 'location': 'Location', 'energy': 'Energy',
                          'technician': 'Technician', 'utility': 'Utility', 'management': 'Management',
                          'weather': 'Weather', 'events': 'List[Event]', 'program': 'Program',
                          'house_details': 'HouseDetails', 'oem_cfg': 'ThermostatOemCfg',
                          'equipment_status': 'six.text_type', 'notification_settings': 'NotificationSettings',
                          'privacy': 'ThermostatPrivacy', 'version': 'Version', 'security_settings': 'SecuritySettings',
                          'filter_subscription': 'ApiFilterSubscription', 'remote_sensors': 'List[RemoteSensor]'}

    def __init__(self, identifier, name=None, thermostat_rev=None, is_registered=None, model_number=None, brand=None,
                 features=None, last_modified=None, thermostat_time=None, utc_time=None, audio=None, alerts=None,
                 reminders=None, settings=None, runtime=None, extended_runtime=None, electricity=None, devices=None,
                 location=None, energy=None, technician=None, utility=None, management=None, weather=None, events=None,
                 program=None, house_details=None, oem_cfg=None, equipment_status=None, notification_settings=None,
                 privacy=None, version=None, security_settings=None, filter_subscription=None, remote_sensors=None):
        """
        Construct a Thermostat instance
        """
        self._identifier = identifier
        self._name = name
        self._thermostat_rev = thermostat_rev
        self._is_registered = is_registered
        self._model_number = model_number
        self._brand = brand
        self._features = features
        self._last_modified = last_modified
        self._thermostat_time = thermostat_time
        self._utc_time = utc_time
        self._audio = audio
        self._alerts = alerts
        self._reminders = reminders
        self._settings = settings
        self._runtime = runtime
        self._extended_runtime = extended_runtime
        self._electricity = electricity
        self._devices = devices
        self._location = location
        self._energy = energy
        self._technician = technician
        self._utility = utility
        self._management = management
        self._weather = weather
        self._events = events
        self._program = program
        self._house_details = house_details
        self._oem_cfg = oem_cfg
        self._equipment_status = equipment_status
        self._notification_settings = notification_settings
        self._privacy = privacy
        self._version = version
        self._security_settings = security_settings
        self._filter_subscription = filter_subscription
        self._remote_sensors = remote_sensors

    @property
    def identifier(self):
        """
        Gets the identifier attribute of this Thermostat instance.

        :return: The value of the identifier attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._identifier

    @property
    def name(self):
        """
        Gets the name attribute of this Thermostat instance.

        :return: The value of the name attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name attribute of this Thermostat instance.

        :param name: The name value to set for the name attribute of this Thermostat instance.
        :type: six.text_type
        """

        self._name = name

    @property
    def thermostat_rev(self):
        """
        Gets the thermostat_rev attribute of this Thermostat instance.

        :return: The value of the thermostat_rev attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._thermostat_rev

    @property
    def is_registered(self):
        """
        Gets the is_registered attribute of this Thermostat instance.

        :return: The value of the is_registered attribute of this Thermostat instance.
        :rtype: bool
        """

        return self._is_registered

    @property
    def model_number(self):
        """
        Gets the model_number attribute of this Thermostat instance.

        :return: The value of the model_number attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._model_number

    @property
    def brand(self):
        """
        Gets the brand attribute of this Thermostat instance.

        :return: The value of the brand attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._brand

    @property
    def features(self):
        """
        Gets the features attribute of this Thermostat instance.

        :return: The value of the features attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._features

    @property
    def last_modified(self):
        """
        Gets the last_modified attribute of this Thermostat instance.

        :return: The value of the last_modified attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._last_modified

    @property
    def thermostat_time(self):
        """
        Gets the thermostat_time attribute of this Thermostat instance.

        :return: The value of the thermostat_time attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._thermostat_time

    @property
    def utc_time(self):
        """
        Gets the utc_time attribute of this Thermostat instance.

        :return: The value of the utc_time attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._utc_time

    @property
    def audio(self):
        """
        Gets the audio attribute of this Thermostat instance.

        :return: The value of the audio attribute of this Thermostat instance.
        :rtype: Audio
        """

        return self._audio

    @audio.setter
    def audio(self, audio):
        """
        Sets the audio attribute of this Thermostat instance.

        :param audio: The audio value to set for the audio attribute of this Thermostat instance.
        :type: Audio
        """

        self._audio = audio

    @property
    def alerts(self):
        """
        Gets the alerts attribute of this Thermostat instance.

        :return: The value of the alerts attribute of this Thermostat instance.
        :rtype: List[Alert]
        """

        return self._alerts

    @property
    def reminders(self):
        """
        Gets the reminders attribute of this Thermostat instance.

        :return: The value of the reminders attribute of this Thermostat instance.
        :rtype: List[ThermostatReminder2]
        """

        return self._reminders

    @property
    def settings(self):
        """
        Gets the settings attribute of this Thermostat instance.

        :return: The value of the settings attribute of this Thermostat instance.
        :rtype: Settings
        """

        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings attribute of this Thermostat instance.

        :param settings: The settings value to set for the settings attribute of this Thermostat instance.
        :type: Settings
        """

        self._settings = settings

    @property
    def runtime(self):
        """
        Gets the runtime attribute of this Thermostat instance.

        :return: The value of the runtime attribute of this Thermostat instance.
        :rtype: Runtime
        """

        return self._runtime

    @property
    def extended_runtime(self):
        """
        Gets the extended_runtime attribute of this Thermostat instance.

        :return: The value of the extended_runtime attribute of this Thermostat instance.
        :rtype: ExtendedRuntime
        """

        return self._extended_runtime

    @property
    def electricity(self):
        """
        Gets the electricity attribute of this Thermostat instance.

        :return: The value of the electricity attribute of this Thermostat instance.
        :rtype: Electricity
        """

        return self._electricity

    @property
    def devices(self):
        """
        Gets the devices attribute of this Thermostat instance.

        :return: The value of the devices attribute of this Thermostat instance.
        :rtype: List[Device]
        """

        return self._devices

    @property
    def location(self):
        """
        Gets the location attribute of this Thermostat instance.

        :return: The value of the location attribute of this Thermostat instance.
        :rtype: Location
        """

        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location attribute of this Thermostat instance.

        :param location: The location value to set for the location attribute of this Thermostat instance.
        :type: Location
        """

        self._location = location

    @property
    def energy(self):
        """
        Gets the energy attribute of this Thermostat instance.

        :return: The value of the energy attribute of this Thermostat instance.
        :rtype: Energy
        """

        return self._energy

    @energy.setter
    def energy(self, energy):
        """
        Sets the energy attribute of this Thermostat instance.

        :param energy: The energy value to set for the energy attribute of this Thermostat instance.
        :type: Energy
        """

        self._energy = energy

    @property
    def technician(self):
        """
        Gets the technician attribute of this Thermostat instance.

        :return: The value of the technician attribute of this Thermostat instance.
        :rtype: Technician
        """

        return self._technician

    @property
    def utility(self):
        """
        Gets the utility attribute of this Thermostat instance.

        :return: The value of the utility attribute of this Thermostat instance.
        :rtype: Utility
        """

        return self._utility

    @property
    def management(self):
        """
        Gets the management attribute of this Thermostat instance.

        :return: The value of the management attribute of this Thermostat instance.
        :rtype: Management
        """

        return self._management

    @property
    def weather(self):
        """
        Gets the weather attribute of this Thermostat instance.

        :return: The value of the weather attribute of this Thermostat instance.
        :rtype: Weather
        """

        return self._weather

    @property
    def events(self):
        """
        Gets the events attribute of this Thermostat instance.

        :return: The value of the events attribute of this Thermostat instance.
        :rtype: List[Event]
        """

        return self._events

    @property
    def program(self):
        """
        Gets the program attribute of this Thermostat instance.

        :return: The value of the program attribute of this Thermostat instance.
        :rtype: Program
        """

        return self._program

    @program.setter
    def program(self, program):
        """
        Sets the program attribute of this Thermostat instance.

        :param program: The program value to set for the program attribute of this Thermostat instance.
        :type: Program
        """

        self._program = program

    @property
    def house_details(self):
        """
        Gets the house_details attribute of this Thermostat instance.

        :return: The value of the house_details attribute of this Thermostat instance.
        :rtype: HouseDetails
        """

        return self._house_details

    @house_details.setter
    def house_details(self, house_details):
        """
        Sets the house_details attribute of this Thermostat instance.

        :param house_details: The house_details value to set for the house_details attribute of this Thermostat instance.
        :type: HouseDetails
        """

        self._house_details = house_details

    @property
    def oem_cfg(self):
        """
        Gets the oem_cfg attribute of this Thermostat instance.

        :return: The value of the oem_cfg attribute of this Thermostat instance.
        :rtype: ThermostatOemCfg
        """

        return self._oem_cfg

    @oem_cfg.setter
    def oem_cfg(self, oem_cfg):
        """
        Sets the oem_cfg attribute of this Thermostat instance.

        :param oem_cfg: The oem_cfg value to set for the oem_cfg attribute of this Thermostat instance.
        :type: ThermostatOemCfg
        """

        self._oem_cfg = oem_cfg

    @property
    def equipment_status(self):
        """
        Gets the equipment_status attribute of this Thermostat instance.

        :return: The value of the equipment_status attribute of this Thermostat instance.
        :rtype: six.text_type
        """

        return self._equipment_status

    @property
    def notification_settings(self):
        """
        Gets the notification_settings attribute of this Thermostat instance.

        :return: The value of the notification_settings attribute of this Thermostat instance.
        :rtype: NotificationSettings
        """

        return self._notification_settings

    @notification_settings.setter
    def notification_settings(self, notification_settings):
        """
        Sets the notification_settings attribute of this Thermostat instance.

        :param notification_settings: The notification_settings value to set for the notification_settings attribute of this Thermostat instance.
        :type: NotificationSettings
        """

        self._notification_settings = notification_settings

    @property
    def privacy(self):
        """
        Gets the privacy attribute of this Thermostat instance.

        :return: The value of the privacy attribute of this Thermostat instance.
        :rtype: ThermostatPrivacy
        """

        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """
        Sets the privacy attribute of this Thermostat instance.

        :param privacy: The privacy value to set for the privacy attribute of this Thermostat instance.
        :type: ThermostatPrivacy
        """

        self._privacy = privacy

    @property
    def version(self):
        """
        Gets the version attribute of this Thermostat instance.

        :return: The value of the version attribute of this Thermostat instance.
        :rtype: Version
        """

        return self._version

    @property
    def security_settings(self):
        """
        Gets the security_settings attribute of this Thermostat instance.

        :return: The value of the security_settings attribute of this Thermostat instance.
        :rtype: SecuritySettings
        """

        return self._security_settings

    @security_settings.setter
    def security_settings(self, security_settings):
        """
        Sets the security_settings attribute of this Thermostat instance.

        :param security_settings: The security_settings value to set for the security_settings attribute of this Thermostat instance.
        :type: SecuritySettings
        """

        self._security_settings = security_settings

    @property
    def filter_subscription(self):
        """
        Gets the filter_subscription attribute of this Thermostat instance.

        :return: The value of the filter_subscription attribute of this Thermostat instance.
        :rtype: ApiFilterSubscription
        """

        return self._filter_subscription

    @filter_subscription.setter
    def filter_subscription(self, filter_subscription):
        """
        Sets the filter_subscription attribute of this Thermostat instance.

        :param filter_subscription: The filter_subscription value to set for the filter_subscription attribute of this Thermostat instance.
        :type: ApiFilterSubscription
        """

        self._filter_subscription = filter_subscription

    @property
    def remote_sensors(self):
        """
        Gets the remote_sensors attribute of this Thermostat instance.

        :return: The value of the remote_sensors attribute of this Thermostat instance.
        :rtype: List[RemoteSensor]
        """

        return self._remote_sensors
