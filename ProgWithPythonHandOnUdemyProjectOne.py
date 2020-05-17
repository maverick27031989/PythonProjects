import operator


def studentDetails():
    print()
    print('Enter the number of students : ')
    numberOfStudents = int(input())
    studentRecord = {}
    for i in range(0, numberOfStudents):
        print('Enter the name of the student : ')
        name = input()
        print('Enter the score of the student : ')
        score = int(input())
        studentRecord[name] = score
    return studentRecord
    print()


def rankStudents(studentRecord):
    sortedStudentRecords = sorted(studentRecord.items(), key=operator.itemgetter(1), reverse=True)
    print("{} has secured first rank by scoring {} marks".format(sortedStudentRecords[0][0], sortedStudentRecords[0][1]))
    print("{} has secured second rank by scoring {} marks".format(sortedStudentRecords[1][0], sortedStudentRecords[1][1]))
    print("{} has secured third rank by scoring {} marks".format(sortedStudentRecords[2][0], sortedStudentRecords[2][1]))
    print()
    return sortedStudentRecords


def rewardStudents(sortedStudentRecords, reward):
    print("{} has awarded ${} for securing first rank".format(sortedStudentRecords[0][0], reward[0]))
    print("{} has awarded ${} for securing second rank".format(sortedStudentRecords[1][0], reward[1]))
    print("{} has awarded ${} for securing third rank".format(sortedStudentRecords[2][0], reward[2]))
    print()


def appreciateStudent(sortedStudentRecords):
    for record in sortedStudentRecords:
        if record[1] >= 950:
            print('Well Done {} on Scoring more than {} marks !!!'.format(record[0], record[1]))
        else:
            break


sd = studentDetails()
rk = rankStudents(sd)

reward = (500, 300, 100)
rewardStudents(rk, reward)

appreciateStudent(rk)
