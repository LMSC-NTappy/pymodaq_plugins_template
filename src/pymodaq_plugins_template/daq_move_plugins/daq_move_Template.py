from pymodaq.control_modules.move_utility_classes import DAQ_Move_base, comon_parameters_fun, main  # common set of parameters for all actuators
from pymodaq.daq_utils.daq_utils import ThreadCommand # object used to send info back to the main thread


class PythonWrapperOfYourInstrument:
    #  TODO Replace this fake class with the import of the real python wrapper of your instrument
    pass


class DAQ_Move_Template(DAQ_Move_base):
    """Plugin for the Template Instrument

    This object inherits all functionality to communicate with PyMoDAQ Module through inheritance via DAQ_Move_base
    It then implements the particular communication with the instrument

    Attributes:
    -----------
    controller: object
        The particular object that allow the communication with the hardware, in general a python wrapper around the
         hardware library
    # TODO add your particular attributes here if any

    """
    _controller_units = 'whatever'  # TODO for your plugin: put the correct unit here
    is_multiaxes = False  # TODO for your plugin set to True if this plugin is controlled for a multiaxis controller
    axes_names = ['Axis1', 'Axis2']  # TODO for your plugin: complete the list

    params = [   # TODO for your custom plugin: elements to be added here as dicts in order to control your custom stage
                ] + comon_parameters_fun(is_multiaxes, axes_names)

    def ini_attributes(self):
        #  TODO declare the type of the wrapper (and assign it to self.controller) you're going to use for easy
        #  autocompletion
        self.controller: PythonWrapperOfYourInstrument = None

        #TODO declare here attributes you want/need to init with a default value
        pass

    def get_actuator_value(self):
        """Get the current value from the hardware with scaling conversion.

        Returns
        -------
        float: The position obtained after scaling conversion.
        """
        ## TODO for your custom plugin
        raise NotImplemented  # when writing your own plugin remove this line
        pos = self.controller.your_method_to_get_the_actuator_value()  # when writing your own plugin replace this line
        pos = self.get_position_with_scaling(pos)
        return pos

    def close(self):
        """Terminate the communication protocol"""
        ## TODO for your custom plugin
        raise NotImplemented  # when writing your own plugin remove this line
        #  self.controller.your_method_to_terminate_the_communication()  # when writing your own plugin replace this line

    def commit_settings(self, param):
        """Apply the consequences of a change of value in the detector settings

        Parameters
        ----------
        param: Parameter
            A given parameter (within detector_settings) whose value has been changed by the user
        """
        ## TODO for your custom plugin
        if param.name() == "a_parameter_you've_added_in_self.params":
           self.controller.your_method_to_apply_this_param_change()
        else:
            pass

    def ini_stage(self, controller=None):
        """Actuator communication initialization

        Parameters
        ----------
        controller: (object)
            custom object of a PyMoDAQ plugin (Slave case). None if only one actuator by controller (Master case)

        Returns
        -------
        info: str
        initialized: bool
            False if initialization failed otherwise True
        """

        raise NotImplemented  # TODO when writing your own plugin remove this line and modify the one below
        self.ini_stage_init(old_controller=controller,
                            new_controller=PythonWrapperOfYourInstrument())

        info = "Whatever info you want to log"
        initialized = self.controller.a_method_or_atttribute_to_check_if_init()  # todo
        return info, initialized

    def move_abs(self, value):
        """ Move the actuator to the absolute target defined by value

        Parameters
        ----------
        value: (float) value of the absolute target positioning
        """

        value = self.check_bound(value)  #if user checked bounds, the defined bounds are applied here
        self.target_position = value
        value = self.set_position_with_scaling(value)  # apply scaling if the user specified one
        ## TODO for your custom plugin
        raise NotImplemented  # when writing your own plugin remove this line
        self.controller.your_method_to_set_an_absolute_value(value)  # when writing your own plugin replace this line
        self.emit_status(ThreadCommand('Update_Status', ['Some info you want to log']))


    def move_rel(self, value):
        """ Move the actuator to the relative target actuator value defined by value

        Parameters
        ----------
        value: (float) value of the relative target positioning
        """
        value = self.check_bound(self.current_position + value) - self.current_position
        self.target_position = value + self.current_position
        value = self.set_position_relative_with_scaling(value)

        ## TODO for your custom plugin
        raise NotImplemented  # when writing your own plugin remove this line
        self.controller.your_method_to_set_a_relative_value(value)  # when writing your own plugin replace this line
        self.emit_status(ThreadCommand('Update_Status', ['Some info you want to log']))


    def move_home(self):
        """Call the reference method of the controller"""

        ## TODO for your custom plugin
        raise NotImplemented  # when writing your own plugin remove this line
        self.controller.your_method_to_get_to_a_known_reference()  # when writing your own plugin replace this line
        self.emit_status(ThreadCommand('Update_Status', ['Some info you want to log']))


    def stop_motion(self):
      """Stop the actuator and emits move_done signal"""

      ## TODO for your custom plugin
      raise NotImplemented  # when writing your own plugin remove this line
      self.controller.your_method_to_stop_positioning()  # when writing your own plugin replace this line
      self.emit_status(ThreadCommand('Update_Status', ['Some info you want to log']))


if __name__ == '__main__':
    main(__file__)
