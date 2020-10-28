
def getEmailList(S, C):
    if len(S) == 0 or len(C) == 0:
        return "One or more input values missing."
    employees = S.split(",")
    processedEmployees = []
    employeeInfoList = []
    for i in employees:

        i = i.strip()
        iSplit = i.split(" ")

        firstInitial = i[0]
        middleNameInital = ""
        lastName = "".replace("-", "")

        if len(iSplit) == 2:
            lastName = iSplit[1].replace("-", "")[:8]
        else:
            middleNameInital = iSplit[1][0]
            lastName = iSplit[2].replace("-", "")[:8]

        employeeInfo = "{} <{}{}{}@{}.com>".format(
            i, firstInitial, middleNameInital, lastName, C)

        if employeeInfo not in employeeInfoList:
            employeeInfoList.append(employeeInfo)
            processedEmployees.append(i)
        elif i in processedEmployees:
            repeatedNames = processedEmployees.count(i)
            employeeInfo = "{} <{}{}{}{}@{}.com>".format(
                i, firstInitial, middleNameInital, lastName, repeatedNames, C)
            employeeInfoList.append(employeeInfo)
            processedEmployees.append(i)

    return ", ".join(employeeInfoList)


S = "John Doe, John Doe, John Doe, John Ham Sandich, Deliria Ortega Gonzalez, Hippo Harry Pot-imusness"
C = "Interactive"

print(getEmailList(S,C))
