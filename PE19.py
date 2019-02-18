#PE19
#20/07/2016
#171

def leap_year(y):
    if y%4:
        return False
    if y%100:
        return True
    if y%400:
        return False
    return True
m_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


#Ne marche que pour une date ultérieure au 07/01/1900
def is_sunday(day,month,year):
    d_r=7
    m_r=1
    y_r=1900
    m_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m_num_ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    d_num=0
    if y_r <= year:
        for y in range(y_r, year):
           d_num+=365 + int(leap_year(y))
           
        l_y=leap_year(year)

        if not l_y:
            d_num+=sum(m_num[m_r - 1: month - 1])
        if l_y:
            d_num+=sum(m_num_ly[m_r - 1: month - 1])

        d_num+=day-d_r

        return d_num%7 == 0

def counting_sundays():
    r=0
    for a in range(1901, 2001):
        for m in range(1,13):
            r+= int(is_sunday(1,m,a))
    return r
