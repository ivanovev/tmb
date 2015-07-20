
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def RLNA_status(ip_addr='192.168.0.1'):
    '''
    Прочитать байт состояния МШУ
    @param ip - ip-адрес устройства
    @return Байт состояния (значения бит: «1» – авария, «0» – норма):
    @return бит 0 (младший) – питание усилителя канала А УК
    @return бит 1 – питание усилителя канала Б УК
    @return бит 2 – питание выходного коммутатора УК
    @return бит 3 – преобразователь напряжения РМШУ
    @return бит 4 – питание МШУ канала А
    @return бит 5 – питание МШУ канала Б
    @return бит 6 – питание микроконтроллера РМШУ
    @return бит 7 – «0»
    '''
    return telnet(ip_addr, 'dm_status')

def RLNA_5v1(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания усилителя канала А
    @param ip - ip-адрес устройства
    @return 0.00..6.10 В
    '''
    return telnet(ip_addr, 'am_5v1')

def RLNA_5v2(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания усилителя канала Б
    @param ip - ip-адрес устройства
    @return 0.00..6.10 В
    '''
    return telnet(ip_addr, 'am_5v2')

def RLNA_2_5v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания коммутатора
    @param ip - ip-адрес устройства
    @return 0.00..3.02 В
    '''
    return telnet(ip_addr, 'am_2_5v')

def RLNA_26v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания преобразователя напряжения
    @param ip - ip-адрес устройства
    @return 0.00..35.00 В
    '''
    return telnet(ip_addr, 'am_26v')

def RLNA_12v1(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания МШУ канала А
    @param ip - ip-адрес устройства
    @return 0.00..13.30 В
    '''
    return telnet(ip_addr, 'am_12v1')

def RLNA_12v2(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания МШУ канала Б
    @param ip - ip-адрес устройства
    @return 0.00..13.30 В
    '''
    return telnet(ip_addr, 'am_12v2')

def RLNA_5_5v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания микроконтроллера
    @param ip - ip-адрес устройства
    @return 0.00..6.10 В
    '''
    return telnet(ip_addr, 'am_5_5v')


def RLNA_channel(ip_addr='192.168.0.1', ch=''):
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

def RLNA_commit(ip_addr='192.168.0.1', en=''):
    """
    Сохранение данных в EFC flash
    @param en - вкл/выкл сохранение данных ("ON" или "OFF") 
    @n пустая строка - чтение
    @return en
    """
    if en:
        return telnet(ip_addr, 'efc commit %s' % en)
    else:
        return telnet(ip_addr, 'efc commit')

