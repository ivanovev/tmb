
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def DC_agc_en(ip_addr='192.168.0.1', enable=''):
    '''
    Прочитать/записать значение индикатора включения АРУ 
    @param ip - ip-адрес устройства
    @return «1» – Вкл, «0»– Выкл
    '''
    if enable:
        return telnet(ip_addr, 'dc_agc', enable)
    else:
        return telnet(ip_addr, 'dm_agc')

def DC_agc_lvl(ip_addr='192.168.0.1', level=''):
    '''
    Прочитать/записать значение индикатора включения АРУ 
    @param ip - ip-адрес устройства
    @return «1» – Вкл, «0»– Выкл
    '''
    if level:
        return telnet(ip_addr, 'sc_agc', level)
    else:
        return telnet(ip_addr, 'sm_agc')

def DC_gain(ip_addr='192.168.0.1', gain=''):
    '''
    Прочитать/записать значение коэффициента усиления сигнального канала (при отключенной АРУ) 
    @param ip - ip-адрес устройства
    @return gain - коэффициент усиления в дБ от 19 до 65 (шаг 0,5)
    '''
    if gain:
        return telnet(ip_addr, 'sc_gain', gain)
    else:
        return telnet(ip_addr, 'sm_gain')

def DC_bpf(ip_addr='192.168.0.1', bpf=''):
    '''
    Прочитать/записать значение полосового фильтрa 
    @param ip - ip-адрес устройства
    @param bpf - «0» – 11 МГц, «2»– 5,5 МГц, «3»– 250 кГц
    '''
    if bpf:
        return telnet(ip_addr, 'dc_bpf', bpf)
    else:
        return telnet(ip_addr, 'dm_bpf')

def DC_bas(ip_addr='192.168.0.1', bas=''):
    '''
    Вывести на разъем БАС сигнал измерителя уровня заданного канала 
    @param ip - ip-адрес устройства
    @param bas - «0» – сигнальный канал, «1»– канал наведения
    '''
    if bas:
        return telnet(ip_addr, 'dc_bas', bas)
    else:
        return telnet(ip_addr, 'dm_bas')

def DC_test(ip_addr='192.168.0.1', test=''):
    '''
    Вывести на разъем TEST требуемый сигнал для контроля 
    @param ip - ip-адрес устройства
    @param Num «0» – СЧ3 (1125-1140,1 МГц), «1» - СЧ2 (150,7 МГц), «2» – КГ (26 МГц), «3» - СЧ1 (835-1140,1 МГц)
    '''
    if test:
        return telnet(ip_addr, 'dc_test', test)
    else:
        return telnet(ip_addr, 'dm_test')

def DC_freq(ip_addr='192.168.0.1', freq='', inv=''):
    '''
    Прочитать/записать значение частоты настройки сигнального канала с учетом инверсии спектра
    @param ip - ip-адрес устройства
    @param freq - частота в МГц от 975,00 до 1000,10 (шаг 0,01)
    @param inv – признак инверсии спектра («1» - инверсия, «0» - норма)
    '''
    if freq:
        return telnet(ip_addr, 'sc_freq', freq, inv)
    else:
        return telnet(ip_addr, 'sm_freq')

def DC_inv(ip_addr='192.168.0.1'):
    '''
    Прочитать значение индикатора инверсии спектра в сигнальном канале 
    @param ip - ip-адрес устройства
    @return «1» - инверсия, «0» - норма
    '''
    return telnet(ip_addr, 'sm_inv')

def DC_freqbr(ip_addr='192.168.0.1', freqbr=''):
    '''
    Прочитать/записать значение частоты настройки канала наведения 
    @param ip - ip-адрес устройства
    @param freqbr - частота в МГц от 975.00 до 1000.10 (шаг 0.01)
    @return частота в МГц от 975.00 до 1000.10 (шаг 0.01)
    '''
    if freqbr:
        return telnet(ip_addr, 'sc_freqbr', freqbr)
    else:
        return telnet(ip_addr, 'sm_freqbr')

