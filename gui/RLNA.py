
from collections import OrderedDict as OD
from util import Data, control_cb, monitor_cb, alarm_trace_cb, dev_io_cb
from .RSW import status_fmt_cb

def get_ctrl(dev):
    ctrl = Data(name='Settings', send=True, io_cb=dev_io_cb)
    ctrl.add('channel', label='Channel selection', wdgt='radio', value=OD([('Channel A', '1'), ('Channel B', '0')]))
    ctrl.add_page('System')
    ctrl.add('commit', label='EFC commit enable', wdgt='combo', state='readonly', value=['ON', 'OFF'], text='ON')
    return ctrl

def get_mntr(dev):
    mntr = Data(name='status', send=True, io_cb=dev_io_cb)
    mntr.add('status', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=status_fmt_cb, msg='ChA LNA power supply')
    add_status = lambda n, msg: mntr.add('status%d' % n, wdgt='alarm', send=False, trace_cb=alarm_trace_cb, fmt_cb=lambda val, read: status_fmt_cb(val,read,n), msg=msg)
    add_status(1, 'ChB LNA power supply')
    add_status(2, 'Output switch power supply')
    add_status(3, 'AC-DC/DC-DC?')
    add_status(4, 'ChA power supply')
    add_status(5, 'ChB power supply')
    add_status(6, 'MCU power supply')
    mntr.add_page('Vcc')
    mntr.add('5v1', wdgt='entry', label='5V1', state='readonly', msg='5V, ChA LNA power supply')
    mntr.add('5v2', wdgt='entry', label='5V2', state='readonly', msg='5V, ChB LNA power supply')
    mntr.add('2_5v', wdgt='entry', label='2.5V', state='readonly', msg='Output switch power supply')
    mntr.add('26v', wdgt='entry', label='26V', state='readonly', msg='AC-DC/DC-DC?')
    mntr.add('12v1', wdgt='entry', label='12V1', state='readonly', msg='ChA power supply')
    mntr.add('12v2', wdgt='entry', label='12V2', state='readonly', msg='ChB power supply')
    mntr.add('5_5v', wdgt='entry', label='5_5V', state='readonly', msg='MCU power supply')
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])

