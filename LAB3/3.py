with open('LAB3/subjectsTask3.txt', 'r') as fileSubjects:
    subjects = fileSubjects.readlines()
    dictSubjects = {}
    for subject in subjects:
        name = subject.split(': ')[0]
        AllLessons = subject.split(': ')[1].split(' ')
        lessons = 0
        for item in AllLessons:
            lessons += int(''.join(x for x in item if x.isdigit()))
        dictSubjects[name] = lessons
print(dictSubjects)