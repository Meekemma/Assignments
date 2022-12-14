import re

#Extration of baby name from file using regex

with open('baby2008_2.html', 'r') as f:
    content = f.read()
    i = re.sub(r'<.*?>', ' ', content)
    
    #drafting out a pattern 
    names = re.compile(r'\s*[1-9]+\s*([A-Z][a-z]+)\s*([A-Z][a-z]+)')
    names = names.findall(i)
    baby_names = []
    #itrating through the name  to get baby_names
    for i in range(len(names)):
        if i == 0:
            continue
        else:
            male = names[i][0]
            female = names[i][1]
            baby_names.append(male)
            baby_names.append(female) 
            baby_names.sort()
            
#printing out babynames            
print("\n3) Baby Names:", baby_names)