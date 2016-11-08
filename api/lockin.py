#! encoding = utf-8

def init_lia(lcHandle):
    ''' Initiate the lockin with default settings. '''

    lcHandle.write('OUTX1\n')      # GPIB output
    lcHandle.write('FMOD0;ISRC0;IGND1;DDEF1,0,0;DDEF2,1,0;FPOP1,1\n')


def read_harm(lcHandle):
    ''' Read current lockin harmonics '''

    try:
        text = lcHandle.query('HARM?\n')
    except:
        text = 'N.A.'

    return text


def read_phase(lcHandle):
    ''' Read current lockin phase '''

    try:
        text = lcHandle.query('PHAS?\n')
    except:
        text = 'N.A.'

    return text


def read_freq(lcHandle):
    ''' Read current lockin frequency '''

    try:
        text = lcHandle.query('FREQ?\n')
    except:
        text = 'N.A.'

    return text


def read_sens(lcHandle):
    ''' Read current lockin sensitivity '''

    try:
        text = lcHandle.query('SENS?\n')
    except:
        text = 'N.A.'

    return text



def set_phase(lcHandle, phase):
    ''' Set the lockin phase to phase_text.
        Arguments
            lcHandle: pyvisa.resources.Resource, Lockin handle
            phase: float
        Returns communication status
            0: safe
            1: fatal
    '''

    try:
        status = lcHandle.write('PHAS{:.2f}'.format(phase), '\n')
        return status
    except:
        return 1


def auto_phase(lcHandle):
    ''' Autophase in lockin '''

    lcHandle.write('APHS\n')


def set_harm(lcHandle, harm):
    ''' Set the lockin harmonics to idx.
        Arguments
            lcHandle: pyvisa.resources.Resource, Lockin handle
            harm: int
        Returns communication status
            0: safe
            1: fatal
    '''

    try:
        status = lcHandle.write('HARM{:d}'.format(harm), '\n')
        return status
    except:
        return 1


def set_sensitivity(lcHandle, sens_index):
    ''' Set the lockin sensitivity.
        Arguments
            lcHandle: pyvisa.resources.Resource, Lockin handle
            sens_index: int, user input.
                        The index directly map to the lockin command
        Returns communication status
            0: safe
            1: fatal
    '''

    stat = lcHandle.write('SENS{:d}'.format(sens_index), '\n')
    return stat


def set_tc(lcHandle, tc_index):
    ''' Set the lockin time constant.
        Arguments
            lcHandle: pyvisa.resources.Resource, Lockin handle
            tc_index: int, user input.
                      The index directly map to the lockin command
        Returns communication status
            0: safe
            1: fatal
    '''

    stat = lcHandle.write('OFLT{:d}'.format(tc_index), '\n')
    return stat


def set_couple(lcHandle, couple_text):
    ''' Set the lockin couple.
        Arguments
            lcHandle: pyvisa.resources.Resource, Lockin handle
            couple_text: str, user input.
        Returns communication status
            0: safe
            1: fatal
    '''

    if couple_text == 'AC':
        lcHandle.write('ICPL0\n')
    elif couple_text == 'DC':
        lcHandle.write('ICPL1\n')
    else:
        return 1


def set_reserve(reserve_text):
    ''' Set the lockin reserve '''

    if reserve_text == 'Low Noise':
        lcHandle.write('RMOD2\n')
    elif reserve_text == 'Normal':
        lcHandle.write('RMOD1\n')
    elif reserve_text == 'High Reserve':
        lcHandle.write('RMOD0\n')
    else:
        return 1
