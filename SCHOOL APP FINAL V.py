# SCHOOL V2
# THE SCHOOL APP
# FUNCTIONS FOR LOGIN AS STUDENT
import csv
import mysql.connector as mc
import random
con=mc.connect(host='localhost',user='root',password='640836',database='school_app')
cur=con.cursor()

# adds new student to the csv file 
def add_student():
    try:
        global sinputname
        uid=input('Enter Admission number : ')
        sinputname=input('Enter your name        : ')
        classinput=input('Enter your class       : ')
        stbusinput=input('Enter bus name (if not opted type "N") : ')
        
        
        if search_student(uid):
            print('ERROR! - This user already exists in the app...')
        else:
            pwd='hhs'+str(uid)+sinputname[0:1].lower()
            print('YOUR PASSWORD PROVIDED BY SCHOOL IS : ',pwd)
            cpwd=input('Confirm password : ')
            if pwd!=cpwd:
                print('ERROR! - password given does not match')
            else:
                r=[uid,pwd,sinputname]
                f=open('Student login.csv','a',newline='')
                w=csv.writer(f)
                w.writerow(r)
                print()
                print('New user account created successfully !!')
                print()
                rnoq="select * from student where class='{}'".format(classinput)
                cur.execute(rnoq)
                r=cur.fetchall()
                clscount=cur.rowcount
                rno=1+clscount

                # new marks insert 
                def insert_marks():
                    
                    s1=round(random.uniform(50.00,100.00),2)
                    s2=round(random.uniform(50.00,100.00),2)
                    s3=round(random.uniform(50.00,100.00),2)
                    s4=round(random.uniform(50.00,100.00),2)
                    s5=round(random.uniform(50.00,100.00),2)
                    l=[s1,s2,s3,s4,s5]
                    if classinput.upper()=='XII A':
                        q="insert into student values({},{},'{}','{}',{},{},{},{},null,{},null,null,null,null,'{}')".format(rno,uid,sinputname,classinput.upper(),s1,s2,s3,s4,s5,stbusinput.upper())
                        cur.execute(q)
                        con.commit()
                    elif classinput.upper()=='XII B':
                        q="insert into student values({},{},'{}','{}',{},{},{},null,{},{},null,null,null,null,'{}')".format(rno,uid,sinputname,classinput.upper(),s1,s2,s3,s4,s5,stbusinput.upper())
                        cur.execute(q)
                        con.commit()
                    elif classinput.upper()=='XII C':
                        q="insert into student values({},{},'{}','{}',null,null,null,null,null,null,{},{},{},{},{},'{}')".format(rno,uid,sinputname,classinput.upper(),s1,s2,s3,s4,s5,stbusinput.upper())
                        cur.execute(q)
                        con.commit()
                    else:
                        print('ERROR')
                        print('New user account creation unsuccessful !')
                        homescreen()
                insert_marks()
                f.close()
    except Exception as e:
        print()
        print('ERROR - ',e)
        print()
        return False
    
# adds teacher
def add_teacher():
    try:
        global tinputname
        uid=input('Enter Registration number : ')
        tinputname=input('Enter your name           : ')
        clinput=input('Enter your class/s        : ')
        subinput=input('Enter your subject        : ')
        tbusinput=input('Enter bus name (if not opted type "N") : ')
        if search_teacher(uid):
            print()
            print('ERROR! - This user already exists in the app...')
        else:
            pwd='hhs'+str(uid)+tinputname[0:1].lower()
            print('YOUR PASSWORD PROVIDED BY SCHOOL IS : ',pwd)
            cpwd=input('Confirm password : ')
            if pwd!=cpwd:
                print()
                print('ERROR! - password given does not match')
            else:
                r=[uid,pwd,tinputname]
                f=open('Teacher login.csv','a',newline='')
                w=csv.writer(f)
                w.writerow(r)
                print()
                print('New user account created successfully !!')
                print()

                # insert teacher details into table
                def insertteacher():
                    qin="insert into teacher values({},'{}','{}','{}','{}')".format(uid,tinputname,subinput,clinput.upper(),tbusinput.upper())
                    cur.execute(qin)
                    con.commit()
                f.close()
    except Exception as e:
        print()
        print('ERROR - ',e)
        print()
        return False

# searching for duplicate accounts

def search_teacher(uid):
    f=open('Teacher login.csv')
    ro=csv.reader(f)
    for r in ro:
        if r[0]==uid:
            f.close()
            return True
    else:
        f.close()
        return False
