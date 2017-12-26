# Graphical assessment of a child's development 
# according to the World Health Organization growth standards 

# Repository & documentation:
# http://github.com/dqsis/child-growth-charts
# -------------------------------------

# Import libraries
import os
from sys import exit
#import library 3rd numpy dan matplotlib pastikan install dulu
import numpy as np
import matplotlib.pyplot as plt


# I/O files path
path = 'data/'

# Read child's data (user input)
chdata = 'child_data.csv'

# Gender (male or female)
childfile = open(os.path.join(path,chdata))
genderline = childfile.readline()

# Age, weight, height, head circumference
charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=2)

# ---
# Not required! Missing data ignored by plotting! 
# Remove rows with missing data | code snippet source: http://bit.ly/ZLKBCA 
# charray = charray[~np.isnan(charray).any(axis=1)]
# ---

if genderline[7] == 'f':
    # read girls' (0-2) WHO charts
    # Read age vs weight WHO data
    awdata = 'g_age_weight.csv'
    awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
    # Read age vs length WHO data
    aldata = 'g_age_length.csv'
    alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
    # Read age vs head circumference WHO data
    ahdata = 'g_age_headc.csv'
    aharray = np.loadtxt(os.path.join(path,ahdata), delimiter=',', skiprows=1)
    # Read lenght vs weight WHO data
    lwdata = 'g_length_weight.csv'
    lwarray = np.loadtxt(os.path.join(path,lwdata), delimiter=',', skiprows=1)
else:
    print('no data available for boys yet')
    exit()

############################ BANTUAN SAJA : BACA ##################
# COBA PRINT DULU SALAH SATU ARRAY DATANYA : print awarray 
print "==================== SEKILAS NUMPY NDARRAY DAN MATRIX ====================================== "
print "*) Ada 2 Jenis format yaitu : 1. Array/N-Dimensional Array (ndarray)"
print "                              2. numpy Matrix" 
print "*) Format keduanya pada dasarnya adalah array[] semua index dimulai dari 0."
print "*) Tetapi sedikit berbeda dengan array biasa (tampilan antar [] tidak ada koma, lihat contoh dibawah!)"
print "*) Format tampilan Keduanya Saat di print SAMA."
print "*) numpy Matrix adalah turunan dari ndArray sehingga cara aksesnya di keduanya sama."
print "*) Kalau perbedaan format 1 dan 2, pada objek numpy matrix bisa dilakukan proses2x OPERASI MATRIX,"
print "   Misalnya perkalian, inverse, Transpose, dsb. Sedangkan ndarray tidak bisa (KECUALI di python versi 3.5 ke atas !!!)"
print "   https://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u \n"
print "====================== ARRAY BIASA ========================================================= "
print "BERIKUT ini adalah FORMAT TAMPILAN Array 2 Dimensi biasa (Bukan dari Numpy) :" 
array_biasa = [[1,2,3,4] , [5,6,7,8]]
print array_biasa
print "CARA AKSES : Kalau mau akses item dengan nilai 2  maka caranya array_biasa[0][1] : "
print array_biasa[0][1]
print "============================================================================================ "

print "====================== NDARRAY DAN NUMPY MATRIX ============================================ "
print "Sedangkan Dalam script ini menggunakan np.loadtxt yang akan mengembalikan format ndArray berikut adalah FORMAT TAMPILAN hasil print dr awarray : "
print "Ini data Age vs Weight yang di load dalam menggunakan library numpy dalam format numpy :"
print awarray
print "\n CARA AKSES : Ada 2 Cara yaitu POSISI ITEM menggunakan method item.(Baris,Kolom) => awarray.item( (2,3) ) = \n"
print awarray.item( (2,3) )
print "\n Atau , dengan INDEX ITEM dimana indeks item ke- 0 dimulai dari kiri atas sampai ke kanan bawah adalah index item ke-n (terakhir)"
print "Misal ndarray/matriks: awarray [B x K] = [24 x 10] , maka utk item ke 11 dari ndarray/matriks trsbt = 3.1611 (lihat hasil print awarray diatas!) = \n" 
print awarray.item(11)
print "============================================================================================ "

####################################################
# Plots
plt.figure()
# Age vs weight

# array[:,0] ==> (Month) slicing semua data ditiap baris di kolom index ke 0 
# array[:,1] ==> slicing semua data ditiap baris di kolom index ke 1 

