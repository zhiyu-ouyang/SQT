# Python Term Project
# Chenqi Liang, Jiaqi Bai, Zhiyu Ouyang
from prettytable import PrettyTable

# transfer the students.txt file to a list
fhandle=open('students.txt')
student_all=[]
for record in fhandle:
    record=record.rstrip()
    record=record.split('\t')
    student=[]
    for info in record:
        student.append(info)
    student_all.append(student)
    record_len = len(student_all)
    student_list = []
    for i in range(1, record_len):
        student_list.append(student_all[i])

graduation_year_lst=[]
for i in student_list:
    graduation_year_lst.append(i[3])

def Name_Choice_Information():
    print('What information do you want to get?')
    print('1. All information')
    print('2. Graduation Year')
    print('3. Graduation Term')
    print('4. Degree Program')

# The welcome page
print('Welcome to Student Query Tool!')

while True:
    # The choice pages
    print()
    print('How do you want to query?')
    print('1. Query by Student Name/ Student ID')
    print('2. Query by Graduation Year')
    print('3. Query by Graduation Term')
    print('4. Query by Degree program')
    print('5. Query information of all students')
    query_choice = input('Please enter the number (1-5): ')

    # Query by Name
    if query_choice == '1':
        query_choice_name = input('Do you know the exact Name or ID? (Y/N)')
        if query_choice_name == 'y' or query_choice_name == 'Y':
            print('1. Query by Name')
            print('2. Query by ID')
            query_choice_name1 = input('Please enter the number: ')

            # Query by first name and last name of a student
            if query_choice_name1 == '1':
                Last_Name = input('Please enter Last Name of student: ')
                First_Name = input('Please enter First Name of student: ')
                Last_Name_List = []
                First_Name_List = []
                for studentinfo in student_list:
                    Last_Name_List.append(studentinfo[1].lower())
                    First_Name_List.append(studentinfo[2].lower())
                if (Last_Name.lower() not in Last_Name_List) and (First_Name.lower() not in First_Name_List):
                    print('Sorry! There is no record found.')
                    continue

                Name_Choice_Information()
                choice_information = input('Please enter the number: ')

                for studentinfo in student_list:
                    if studentinfo[2].lower() == First_Name.lower() and studentinfo[1].lower() == Last_Name.lower():
                        if choice_information == '1':  # print all the information of the student
                            for i in range(6):
                                print(student_all[0][i]+': '+ studentinfo[i])
                        elif choice_information == '2':  # print graduation year of the student
                            for i in range(4):
                                print(student_all[0][i]+': '+ studentinfo[i])
                        elif choice_information == '3':   # print graduation term of the student
                            for i in [0, 1, 2, 4]:
                                print(student_all[0][i]+': '+ studentinfo[i])
                        elif choice_information == '4':   # print degree program of the student
                            for i in [0, 1, 2, 5]:
                                print(student_all[0][i]+': '+ studentinfo[i])
                        else:
                                print('Error!')
                                continue

           # Query by student ID
            elif query_choice_name1 == '2':
                ID = input('Please enter ID of student: ')
                ID_List = []
                for studentinfo in student_list:
                    ID_List.append(studentinfo[0])
                if ID not in ID_List:
                    print('Sorry! There is no record found.')
                    continue

                Name_Choice_Information()
                choice_information = input('Please enter the number: ')
                for studentinfo in student_list:
                    if studentinfo[0] == ID:
                        if choice_information == '1':
                            for i in range(6):
                                print(student_all[0][i] + ': ' + studentinfo[i])
                        elif choice_information == '2':
                            for i in range(4):
                                print(student_all[0][i]+': '+ studentinfo[i])
                        elif choice_information == '3':
                            for i in [0, 1, 2, 4]:
                                print(student_all[0][i]+': '+ studentinfo[i])
                        elif choice_information == '4':
                            for i in [0, 1, 2, 5]:
                                print(student_all[0][i]+': '+ studentinfo[i])
                        else:
                                print('Error!')
                                continue
            else:
                print('Error!')
                continue

        # Query by the start of the last name of students
        elif query_choice_name == 'n' or query_choice_name == 'N':
            name_start = input('Please enter the start letters of the Last Name: ')
            List_Name_Start = []
            for studentinfo in student_list:
                list_name_start = studentinfo[1][0:len(name_start)].lower()
                List_Name_Start.append(list_name_start)
            if name_start.lower() not in List_Name_Start:
                print('Sorry! There is no record found.')
                continue

            Name_Choice_Information()
            choice_information = input('Please enter the number: ')

            # print all the information of the students
            if choice_information == '1':
                table = PrettyTable(student_all[0])
                for studentinfo in student_list:
                    list_name_start = studentinfo[1][0:len(name_start)]
                    if list_name_start.lower() == name_start.lower():
                        table.add_row(studentinfo)
                print(table)

            # print graduation year of the student
            elif choice_information == '2':
                table = PrettyTable(student_all[0][0:4])
                for studentinfo in student_list:
                    list_name_start = studentinfo[1][0:len(name_start)]
                    if list_name_start.lower() == name_start.lower():
                        table.add_row(studentinfo[0:4])
                print(table)

            # print graduation term of the student
            elif choice_information == '3':
                title = student_all[0][0:3]
                title.append(student_all[0][4])
                table = PrettyTable(title)
                for studentinfo in student_list:
                    list_name_start = studentinfo[1][0:len(name_start)]
                    if list_name_start.lower() == name_start.lower():
                        stu_term = studentinfo[0:3]
                        stu_term.append(studentinfo[4])
                        table.add_row(stu_term)
                print(table)

            # print degree program of the student
            elif choice_information == '4':
                title = student_all[0][0:3]
                title.append(student_all[0][5])
                table = PrettyTable(title)
                for studentinfo in student_list:
                    list_name_start = studentinfo[1][0:len(name_start)]
                    if list_name_start.lower() == name_start.lower():
                        degree = studentinfo[0:3]
                        degree.append(studentinfo[5])
                        table.add_row(degree)
                print(table)
            else:
                print('Error!')

        else:
            print('Error!')
            continue

    # Query by Graduation Year
    elif query_choice == '2':
        graduation_year=input('Please enter the Graduation Year: ')
        if not graduation_year in graduation_year_lst:
            print("Sorry! There is no record found.")
            continue
        on_after=input('If this year, enter 1; after this year, enter 2: ')
        # for students graduating on a certain year
        if on_after=='1':
            print()
            print('1. Number and percent of students')
            print('2. Number and percent of students in each program')
            print('3. Number and percent of students in each term')
            print('4. All records of students')
            option=input('What information do you want to get? Please enter the number: ')
            # Number and percent of students on a certain year
            if option=='1':
                student_count=0
                for i in student_list:
                    if i[3]==graduation_year:
                        student_count=1+student_count
                print('The number of students who graduated in', graduation_year,'is',student_count)
                print(f'The percent of students who graduated in {graduation_year} is {(student_count/(record_len-1) * 100):.2f}%')
            elif option=='2':
                # Number and percent of students in each program on a certain year
                degree_dict={}
                degree_dict_all={}
                for i in student_list:
                    degree_dict_all[i[5]]=degree_dict_all.get(i[5],0)+1
                    if i[3]==graduation_year:
                        degree_dict[i[5]]=degree_dict.get(i[5],0)+1
                for key,value in degree_dict.items():
                    print('The number of students who graduated in', key, 'program is',value, 'in', graduation_year)
                    for k,v in degree_dict_all.items():
                        if key==k:
                            print(f'The percent of students who graduated in {key} program is {(value/v * 100):.2f}% in {graduation_year}')
            elif option=='3':
                # Number and percent of students in each term on a certain year
                term_dict={}
                term_dict_all={}
                for i in student_list:
                    term_dict_all[i[4]]=term_dict_all.get(i[4],0)+1
                    if i[3]==graduation_year:
                        term_dict[i[4]]=term_dict.get(i[4],0)+1
                for key,value in term_dict.items():
                    print('The number of students who graduated in', key, 'term is',value, 'in', graduation_year)
                    for k,v in term_dict_all.items():
                        if key==k:
                            print(f'The percent of students who graduated in {key} term is {(value/v * 100):.2f}% in {graduation_year}')
            elif option=='4':
                # all information of students on a certain year
                a=PrettyTable(['ID','Last','First','GradYear','GradTerm','DegreeProgram'])
                for i in student_list:
                    if i[3]==graduation_year:
                        a.add_row(i)
                print(a)
            else:
                print('Error!')
                continue

        # for students graduating after a certain year
        elif on_after=='2':
            print()
            print('1. Number and percent of students')
            print('2. Number and percent of students in each program')
            print('3. Number and percent of students in each term')
            print('4. All records of students')
            option=input('What information do you want to get? Please enter the number: ')
            if option=='1':
                # Number and percent of students after a certain year
                student_count=0
                for i in student_list:
                    if i[3]>graduation_year:
                        student_count=1+student_count
                print('The number of students who graduated after', graduation_year,'is',student_count)
                print(f'The percent of students who graduated after {graduation_year} is {(student_count/(record_len-1) * 100):.2f}%')
            elif option=='2':
                # Number and percent of students in each program after a certain year
                degree_dict={}
                degree_dict_all={}
                for i in student_list:
                    degree_dict_all[i[5]]=degree_dict_all.get(i[5],0)+1
                    if i[3]>graduation_year:
                        degree_dict[i[5]]=degree_dict.get(i[5],0)+1
                for key,value in degree_dict.items():
                    print('The number of students who graduated in', key, 'program is',value, 'after', graduation_year)
                    for k,v in degree_dict_all.items():
                        if key==k:
                            print(f'The percent of students who graduated in {key} program is {(value/v * 100):.2f}% after {graduation_year}')
            elif option=='3':
                # Number and percent of students in each term on after certain year
                term_dict={}
                term_dict_all={}
                for i in student_list:
                    term_dict_all[i[4]]=term_dict_all.get(i[4],0)+1
                    if i[3]>graduation_year:
                        term_dict[i[4]]=term_dict.get(i[4],0)+1
                for key,value in term_dict.items():
                    print('The number of students who graduated in', key, 'term is',value, 'after', graduation_year)
                    for k,v in term_dict_all.items():
                        if key==k:
                            print(f'The percent of students who graduated in {key} term is {(value/v * 100):.2f}% after {graduation_year}')
            elif option=='4':
                # All information of students after a certain year
                a=PrettyTable(['ID','Last','First','GradYear','GradTerm','DegreeProgram'])
                for i in student_list:
                    if i[3]==graduation_year:
                        a.add_row(i)
                print(a)
            else:
                print('Error!')
                continue
        else:
            print('Error!')
            continue

     #Query by Graduation Term
    elif query_choice == '3':
         query_choice_term = input('Please enter the Graduation Term (Fall/Spring/Summer):')
         term_empty = []
         for student_info_term in student_list:
             if student_info_term[5].lower() == query_choice_term.lower():
                 term_empty.append(student_info_term)
         if term_empty == []:
             print('Sorry! There is no record found.')
             continue

         print('What information do you want to get?')
         print('1. Number and percent of students')
         print('2. Number and percent of students in each program')
         print('3. All records of students')

         query_choice_term1 = input('Please enter the number: ')
         n = 0
         term_info = []
         program = []
         prog_n = []
         term_table = PrettyTable(student_all[0])

         #Print number and percent of students
         if query_choice_term1 == '1':
             for student_info_term in student_list:
                 if student_info_term[4].lower() == query_choice_term.lower():
                     n += 1
                 print('Number of students who graduated in', query_choice_term, 'term:', n)
                 print(f'Percent of students who graduated in {query_choice_term} term: {(n / record_len * 100):.2f}%')

         #Print number and percent of students in each program
         elif query_choice_term1 == '2':
             for student_info_term in student_list:
                 if student_info_term[4].lower() == query_choice_term.lower():
                     term_info.append(student_info_term)
             for each_program in term_info:
                 if not each_program[5] in program:
                     program.append(each_program[5])
             for prog in program:
                 m = 0
                 for each_program in term_info:
                      if each_program[5] == prog:
                          m += 1
                 prog_n.append(m)
             for p in range(0, len(program)):
                 print('Number of students who graduated in', program[p], 'term:', prog_n[p])
                 print(f'Percent of students who graduated in {program[p]} term: {(prog_n[p] / (len(term_info) - 1) * 100):.2f}%')

         #Print all records of students
         elif query_choice_term1 == '3':
             for student_info_term in student_list:
                 if student_info_term[4].lower() == query_choice_term.lower():
                     term_table.add_row(student_info_term)
             print(term_table)

         else:
             print('Error')
             continue

    #Query by Graduation Program
    elif query_choice == '4':
         query_choice_program = input('Please enter the Degree Program:')
         program_empty = []
         for student_info_program in student_list:
             if student_info_program[5].lower() == query_choice_program.lower():
                 program_empty.append(student_info_program)
         if program_empty == []:
             print('Sorry! There is no record found.')
             continue

         print('What information do you want to get?')
         print('1. Number and percent of students in each graduation year')
         print('2. All records of students who graduated in an exact year')
         print('3. All records of students')
         query_choice_program1 = input('Please enter the number: ')

         n = 0
         program_info = []
         year = []
         year_n = []
         program_table = PrettyTable(student_all[0])

         #Print number and percent of students in each graduation year
         if query_choice_program1 == '1':
             for student_info_program in student_list:
                 if student_info_program[5].lower() == query_choice_program.lower():
                     program_info.append(student_info_program)
             for each_year in program_info:
                 if not each_year[3] in year:
                     year.append(each_year[3])
             for y in year:
                 m = 0
                 for each_year in program_info:
                     if each_year[3] == y:
                         m += 1
                 year_n.append(m)
             for e in range(0, len(year)):
                 print('Number of students who graduated in', year[e], ':', year_n[e])
                 print(f'Percent of students who graduated in {year[e]} term: {(year_n[e] / (len(program_info) - 1) * 100):.2f}%')

         #Print all records of students who graduated in an exact year
         elif query_choice_program1 == '2':
             exact_year = input('Please enter the graduation year: ')
             for student_info_program in student_list:
                 if student_info_program[5].lower() == query_choice_program.lower() and student_info_program[3] == exact_year:
                     program_table.add_row(student_info_program)
                     program_empty.append(student_info_program)
             if program_empty == []:
                 print('Sorry! There is no record found.')
             else:
                 print(program_table)

         #Print all records of students
         elif query_choice_program1 == '3':
             for student_info_program in student_list:
                 if student_info_program[5].lower() == query_choice_program.lower():
                     program_table.add_row(student_info_program)
             print(program_table)

    # Query information of all students
    elif query_choice == '5':
         b=PrettyTable(['ID','Last','First','GradYear','GradTerm','DegreeProgram'])
         for i in student_list:
             b.add_row(i)
         print(b)

    else:
        print('Error!')
        continue

    #Ask users if they what to keep querying
    continue_option=input('Press any button to keep querying. Or press N to quit.')
    if continue_option=='N' or continue_option=='n':quit()
    else:
        continue