def login_student():
    f=open('Student login.csv')
    ro=csv.reader(f)
    global uid
    uid=input('Enter user id : ')
    for r in ro:
        if r[0]==uid:
            pwd=input('Enter password : ')
            if r[1]==pwd:
                print()
                global student_name
                student_name=r[2]
                return True
                break
            else:
                print('ERROR! - Invalid password')
                print()
                return False
    else:
        print("ERROR - USER ACCOUNT DOESN'T EXIST")     
        print()
        return False
    f.close()


def search_student(uid):
    f=open('Student login.csv')
    ro=csv.reader(f)
    for r in ro:
        if r[0]==uid:
            f.close()
            return True
    else:
        f.close()
        return False
    
def login_teacher():
    f=open('Teacher login.csv')
    ro=csv.reader(f)
    uid=input('Enter user id : ')
    for r in ro:
        if r[0]==uid:
            pwd=input('Enter password : ')
            if r[1]==pwd:
                print()
                global teacher_name
                teacher_name=r[2]
                return True
                break
            else:
                print('ERROR! - Invalid password')
                print()
                return False
    else:
        print("ERROR - USER ACCOUNT DOESN'T EXIST")     
        print()
        return False
    f.close()

# INTERFACE 1 FOR STUDENT
def student_ui():
    print('-'*70)
    print('✔ ✔ ✔ Ignite Your Passion for Learning ✔ ✔ ✔'.center(70))
    print('-'*70)
    print()
    print('    ','-'*23,' '*9,'    ','-'*23,' '*9,'    ')
    print(' '*4,'|  1. YOUR ACADEMICS',' |',' '*14,'|','','2. TRANSPORTATION',' |')
    print('    ','-'*23,' '*9,'    ','-'*23,' '*9,'    ')
    print()
    print(' '*24,'-'*23,' '*9,'    ')
    print(' '*24,'|    ','3. YOUR FEE','    |',' '*14)
    print(' '*24,'-'*23,' '*9,'    ')
    print()
    print('-'*70)
def teacher_ui():
    print('-'*70)
    print('✔ ✔ ✔ Ignite Your Passion for Teaching ✔ ✔ ✔'.center(70))
    print('-'*70)
    print()
    print('    ','-'*24,' '*9,'    ','-'*24,' '*9,'    ')
    print(' '*4,'| 1. CLASS PERMORMANCE','|',' '*14,'|','','  2. REPORT CARD','   |')
    print('    ','-'*24,' '*9,'    ','-'*24,' '*9,'    ')
    print()
    print(' '*23,'-'*24,' '*9,'    ')
    print(' '*23,'|','   3. UPDATE MARKS  ','|',' '*14)
    print(' '*23,'-'*24,' '*9,'    ')
    print()
    print('-'*70)

# we are generating a mark sheet for the class using the values from the database

def csperformance():
    try:
        perfch='1'
        if perfch=='1':
            clas=input('Enter the class information to be retrieved : ')
            if clas.lower()=='xii a':
                qse='''select roll_no as RNO,NAME,
MATHS as MATH,PHYSICS as PHY,chemistry as CHEM,BIOLOGY as BIO,
ENGLISH as ENG, (maths+chemistry+physics+english+biology)//500*100 as TOTAL
from student where class='{}' order by roll_no'''.format(clas)
                cur.execute(qse)
                r=cur.fetchall()
                print('-'*70)
                print('RNO  NAME             MATHS    PHY    CHEM     BIO     ENG    TOTAL')
                print('-'*70)
                for a in r:
                    le=len(a[1])
                    rno=str(a[0])
                    lr=len(rno)
                    sp=15-le
                    sp2=3-lr
                    print(a[0],' '*sp2,a[1],' '*sp,a[2],' ',a[3],' ',a[4],' ',a[5],' ',a[6],' ',a[7])
                print('-'*70)
            elif clas.lower()=='xii b':
                qse='''select roll_no as RNO,NAME,
MATHS as MATH,PHYSICS as PHY,chemistry as CHEM,COMPUTER as COMP,
ENGLISH as ENG, (maths+chemistry+physics+english+computer)//500*100 as TOTAL
from student where class='{}' order by roll_no'''.format(clas)
                cur.execute(qse)
                r=cur.fetchall()
                print('-'*70)
                print('RNO  NAME             MATHS    PHY    CHEM    COMP     ENG    TOTAL')
                print('-'*70)
                for a in r:
                    le=len(a[1])
                    rno=str(a[0])
                    lr=len(rno)
                    sp=15-le
                    sp2=3-lr
                    print(a[0],' '*sp2,a[1],' '*sp,a[2],' ',a[3],' ',a[4],' ',a[5],' ',a[6],' ',a[7])
                print('-'*70)
            elif clas.lower()=='xii c':
                qse='''select roll_no as RNO,NAME,
accountancy as ACC,economics as ECO,info_practices as IP,business as BST,
ENGLISH as ENG, (accountancy+economics+info_practices+business+english)//500*100 as TOTAL
from student where class='{}' order by roll_no'''.format(clas)
                cur.execute(qse)
                r=cur.fetchall()
                print('-'*70)
                print('RNO  NAME              ACC     ECO     IP      BST     ENG    TOTAL')
                print('-'*70)
                for a in r:
                    le=len(a[1])
                    rno=str(a[0])
                    lr=len(rno)
                    sp=15-le
                    sp2=3-lr
                    print(a[0],' '*sp2,a[1],' '*sp,a[2],' ',a[3],' ',a[4],' ',a[5],' ',a[6],' ',a[7])
                print('-'*70)
            elif clas.lower()=='log out':
                print('LOGGIN OUT OF YOUR ACCOUNT....')
                homescreen()
    except Exception as e:
        print()
        print('ERROR - ',e)
        print()
        return False

