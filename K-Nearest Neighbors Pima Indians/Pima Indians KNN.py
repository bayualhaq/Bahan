import math
import pandas as pd
import matplotlib.pyplot as plt

#memasukkan file csv dari excel ke python
dataset = pd.read_csv('PimaIndians1.csv')

col_pre = dataset.iloc[:, 0].values #mengambil kolom 1 dari excel (pregnant)
col_glu = dataset.iloc[:, 1].values #mengambil kolom 2 dari excel (glucose)
col_dias = dataset.iloc[:, 2].values #mengambil kolom 3 dari excel (diastilic)
col_tri = dataset.iloc[:, 3].values #mengambil kolom 4 dari excel (triceps)
col_ins = dataset.iloc[:, 4].values #mengambil kolom 5 dari excel (insulin)
col_ins = dataset.iloc[:, 5].values #mengambil kolom 6 dari excel (bmi)
col_bmi = dataset.iloc[:, 6].values #mengambil kolom 7 dari excel (diabetes)
col_glu = dataset.iloc[:, 7].values #mengambil kolom 8 dari excel (age)
col_test = dataset.iloc[:, 8].values #mengambil kolom 9 dari excel (test)

knn=int(input("Masukkan Nilai K = "))

pre=[]
glu= []
dias= []
tri= []
ins= []
bmi= []
diab= []
age= []
test= []

pre_dt=[]
glu_dt= []
dias_dt= []
tri_dt= []
ins_dt= []
bmi_dt= []
diab_dt= []
age_dt= []
test_dt= []

Hasil=[]
benar=[]
data=[]
accuracy=[]
knn_graf=[]

#fungsi mengambil data train yang mempunyai nilai class 0 dengan nama masuk_data_train_0
def masuk_data_train_0 (data,masuk):
    a=0
    for i in range (len (data)):
        if (col_test[i] ==0 and a<26):
            masuk.append(data[i])
            a=a+1

#fungsi mengambil data train yang mempunyai nilai class 1 dengan nama masuk_data_train_1
def masuk_data_train_1 (data,masuk):
    a=0
    for i in range (len (data)):
        if (col_test[i] == 1 and a<13):
            masuk.append(data[i])
            a=a+1

#fungsi mengambil data tes yang mempunyai nilai class 0 dengan nama masuk_data_test_0        
def masuk_data_test_0 (data,masuk):
    a=0
    for i in range (len (data)):
        if (col_test[i] == 0):
            a+=1
            if(a>26):
                masuk.append(data[i])

#fungsi mengambil data tes yang mempunyai nilai class 1 dengan nama masuk_data_test_1      
def masuk_data_test_1 (data,masuk):
    a=0
    for i in range (len (data)):
        if (col_test[i] == 1):
            a+=1
            if(a>13):
                masuk.append(data[i])

#fungsi mengambil data dari beberapa variable data train, data tes, knn, dan menampilkan hasil
def pcx(data1,data2,data3,data4,data5,data6,data7,data8,data9,
        dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9,
        k,out):
    #membuat perulangan untuk menghitung jarak dari data asli dengan data tes 
    for i in range(len(dt1)):
        dist1=[]
        test=[]
        coba=0
        for a in range(len(data1)):
           dist = math.sqrt( 
                         ((data1[a] - dt1[i])**2) +
                         ((data2[a] - dt2[i])**2) + 
                         ((data3[a] - dt3[i])**2) +
                         ((data4[a] - dt4[i])**2) +
                         ((data5[a] - dt5[i])**2) + 
                         ((data6[a] - dt6[i])**2) +
                         ((data7[a] - dt7[i])**2) +
                         ((data8[a] - dt8[i])**2))
           
           dist1.append(dist) 
        dist1,test  = zip(*sorted(zip(dist1,data9)))
        for z in range(k):
            if (test[z]==0) :
                coba+=1
                        
        if ((z/2)<=coba):
            a=0
            out.append(a)
        else :
            a=1
            out.append(a)
        del dist1
        del test
        coba=0
        
def hasil(data_asli,data_perbandingan,out,out2,out3):
    a=0
    for x in range(len(data_asli)):
        if (data_asli[x]==data_perbandingan[x]):
            a+=1
    out.append(a)
    out2.append(353)
    out3.append(a/353)


#memasukkan data train mempunyai nilai class 0  
masuk_data_train_0(col_pre,pre)
masuk_data_train_0(col_glu,glu)
masuk_data_train_0(col_dias,dias)
masuk_data_train_0(col_tri,tri)
masuk_data_train_0(col_ins,ins)
masuk_data_train_0(col_ins,bmi)
masuk_data_train_0(col_bmi,diab)
masuk_data_train_0(col_glu,age)
masuk_data_train_0(col_test,test)

#memasukkan data train mempunyai nilai class 1
masuk_data_train_1(col_pre,pre)
masuk_data_train_1(col_glu,glu)
masuk_data_train_1(col_dias,dias)
masuk_data_train_1(col_tri,tri)
masuk_data_train_1(col_ins,ins)
masuk_data_train_1(col_ins,bmi)
masuk_data_train_1(col_bmi,diab)
masuk_data_train_1(col_glu,age)
masuk_data_train_1(col_test,test)

#memasukkan data tes mempunyai nilai class 0
masuk_data_test_0(col_pre,pre_dt)
masuk_data_test_0(col_glu,glu_dt)
masuk_data_test_0(col_dias,dias_dt)
masuk_data_test_0(col_tri,tri_dt)
masuk_data_test_0(col_ins,ins_dt)
masuk_data_test_0(col_ins,bmi_dt)
masuk_data_test_0(col_bmi,diab_dt)
masuk_data_test_0(col_glu,age_dt)
masuk_data_test_0(col_test,test_dt)

#memasukkan data train mempunyai nilai class 1
masuk_data_test_1(col_pre,pre_dt)
masuk_data_test_1(col_glu,glu_dt)
masuk_data_test_1(col_dias,dias_dt)
masuk_data_test_1(col_tri,tri_dt)
masuk_data_test_1(col_ins,ins_dt)
masuk_data_test_1(col_ins,bmi_dt)
masuk_data_test_1(col_bmi,diab_dt)
masuk_data_test_1(col_glu,age_dt)
masuk_data_test_1(col_test,test_dt)

for knnn in range(knn-1):
    knnn+=2
    del Hasil
    Hasil=[]
    
    pcx(pre,glu,dias,tri,ins,bmi,diab,age,test,
        pre_dt,glu_dt,dias_dt,tri_dt,ins_dt,bmi_dt,diab_dt,age_dt,test_dt,
        knnn,Hasil)
        
    hasil(test_dt,Hasil,benar,data,accuracy)
        
    knn_graf.append(knnn)



df = pd.DataFrame({'knn':knn_graf,'databenar':benar, 'Jmldata':data, 'accuracy':accuracy})
df.plot(kind='line',x='knn',y='accuracy',color='blue')
print (df)

plt.show()