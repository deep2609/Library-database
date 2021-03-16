from pickle import load,dump
import sys
import os
class books():
    def assignsno(self):
        f=open('sno.txt','a+')
        d=f.read()
        if f.tell()==0:
            f.write('0')
        else:
            pass
        f.close()
        f1=open('sno.txt','r')
        s=int(f1.read())
        self.sno=s
        s+=1
        f1.close
        f2=open('sno.txt','w')
        f2.write(str(s))
    def input (self):
        self.name=raw_input('Enter book name : ')
        while True: 
            self.issue=[input('Enter date : '),input("enter month number : "),input("enter year : ")]
            if self.issue[1] in [1,2,3,4,5,6,7,8,9,10,11,12] and 1<=self.issue[0]<=31:
                if (self.issue[2])%4==0:
                    
                    if self.issue[1]==2:
                        if 1<=self.issue[0]<=29:
                            print "Valid"
                            break
                        else:
                                print 'wrong input'
                    elif self.issue[1] in [1,3,5,7,8,10,12]:
                            if 1<=self.issue[0]<=31:
                                print "Valid"
                                break
                            else:
                                print 'wrong input'
                    elif self.issue[1] in [4,6,9,11]:
                            if 1<=self.issue[0]<=30:
                                print "Valid"
                                break
                            else:
                                print 'wrong input'
                
                elif (self.issue[2])%4!=0:
                    
                    if self.issue[1]==2:
                        if 1<=self.issue[0]<=28:
                            print "Valid"
                            break
                        else:
                            print 'wrong input'
                    elif self.issue[1] in [1,3,5,7,8,10,12]:
                            if 1<=self.issue[0]<=31:
                                print "Valid"
                                break
                            else:
                                print 'wrong input'
                    elif self.issue[1] in [4,6,9,11]:
                            if 1<=self.issue[0]<=30:
                                print "Valid"
                                break
                            else:
                                print 'wrong input'
                else:
                    print "wrong input"
            else:
                    print "Wrong date","....Enter Again"
        self.returndate=[0,0,0]
        if 1<=self.issue[0]<=21:
            self.returndate[0]=self.issue[0]+7
            self.returndate[1]=self.issue[1]
            self.returndate[2]=self.issue[2]
        elif self.issue[0]==22 and self.issue[2]%4==0 and self.issue[1]==2:
            self.returndate[0]=self.issue[0]+7
            self.returndate[1]=self.issue[1]
            self.returndate[2]=self.issue[2]
        elif self.issue[0]==[25,26,27,28,29,24,23] and (self.issue[2]%4==0 and self.issue[1]==2):
            self.returndate[0]=self.issue[0]+7-29
            self.returndate[1]=self.issue[1]+1
            self.returndate[2]=self.issue[2]
        elif self.issue[0] in [22,23,24,25,26,27,28] and self.issue[1]==2:
            self.returndate[0]=self.issue[0]+7-28
            self.returndate[1]=self.issue[1]+1
            self.returndate[2]=self.issue[2]
            
        elif self.issue[0]==23 and self.issue[1]!=2:
            self.returndate[0]=self.issue[0]+7
            self.returndate[1]=self.issue[1]
            self.returndate[2]=self.issue[2]
        elif self.issue[0]==24 and self.issue[1]not in (2,4,6,9,11,12):
            self.returndate[0]=self.issue[0]+7
            self.returndate[1]=self.issue[1]
            self.returndate[2]=self.issue[2]
        elif self.issue[0] in (24,25,26,27,28,29,30) and self.issue[1]not in (2,1,3,5,7,8,10,12):
            self.returndate[0]=self.issue[0]+7-30
            self.returndate[1]=self.issue[1]+1
            self.returndate[2]=self.issue[2]
        elif self.issue[0] in(25,26,27,28,29,30,31) and self.issue[1] not in (2,4,6,9,11,12):
            self.returndate[0]=self.issue[0]+7-31
            self.returndate[1]=self.issue[1]+1
            self.returndate[2]=self.issue[2]
        elif self.issue[0] in (25,26,27,28,29,30,31) and self.issue[1]==12:
            self.returndate[0]=self.issue[0]+7-31
            self.returndate[1]=self.issue[0]-12+1
            self.returndate[2]=self.issue[2]+1
        self.issuername=raw_input('enter name of issuer')
        self.assignsno()
        
        
    def disp (self):
        return self.sno,self.name,self.issue,self.returndate,self.issuername
def create(fname):
    s1=books()
    f=open(fname,'wb')
    choice='y'
    while choice=='y':
        print 'Enter details'
        s1.input()
        dump (s1,f)
        choice=raw_input('Want to enter y or n')
        if choice.lower()=='n':
            break
    f.close()