# update marks

def update_marks():
    try:
        def newmarks(rvclass,adno):
            if rvclass.lower()=='xii a':
                print('ENTER NEW MARKS...')
                print()
                ns1=float(input('Enter marks for PHYSICS   : '))
                ns2=float(input('Enter marks for MATHS     : '))
                ns3=float(input('Enter marks for BIOLOGY   : '))
                ns4=float(input('Enter marks for CHEMISTRY : '))
                ns5=float(input('Enter marks for ENGLISH   : '))
                print()
                sureity=input('ARE YOU SURE THE DATA IS CORRECT (Y/N/EXIT) : ')
                if sureity.lower()=='y':
                    qn='''update student set physics={},maths={},biology={},
            chemistry={},english={} where admission_no={}'''.format(ns1,ns2,ns3,ns4,ns5,adno)
                    cur.execute(qn)
                    con.commit()
                    print()
                    print('DATA UPDATED SUCCESSFULLY....')
                    print()
                    print('PRESS "ENTER" TO CONTINUE OR TYPE "EXIT"')
                    nextst=input('Do you want to continue ? : ')
                    
                    if nextst.lower()=='exit':
                        print()
                        print('EXITTING CLASS MARK UPDATION PORTAL...')
                        print()
                        return False
                    elif nextst=='':
                        print()
                    else:
                        print('ERROR')
                else:
                    print('Re - routing to updation UI..')
                    print()
                    update_marks()

            elif rvclass.lower()=='xii b':
                print('ENTER NEW MARKS...')
                print()
                ns1=float(input('Enter marks for PHYSICS   : '))
                ns2=float(input('Enter marks for MATHS     : '))
                ns3=float(input('Enter marks for COMPUTER  : '))
                ns4=float(input('Enter marks for CHEMISTRY : '))
                ns5=float(input('Enter marks for ENGLISH   : '))
                print()
                sureity=input('ARE YOU SURE THE DATA IS CORRECT (Y/N) : ')
                if sureity.lower()=='y':
                    qn='''update student set physics={},maths={},computer={},
        chemistry={},english={} where admission_no={}'''.format(ns1,ns2,ns3,ns4,ns5,adno)
                    cur.execute(qn)
                    con.commit()
                    print()
                    print('DATA UPDATED SUCCESSFULLY....')
                    print()
                    print('PRESS "ENTER" TO CONTINUE OR TYPE "EXIT"')
                    nextst=input('Do you want to continue ? : ')
                    
                    if nextst.lower()=='exit':
                        print()
                        print('EXITTING CLASS MARK UPDATION PORTAL...')
                        print()
                        return False
                    elif nextst=='':
                        print()
                    else:
                        print('ERROR')
                        
                else:
                    print('Re - routing to updation UI..')
                    print()
                    update_marks()

            elif rvclass.lower()=='xii c':
                print('ENTER NEW MARKS...')
                print()
                ns1=float(input('Enter marks for ACCOUNTANCY    : '))
                ns2=float(input('Enter marks for ECONOMICS      : '))
                ns3=float(input('Enter marks for INFO PRACTICES : '))
                ns4=float(input('Enter marks for BUSINESS       : '))
                ns5=float(input('Enter marks for ENGLISH        : '))
                print()
                sureity=input('ARE YOU SURE THE DATA IS CORRECT (Y/N) : ')
                if sureity.lower()=='y':
                    qn='''update student set accountancy={},economics={},info_practices={},
        business={},english={} where admission_no={}'''.format(ns1,ns2,ns3,ns4,ns5,adno)
                    cur.execute(qn)
                    con.commit()
                    print()
                    print('DATA UPDATED SUCCESSFULLY....')
                    print()
                    print('PRESS "ENTER" TO CONTINUE OR TYPE "EXIT"')
                    nextst=input('Do you want to continue ? : ')
                    
                    if nextst.lower()=='exit':
                        print()
                        print('EXITTING CLASS MARK UPDATION PORTAL...')
                        print()
                        return False
                    elif nextst=='':
                        print()
                    else:
                        print('ERROR')
                elif sureity.lower()=='n':
                    print()
                    newmarks(rvclass,adno)
                else:
                    print('Re - routing to updation UI..')
                    print()
                    update_marks()
            '''
            else:
                print()
                print('CLICK "ENTER" TO CONTINUE....')
                gon=input()
                if gon=='':
                    student_ui()'''
        upc1=0
        print()
        print('='*70)
        print('MARK UPDATION PORTAL'.center(70))
        print('='*70)
        print('---------------------------'.center(70))
        print('|  1. CLASS MARKS UPADTE  |'.center(70))
        print('---------------------------'.center(70))
        print()
        print('---------------------------'.center(70))
        print('| 2. SINGLE MARKS UPADTE  |'.center(70))
        print('---------------------------'.center(70))
        print('='*70)
        print()
        umch=input('Enter your menu choice : ')
        if umch=='1':
            print()
            print('-'*70)
            print('WELCOME TO MARK UPDATION PROCESS'.center(70))
            print('-'*70)
            print()
            aclu=input('Enter the class : ')
            print('-'*70)
            sentence='MARK UPDATION FOR '+aclu.upper()
            print(sentence.center(70))
            print('-'*70)
            print()
            qsearch="select roll_no,name,class,admission_no from student where class='{}' order by roll_no".format(aclu)
            cur.execute(qsearch)
            rn=cur.fetchall()
            for a in rn:
                print('-'*70)
                print('NAME               : ',a[1])
                print('CLASS              : ',a[2])
                print('ROLL NUMBER        : ',a[0])
                print('-'*70)
                newmarks(aclu,a[3])
            else:
                print()
                print('EXITTING MENU....')
                print()
        elif umch=='2':
            print()
            print('-'*70)
            print('WELCOME TO MARK UPDATION PROCESS'.center(70))
            print('-'*70)
            print()
            rvst=input('Enter the admission number of student : ')
            qsearch="select roll_no,name,class from student where admission_no={}".format(rvst)
            cur.execute(qsearch)
            deta=cur.fetchone()
            rvname=input('Enter the name of the student : ')
            rvclass=input('Enter the class of the student : ')
            print()
            print('SEARCHING........')
            print()
            upcl2=0
            print('-'*70)
            if rvclass.lower()=='xii a':
                print('NAME               : ',deta[1])
                print('CLASS              : ',deta[2])
                print('ADMISSION NUMBER   : ',rvst)
                print('-'*70)
                q="select physics,maths,biology,chemistry,english from student where admission_no={}".format(rvst)
                cur.execute(q)
                cr=cur.fetchone()
                print('CURRENT MARKS'.center(70))
                print('-'*70)
                print('PHYSICS        : ',cr[0])
                print('MATHEMATICS    : ',cr[1])
                print('BIOLOGY        : ',cr[2])
                print('CHEMISTRY      : ',cr[3])
                print('ENGLISH        : ',cr[4])
                print('-'*70)
                print()
                newmarks(rvclass,rvst)
                
            elif rvclass.lower()=='xii b':
                print('NAME               : ',rvname)
                print('CLASS              : ',rvclass)
                print('ADMISSION NUMBER   : ',rvst)
                print('-'*70)
                q="select physics,maths,computer,chemistry,english from student where admission_no={}".format(rvst)
                cur.execute(q)
                cr=cur.fetchone()
                print('CURRENT MARKS'.center(70))
                print('-'*70)
                print('PHYSICS        : ',cr[0])
                print('MATHEMATICS    : ',cr[1])
                print('COMPUTER       : ',cr[2])
                print('CHEMISTRY      : ',cr[3])
                print('ENGLISH        : ',cr[4])
                print('-'*70)
                print()
                newmarks(rvclass,rvst)

            elif rvclass.lower()=='xii c':
                print('NAME               : ',rvname)
                print('CLASS              : ',rvclass)
                print('ADMISSION NUMBER   : ',rvst)
                print('-'*70)
                q="select accountancy,economics,info_practices,business,english from student where admission_no={}".format(rvst)
                cur.execute(q)
                cr=cur.fetchone()
                print('CURRENT MARKS'.center(70))
                print('-'*70)
                print('ACCOUNTANCY        : ',cr[0])
                print('ECONOMICS          : ',cr[1])
                print('INFO PRACTICES     : ',cr[2])
                print('BUSINESS           : ',cr[3])
                print('ENGLISH            : ',cr[4])
                print('-'*70)
                print()
                newmarks(rvclass,rvst)

            elif upc2==3:
                print('OUT OF ATTEMPTS !!')
                return False

            else:
                print('ERROR !!')
                upc2+=1
                update_marks()
                
        elif upc1==3:
            print('OUT OF ATTEMPTS !!')
            return False

        elif umch.lower()=='back':
            return False
        
        elif newmarks()==False:
            return False
        
        else:
            print('ERROR !!')
            update_marks()
            upc1+=1
    except Exception as e:
        print()
        print('ERROR - ',e)
        print()
        return False
    
