import os
import struct
import time
const = 0
        
def bucketSort(f, length, bucket_files, result_length):
    global const
    for j in xrange(0, length, 4):
        variable = imti(f, j)
        range = variable / 1000000000
        const += 2
        if bucket_files.has_key(range):
            sort_insertion(bucket_files[range], result_length[range], imti(f, j), imti_b(f, j))
            result_length[range] += 4
            const += 2
    pos = 0
    dict_list = sorted(bucket_files)
    const += 2
    for i in xrange(0, len(dict_list)):
        for j in xrange(0, result_length[dict_list[i]], 4):
            val = imti_b(bucket_files[dict_list[i]], j)
            deti(f, pos, val)
            pos += 4
            const += 3

def rik(failo_pav, rez_failo_pav="Bucket"):
    global const
    f = open(failo_pav, 'r+b')
    bucket_files = {}
    result_length = {}  
    for i in xrange(-10, 10):
        open(rez_failo_pav+"_"+str(i), 'w').close()
        w = open(rez_failo_pav+"_"+str(i), 'r+b')
        w.truncate()
        new_category = {i: w}
        new_length = {i: 0}
        bucket_files.update(new_category)
        result_length.update(new_length)
        const += 7
    length = os.path.getsize(failo_pav)
    #failo_isvedimas(f, length)
    time1 = time.time()
    bucketSort(f, length, bucket_files, result_length)
    time2 = time.time()
    skirtumas = time2 - time1
    print "-----ISRIKIUOTAS-----"
    #failo_isvedimas(f, length)
    print "Bendras uztruktas laikas sekundemis: %(time)s" %{'time': skirtumas}
    const += 12
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