def append(fname):
    s1=books()
    f=open(fname,'ab')
    choice='y'
    
    while choice=='y':
        
        print 'Enter details'
        s1.input()
        dump (s1,f)
        choice=raw_input('Want to enter y or n')
        if choice.lower()=='n':
            break
    f.close()


def display(fname):
    
    s1=books()
    if not os.path.isfile(fname):
        print "file doesn't exist"
    else:
        f=open(fname,'rb')
        try:
            while True:
                s1=load(f)
                print s1.disp()
        except EOFError :
            pass
        finally :
            f.close()
            
def search(fname):
    
    s1=books()
    a=0
    if not os.path.isfile(fname):
        print "file doesn't exist"
    else:
        f=open(fname,'rb')
        print """ Do you want to search by :
                    1. Serial number
                    2. Book Name
                    3. Date of issue month
                    4. Date of issue year
                    5. Name of issuer
                    6. Month of return"""

        ch= input("enter choice number : ")
        if ch==1:
                no=input("enter serial no : ")
                try:
                    while True:
                        s1=load(f)
                        if s1.sno==no:
                            a=1
                            print s1.disp()
                except EOFError :
                    if a==0:
                        print "Sorry not found"
                finally :
                    f.close()
        elif ch==2:
            n=raw_input("enter book name :  ")
            try:
                        while True:
                            s1=load(f)
                            if s1.name.upper()==n.upper():
                                a=1
                                print s1.disp()
            except EOFError :
                         if a==0:
                            print "Sorry not found"
            finally :
                        f.close()
        elif ch==6:
            no=input("enter return month : ")
            try:
                    while True:
                        s1=load(f)
                        if s1.returndate[1]==no:
                            a=1
                            print s1.disp()
            except EOFError :
                    if a==0:
                            print "Sorry not found"
            finally :
                    f.close()
        elif ch==3:
            n= input("enter issue month  : ")
            try:
                    while True:
                        s1=load(f)
                        if s1.issue[1]==n:
                            a=1
                            print s1.disp()
            except EOFError :
                    if a==0:
                            print "Sorry not found"
            finally :
                    f.close()
        elif ch==4:
            no=input("enter issue year : ")
            try:
                    while True:
                        s1=load(f)
                        if s1.issue[2]==no:
                            a=1
                            print s1.disp()
            except EOFError :
                    if a==0:
                            print "Sorry not found"
            finally :
                    f.close()
        elif ch==5:
            no=raw_input("enter name of issuer : ")
            try:
                    while True:
                        s1=load(f)
                        if s1.issuername.lower()==no.lower():
                            a=1
                            print s1.disp()
            except EOFError :
                    if a==0:
                            print "Sorry not found"
            finally :
                    f.close()
        else:
            print 'wrong choice...'
   
def delete(fname):
    s1=books()
    if not os.path.isfile(fname):
        print "file doesn't exist"
    else:
        f=open(fname,'rb')
        f1=open('temp.dat','wb')
        print """ Do you want to delete by :
                1. Serial number
                    2. Book Name
                    3. Date of issue month
                    4. Date of issue year
                    5. Name of issuer
                    6. Month of return"""
    while 3:
        ch= input("enter choice number : ")
        if ch==1:
                no=input("enter serial no : ")
                try :
                    flag=0
                    while True:
                        s1=load(f)
                        if s1.sno==no:
                            flag=1
                        else:
                            dump(s1,f1)
                except EOFError :
                    if flag==0:
                        print "serial no NF"
                finally :
                        f.close()
                        f1.close()
                        os.remove(fname)
                        os.rename('temp.dat',fname)
                        break

        elif ch==2:
            n=raw_input("enter book name :  ")
            try :
                    flag=0
                    while True:
                        s1=load(f)
                        if s1.name.upper()==n.upper():
                            flag=1
                        else:
                            dump(s1,f1)
            except EOFError :
                    if flag==0:
                        print "name NF"
            finally :
                        f.close()
                        f1.close()
                        os.remove(fname)
                        os.rename('temp.dat',fname)
                        break

        elif ch==3:
            no=input("enter isssue date : ")
            try :
                    flag=0
                    while True:
                        s1=load(f)
                        if s1.issue[1]==no:
                            flag=1
                        else:
                            dump(s1,f1)
            except EOFError :
                    if flag==0:
                        print "date NF"
            finally :
                        f.close()
                        f1.close()
                        os.remove(fname)
                        os.rename('temp.dat',fname)
                        break

        elif ch==4:
            n=input("enter issue year : ")
            try :
                    flag=0
                    while True:
                        s1=load(f)
                        if s1.issue[2]==n:
                            flag=1
                        else:
                            dump(s1,f1)
            except EOFError :
                    if flag==0:
                        print "month NF"
            finally :
                        f.close()
                        f1.close()
                        os.remove(fname)
                        os.rename('temp.dat',fname)
                        break

        elif ch==6:
            no=input("enter return month : ")
            try :
                    flag=0
                    while True:
                        s1=load(f)
                        if s1.returndate[1]==no:
                            flag=1
                        else:
                            dump(s1,f1)
            except EOFError :
                    if flag==0:
                        print "year NF"
            finally :
                        f.close()
                        f1.close()
                        os.remove(fname)
                        os.rename('temp.dat',fname)
                        break

        elif ch==6:
            no=raw_input("enter name of issuer : ")
            try :
                    flag=0
                    while True:
                        s1=load(f)
                        if s1.issuername.lower()==no.lower():
                            flag=1
                        else:
                            dump(s1,f1)
            except EOFError :
                    if flag==0:
                        print "noa NF"
            finally :
                        f.close()
                        f1.close()
                        os.remove(fname)
                        os.rename('temp.dat',fname)
                        break

        else:
            print 'wrong choice...'
            break