# function handles all the necessary details needed for bus like displaying routes and updating bus

def busui():
    try:
        q="select NAME,CLASS,BUS,ADMISSION_NO from student where name='{}'".format(student_name)
        cur.execute(q)
        r=cur.fetchone()
        print('='*70)
        print('HORIZON HIGH SCHOOL, KOCHI'.center(70))
        print('='*70)
        print('BUS DETAILS OF YEAR 2023 - 2024')
        print('-'*70)
        print('NAME           : ',student_name)
        print('CLASS          : ',r[1])
        print('ADMISSION NO   : ',r[3])
        print('CURRENT BUS    : ',r[2])
        print('='*70)
        print('-------------------------'.center(70))
        print('|     1. CHANGE BUS     |'.center(70))
        print('-------------------------'.center(70))
        print()
        print('-------------------------'.center(70))
        print('| 2. DISPLAY BUS ROUTES |'.center(70))
        print('-------------------------'.center(70))
        print('='*70)
        cbusui=0
        print()
        bus1=input('Enter bus menu choice : ')
        if bus1=='1':
            print('-'*70)
            chbus=input('ENTER THE BUS TO BE CHANGED INTO : ')
            if chbus.upper() in 'ABC':
                qb="update student set bus='{}' where admission_no={}".format(chbus.upper(),uid)
                cur.execute(qb)
                sure=input('ARE YOU SURE TO CHANGE (y/n) : ')
                if sure.lower()=='y':
                    con.commit()
                    print()
                    print('DATA UPDATED SUCCESSFULLY')
                    print()
                        
                else:
                    con.rollback()
                    print()
                    print('DATA UPDATION FAILED')
                    print()
                    print('CLICK "ENTER" TO CONTINUE....')
                    gon=input()
                    if gon=='':
                        student_ui
            else:
                print('TRY AGAIN...')
                cbusui+=1
        elif bus1=='2':
            print()
            print('='*70)
            print('BUS ROUTES'.center(70))
            print('='*70)
            print(' BUS NAME \t ROUTE \t\t\t\t TIME')
            print('='*70)
            print('         \t MG ROAD                   \t 5.00AM - 5.00PM')
            print('         \t  |')
            print('    A    \t PALARIVATTOM              \t 6.00AM - 4.00PM')
            print('         \t  |')
            print('         \t SCHOOL                    \t 7.45AM - 3.00PM')
            print('-'*70)
            print('         \t VYTILLA                   \t 5.00AM - 5.00PM')
            print('         \t  |')
            print('    B    \t IRUMPANAM                 \t 6.00AM - 4.00PM')
            print('         \t  |')
            print('         \t SCHOOL                    \t 7.45AM - 3.00PM')
            print('-'*70)
            print('         \t PALLIKARA                 \t 5.00AM - 5.00PM')
            print('         \t  |')
            print('    C    \t THEVAKKAL                 \t 6.00AM - 4.00PM')
            print('         \t  |')
            print('         \t SCHOOL                    \t 7.45AM - 3.00PM')
            print('='*70)
            print()
            print('CLICK "ENTER" TO CONTINUE....')
            gon=input()
            if gon=='':
                busui()
        elif bus1.lower()=='back':
            print()
            return False
        elif cbusui==5:
            print('OUT OF ATTEMPTS....')
            return False
        else:
            print('TRY AGAIN...')
            busui()
            cbusui+=1
    except Exception as e:
        print()
        print('ERROR - ',e)
        print()
        return False

