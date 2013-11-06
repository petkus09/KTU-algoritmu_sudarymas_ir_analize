import os
import struct

#------------------------------------------------------
def pereiti(f, j):
    global const
    i = f.tell()
    const += 1
    if i < j:
        for x in xrange(i+4, j+4, 4):
            f.seek(x)
            const += 1
    if i > j:
        for x in xrange(i-4, j-4, -4):
            f.seek(x)
            const += 1
    if i == j:
        pass
    const += 1
        
def imti_list(f, j):
    global const
    pereiti(f, j)
    val = f.read(4)
    const += 2
    if val == '':
        const += 1
        return ''
    else:
        const += 1
        return struct.unpack('i', val)[0]

def imti_list_b(f, j):
    global const
    pereiti(f, j)
    const += 2
    return f.read(4)

def deti_list(f, j, r):
    global const
    pereiti(f, j)
    f.write(r)
    const += 2
    
def failo_isvedimas_list(f):
    global const
    value = 0
    f.seek(0)
    offset = 0
    const += 3
    while value != '':
        value = imti_list(f, offset)
        const += 1
        if value == '':
            const += 1
            break
        print (value)
        offset += 4
        const += 2
        
def sukeisti_list(f, i, j):
    global const
    var_a = imti_list_b(f, i)
    var_b = imti_list_b(f, j)
    deti_list(f, i, var_b)
    deti_list(f, j, var_a)
    const += 4
#------------------------------------------------------
def imti(f, i):
    global const
    f.seek(i)
    var = struct.unpack('i', f.read(4))[0]
    const += 3
    return var

def imti_b(f, i):
    global const
    f.seek(i)
    var = f.read(4)
    const += 3
    return var

def deti(f, i, r):
    global const
    f.seek(i)
    f.write(r)
    const += 2
    
def sukeisti(f, i, j):
    global const
    f.seek(i)
    var_a = f.read(4)
    f.seek(j)
    var_b = f.read(4)
    f.seek(i)
    f.write(var_b)
    f.seek(j)
    f.write(var_a)
    const += 8
    
def failo_isvedimas(f, length):
    global const
    for j in xrange(0, length, 4):
        print imti(f, j)
        const += 1
        
def sort_insertion(f, length, value, value_b):
    global const
    if length == 0:
        deti(f, 0, value_b)
        const += 1
    else:
        j = 0
        const += 1
        while j < length and imti(f, j) < value:
            j += 4
            const += 1
        value_to_write = value_b
        value_to_take = imti_b(f, j)
        const += 2
        for x in xrange(j, length + 4, 4):
            deti(f, x, value_to_write)
            value_to_write = value_to_take
            const += 2
            try:
                value_to_take = imti_b(f, x+4)
                const += 1
            except:
                const += 1
                pass
            