# -*-coding: utf-8 -*-

# Q1
data1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {2, 4, 6, 8, 10}
odd = data1 - even
print('Q1:', odd)

# Q2
data2 = ('moda', ('走', '了'), ('買', '肥宅', '歡樂水'))
data = list(data2)
a = 0
while a < len(data):
    a +=1
    try:
        index = data[a].index('歡樂水')
        print('Q2:', index, data[2][2])
    except:
        pass

# Q3
data3 = {39, 12, 61, 10, 3, 99, 78, 87, 93, 11, 666, 999}
data3 = list(data3)
print('Q3-1:', sum(data3))

sorted_data3 = sorted(data3)
print('Q3-2: data3_max:', sorted_data3[-1], ',', 'data3_min:', sorted_data3[0])

data3.sort(reverse=True)
print('Q3-3: data3_desc:', sorted_data3, ',', 'data3_asc:', data3)

# Q4
data4 = ['moda', '走', '了', '~', '買', '肥宅', '歡樂水']
data = data4.copy()
data[0] = '米血'
joined = ''.join(data)
print('Q4-1:', joined)

joined2 = ''.join(data4)
a = joined2[::-1]
print('Q4-2:', a)