# plt.plot(x,y,[kode_utk_nampilin_jenis_point_di_matlab_ex: r, r--, bo, k-, dll.])
plt.subplot(2,2,1)
plt.plot(\
awarray[:,0],awarray[:,1],'r',\
awarray[:,0],awarray[:,2],'r--',\
awarray[:,0],awarray[:,3],'r--',\
awarray[:,0],awarray[:,4],'r--',\
awarray[:,0],awarray[:,5],'k-',\
awarray[:,0],awarray[:,6],'r--',\
awarray[:,0],awarray[:,7],'r--',\
awarray[:,0],awarray[:,8],'r--',\
awarray[:,0],awarray[:,9],'r--',\
charray[:,0],charray[:,1],'bo')

plt.grid(True)
# set label untuk axis (horizontal X)
plt.xlabel('age [months]')
# set label untuk axis (Vertikal Y)
plt.ylabel('weight [kg]')
# set limit lebar satuan axis X sampai 24 satuan (Month)
plt.xlim([0,24])
# set garis selisish jarak yang ditampilkan pada chart = 3 
plt.xticks(np.arange(0,25,3)) 

#Menambahkan point (tulisan) pada plot
plt.text(awarray[13,0], awarray[13,1],'2%',fontsize=6)
plt.text(awarray[14,0], awarray[14,2],'5%',fontsize=6)
plt.text(awarray[15,0], awarray[15,3],'10%',fontsize=6)
plt.text(awarray[16,0], awarray[16,4],'25%',fontsize=6)
plt.text(awarray[17,0], awarray[17,5],'50%',fontsize=6)
plt.text(awarray[18,0], awarray[18,6],'75%',fontsize=6)
plt.text(awarray[19,0], awarray[19,7],'90%',fontsize=6)
plt.text(awarray[20,0], awarray[20,8],'95%',fontsize=6)
plt.text(awarray[21,0], awarray[21,9],'98%',fontsize=6)


# Age vs length
plt.subplot(2,2,2)
plt.plot(\
alarray[:,0],alarray[:,1],'r--',\
alarray[:,0],alarray[:,2],'r--',\
alarray[:,0],alarray[:,3],'r--',\
alarray[:,0],alarray[:,4],'r--',\
alarray[:,0],alarray[:,5],'k-',\
alarray[:,0],alarray[:,6],'r--',\
alarray[:,0],alarray[:,7],'r--',\
alarray[:,0],alarray[:,8],'r--',\
alarray[:,0],alarray[:,9],'r--',\
charray[:,0],charray[:,2],'bo')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('length [cm]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3))


# Age vs head circumference
plt.subplot(2,2,3)
plt.plot(\
aharray[:,0],aharray[:,1],'r--',\
aharray[:,0],aharray[:,2],'r--',\
aharray[:,0],aharray[:,3],'r--',\
aharray[:,0],aharray[:,4],'r--',\
aharray[:,0],aharray[:,5],'k-',\
aharray[:,0],aharray[:,6],'r--',\
aharray[:,0],aharray[:,7],'r--',\
aharray[:,0],aharray[:,8],'r--',\
aharray[:,0],aharray[:,9],'r--',\
charray[:,0],charray[:,3],'bo')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('head circumference [cm]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3)) 


# Length vs weight
plt.subplot(2,2,4)
plt.plot(\
lwarray[:,0],lwarray[:,1],'r--',\
lwarray[:,0],lwarray[:,2],'r--',\
lwarray[:,0],lwarray[:,3],'r--',\
lwarray[:,0],lwarray[:,4],'r--',\
lwarray[:,0],lwarray[:,5],'k-',\
lwarray[:,0],lwarray[:,6],'r--',\
lwarray[:,0],lwarray[:,7],'r--',\
lwarray[:,0],lwarray[:,8],'r--',\
lwarray[:,0],lwarray[:,9],'r--',\
charray[:,2],charray[:,1],'bo')

plt.grid(True)
plt.xlabel('lenght [cm]')
plt.ylabel('weight [kg]')
plt.xlim([45,110])
plt.xticks(np.arange(45,111,10)) 

# Adjust distance between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Show & save graphs
#plt.show()

plt.savefig(os.path.join(path,'growth.pdf'))
plt.savefig(os.path.join(path,'growth.png'))

# END +++
