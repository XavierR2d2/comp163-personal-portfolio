student_name = "XavierRothwell"
current_gpa = float(3.2)
study_hours = int(23)
social_points = int(35)
stress_level = int(74)

#Added after Commit 1
print("Pick a Difficulty Easy(12), Medium(15), or Hard(18):")
Level_choice = input()
Easy = ("Easy Difficulty: 12 Credits")
Medium = ("Medium Difficulty: 15 Credits")
Hard = ("Hard Difficulty: 18 Credits")

#Added after Commit 2
print("")
print("First Decision: Theres an Exam tommorrow what will you do?")
print(f"[0]{Route_List[0]}")
print(f"[1]{Route_List[1]}")
print(f"[2]{Route_List[2]}")
print(f"[3]{Route_List[3]}")
print("----------------------------------")
Route_choice = int(input())
if Route_choice not in [0, 1, 2, 3]:
        print("Invalid Choice: Decide again.")
if Route_choice == 0:
    print("----------------------------------")
    print("You play outside all day and forget all about the exam[]0")
    print("YOU FAILED")
elif Route_choice == 1:
    print("----------------------------------")
    print("You all day, your friends are mad at you but at least you memorized the material.")
    print("YOU PASS WITH FLYING COLORS")
elif Route_choice == 2:
    print("----------------------------------")
    print("You study for the Exam for a couple hours then went to play with your friends still memorizing most of the material needed.")
    print("YOU BARELY PASS BUT AT LEAST YOU HAD FUN AND PASS I GUESS")
elif Route_choice == 3:
    print("----------------------------------")
    print("You played outside all day and studied all night but when you tried to take an hour nap before you had to get to the exam you slept through it")
    print("YOU WERE ABLE TO RETAKE THE EXAM ON ANOTHER DAY THANKFULLY BUT DID YOU LEARN YOUR LESSON?")
    print("Y/N")
    Answer = input()
    if Answer == "Y":
        print("----------------------------------")
        print("YOU PASSED DONT LET IT HAPPEN AGAIN")
    if Answer == "N":
        print("----------------------------------")
        print("YOU GO BACK AND DO THE SAME THING AGAIN MISSING THE MAKE UP EXAM TIME")
        print("YOU FAILED")
    if Route_choice not in [0, 1, 2, 3]:
            print("Invalid Choice: Decide again.")