def DC_gainbr(ip_addr='192.168.0.1', gainbr=''):
    '''
    Установить коэффициент усиления канала наведения
    @param ip - ip-адрес устройства
    @param gainbr - коэффициент усиления в дБ от 29.5 до 77.5 (шаг 0,5)
    @return коэффициент усиления в дБ от 29.5 до 77.5 (шаг 0,5)
    '''
    if gainbr:
        return telnet(ip_addr, 'sc_gainbr', gainbr)
    else:
        return telnet(ip_addr, 'sm_gainbr')

def DC_thrs1(ip_addr='192.168.0.1', thrs1=''):
    '''
    Прочитать/записать значение нижнего порога срабатывания детектора наличия рабочего сигнала 
    @param ip - ip-адрес устройства
    @param thrs1 – значение порога 0..200мВ
    @return значение порога 0...200мВ
    '''
    if thrs1:
        return telnet(ip_addr, 'ac_thrs1', thrs1)
    else:
        return telnet(ip_addr, 'am_thrs1')

def DC_thrs2(ip_addr='192.168.0.1', thrs2=''):
    '''
    Прочитать/записать значение верхнего порога срабатывания детектора наличия рабочего сигнала 
    @param ip - ip-адрес устройства
    @param thrs2 – значение порога 0..200мВ
    @return значение порога 0...200мВ
    '''
    if thrs2:
        return telnet(ip_addr, 'ac_thrs2', thrs2)
    else:
        return telnet(ip_addr, 'am_thrs2')

def DC_thrsb(ip_addr='192.168.0.1', thrsb=''):
    '''
    Прочитать/записать порог срабатывания детектора наличия сигнала наведения 
    @param ip - ip-адрес устройства
    @param thrsb – значение порога 0..10В
    @return значение порога 0...10В
    '''
    if thrsb:
        return telnet(ip_addr, 'ac_thrsb', thrsb)
    else:
        return telnet(ip_addr, 'am_thrsb')

def DC_status(ip_addr='192.168.0.1'):
    '''
    Прочитать состояние БПЧВН
    @param ip - ip-адрес устройства
    @return Слово состояния (значения бит: «1» – авария, «0» – норма):
    @return бит 0 (младший) – состояние блока питания
    @return бит 1 – состояние захвата СЧ1 (сигнальный канал)
    @return бит 2 – состояние захвата СЧ2 (вспомогательный)
    @return бит 3 – состояние захвата СЧ3 (канал наведения)
    @return бит 4 – напряжение в сигнальном канале ниже заданного порога
    @return бит 5 – напряжение в канале наведения ниже заданного порога
    @return бит 6-15 – «0»
    '''
    return telnet(ip_addr, 'dm_status')

def DC_5_5v(ip_addr='192.168.0.1'):
    '''
    Прочитать напряжение блока питания (+5,5 В) 
    @param ip - ip-адрес устройства
    @return 0,00 .. 6,10 В
    '''
    return telnet(ip_addr, 'am_5_5v')

def DC_rxl(ip_addr='192.168.0.1'):
    '''
    Прочитать значение выхода (Vrms) сигнального канала 
    @param ip - ip-адрес устройства
    @return 0,00 .. 0,65 В
    '''
    return telnet(ip_addr, 'am_rxl')

def DC_brl(ip_addr='192.168.0.1'):
    '''
    Прочитать значение выхода (Vrms) канала наведения 
    @param ip - ip-адрес устройства
    @return 0 .. 10 В
    '''
    return telnet(ip_addr, 'am_brl')

def DC_commit(ip_addr='192.168.0.1', en=''):
    """
    Сохранение данных в EFC flash
    @param en - вкл/выкл сохранение данных ("ON" или "OFF") 
    @n пустая строка - чтение
    @return en
    """
    return telnet(ip_addr, 'efc commit %s' % en)

