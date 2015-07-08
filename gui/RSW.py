
from collections import OrderedDict as OD
from util.mainwnd import control_cb, monitor_cb
from util import Data, alarm_trace_cb, dev_io_cb

def status_fmt_cb(val, read=True, n=0):
    val = int(val, 16)
    return '1' if val & (1 << n) else '0'

def get_ctrl(dev):
    ctrl = Data(name='ctrl', send=True, io_cb=dev_io_cb)
    ctrl.add('chup', label='Channel UP', wdgt='combo', state='readonly', value=OD([('Channel A', '1'), ('Channel B', '0')]))
    ctrl.add('chdn', label='Channel DOWN', wdgt='combo', state='readonly', value=OD([('Channel A', '1'), ('Channel B', '0')]))
    ctrl.add('test', label='Test signal', wdgt='combo', state='readonly', value=OD([('UC-HF', '0'), ('UC-IF', '1'), ('DC-HF', '2'), ('DC-IF', '3')]))
    return ctrl

def get_mntr(dev):
    mntr = Data(name='status', send=True, io_cb=dev_io_cb)
    mntr.add('status', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=status_fmt_cb, msg='Power supply')
    add_status = lambda n, msg: mntr.add('status%d' % n, wdgt='alarm', send=False, trace_cb=alarm_trace_cb, fmt_cb=lambda val, read: status_fmt_cb(val,read,n), msg=msg)
    add_status(1, 'Ch1 (sig)')
    add_status(2, 'Ch2 (aux)')
    add_status(3, 'Ch3 (br)')
    add_status(4, 'Uch1 (sig) < LVL')
    add_status(5, 'Uch3 (br) < LVL')
    mntr.add_page('Vcc')
    mntr.add('3v', wdgt='entry', label='3V', state='readonly', msg='3V')
    mntr.add('11v', wdgt='entry', label='11V', state='readonly', msg='11V')
    mntr.add('2_5v1', wdgt='entry', label='UC 2.5V', state='readonly', msg='UC 2.5V')
    mntr.add('2_5v2', wdgt='entry', label='DC 2.5V', state='readonly', msg='DC 2.5V')
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])
