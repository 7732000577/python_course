class Student:
    def __init__(self,first_name,last_name,courses=None):
        self.first_name = first_name
        self.last_name = last_name
        #self.courses = courses
        if courses==None:
            self.courses = []
        else:
            self.courses = courses

    def add_courses(self,courses):
        if courses in self.courses:
            print("already enrolled ")
        else:
            self.courses.append(courses)

    def remove_courses(self,courses):
        if courses not in self.courses:
            print("already not enrolled")
        else:
            self.courses.remove(courses)

    # def len(self):
    #     return len(self.courses)
    def find_in_file(self,filename):

        with open("test.txt") as f:
            for line in f:
                first_name,last_name,courses = Student.prep_record(line.strip())
                student_read_in = Student(first_name,last_name,courses)
                if self == student_read_in:
                    return True
            return False

    def add_in_file(self,filename):
        if Student.find_in_file(self,filename):
            return "record already exist"
        else:
            add_record = Student.prep_to_write(self.first_name,self.last_name,self.courses)
            #to add_lines
            with open(filename,"+a") as to_write:
                to_write.write(add_record+"\n")
            return "record_added"

    @staticmethod
    def prep_record(line):
            line = line.split(":")
            line1 = line[0].split(",")
            first_name = line1[0]
            last_name = line1[1]
            courses = line[1].rstrip().split(",")
            return first_name,last_name,courses


    @staticmethod
    def prep_to_write(first_name,last_name,courses):
        full_name = first_name +","+last_name
        courses = ",".join(courses)
        return full_name+":"+courses

    def __len__(self):
        return len(self.courses)

    def __eq__(self,other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name


    def __str__(self):
        return f'first name {self.first_name.capitalize()}\
        \nlast_name {self.last_name.capitalize()}\
        \ncourses: {",".join(map(str.capitalize,self.courses))}'

class StudentAthlete(Student):
    def __init__(self,first_name,last_name,courses=None,sport = None):
        super().__init__(first_name,last_name,courses)
        self.sport = sport

courses = ['python','java','ruby']
first_instance = Student('chandu','shekhar',courses)
print(first_instance.find_in_file("test.txt"))
print(first_instance.add_in_file("test.txt"))

second_instance = Student("dhiru","Kasaudhan",courses)
print(second_instance.find_in_file("test.txt"))
print(second_instance.add_in_file("test.txt"))
# print(first_instance.first_name)
# print(first_instance.last_name)
# print(first_instance.courses
#
# first_instance.remove_courses('java')
# print(first_instance.courses)
#
# first_instance.add_courses('c++')
# print(first_instance.courses)
#
# print(first_instance)
# print(str(first_instance))
# print(first_instance.len())
# #print(len(first_instance))
# print(first_instance.__str__())
# print(first_instance.__dir__)
# print(dir(first_instance))

bade = StudentAthlete('shekhar','chandu',courses,'Basketball')
print(bade.sport)
check = isinstance(bade,StudentAthlete)
print(check)
