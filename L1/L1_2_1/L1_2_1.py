import os
import struct
import time
const = 0

def dalinti ( kaire, desine, f):
    global const
    t = indeksas = kaire
    var_kaire = imti(f, kaire)
    const += 2
    for j in xrange( kaire + 4, desine + 4, 4):
        var_j = imti(f, j)
        const += 1
        if var_j < var_kaire:
            indeksas += 4
            sukeisti(f, indeksas, j)
            const += 2
    sukeisti(f, kaire, indeksas)
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
    #failo_isvedimas(f, length)
    time1 = time.time()
    rusiuoti (0, length-4 ,f)
    time2 = time.time()
    skirtumas = time2 - time1
    #print "-----ISRIKIUOTAS-----"
    #failo_isvedimas(f, length)
    print "Bendras uztruktas laikas sekundemis: %(time)s" %{'time': skirtumas}
    const += 10
    print "Eiluciu kiekis: %(const)s" %{'const': const}
    
def script(parent):
    global const
    for x in xrange(1, 18):
        const = 0
        file_name = "T%(test)s" %{'test': x}
        print file_name
        rik(parent+file_name)
    
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