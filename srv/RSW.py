
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def RSW_chup(ip_addr='192.168.0.1', ch=''):
    '''
    Прочитать/записать рабочий канал ВВЕРХ 
    @param ip - ip-адрес устройства
    @param ch - Номер канала 1 - канал А, 0 - канал Б
    '''
    if ch:
        return telnet(ip_addr, 'dc_chup', ch)
    else:
        return telnet(ip_addr, 'dm_chup')

def RSW_chdn(ip_addr='192.168.0.1', ch=''):
    '''
    Прочитать/записать рабочий канал ВНИЗ
    @param ip - ip-адрес устройства
    @param ch - Номер канала 1 - канал А, 0 - канал Б
    '''
    if ch:
        return telnet(ip_addr, 'dc_chdn', ch)
    else:
        return telnet(ip_addr, 'dm_chdn')

def RSW_test(ip_addr='192.168.0.1', ch=''):
    '''
    Вывести на разъем TEST требуемый сигнал для контроля 
    @param ip - ip-адрес устройства
    @param ch - 0 - ВЧ-ВВЕРХ, 1 - ПЧ-ВВЕРХ, 2 - ВЧ-ВНИЗ, 3 - ПЧ-ВНИЗ
    '''
    if ch:
        return telnet(ip_addr, 'dc_test', ch)
    else:
        return telnet(ip_addr, 'dm_test')

def RSW_status(ip_addr='192.168.0.1'):
    '''
    Прочитать слово состояния переключателя резерва
    @param ip - ip-адрес устройства
    @return Слово состояния(значения бит: «1» – авария, «0» – норма):
    @return бит 0 (младший) – состояние блока питания
    @return бит 1 – состояние захвата СЧ1 (сигнальный канал)
    @return бит 2 – состояние захвата СЧ2 (вспомогательный)
    @return бит 3 – состояние захвата СЧ3 (канал наведения)
    @return бит 4 – напряжение в сигнальном канале ниже заданного порога
    @return бит 5 – напряжение в канале наведения ниже заданного порога
    @return бит 6-15 – «0»
    '''
    return telnet(ip_addr, 'dm_status')

def RSW_3v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания коммутатора ВЧ-ВВЕРХ (+3,0 В)
    @param ip - ip-адрес устройства
    @return 0.00..4.07 В
    '''
    return telnet(ip_addr, 'am_3v')

def RSW_2_5v1(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания коммутатора ПЧ-ВВЕРХ и коммутатора ТЕСТ (+2,5 В)
    @param ip - ip-адрес устройства
    @return 0.00..3.02 В
    '''
    return telnet(ip_addr, 'am_2_5v1')

def RSW_2_5v2(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания коммутатора ПЧ-ВНИЗ и коммутатора ВЧ-ВНИЗ (+2,5 В)
    @param ip - ip-адрес устройства
    @return 0.00..3.02 В
    '''
    return telnet(ip_addr, 'am_2_5v2')

def RSW_11v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение питания коммутатора БАС (+11 В)
    @param ip - ip-адрес устройства
    @return 0.00..14.1 В
    '''
    return telnet(ip_addr, 'am_11v')

def RSW_commit(ip_addr='192.168.0.1', en=''):
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