# does all the arithemetic calculation needed to generate marks and updates them

def academics():
    try:
        print('='*70)
        print('HORIZON HIGH SCHOOL - KOCHI'.center(70))
        print('='*70)
        print('REPORT CARD FOR YEAR 2023 - 24'.center(70))
        print('='*70)
        q1="select class,name from student where admission_no={}".format(uid)
        cur.execute(q1)
        cls=cur.fetchall()
        print('NAME               : ',cls[0][1])
        print('CLASS              : ',cls[0][0])
        print('ADMISSION NUMBER   : ',uid)
        if str(cls[0][0])=='XII A':
            q="select physics,maths,biology,chemistry,english from student where admission_no={}".format(uid)
            cur.execute(q)
            record=cur.fetchall()
            print()
            r1=record[0][0]
            r2=record[0][1]
            r3=record[0][2]
            r4=record[0][3]
            r5=record[0][4]
            print('PHYSICS        : ',r1)
            print('MATHEMATICS    : ',r2)
            print('BIOLOGY        : ',r3)
            print('CHEMISTRY      : ',r4)
            print('ENGLISH        : ',r5)
            print()
            mtotal=(r1+r2+r3+r4+r5)/5
            print('TOTAL PERCENTAGE     :',mtotal,'%')
            print()
        elif str(cls[0][0])=='XII B': 
            q="select physics,maths,computer,chemistry,english from student where admission_no={}".format(uid)
            cur.execute(q)
            record=cur.fetchall()
            #print(float(record[0][4]))
            print()
            r1=record[0][0]
            r2=record[0][1]
            r3=record[0][2]
            r4=record[0][3]
            r5=record[0][4]
            print('PHYSICS              : ',r1)
            print('MATHEMATICS          : ',r2)
            print('COMPUTER             : ',r3)
            print('CHEMISTRY            : ',r4)
            print('ENGLISH              : ',r5)
            print()
            mtotal=(r1+r2+r3+r4+r5)/5
            print('TOTAL PERCENTAGE     :',mtotal,'%')
        elif str(cls[0][0])=='XII C':
            q="select business,info practices,accountancy,economics,english from student where admission_no={}".format(uid)
            cur.execute(q)
            record=cur.fetchall()
            #print(float(record[0][4]))
            print()
            r1=record[0][0]
            r2=record[0][1]
            r3=record[0][2]
            r4=record[0][3]
            r5=record[0][4]
            print('BUSINESS          : ',r1)
            print('INFO PRACTICES    : ',r2)
            print('ACCOUNTANCY       : ',r3)
            print('ECONOMICS         : ',r4)
            print('ENGLISH           : ',r5)
            print()
            mtotal=(r1+r2+r3+r4+r5)/5
            print('TOTAL PERCENTAGE  :',mtotal,'%')
        else:
            pass
    except Exception as e:
        print()
        print('ERROR - ',e)
        print()
        return False

