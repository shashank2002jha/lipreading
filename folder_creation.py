import os

path = 'C:\\Users\\s27jh\\OneDrive\\Desktop'
os.chdir(path)
# n = input("Enter name of your folder : ")
os.mkdir("Frame Sequence")

# os.chdir(n)
os.chdir("Frame Sequence")
path_new = os.getcwd()
# path_new = 'C:\\Users\\s27jh\\OneDrive\\Desktop\\n'
# os.makedirs("Subject/Verb/Object/Silence")
# speaker = ['Speaker1', 'Speaker2', 'Speaker3']
list = ['Subject', 'Verb', 'Object', 'Silence']
  
for items in list:
    os.mkdir(items)
  
os.chdir(path + "\\Frame Sequence" +"\\Subject")
path_new = os.getcwd()
# print(os.path.exists("path"))
Subject = ['moi', 'aji', 'xi', 'tai', 'teu', 'tumi', 'xihote', 'kali', 'ami', 'kaile', 'mekuri', 'deuta', 'dada','maae', 'bhonti','hah','mur','bandore']


for i in Subject:
    os.mkdir(i)
    sub_dir = path_new + "/" + i
    for i in range(1,4):
         speaker_name = "Speaker_" + str(i)
         os.mkdir(os.path.join(sub_dir, speaker_name))


os.chdir(path + "\\Frame Sequence" + "\\Object")
path_new = os.getcwd()
object = ['furibo', 'mondirot', 'khelibo','gari','bahi', 'bozar', 'ghorole','gan', 'kot','bahirot','porikha','school', 'ratipua', 'zuta', 'kitap', 'kamtu', 'gosot', 'dukan', 'ki',  'khana', 'khabo', 'puza','dorob','boroxun', 'ketia','kapur', 'mas', 'rod', 'sah', 'potharole', 'xui', 'kolom', 'gakhir', 'sobi', 'relot', 'suli', 'panit', 'tv', 'kotha', 'nasibo', 'kali', 'bhat', 'bhuk', 'bike', 'khirki', 'football', 'jailot', 'call' , 'sobji', 'kheli', 'tuponi' ,'golaghatot','thanda','sosma', 'dukant','gamusa','rasana','duporia', 'hindi','mangxo','bohut','bidyaleye','sakori','ghorot', 'kobita', 'aam', 'mithai', 'ruti','ketiya', 'cricket', 'gorom', 'muk', 'borokhun', 'phuribo', 'chess', 'godhuli']
# print(len(subject))


for i in object:
    os.mkdir(i)
    sub_dir = path_new + "/" + i
    for i in range(1,4):
         speaker_name = "Speaker_" + str(i)
         os.mkdir(os.path.join(sub_dir, speaker_name))

os.chdir(path + "\\Frame Sequence" + "\\Verb")
path_new = os.getcwd()n

verb = ['khalu', 'zabo', 'nazai', 'ase', 'zau', 'kinilu', 'goise', 'bonaisu', 'kinisu', 'zam', 'kinile', 'golu', 'dise', 'goisilu', 'bozai', 'asu', 'gai', 'gol', 'nazau', 'thakiba', 'kinise', 'solau', 'khele', 'khula', 'bondho', 'goisa', 'disile','korile', 'porise', 'zai', 'uthisilu', 'nogole', 'matisile', 'paisilu', 'saisilu', 'porhe', 'porhu', 'khaisu', 'likhisu', 'khale', 'gaisile','solai', 'khelu', 'asile', 'porhisu', 'zanu', 'zane', 'lagise', 'dekhila', 'gaise', 'sorise', 'kinim', 'uthise', 'korisilu', 'korisile', 'uthisu', 'goisila', 'goisile', 'kotalu', 'bozau', 'thaku', 'aku', 'goisu', 'aake', 'korilu','korila', 'korise', 'gorom', 'jane', 'ahim', 'ahiba', 'ahibo', 'ahilu', 'bhagise', 'patisile']
# print(len(verb))
for i in verb:
    os.mkdir(i)
    sub_dir = path_new + "/" + i
    for i in range(1,4):
         speaker_name = "Speaker_" + str(i)
         os.mkdir(os.path.join(sub_dir, speaker_name))

os.chdir(path + "\\Frame Sequence" + "\\Silence")
silence = ['Start_Sil', 'End_Sil', 'Sil']
for i in silence:
    os.mkdir(i)



