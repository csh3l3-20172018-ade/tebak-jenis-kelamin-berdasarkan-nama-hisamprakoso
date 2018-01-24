
# coding: utf-8

# In[140]:


nama = input("Siapakah nama anda : ") #merupakan nama lengkap yang akan diinputkan
print(nama)
huruf=nama.split(" ") #memisahkan setiap kata dengan parameternya
huruf=huruf[0]
cow=0
cew=0
a=0
i=0
u=0
e=0
t=0
l=0

for mulai in huruf: 
 if mulai=='b' or mulai== 'B': #jika terdapat huruf b/B maka huruf akan di simpan kedalam variabel b
     b+=1
     cow+=1
 elif mulai=='d' or mulai== 'D': #jika terdapat huruf d/D maka huruf akan di simpan kedalam variabel d
     d+=1
     cow+=1
 elif mulai=='o' or mulai== 'O': #jika terdapat huruf o/O maka huruf akan di simpan kedalam variabel o
     o+=1
     cow+=1
for mulai1 in huruf:
 if mulai1=='i' or mulai1== 'I': #jika terdapat huruf i/I maka huruf akan di simpan kedalam variabel i
     i+=1
     cew+=1
 elif mulai1=='a' or mulai1== 'A': #jika terdapat huruf a/A maka huruf akan di simpan kedalam variabel a
     a+=1
     cew+=1
 elif mulai1=='u' or mulai1== 'U': #jika terdapat huruf u/U maka huruf akan di simpan kedalam variabel u
     u+=1
     cew+=1
 elif mulai1=='e' or mulai1== 'E': #jika terdapat huruf e/E maka huruf akan di simpan kedalam variabel e
     e+=1
     cew+=1
 elif mulai1=='t' or mulai1== 'T': #jika terdapat huruf t/T maka huruf akan di simpan kedalam variabel t
     t+=1
     cew+=1
 elif mulai1=='l' or mulai1== 'L': #jika terdapat huruf l/L maka huruf akan di simpan kedalam variabel l
     l+=1
     cew+=1
if(cew>cow): #kondisi apabila jumlah perempuan lebih banyak daripada laki-laki maka akan muncul keterangan "jens kelamin perempuan" 
    print("jenis kelamin perempuan")
elif(cow>cew): #kondisi apabila jumlah laki-laki lebih banyak daripada perempuan maka akan muncul keterangan "jens kelamin laki-laki"
    print("jenis kelamin laki-laki")
else : print("jenis kelamin tidak cocok") #kondisi apabila selain yang sudah di tentukan maka akan muncul keterangan "jens kelamin tidak cocok"
    

