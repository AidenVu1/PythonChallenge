T = "1"
E = "00"
A = "0010"
K = "0110"
C = "1010"
R = "1110"
TEACRATE = T+E+A+C+R+A+T+E
EATCAKE = E+A+T+C+A+K+E
TAKECARE = T+A+K+E+C+A+R+E
RETAKE = R+E+T+A+K+E
if TEACRATE == "1001001100010100010111000":
    print("The answer is: TEACRATE - " + TEACRATE)
elif EATCAKE == "1001001100010100010111000":
    print("The answer is: EATCAKE - " + EATCAKE)
elif TAKECARE == "1001001100010100010111000":
    print("The answer is: TAKECARE - " + TAKECARE)
elif RETAKE == "1001001100010100010111000":
    print("The answer is: RETAKE - " + RETAKE)