def modify(fname):
    a=0
    s1=books()
    if not os.path.isfile(fname):
        print "File doesn't exist"
    else:
        no = input("enter serial no of book to be modified : ")
        f1=open(fname,'rb')
        f2=open('temp.dat','wb')
        print  """ SERIAL NUMBER CAN'T BE MODIFIED - UNIQUE FOR EACH BOOK
Do u want to modify :
1. Book Name
2. Date of issue
3. Month of issue
4. Year of issue
5. Name of issuer """
    ch= input("enter choice : ")
    if ch==1:
        name= raw_input("enter new name : ")
        try :
            while True :
                s1=load(f1)
                if s1.sno==no:
                    s1.name=name
                    a=1
                dump(s1,f2)
        except EOFError :
            if a==0:
                print "Sorry can't modify"
            else:
                print "MODIFIED"
        finally :
            f1.close()
            f2.close()
            os.remove(fname)
            os.rename('temp.dat',fname)
    elif ch==2:
        date= input("enter new date : ")
        try :
            while True :
                s1=load(f1)
                if s1.sno==no:
                    s1.issue[0]=date
                    a=1
                dump(s1,f2)
        except EOFError :
            if a==0:
                print "Sorry can't modify"
            else:
                print "MODIFIED"
        finally :
            f1.close()
            f2.close()
            os.remove('books.dat')
            os.rename('temp.dat','books.dat')
    elif ch==3:
        month= input("enter new month number : ")
        try :
            while True :
                s1=load(f1)
                if s1.sno==no:
                    s1.issue[1]=month
                    a=1
                dump(s1,f2)
        except EOFError :
            if a==0:
                print "Sorry can't modify"
            else:
                print "MODIFIED"
        finally :
            f1.close()
            f2.close()
            os.remove('books.dat')
            os.rename('temp.dat','books.dat')
    elif ch==4:
        year= input("enter new year : ")
        try :
            while True :
                s1=load(f1)
                if s1.sno==no:
                    s1.issue[2]=year
                    a=1
                dump(s1,f2)
    
        except EOFError :
            if a==0:
                print "Sorry can't modify"
            else:
                print "MODIFIED"
        finally :
            f1.close()
            f2.close()
            os.remove('books.dat')
            os.rename('temp.dat','books.dat')
    elif ch==5:
        n=raw_input("enter new name of issuer : ")
        try :
            while True :
                s1=load(f1)
                if s1.sno==no:
                    s1.issuername=n
                    a=1
                dump(s1,f2)
    
        except EOFError :
            if a==0:
                print "Sorry can't modify"
            else:
                print "MODIFIED"
        finally :
            f1.close()
            f2.close()
            os.remove('books.dat')
            os.rename('temp.dat','books.dat')
    else:
        print "WRONG INPUT... "
def main ():
    while True :
        print """ 1. Create an books Record
                  2. Append a new books record
                  3. Delete a book record
                  4. Display all the books
                  5. Search for a particular book
                  6. Modify the books record
                  7. EXIT """
        choice = input ("enter your choice number : ")
        if choice==1:
            create('books.dat')
        elif choice==2:
            append('books.dat')
        elif choice==3:
            delete('books.dat')
        elif choice==4:
            display('books.dat')
        elif choice==5:
            search('books.dat')
        elif choice==6 :
            modify('books.dat')
        elif choice==7:
            print "Bye"
            break
        else:
            print "WRONG CHOICE.... Choose Again... "
main()
