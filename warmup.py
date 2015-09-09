# Simple Array Sum
def simpleArraySum():
    n = int(raw_input())                 # first input
    a = map(int,raw_input().split())     # second input
    ans = 0

    for i in range(n):
        ans += a[i]

    print ans


# A Very Big Sum
def aVeryBigSum():
    n = int(raw_input())                 # first input integer N
    a = map(int,raw_input().split())     # second input array A
    ans = 0

    for i in range(n):
        ans += a[i]

    print ans                            # output result


# Diagonal Difference
def diagonalDifference():
    n = int(raw_input())                 # first input integer N
    first_diag = 0
    second_diag = 0

    for i in range(n):
        a = raw_input().split()          # following input assigning rows of array A to a
        first_diag += int(a[i])
        second_diag += int(a[n-1-i])

    if first_diag >= second_diag:
        print first_diag - second_diag
    else:
        print second_diag - first_diag


# Plus Minus
def plusMinus():
    n = int(raw_input())                # total number of elements in array
    a = map(int, raw_input().split())   # input array, mapped to integer
    pos, neg = 0, 0

    for i in range(n):
        if a[i] > 0:
            pos += 1.
        elif a[i] < 0:
            neg += 1.

    for ans in [pos/n, neg/n, 1-(pos+neg)/n]:
        print "%.3f" %(ans)


# Staircase
def staircase():
    h = int(raw_input())        # height of the staircase
    for i in range(h):
        print " " * (h-i-1) + "#" * (i+1)



# Time Conversion
def timeCoversion():
    timeAMPM = raw_input()          # time in AM/PM format
    hour = timeAMPM[0:2]            # extract hour

    if timeAMPM[8] == "P":
        if int(hour) != 12:
            hour = str(int(hour) + 12)
    elif timeAMPM[8] == "A":
        if int(hour) == 12:
            hour = "00"

    print hour + timeAMPM[2:-2]


# Library Fine
def libraryFine():
    actual = map(int, raw_input().split())
    expect = map(int, raw_input().split())
    fine = 0

    if actual[2] > expect[2]:           # first compare year
        fine = 10000
    elif actual[2] == expect[2]:        # same year
    
        if actual[1] > expect[1]:       # second compare month
            fine = 500 * (actual[1]-expect[1])
        elif actual[1] == expect[1]:    # same month
        
            if actual[0] > expect[0]:   # third compare date
                fine = 15 * (actual[0]-expect[0])
        else:
            pass
    else:
        pass                            # returned years before

    print fine


# Extra long factorials
def extraLongFactorials():
    n = int(raw_input())                 # input N

    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n*factorial(n-1)

    print factorial(n)


if __name__ == "__main__":
    simpleArraySum()
    #aVeryBigSum()
    #diagonalDifference()
    #extraLongFactorials()
    #plusMinus()
    #staircase()
    #timeCoversion()
    #libraryFine()
    #extraLongFactorials()