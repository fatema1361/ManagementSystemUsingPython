class StudentDatabase:
    student_list=[]
    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)

class Student:
    def __init__(self,student_id,name,department,is_enrolled=True):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=is_enrolled

        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print("Error:Student is already enrolled.")
        else:
            self.__is_enrolled=True
            print("Student enrolled successfully!")
        
    def drop_student(self):
        if not self.__is_enrolled:
            print("Error:Student is not enrolled.")
        else:
            self.__is_enrolled=False
            print("Student dropped successfully!")

    def view_student_info(self):
        print("\n----Student Information------\n")
        print("Student Id:",self.__student_id)
        print("Name",self.__name)
        print("Department",self.__department)

        if self.__is_enrolled:
            print("Status: Enrolled")
        else:
            print("Status: Not Enrolled")


s1=Student("001","fatema","IIT",True)
s2=Student("002","fate","IIT",True)
s3=Student("003","tem","IIT",False)

while True:
    print("\n----Student database System----\n")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
   
    choice=input("Enter your choice: ")
    if choice=="1":
      if not StudentDatabase.student_list:
        print("No students found")
      else:
        for student in StudentDatabase.student_list:
            student.view_student_info()

    elif choice=="2":
        student_id=input("Enter Student Id: ")
        found=False
        for student in StudentDatabase.student_list:
            if student.get_student_id()==student_id:
                student.enroll_student()
                found=True
                break
        if not found:
            print("Error:Invalid Student Id.")
    elif choice=="3":
        student_id=input("Enter Student Id: ")
        found=False
        for student in StudentDatabase.student_list:
            if student.get_student_id()==student_id:
                student.drop_student()
                found=True
                break

        if not found:
            print("Error:Invalid Student Id.")
    elif choice=="4":
        print("Thank you for using Student Database System!")   
        break
    else:
        print("Invalid choice! Please select 1-4.")
        
        