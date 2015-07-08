
from collections import OrderedDict as OD
from util.mainwnd import control_cb, monitor_cb
from util import Data, alarm_trace_cb, dev_io_cb
from .RSW import status_fmt_cb

def get_ctrl(dev):
    ctrl = Data(name='ctrl', send=True, io_cb=dev_io_cb)
    ctrl.add('agc_en', label='AGC Enable', wdgt='radio', value=OD([('ON', '1'), ('OFF', '0')]))
    ctrl.add('agc_lvl', label='AGC Level', wdgt='spin', value=Data.spn(0, 2.5, 0.1))
    ctrl.add('gain', label='Gain (sig)', wdgt='spin', value=Data.spn(19, 65, 0.1))
    ctrl.add('bpf', label='BPF', wdgt='combo', state='readonly', value=OD([('11MHz', '0'), ('5.5MHz', '2'), ('250kHz', '3')]))
    ctrl.add('bas', label='BAS output', wdgt='radio', value=OD([('Ch1 (sig)', '0'), ('Ch3 (br)', '1')]))
    ctrl.add('test', label='TEST output', wdgt='combo', state='readonly', value=OD([('Synth3(1125-1140,1MHz)', '0'), ('Synth2(150,7MHz)', '1'), ('XTAL(26MHz)', '2'), ('Synth1(835-1140,1MHz)', '3')]))
    ctrl.add('freq', label='Channel1 freq', wdgt='spin', value=Data.spn(975, 1000, 0.01))
    ctrl.add('inv', label='Channel1 inv', wdgt='check')
    ctrl.add('freqbr', label='Channel3 freq', wdgt='spin', value=Data.spn(975, 1000.1, 0.01))
    ctrl.add('gainbr', label='Gain (br)', wdgt='spin', value=Data.spn(29.5, 77.5, 0.1))
    ctrl.add('thrs1', label='Threshold1', wdgt='spin', value=Data.spn(0, 200, 1))
    ctrl.add('thrs2', label='Threshold2', wdgt='spin', value=Data.spn(0, 200, 1))
    ctrl.add('thrsb', label='Threshold (BR)', wdgt='spin', value=Data.spn(0, 10, 0.1))
    return ctrl

def get_mntr(dev):
    mntr = Data(name='status', send=True, io_cb=dev_io_cb)
    mntr.add('status', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=status_fmt_cb, msg='Power supply')
    add_status = lambda n, msg: mntr.add('status%d' % n, wdgt='alarm', send=False, trace_cb=alarm_trace_cb, fmt_cb=lambda val, read: status_fmt_cb(val,read,n), msg=msg)
    add_status(1, 'Ch1')
    add_status(2, 'Ch2')
    add_status(3, 'Ch3')
    add_status(4, 'Uch1 < LVL')
    add_status(5, 'Uch3 < LVL')
    mntr.add_page('mntr')
    mntr.add('5_5v', wdgt='entry', label='5.5V', state='readonly', msg='5.5V')
    mntr.add('rxl', wdgt='entry', label='RXL', state='readonly', msg='RX signal level')
    mntr.add('brl', wdgt='entry', label='BRL', state='readonly', msg='Beacon signal level')
    mntr.cmds.columns = 3
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])
