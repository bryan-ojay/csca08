class LightSwitch():
    '''A class to represent a light switch.'''

    def __init__(self, on_off):
        '''(LightSwitch, str) -> NoneType
        Set up a new lightswitch that is either turned on or turned off.
        REQ: on_off in ['on', 'off']
        '''
        # set _is_on bool to True if light should be on
        # set _is_on bool to False if light should be off
        if on_off == "on":
            self._is_on = True

        elif on_off == 'off':
            self._is_on = False

    def __str__(self):
        '''(LightSwitch) -> str
        Returns a sentence describing the state of the current light switch.
        '''
        if self._is_on:
            return "I am on"
        else:
            return "I am off"

    def turn_on(self):
        '''(LightSwitch) -> NoneType
        Turns the light on, _is_on is set to True.
        '''
        if not self._is_on:
            self._is_on = True

    def turn_off(self):
        '''(LightSwitch) -> NoneType
        Turns the light off; _is_on is set to False.
        '''
        if self._is_on:
            self._is_on = False

    def flip(self):
        '''(LightSwitch) -> NoneType
        Turns the light on if it was previously off, and turns the light off
        if it was previously on.
        '''
        self._is_on = not self._is_on


class SwitchBoard():
    '''A class to represent a board of light switches.'''

    def __init__(self, num_switches):
        '''(Switchboard, int) -> NoneType
        Set up a new switch board with a specified number of light switches
        organized in a list
        REQ: num_switches > 0
        '''
        self._switches = []  # setup list for number of switvhes
        for light_switch in range(num_switches):  # add n number of switches
            self._switches.append(LightSwitch('off'))

    def find_switches(self, data_type):
        '''(Switchboard, int) -> (str or list)
        Takes in an integer that determines a data type to return for a
        sequence of light switches on the board that are currently turned on.
        Returns a string if data_type is 0 and a list if data_type is 1.
        is 1.
        REQ: 0 <= data_type <= 1
        '''
        # find switches that are on
        on_switch_string = ""
        on_switch_list = []

        # run through the whole switch board
        for light_switch in range(len(self._switches)):

            # if this light is on, add it to the string of on switches
            if self._switches[light_switch]._is_on:
                on_switch_string += (" " + str(light_switch))
                on_switch_list.append(light_switch)

        if data_type == 0:
            statement = ("The following switches are on:" + on_switch_string)

        elif data_type == 1:
            statement = on_switch_list

        return statement

    def __str__(self):
        '''(Switchboard) -> str
        Returns a string stating which of the light switches on the board are
        currently turned on.
        '''
        # use find_switches to find which lights are on
        on_switches = self.find_switches(0)
        return on_switches

    def which_switch(self):
        '''(Switchboard) -> list
        Returns a list representing the light switches on the board are
        currently turned on.
        '''
        # use find_switches to find which lights are on
        on_switches = self.find_switches(1)
        return on_switches

    def flip(self, switch_num):
        '''(Switchboard, int) -> NoneType
        Takes in an integer representing the index of the desired light switch
        to flip its state.
        REQ: 0 <= switch_num < len(self)
        '''
        if 0 <= switch_num < len(self._switches):
            self._switches[switch_num].flip()

    def flip_every(self, switch_step):
        '''(Switchboard, int) -> NoneType
        Takes in an integer, flips every light switch on an increment as
        specified by the integer (i.e: if the integer is 3, every 3rd light,
        starting from 0, is flipped.)
        REQ: switch_step > 0
        '''
        # run through the list on an increment defined by switch_step
        for light_switch in self._switches[::switch_step]:
            light_switch.flip()

    def reset(self):
        '''(Switchboard) -> NoneType
        Turns off all the light switches on the switchboard.
        '''
        for light_switch in self._switches:
            light_switch.turn_off()

if __name__ == "__main__":
    switchboard = SwitchBoard(1024)
    switches = switchboard._switches
    for index in range(1, len(switches)):
        for light_switch in switches[::index]:
            light_switch.flip()
    print(switchboard)
    print(switchboard.which_switch())
