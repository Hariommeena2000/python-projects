st=[]
class students:
    def __init__(self,name,rollno,marks1,marks2):
        self.Name=name
        self.Rollno=rollno
        self.Marks1=marks1
        self.Marks2=marks2
a=students("Hari","39",56,87)
st.append(a)
b=students("om","56",67,34)
st.append(b)
c=students("raksha","45",45,34)
st.append(c)
def addstudent():
    N=input("name")
    R=input("rolll")
    M1=input("m1")
    M2=input("m2")
    new=students(N,R,M1,M2)
    st.append(new)

def display():
    print("Name\t\t\tRollNo\t\t\tMarks1\t\t\tMarks2\n")
    for i in st:
        print(i.Name,i.Rollno,i.Marks1,i.Marks2,sep="\t\t\t")
        
def search():
    roll=input("enter roll no to delete student")
    for i in st:
        if i.Rollno==roll:
            print("Name\t\t\tRollNo\t\t\tMarks1\t\t\tMarks2\n")
            print(i.Name,i.Rollno,i.Marks1,i.Marks2,sep="\t\t\t")
            break
    else:
        print("please enter valid roll no")
            
def delete():
    roll=input("enter roll no to delete student")
    for i in st:
        if i.Rollno==roll:
            st.remove(i)
            break
    else:
        print("please enter valid roll no")
        
def update():
    roll=input("please enter the rollno to updat details")
    for i in st:
        if i.Rollno==roll:
            i.Name=input("New name")
            i.Marks1=input("Updated Marks1")
            i.Marks2=input("Updated Marks2")
            break
    else:
        print("Please enter valid roll no")


# In[ ]:




