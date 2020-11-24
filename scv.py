import os

dir1 = "./food101/images/train/"
dir2 = "./food101/texts_txt/"
foodclass = os.listdir(dir1)
print(foodclass)
with open("trainfood.csv",'w') as f:
    for i in foodclass:
        images = os.path.join(dir1,i)
        for j in os.listdir(images):
            name=j.split('.')[0] + '.txt'          
            str1 = dir2 + i +'/'+ name + '|' + i + '|' + images +'/' + j + '\n'
            if name in os.listdir(os.path.join(dir2,i)):
                f.write(str1)