# does all the arithemetic calculation needed to generate fees and updates them

def feeui():
    try:
        q="select NAME,CLASS,BUS,ADMISSION_NO from student where name='{}'".format(student_name)
        cur.execute(q)
        r=cur.fetchone()
        print('='*70)
        print('HORIZON HIGH SCHOOL - KOCHI'.center(70))
        print('='*70)
        print('NAME           : ',student_name)
        print('CLASS          : ',r[1])
        print('ADMISSION NO   : ',r[3])
        print('BUS            : ',r[2])
        print('='*70)
        print('FEE DETAILS FOR 2023 - 24'.center(70))
        print('-'*70)
        print('TERM 1 FEE      : ','25000/-')
        print('TERM 2 FEE      : ','28000/-')
        print('TERM 3 FEE      : ','30000/-')
        print('BUS FEE         : ','35000/-')
        print('='*70)
        print()
        ynf1=input('FIRST TERM FEE PAID (yes/no)  : ')
        ynf2=input('SECOND TERM FEE PAID (yes/no) : ')
        ynf3=input('THIRD TERM FEE PAID (yes/no)  : ')
        ynbf=input('FULL BUS FEE PAID (yes/no)    : ')
        print()

        if ynf1.lower()=='yes':
            pf1=25000
        elif ynf1.lower()=='no':
            pf1=int(input('Enter term 1 fee paid : '))
            if pf1>25000:
                print('ERROR')
                pf1=int(input('Enter term 1 fee paid : '))
                if pf1>25000:
                    return False
                    print()
        else:
            print('ERROR')
            print()
            feeui()
            
        if ynf2.lower()=='yes':
            pf2=28000
        elif ynf2.lower()=='no':
            pf2=int(input('Enter term 2 fee paid : '))
            if pf2>28000:
                print('ERROR')
                pf2=int(input('Enter term 2 fee paid : '))
                if pf2>28000:
                    return False
                    print()
        else:
            print('ERROR')
            print()
            feeui()
            
        if ynf3.lower()=='yes':
            pf3=30000
        elif ynf3.lower()=='no':
            pf3=int(input('Enter term 3 fee paid : '))
            if pf3>30000:
                print('ERROR')
                pf3=int(input('Enter term 3 fee paid : '))
                if pf3>30000:
                    return False
                    print()
        else:
            print('ERROR')
            print()
            feeui()

        if ynbf.lower()=='yes':
            pbf=35000
        elif ynbf.lower()=='no':
            pbf=int(input('Enter bus fee paid : '))
            if pbf>35000:
                print('ERROR')
                pbf=int(input('Enter bus fee paid : '))
                if pbf>35000:
                    return False
                    print()
        else:
            print('ERROR')
            print()
            feeui()
        print()
        checkfee=input('ARE YOU SURE DATA IS ENTERED CORRECT (y/n): ')
        print()
        print('='*70)
        print('HORIZON HIGH SCHOOL - KOCHI'.center(70))
        print('='*70)
        print('NAME           : ',student_name)
        print('CLASS          : ',r[1])
        print('ADMISSION NO   : ',r[3])
        print('BUS            : ',r[2])
        print('='*70)
        print('FEE PAYMENT RECIET'.center(70))
        print('='*70)
        print('FEE DETAILS FOR 2023 - 24')
        print('-'*70)
        print('TERM 1 FEE      : ','25000/-')
        print('TERM 2 FEE      : ','28000/-')
        print('TERM 3 FEE      : ','30000/-')
        print('BUS FEE         : ','35000/-')
        print('='*70)
        
        if checkfee.lower()=='y':
            print('FEE PAID'.center(70))
            print('='*70)
            print('TERM 1 FEE      : ',pf1,'/-')
            print('TERM 2 FEE      : ',pf2,'/-')
            print('TERM 3 FEE      : ',pf3,'/-')
            print('BUS FEE         : ',pbf,'/-')
            print('='*70)
            print('FEE TO BE PAID'.center(70))
            print('='*70)
            print('TERM 1 FEE      : ',25000-pf1,'/-')
            print('TERM 2 FEE      : ',28000-pf2,'/-')
            print('TERM 3 FEE      : ',30000-pf3,'/-')
            print('BUS FEE         : ',35000-pbf,'/-')
            print('TOTAL AMOUNT TO BE DEPOSITED : ',(25000-pf1)+(28000-pf2)+(30000-pf3)+(35000-pbf),'/-')
            print('='*70)
            pass
        else:
            print('GO BACK TO MENU AND TRY AGAIN !!')
            return False
        
    except Exception as e:
        print()
        print('ERROR - ',e)
        print()
        return False

