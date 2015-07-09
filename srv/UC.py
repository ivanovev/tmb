
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def UC_test(ip_addr='192.168.0.1', test=''):
    '''
    Вывести на разъем TEST требуемый сигнал для контроля 
    @param ip - ip-адрес устройства
    @param test 0 – КГ (26 МГц), 1 - СЧ1 (680-957 МГц), 2 - СЧ2 (151 МГц)
    @return 0, 1, 2
    '''
    if test:
        return telnet(ip_addr, 'dc_test', test)
    else:
        return telnet(ip_addr, 'dm_test')

def UC_freq(ip_addr='192.168.0.1', freq='', inv=''):
    '''
    Прочитать/записать значение частоты настройки сигнального канала с учетом инверсии спектра
    @param ip - ip-адрес устройства
    @param freq - частота в МГц от 805,00 до 831,00 (шаг 0,01)
    @param inv – признак инверсии спектра («1» - инверсия, «0» - норма)
    @return частота в МГц от 805,00 до 831,00 (шаг 0,01)
    '''
    if freq:
        return telnet(ip_addr, 'sc_freq', freq, inv)
    else:
        return telnet(ip_addr, 'sm_freq')

def UC_inv(ip_addr='192.168.0.1'):
    '''
    Прочитать значение индикатора инверсии спектра в сигнальном канале 
    @param ip - ip-адрес устройства
    @return «1» - инверсия, «0» - норма
    '''
    return telnet(ip_addr, 'sm_inv')

def UC_gain(ip_addr='192.168.0.1', gain=''):
    '''
    Прочитать/записать коэффициент усиления 
    @param ip - ip-адрес устройства
    @param gain – коэффициент усиления в дБ от -10.5 до 15 (шаг 0,5)
    @return новое значение коэффициента усиления (может быть меньше gain)
    '''
    if gain:
        return telnet(ip_addr, 'sc_gain', gain)
    else:
        return telnet(ip_addr, 'sm_gain')

def UC_thrs(ip_addr='192.168.0.1', thrs=''):
    '''
    Прочитать/записать порог срабатывания детектора наличия выходного сигнала 
    @param ip - ip-адрес устройства
    @param thrs – значение порога в дБм от -40 до 20 (с шагом 0,5 дБ)
    '''
    if thrs:
        return telnet(ip_addr, 'ac_thrs', thrs)
    else:
        return telnet(ip_addr, 'am_thrs')

def UC_status(ip_addr='192.168.0.1'):
    '''
    Получить состояние БПЧВВ
    @param ip - ip-адрес устройства
    @return Слово состояния значения бит: «1» – авария, «0» – норма):
    @return бит 0 (младший) – состояние блока питания
    @return бит 1 – состояние захвата СЧ1 (сигнальный канал)
    @return бит 2 – состояние захвата СЧ2 (вспомогательный)
    @return бит 3 – уровень выходного сигнала ниже заданного порога
    @return бит 4-15 – «0»
    '''
    return telnet(ip_addr, 'dm_status')

def UC_5_5v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение блока питания (+5,5 В) 
    @param ip - ip-адрес устройства
    @return 0,00 .. 6,10 В
    '''
    return telnet(ip_addr, 'am_5_5v')

def UC_txl(ip_addr='192.168.0.1'):
    '''
    Прочитать уровень мощности выходного сигнала 
    @param ip - ip-адрес устройства
    @return -40,00 .. +20,0 дБм
    '''
    return telnet(ip_addr, 'am_txl')

