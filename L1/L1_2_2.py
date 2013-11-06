import os
import struct
import time
const = 0

def dalinti ( kaire, desine, f):
    global const
    t = indeksas = kaire
    var_kaire = imti_list(f, kaire)
    const += 2
    for j in xrange( kaire + 4, desine + 4, 4):
        var_j = imti_list(f, j)
        const += 1
        if var_j < var_kaire:
            indeksas += 4
            sukeisti_list(f, indeksas, j)
            const += 2
    sukeisti_list(f, kaire, indeksas)
    const += 1
    return indeksas

def rusiuoti( kaire, desine, failas):
    global const
    if kaire < desine :
        indeksas = dalinti( kaire, desine, failas)
        rusiuoti(kaire, indeksas-4, failas)
        rusiuoti(indeksas+4, desine, failas)
        const += 3

def rik(failo_pav):
    global const
    f = open(failo_pav, 'r+b')
    length = os.path.getsize(failo_pav)
    #failo_isvedimas_list(f)
    time1 = time.time()
    rusiuoti (0, length-4 ,f)
    time2 = time.time()
    skirtumas = time2 - time1
    print "-----ISRIKIUOTAS-----"
    #failo_isvedimas_list(f)
    print "Bendras uztruktas laikas sekundemis: %(time)s" %{'time': skirtumas}
    const += 10
    print "Eiluciu kiekis: %(const)s" %{'const': const}
    
def script():
    global const
    for x in xrange(1, 15):
        const = 0
        file_name = "T%(test)s" %{'test': x}
        print file_name
        rik(file_name)
    
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