import csv
import json
inp=int(input("ENter the no.of semester to calculate CGPA:"))
p=[]

print(f"Enter the {inp} semester grade sheet as semester.csv format and enter it one by one:")
for _ in range(inp):
    p.append(input())
total=[]
sum2=0
arrear=[]



with open("results.txt", "r+") as f:
    f.seek(0)
    f.truncate()
def calculator(total,arrear):
    grade=[]
    credit=[]
    subjects=[]
    global ran
    global sum2
    global data
    filename=p[ran].lower()
    try:

        with open(filename,'r',newline= '') as f:
            reader=csv.DictReader(f)
            for row in reader:
                subjects.append(row['COURSE_NAME'])
                grade.append(row['GRADE'])
                credit.append(float(row['CREDITS']))
            #To update the arrear list
            for i in range(len(arrear)):
                for j in range(len(subjects)):
                    if(len(arrear)>0):
                        if(arrear[i]==subjects[j] and grade[j]!="U"):
                                arrear.pop(i)
                    else:
                        break
        
            for i in range(len(grade)):
                if(grade[i]=="O"):
                    grade[i]=10
                elif(grade[i]=="A+"):
                    grade[i]=9
                elif(grade[i]=="A"):
                    grade[i]=8
                elif(grade[i]=="B+"):
                    grade[i]=7
                elif(grade[i]=="B"):
                    grade[i]=6
                elif(grade[i]=="C"):
                    grade[i]=5
                elif(grade[i]== "U" or grade[i]=="RA" or grade[i]=="SA" or grade[i]== "w"):
                    if subjects[i] not in arrear:
                        arrear.append(subjects[i])
                    grade[i]=0
                    credit[i]=0
                else:
                    print("INVALID GRADE")
                    break;
            c=sum(credit)
            total.append(c)
            gra=[float(i) for i in grade]
            sum1=0
            
        
            for i in range(len(credit)):
                    
                if(len(credit)==len(gra)):
                    result=credit[i]*gra[i]
                    sum1+=result
                    sum2+=result
            g=round((sum1/c),2)
            if(len(total)!=0):
                t=round((sum2/sum(total)),2)
            if(len(arrear)==0):
                arrear="NULL"
            data={}
            product=filename[:-4]
            data[product]=[]
            data[product].append({
                'GPA':g,
                'CGPA':t,
                'Current arrears':arrear
            })
            
            with open ('results.txt','a') as files:
                json.dump(data,files,indent=2)
            
    except FileNotFoundError:
        print(f"No such file {filename} present in this folder")
    except Exception as e:
        print("The error is: ",e)
        

ran=0
while inp!=0:
    calculator(total,arrear)
    ran+=1
    inp-=1


with open('results.txt','r') as files:
    content=files.read()
print(content)
