
from collections import OrderedDict as OD
from util.mainwnd import control_cb, monitor_cb
from util import Data, alarm_trace_cb, dev_io_cb
from .RSW import status_fmt_cb
from .DC import inv_fmt_cb, inv_trace_cb, freq_cmd_cb

def get_ctrl(dev):
    ctrl = Data(name='ctrl', send=True, io_cb=dev_io_cb)
    ctrl.add('test', label='TEST output', wdgt='radio', value=OD([('Synth1(679-957MHz)', '0'), ('XTAL(26MHz)', '1'), ('Synth2(151MHz)', '2')]))
    ctrl.add('freq', label='Output frequency, MHz', wdgt='spin', value=Data.spn(805, 831, 0.01), cmd_cb=freq_cmd_cb)
    ctrl.add('inv', label='Inversion', wdgt='check', fmt_cb=inv_fmt_cb, trace_cb=inv_trace_cb)
    ctrl.add('gain', label='Gain, dB', wdgt='spin', value=Data.spn(-10.5, 15, 0.5))
    ctrl.add('thrs', label='Threshold, dBm', wdgt='spin', value=Data.spn(-40, 20, 1))
    return ctrl

def get_mntr(dev):
    mntr = Data(name='status', send=True, io_cb=dev_io_cb)
    mntr.add('status', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=status_fmt_cb, msg='Power supply')
    add_status = lambda n, msg: mntr.add('status%d' % n, wdgt='alarm', send=False, trace_cb=alarm_trace_cb, fmt_cb=lambda val, read: status_fmt_cb(val,read,n), msg=msg)
    add_status(1, 'Synth1 lock detect')
    add_status(2, 'Synth2 (aux) lock detect')
    add_status(3, 'Output level < threshold')
    mntr.add_page('mntr')
    mntr.add('5_5v', wdgt='entry', label='5.5V', state='readonly', msg='5.5V')
    mntr.add('txl', wdgt='entry', label='TXL', state='readonly', msg='TX signal level')
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])
