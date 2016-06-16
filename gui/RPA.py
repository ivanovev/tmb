
from collections import OrderedDict as OD
from util import Data, control_cb, monitor_cb, alarm_trace_cb, dev_io_cb
from .RSW import status_fmt_cb

def get_ctrl(dev):
    ctrl = Data(name='Settings', send=True, io_cb=dev_io_cb)
    ctrl.add('channel', label='Channel selection', wdgt='radio', value=OD([('Channel A', '1'), ('Channel B', '0')]))
    ctrl.add('tx', label='TX enable', wdgt='radio', value=OD([('ON', '1'), ('OFF', '0')]))
    ctrl.add('fan', label='FAN enable', wdgt='radio', value=OD([('ON', '1'), ('OFF', '0')]))
    ctrl.add('thrt1', label='Threshold1, C', wdgt='spin', value=Data.spn(0, 100, 1))
    ctrl.add('thrt2', label='Threshold2, C', wdgt='spin', value=Data.spn(0, 100, 1))
    ctrl.add_page('System')
    ctrl.add('commit', label='EFC commit enable', wdgt='combo', state='readonly', value=['ON', 'OFF'], text='ON')
    return ctrl

def get_mntr(dev):
    mntr = Data(name='status', send=True, io_cb=dev_io_cb)
    mntr.add('status', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=status_fmt_cb, msg='AC-DC?')
    add_status = lambda n, msg: mntr.add('status%d' % n, wdgt='alarm', send=False, trace_cb=alarm_trace_cb, fmt_cb=lambda val, read: status_fmt_cb(val,read,n), msg=msg)
    add_status(1, 'MCU power supply')
    add_status(2, 'Output indicator power supply')
    add_status(3, 'Fan current')
    add_status(4, 'PA1 power enable')
    add_status(5, 'PA1 temperature error')
    add_status(6, 'PA1 power diagnostics error')
    add_status(6, 'PA1 DC-DC?')
    add_status(7, 'PA2 power enable')
    add_status(8, 'PA2 temperature error')
    add_status(9, 'PA2 power diagnostics error')
    add_status(10, 'PA2 DC-DC?')
    mntr.add_page('Vcc')
    mntr.add('p_in', wdgt='entry', label='Pin', state='readonly', msg='Input power level, dBm')
    mntr.add('p_out', wdgt='entry', label='Pout', state='readonly', msg='Output power level, dBm')
    mntr.add('vswr1', wdgt='entry', label='VSWR1', state='readonly', msg='PA1 VSWR, V')
    mntr.add('vswr2', wdgt='entry', label='VSWR2', state='readonly', msg='PA2 VSWR, V')
    mntr.add('5_5v1', wdgt='entry', label='5.5V1', state='readonly', msg='MCU input voltage, V')
    mntr.add('5_5v2', wdgt='entry', label='5.5V2', state='readonly', msg='Output indicator voltage, V')
    mntr.add('28v1', wdgt='entry', label='28V1', state='readonly', msg='PA1 input voltage, V')
    mntr.add('28v2', wdgt='entry', label='28V2', state='readonly', msg='PA2 input voltage, V')
    mntr.add('26v', wdgt='entry', label='26V', state='readonly', msg='AD-DC? output, V')
    mntr.add('i_fan', wdgt='entry', label='Ifan', state='readonly', msg='Fan current, A')
    mntr.add('i1', wdgt='entry', label='I(PA1)', state='readonly', msg='PA1 current, A')
    mntr.add('i2', wdgt='entry', label='I(PA2)', state='readonly', msg='PA2 current, A')
    mntr.add('t1', wdgt='entry', label='T(PA1)', state='readonly', msg='PA1 temperature, C')
    mntr.add('t2', wdgt='entry', label='T(PA2)', state='readonly', msg='PA2 temperature, C')
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])

