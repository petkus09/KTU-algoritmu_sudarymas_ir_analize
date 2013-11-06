import os
import struct
import time

const = 0;

def rusiuoti(f, w, offset):
    global const
    if offset[0] == offset[1]:
        const += 1
        return offset
    if offset[0] + 1 == offset[1]:
        of1_f = of1_t = offset[0]
        of2_f = of2_t = offset[1]
        const += 2
    else:
        of1_f = offset[0]
        of1_t = (offset[0] + offset[1]) / 2
        const += 2
        if of1_t + 1 > offset[1]:
            of2_f = offset[1]
            const += 1
        else:
            of2_f = of1_t + 1
            const += 1
        of2_t = offset[1]
        const += 1
    return sujungti(f, w, rusiuoti(f, w, [of1_f, of1_t]), rusiuoti(f, w, [of2_f, of2_t]))

def sujungti(f, w, left, right):
    global const
    test_list = []
    begin = left[0]
    i = j = 0
    const += 3
    while i < (left[1] - left[0] + 1) and j < (right[1] - right[0] + 1):
        var_i = imti(f, (left[0]*4)+i*4)
        var_j = imti(f, (right[0]*4)+j*4)
        const += 2
        if var_i < var_j:
            var_bin = imti_b(f, (left[0]*4)+i*4)
            deti(w, begin*4, var_bin)
            begin += 1
            i += 1
            const += 4
        else:
            var_bin = imti_b(f, (right[0]*4)+j*4)
            deti(w, begin*4, var_bin)
            begin += 1
            j += 1
            const += 4
    for tt in xrange(left[0] + i, left[1] + 1):
        var = imti_b(f, tt*4)
        deti(w, begin*4, var)
        begin += 1
        const += 3
    for tt in xrange(right[0] + j, right[1] + 1):
        var = imti_b(f, tt*4)
        deti(w, begin*4, var)
        begin += 1
        const += 3
    for tt in xrange(left[0], right[1] + 1):
        var = imti_b(w, tt*4)
        deti(f, tt*4, var)
        const += 2
    return [left[0], right[1]]

def rik(failo_pav, rez_failo_pav="Laikinas"):
    global const
    f = open(failo_pav, 'r+b')
    open(rez_failo_pav, 'w').close()
    w = open(rez_failo_pav, 'r+b')
    w.truncate()
    length = os.path.getsize(failo_pav)
    #failo_isvedimas(f, length)
    time1 = time.time()
    rusiuoti(f, w, [0, length/4 - 1])
    time2 = time.time()
    print "-----ISRIKIUOTAS-----"
    skirtumas = time2 - time1
    #failo_isvedimas(f, length)
    print "Bendras uztruktas laikas sekundemis: %(time)s" %{'time': skirtumas}
    const += 13
    print "Eiluciu kiekis: %(const)s" %{'const': const}
    
def script():
    global const
    for x in xrange(1, 15):
        const = 0
        file_name = "T%(test)s" %{'test': x}
        print file_name
        rik(file_name)
    
def imti(f, i):
    global const
    f.seek(i)
    var = struct.unpack('i', f.read(4))[0]
    const += 2
    return var

def imti_b(f, i):
    global const
    f.seek(i)
    var = f.read(4)
    const += 2
    return var

def deti(f, i, r):
    global const
    f.seek(i)
    f.write(r)
    const += 2
    
def failo_isvedimas(f, length):
    global const
    for j in xrange(0, length, 4):
        print imti(f, j)
        const += 1