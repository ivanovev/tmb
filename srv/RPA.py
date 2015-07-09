
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def RPA_status(ip_addr='192.168.0.1'):
    '''
    Прочитать слово состояния РУМ
    @param ip ip-адрес устройства
    @return Слово состояния(значения бит: «1» – авария, «0» – норма):
    @return бит 0 (младший) – преобразователь напряжения
    @return бит 1 – питание микроконтроллера
    @return бит 2 – питание измерителей мощности
    @return бит 3 – ток потребления вентилятора
    @return бит 4 – питание УМ1
    @return бит 5 – защита УМ1 по температуре
    @return бит 6 – диагностика напряжения источника питания УМ1
    @return бит 7 – диагностика преобразователя источника питания УМ1
    @return бит 8 – питание УМ2
    @return бит 9 – защита УМ2 по температуре
    @return бит 10 – диагностика напряжения источника питания УМ2
    @return бит 11 – диагностика преобразователя источника питания УМ2
    @return бит 12-15 – «0»
    '''
    return telnet(ip_addr, 'dm_status')

def RPA_p_in(ip_addr='192.168.0.1'):
    '''
    Прочитать величину мощности на входе РУМ 
    @param ip ip-адрес устройства
    @return -43.1..+26.9 дБм
    '''
    return telnet(ip_addr, 'am_pin')

def RPA_p_out(ip_addr='192.168.0.1'):
    '''
    Прочитать величину мощности на выходе РУМ
    @param ip ip-адрес устройства
    @return -14.75..+55.25 дБм
    '''
    return telnet(ip_addr, 'am_pout')

def RPA_vswr1(ip_addr='192.168.0.1'):
    '''
    Прочитать относительное значение КСВН нагрузки УМ1 
    @param ip ip-адрес устройства
    @return 0.50..2.00 В
    '''
    return telnet(ip_addr, 'am_vswr1')

def RPA_vswr2(ip_addr='192.168.0.1'):
    '''
    Прочитать относительное значение КСВН нагрузки УМ2
    @param ip ip-адрес устройства
    @return 0.50..2.00 В
    '''
    return telnet(ip_addr, 'am_vswr2')

def RPA_5_5v1(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания микроконтроллера 
    @param ip ip-адрес устройства
    @return 0.00..6.10 В
    '''
    return telnet(ip_addr, 'am_5_5v1')

def RPA_5_5v2(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания измерителей мощности 
    @param ip ip-адрес устройства
    @return 0.00..6.10 В
    '''
    return telnet(ip_addr, 'am_5_5v2')

def RPA_26v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания преобразователя напряжения 
    @param ip ip-адрес устройства
    @return 0.00..35.00 В
    '''
    return telnet(ip_addr, 'am_26v')

def RPA_28v1(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение источника питания УМ1
    @param ip ip-адрес устройства
    @return 0.00..32.10 В
    '''
    return telnet(ip_addr, 'am_28v1')

def RPA_28v2(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение источника питания УМ2
    @param ip ip-адрес устройства
    @return 0.00..32.10 В
    '''
    return telnet(ip_addr, 'am_28v2')

def RPA_i1(ip_addr='192.168.0.1'):
    '''
    Прочитать относительное значение тока потребления УМ1
    @param ip ip-адрес устройства
    @return 0.50..2.00 А
    '''
    return telnet(ip_addr, 'am_cur1')

def RPA_i2(ip_addr='192.168.0.1'):
    '''
    Прочитать относительное значение тока потребления УМ2
    @param ip ip-адрес устройства
    @return 0.50..2.00 А
    '''
    return telnet(ip_addr, 'am_cur2')

def RPA_i_fan(ip_addr='192.168.0.1'):
    '''
    Прочитать относительное значение тока потребления вентилятора 
    @param ip ip-адрес устройства
    @return 0.00..2.50 А
    '''
    return telnet(ip_addr, 'am_vent')

def RPA_t1(ip_addr='192.168.0.1'):
    '''
    Прочитать температуру ИМ1 
    @param ip ip-адрес устройства
    @return -60.0..+100.0 С
    '''
    return telnet(ip_addr, 'am_temp1')

def RPA_t2(ip_addr='192.168.0.1'):
    '''
    Прочитать температуру ИМ2
    @param ip ip-адрес устройства
    @return -60.0..+100.0 С
    '''
    return telnet(ip_addr, 'am_temp2')

def RPA_channel(ip_addr='192.168.0.1', ch=''):
    '''
    Прочитать/записать номер рабочего канала
    @param ip - ip-адрес устройства
    @param ch - номер рабочего канала: 1 - канал А, 0 - канал Б
    @return «1» – канал А, «0» – канал Б
    '''
    if ch:
        return telnet(ip_addr, 'dc_channel %s' % ch)
    else:
        return telnet(ip_addr, 'dm_channel')

def RPA_tx(ip_addr='192.168.0.1', enable=''):
    '''
    Прочитать/записать состояние усилителя вкл/выкл
    @param ip ip-адрес устройства
    @param enable - 1 - вкл, 0 - выкл
    @return 1 - вкл, 0 - выкл
    '''
    if enable:
        return telnet(ip_addr, 'dc_tx %s' % enable)
    else:
        return telnet(ip_addr, 'dm_tx')

def RPA_fan(ip_addr='192.168.0.1', enable=''):
    '''
    Прочитать/записать состояние вентилятора вкл/выкл
    @param ip ip-адрес устройства
    @param enable - 1 - вкл, 0 - выкл
    @return 1 - вкл, 0 - выкл
    '''
    if enable:
        return telnet(ip_addr, 'dc_vent %s' % enable)
    else:
        return telnet(ip_addr, 'dm_vent')

def RPA_fan(ip_addr='192.168.0.1', enable=''):
    '''
    Прочитать/записать состояние вентилятора вкл/выкл
    @param ip ip-адрес устройства
    @param enable - 1 - вкл, 0 - выкл
    @return 1 - вкл, 0 - выкл
    '''
    if enable:
        return telnet(ip_addr, 'dc_vent %s' % enable)
    else:
        return telnet(ip_addr, 'dm_vent')

def RPA_thrs1(ip_addr='192.168.0.1', thrs1=''):
    '''
    Прочитать/записать нижний порог температуры усилителя (по достижении температуры ниже порога вентилятор автоматически выключается)
    @param ip - ip-адрес устройства
    @param thrs1 - нижний порог температуры усилителя
    @return 0..+100.0 С
    '''
    if thrs1:
        return telnet(ip_addr, 'dc_thrt1 %s' % thrs1)
    else:
        return telnet(ip_addr, 'dm_thrt1')

def RPA_thrs2(ip_addr='192.168.0.1', thrs2=''):
    '''
    Прочитать/записать верхний порог температуры усилителя (по достижении температуры ниже порога вентилятор автоматически выключается)
    @param ip - ip-адрес устройства
    @param thrs2 - нижний порог температуры усилителя
    @return 0..+100.0 С
    '''
    if thrs2:
        return telnet(ip_addr, 'dc_thrt2 %s' % thrs2)
    else:
        return telnet(ip_addr, 'dm_thrt2')

