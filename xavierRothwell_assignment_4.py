#Test case 1
student_name = input("Name?: ")
current_gpa = float(input("GPA? (1-4): "))
if (1.0 > current_gpa) or (current_gpa > 4.0):
    print("GPA must be between 1.0 and 4.0.")
study_hours = int(input("Study Hours?(1-12): "))
if study_hours > 13:
    print("Try again Be Realistic.")
social_points = int(input("Social status? (1-100): "))
if (1 > social_points) or (social_points > 100):
    print("Only input 1-100.")
stress_level = int(input("Stress Level? (1-100): "))
if (1 > stress_level) or (stress_level > 100):
    print("Only input 1-100.")
print("----------------------------------")

#Added after Commit 1
print("Pick a Difficulty Easy(12), Medium(15), or Hard(18):")
Level_choice = input()
Easy = ("Easy Difficulty: 12 Credits")
Medium = ("Medium Difficulty: 15 Credits")
Hard = ("Hard Difficulty: 18 Credits")

#Added after Commit 2
Route_List = ["Play Outside in the Snow with friends",
              "Study for your mid Term exam, that is tomorrow",
              "Study for a couple hours then go play in the snow",
              "Play Outside all day with your friends then study all night"
              ]

#Test 1 Prints
#Added after Commit 3
print(f'Student Name: {student_name}')
print(f'Current GPA: {current_gpa:.2f}')
print(f'Study Hours: {study_hours}')
print(f'Social Points: {social_points}')
print(f'Stress Level: {stress_level}\n')

#Test 2 Prints
#Added after Commit 4
print("Make Your Choice:")
if Level_choice == "Easy":
    print(f"Mode Chosen: {Easy}")
elif Level_choice == "Medium":
    print(f"Mode Chosen: {Medium}")
elif Level_choice == "Hard":
    print(f"Mode Chosen: {Hard}")
else:
    print("Invalid Choice: Decide again.")
print("----------------------------------")
print("")
print("First Decision: Theres an Exam tommorrow what will you do?")
print(f"[0]{Route_List[0]}")
print(f"[1]{Route_List[1]}")
print(f"[2]{Route_List[2]}")
print(f"[3]{Route_List[3]}")
print("----------------------------------")
Route_choice = int(input())
if Route_choice is not ["0", "1", "2", "3"]:
    print("Invalid Choice: Decide again.")
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


#Test 3 prints
#Added after Commit 5
Study_choices = ["Programming", "Math", "English", "History"]
print("What subject would you like to study? (Only Pick: Programming, Math, English, History): ")
Study_option_chosen = input()
if Study_option_chosen not in Study_choices:
    print("Invalid Choice: Decide again.")
else:
    if (Study_option_chosen in ["Programming", "Math"]) and (stress_level < 80):
        current_gpa += 0.1
        print("YOUR GPA INCREASED BY 0.1!!")
    elif Study_option_chosen in ["English", "History"]:
        social_points += 5
        print("SOCIAL POINTS INCREASED BY 5!!")
    else:
        print("GPA DIDN'T GO UP — NO PAIN, NO GAIN (STRESS LEVEL WASN'T LOW ENOUGH)")
