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
        
#Test 4 prints
#Added after Commit 6
Route2_List = ["Go to the party",
              "Stay home",
              "Stay home and drink with friends",
              "Drink and then go to the party"
              ]
print("First Decision: Theres an Exam tommorrow what will you do?")
print(f"[0]{Route2_List[0]}")
print(f"[1]{Route2_List[1]}")
print(f"[2]{Route2_List[2]}")
print(f"[3]{Route2_List[3]}")
print("----------------------------------")
Route2_choice = int(input())
if Route2_choice not in [0, 1, 2, 3]:
        print("Invalid Choice: Decide again.")
if Route2_choice == 0:
    print("----------------------------------")
    print("Go to the party")
    print("You get to the party and realize you dont have enough money and get laughed at by your friends")
    social_points -= 15
    stress_level += 30
    print("SOCIAL POINTS DECREASED BY 15. HOW HORRIBLE!!")
    print("STRESS LEVEL INCREASED BY 30")
    print(f'{social_points:.2f}')
    print(f'{stress_level:.2f}')
elif Route2_choice == 1:
    print("----------------------------------")
    print("Stay home")
    print("You stay home and watch tv with your rommate and do whatever work is due in the future")
    social_points += 5
    study_hours += 2
    stress_level -= 20
    print("SOCIAL POINTS INCREASED BY 5!!")
    print("STUDY HOURS INCREASED BY 2!!")
    print("STRESS LEVEL DROPPED BY 20 (DUE TO IT BEING KIND OF RELAXING)")
    print(f'{social_points:.2f}')
    print(f'{study_hours:.2f}')
    print(f'{stress_level:.2f}')
elif Route2_choice == 2:
    print("----------------------------------")
    print("Stay home and drink with friends")
    print("You and your friends get into an argument while drunk and they beat you up.")
    social_points -= 25
    stress_level += 20
    print("SOCIAL POINTS DESCREASED BY 25!!")
    print("STRESS LEVEL INCREASED BY 20")
    print(f'{social_points:.2f}')
    print(f'{stress_level:.2f}')
elif Route2_choice == 3:
    print("----------------------------------")
    print("Drink and then go to the party")
    print("Due to drinking before the party you dont remember much but checking your phone it looks like you had a good time")
    social_points += 5
    study_hours -= 2
    stress_level += 20
    print("SOCIAL POINTS INCREASED BY 5!!")
    print("STUDY HOURS DECREASED BY 2(DUE TO THE HEADACHE THE NEXT DAY)")
    print("STRESS LEVEL INCREASED BY 20(DUE TO YOU NOT KNOWING WHAT HAPPENED THAT NIGHT")
    print(f'{social_points:.2f}')
    print(f'{study_hours:.2f}')
    print(f'{stress_level:.2f}')
print("----------------------------------")
print("FINAL RESULTS")
print(f'Current GPA: {current_gpa:.2f}')
print(f'Study Hours: {study_hours}')
print(f'Social Points: {social_points}')
print(f'Stress Level: {stress_level}')

#Different Endings
if current_gpa >= 3.5:
    if stress_level <= 40:
        print("Sochlar Ending: You aced your semester! Balanced, calm, and thriving.(There is 8 endings try to find all of them)")
    elif stress_level > 40 and stress_level <= 70:
        print("Average student Ending 2: Strong grades, but you're feeling the pressure. Take a break!(There is 8 endings try to find all of them)")
    else:
        print("Good student Ending 3: High achiever, but you're burned out. Be careful next semester. (There is 8 endings try to find all of them)")
elif 2.5 <= current_gpa < 3.5:
    if study_hours >= 8 and social_points >= 50:
        print("decent student Ending 4: You're doing fine! A little more effort and you'll be a star.(There is 8 endings try to find all of them)")
    else:
        print("Mid student Ending 5: You're doing okay, but you're not reaching your full potential.(There is 8 endings try to find all of them)")
else:
    if stress_level > 80:
        print("BAD Ending 6: You're overwhelmed and failing. Consider asking for help.(There is 8 endings try to find all of them)")
    elif social_points < 20:
        print("Loner Ending 7: You're isolated and struggling. Try reaching out more.(There is 8 endings try to find all of them)")
    else:
        print("C's get Degrees Ending 8: You barely made it through. Let's do better next time.(There is 8 endings try to find all of them)")