# HOME SCREEN
def homescreen():
    print('-'*70)
    print('HORIZON HIGH SCHOOL - KOCHI'.center(70))
    print('-'*70)
    print('SCHOOL APP'.center(70))
    print('-'*70)
    print(' *'*34)
    print('* '*15,'WELCOME',' *'*15)
    print(' *'*34)
    print('-'*70)
    print('1. LOGIN'.center(70))
    print('2. CREATE NEW ACCOUNT'.center(70))
    print('3. EXIT APPLICATION'.center(70))
    print()
    print('''AFTER LOGGING IN YOU CAN TYPE "LOG OUT"'''.center(70))
    print('''AT ANY PROMT POINT FOR LOGGING OUT OF YOUR ACCOUNT'''.center(70))
    print()
    print('TYPE IN "BACK" IF YOU WANT TO GO BACK FROM SUB MENU TO MAIN MENU'.center(70))
    print()
    print('-'*70)
homescreen()
# LOGIN PAGE
creslog=0
try:
    
    while True:
        creslog+=1
        response1=int(input('Enter your choice (1-3) : '))
        print('-'*70)
        if response1==1:
            print()
            print('TEACHER (T)'.center(70))
            print('STUDENT (S)'.center(70))
            print()
            print('-'*70)
            tos=input('Login as Teacher or Student (T/S): ')
            print('-'*70)
            if tos.lower()=='t':
                for att in range(3):
                    if login_teacher():
                        print('You have successfully logged in to the app !!')
                        print()
                        print('Welcome back',teacher_name.split()[0],'!!!')
                        teacher_ui()
                        while True:
                            menucountteach=0
                            menuch=input('Enter your menu choice : ')
                            if menuch=='1':
                                print()
                                csperformance()
                                print()
                                print('CLICK "ENTER" TO CONTINUE....')
                                gon=input()
                                if gon=='':
                                    teacher_ui()
                                print()
                            elif menuch=='2':
                                print()
                                uid=int(input('Enter the admission no of student to be searched  : '))
                                print()
                                academics()
                                print('-'*70)
                                print()
                                print('CLICK "ENTER" TO CONTINUE....')
                                gon=input()
                                if gon=='':
                                    teacher_ui()
                            elif menuch=='3':
                                print()
                                print('-'*70)
                                update_marks()
                                print()
                                if update_marks()==False:
                                    teacher_ui
                                print('CLICK "ENTER" TO CONTINUE....')
                                gon=input()
                                if gon=='':
                                    teacher_ui()
                            elif menuch.lower()=='log out':
                                print()
                                print('LOGGING OUT OF YOUR ACCOUNT.......')
                                print()
                                homescreen()
                                break
                            elif menucountteach==3:
                                print('Out of attempts')
                                break
                            else:
                                menucounteach+=1
                                print('Try Again !!')
                        break
                else:
                    print('Oops ! OUT OF ATTEMPTS !!')
                    break
            elif tos.lower()=='s':
                for att in range(3):
                    if login_student():
                        print('You have successfully logged in to the app !!')
                        print()
                        print('Welcome back',student_name.split()[0],'!!!')
                        student_ui()
                        while True:
                            menucount=0
                            menuch=input('Enter your menu choice : ')
                            if menuch=='1':
                                print('-'*70)
                                print("CHECK YOUR ACADEMICS".center(70))
                                print('-'*70)
                                academics()
                                print('='*70)
                                print()
                                print('CLICK "ENTER" TO CONTINUE....')
                                gon=input()
                                if gon=='':
                                    student_ui()
                            elif menuch=='2':
                                print()
                                busui()
                                print()
                                print('CLICK "ENTER" TO CONTINUE....')
                                gon=input()
                                if gon=='':
                                    student_ui()
                                    
                            elif menuch=='3':
                                print()
                                feeui()
                                print()
                                print('CLICK "ENTER" TO CONTINUE....')
                                gon=input()
                                if gon=='':
                                    student_ui()
                                
                            elif menuch.lower()=='log out':
                                print()
                                print('LOGGING OUT OF YOUR ACCOUNT.......')
                                print()
                                homescreen()
                                break
                            elif menucount==3:
                                print('Out of attempts')
                                break
                            else:
                                menucount+=1
                                print('Try Again !!')
                                print()
                        break
                else:
                    print('Oops ! OUT OF ATTEMPTS !!')
            else:
                print('Oops ! Try Again')
                print('-'*70)
        elif response1==2:
            print()
            print('TEACHER (T)'.center(70))
            print('STUDENT (S)'.center(70))
            print()
            tos=input('Create account for Teacher or Student (T/S): ')
            if tos.lower()=='t':
                add_teacher()
                print('-'*70)
            elif tos.lower()=='s':
                add_student()
                print('-'*70)
            else:
                print('Oops !! Try again')
        elif creslog==3:
            break
        elif response1==3:
            print('EXITING APPLICATION.......')
            break
        else:
            print('Oops !! Try again')
except Exception as e:
    print()
    print('ERROR - ',e)
    print()
    print('RESTART APPLICATION')
