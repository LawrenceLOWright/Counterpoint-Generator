#First species maker
#Takes user input to write a first species counterpoint
#Lawrence Wright

import random

#valid input array 
valid_input = ["C major", "G major", "D major", "A major", "E major", "B major", "F sharp major", "B sharp major", "F major", "B flat major", "E flat major",
"A flat major", "D flat major", "G flat major", "C flat major"]

#Arrays for each key
cmaj = ["C", "D", "E", "F", "G", "A", "B"] 

#sharp keys
gmaj = ["G", "A", "B", "C", "D", "E", "F#"]
dmaj = ["D", "E", "F#", "G", "A", "B", "C#"]
amaj = ["A", "B", "C#", "D", "E", "F#", "G#"]
emaj = ["E", "F#", "G#", "A", "B", "C#", "D#"]
bmaj = ["B", "C#", "D#", "E", "F#", "G#", "A#"]
fsmaj = ["F#", "G#", "A#", "B", "C#", "D#", "E"]
bsmaj = ["B#", "C#", "D#", "E#", "F#", "G#", "A#"]

#flat keys
fmaj = ["F", "G", "A", "Bb", "C", "D", "E"]
bfmaj = ["Bb", "C", "D", "Eb", "F", "G", "A"]
efmaj = ["Eb", "F", "G", "Ab", "Bb", "C", "D"]
afmaj = ["Ab", "Bb", "C", "Db", "Eb", "F", "G"]
dfmaj = ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"]
gfmaj = ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"]
cfmaj = ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"]

#initializing cantus firmus variables
pitches = [] #blank array to hold pitches
current_pitch = 0 #holds the current pitch
jump = 0 #whether we've jumped 5 or 6 recently
run = 0 #if the whole program is still running 
done = 0 #if the cantus generating bit is running
max = 0 #highest note in the cantus (climax)
max_num = -1 #how many climaxes the cantus has
leap_direction = -1 #what direction the most recent leap was
leap = 0 #whether the cantus lept
last_leap = 0 #whether the cantus lept last turn

#initializing first species variables
fs_pitches = [] #blank array to hold pitches
perfect_consonance = 0 #keeps track of if the generated number is a perfect consonance
last_rand_pitch = -20 #keeps track of the previous pitch
pitch_repeats = 0 #keeps track of how many of the same pitches in a row 
tritone_detector = 0 #keeps track of if the next interval could be a tritone

#get user input
print("Welcome to the first species counterpoint generator! This program generates a cantus firmus and first species counterpoint.\n")

while (run == 0):
    print("Enter 1 to generate just a cantus firmus, and 2 to generate a cantus with counterpoint.")
    c_or_c = input()

    while (c_or_c.isdigit() == False):
        c_or_c = input("Invalid input. Please enter a number between 8 and 16: ")

    c_or_c = int(c_or_c)

    while (c_or_c > 2 or c_or_c < 1):
        c_or_c = input("Invalid input. Please enter 1 or 2: ")
        c_or_c = int(c_or_c)


    print("")
    print("How many measures do you want your cantus to be? Please enter a number between 8 and 16.")

    length = input()

    while (length.isdigit() == False):
        length = input("Invalid input. Please enter a number between 8 and 16: ")

    length = int(length)

    #check if user length input is valid
    while (length > 16 or length < 8):
        length = input("Invalid input. Please enter a number between 8 and 16: ")
        length = int(length)

    print("")

    #Get user input for key

    key = input("Enter 1 for C major, 2 for sharp keys, and 3 for flat keys. \n")

    print("")
    
    while (key.isdigit() == False or int(key) > 3 or int(key) < 1):
        key = input("Please enter a valid input. ")
        print("")

    key = int(key)

    #change key input into usable variables 
    if (key == 1):
        key = cmaj

    if (key == 2):
        key = input("1. G major \n2. D major \n3. A major \n4. E major \n5. B major \n6. F sharp major \n7. B sharp major \n")

        while (key.isdigit() == False or int(key) > 7 or int(key) < 1):
            key = input("Please enter a valid input. ")
            print("")
        
        key = int(key)
        
        if (key == 1):
            key = gmaj 

        if (key == 2):
            key = dmaj 

        if (key == 3):
            key = amaj
        
        if (key == 4):
            key = emaj
        
        if (key == 5):
            key = bmaj
        
        if (key == 6):
            key = fsmaj
        
        if (key == 7):
            key = bsmaj
    
    if (key == 3):
        key = input("1. F major \n2. B flat major \n3. E flat major \n4. A flat major \n5. D flat major \n6. G flat major \n7. C flat major \n")   

        while (key.isdigit() == False or int(key) > 7 or int(key) < 1):
            key = input("Please enter a valid input. ")
            print("")
        
        key = int(key)
        
        if (key == 1):
            key = fmaj 

        if (key == 2):
            key = bfmaj 

        if (key == 3):
            key = efmaj
        
        if (key == 4):
            key = afmaj
        
        if (key == 5):
            key = dfmaj
        
        if (key == 6):
            key = gfmaj
        
        if (key == 7):
            key = cfmaj

    #Cantus maker
    while (done == 0):
        #cantus always starts on do
        pitches.append(0)

        for i in range (length-3):

            #Normal note choosing array
            if (jump == 0):
                rand_note = random.choice([1, 1, 1, 1, 1, 3, 5, 6])
                rand_direction = random.choice([0, 1])
            
            #If we jumped 5 or 6 last time, go one in the opposite direction
            if (jump == 1):
                rand_note = 1
                jump = 0

                if (rand_direction == 0):
                    rand_direction = 1

                if (rand_direction == 1):
                    rand_direction = 0
            
            #If we jumped, make sure to go the opposite direction the next time we jump
            #Also, make sure we don't jump twice in a row
            if (rand_note == 3 or rand_note == 5 or rand_note == 6):
                if (last_leap != 0):
                    rand_note = 1
                    last_leap = 0
                else:
                    last_leap = 1

                if (leap == 0):
                    leap_direction = rand_direction
                    leap = leap + 1
                
                if (leap != 0):
                    if (rand_direction == leap_direction):
                        if (rand_direction == 1):
                            rand_direction = 0

                        if (rand_direction == 0):
                            rand_direction = 1
                        
                        leap_direction = rand_direction

            #check if we jumped 5 or 6 for earlier opposite direction 
            if (rand_note == 5 or rand_note == 6):
                jump = 1

            #Going up
            if (rand_direction == 0):
                current_pitch = current_pitch + rand_note

                #Check if we have multiple climaxes
                if (current_pitch == max):
                    max_num = max_num + 1

                #Check if a note is higher than the previous climax
                if (current_pitch > max):
                    max = current_pitch
                    max_num = 0

            #Going down
            if (rand_direction == 1):
                current_pitch = current_pitch - rand_note
            
            if (i == length-4 and current_pitch == -6):
                current_pitch = 0
            
            if (i == length-4 and current_pitch == 1):
                if (rand_direction == 0):
                    current_pitch = 2

                if (rand_direction == 1):
                    current_pitch = 0

            
            #Make sure notes stay within an octave range
            while (current_pitch >= 7):
                current_pitch = current_pitch - 7
            
            while (current_pitch <= -7):
                current_pitch = current_pitch + 7

            #Add the new pitch to the pitch array

            pitches.append(current_pitch)

        #cantus ends on re do or (very small possibility) ti do
        if (rand_note != 5):
            pitches.append(1)
            pitches.append(0)

        if (rand_note == 5 or rand_note == -5):
            pitches.append(6)
            pitches.append(0)
        
        #If there are multiple climaxes, reset variables and start over
        if (max_num != 0):
            pitches = []
            jump = 0
            max = 0
            max_num = -1
            current_pitch = 0
            leap_direction = -1
            leap = 0
            last_leap = 0

        #if everything is okay, end the loop
        if (max_num == 0):
            done = 1

    #Printing the final cantus
    print("\nYour cantus firmus is: ")

    for i in range(len(pitches)):
        note = pitches[i]
        print(key[note], end = " ")

    print("")
    print("")

    #First species counterpoint generator
    rand_pitch = random.choice([0, 5])
    fs_pitches.append(rand_pitch)
    last_pitch = rand_pitch
    
    for i in range(len(pitches) - 3):
        if (perfect_consonance == 0):
            rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])

        if (perfect_consonance == 1):
            rand_pitch = random.choice([3, 6])
            perfect_consonance = 0

        rand_direction = random.choice([0, 1])

        if (rand_pitch == 0 or rand_pitch == 5):
            if (perfect_consonance == 1):
                perfect_consonance = 0
            
            else:
                perfect_consonance = 1
        
        #Fixing specific errors
        if (pitches[i+1] == 2 and rand_pitch == 3 and rand_direction == 0):
            rand_pitch = random.choice([0, 5, 5, 6, 6, 6, 6])

        if (pitches[i+1] == -2 and rand_pitch == 3 and rand_direction == 1):
            rand_pitch = random.choice([0, 5, 5, 6, 6, 6, 6])
        
        if (pitches[i+1] == 0 and rand_pitch == 6 and rand_direction == 0):
            rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5])

        if (pitches[i+1] == 0 and rand_pitch == 6 and rand_direction == 1):
            rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5])

        #Find out how many times the pitch has repeated
        if (rand_pitch == last_rand_pitch):
            pitch_repeats = pitch_repeats + 1
        
        if (rand_pitch != last_rand_pitch):
            pitch_repeats = 0

        last_rand_pitch = rand_pitch

        if (pitch_repeats > 3):
            if (rand_pitch == 0):
                rand_pitch = random.choice([3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
            
            if (rand_pitch == 3):
                rand_pitch = random.choice([0, 5, 5, 6, 6, 6, 6])
            
            if (rand_pitch == 5):
                rand_pitch = random.choice([0, 3, 3, 3, 3, 6, 6, 6, 6])
            
            if (rand_pitch == 6):
                rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5])


        #add the random number to current pitch
        if (rand_direction  == 0):
            current_pitch = pitches[i+1] + rand_pitch
        
        if (rand_direction  == 1):
            current_pitch = pitches[i+1] - rand_pitch
        
        while (current_pitch >= 7):
            current_pitch = current_pitch - 8
            
        while (current_pitch <= -7):
            current_pitch = current_pitch + 8

        #Error handling (having 1 negative and 1 positive gets trippy)
        if (current_pitch < 0 and pitches[i+1] > 0):
            current_pitch = current_pitch * -1

        if (current_pitch > 0 and pitches[i+1] < 0):
            current_pitch = current_pitch * -1

        #If the last note indicates that there could be a tritone, check closer. If there is a tritone, pick a different note
        if (tritone_detector == 1):
            old_rand_pitch = rand_pitch

            if (first_tritone == 6 and current_pitch == 3):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch
            
            if (first_tritone == 3 and current_pitch == 6):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch
            
            if (first_tritone == -1 and current_pitch == -5):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])

                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch
            
            if (first_tritone == -5 and current_pitch == -1):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch

            if (first_tritone == 3 and current_pitch == -1):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch

            if (first_tritone == -1 and current_pitch == 3):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch
            
            if (first_tritone == 6 and current_pitch == -5):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch
            
            if (first_tritone == -5 and current_pitch == 6):
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
        
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch

            tritone_detector = 0
        
        #Alert the tritone detector for next time!
        if (current_pitch == 3 or current_pitch == 6 or current_pitch == -1 or current_pitch == -5):
            tritone_detector = 1
            first_tritone = current_pitch
        
        #test for a 7th - if the absolute value last pitch + abs of current pitch = 6, it's a 7th
        if (last_pitch != 0 and current_pitch != 0):
            if (((last_pitch*last_pitch)/last_pitch) + ((current_pitch*current_pitch)/current_pitch) == 6):
                old_rand_pitch = rand_pitch
                
                while (rand_pitch == old_rand_pitch):
                    rand_pitch = random.choice([0, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6])
                    
                if (rand_direction  == 0):
                    current_pitch = pitches[i+1] + rand_pitch
            
                if (rand_direction  == 1):
                    current_pitch = pitches[i+1] - rand_pitch
        
        last_pitch = current_pitch

        fs_pitches.append(current_pitch)

    if (pitches[len(pitches) - 2] == 1):
        fs_pitches.append(6)
    
    if (pitches[len(pitches) - 2] == 6):
        fs_pitches.append(1)
    
    fs_pitches.append(0)
    
    if (c_or_c == 2):
        print("Your first species counterpoint is: ")
        for i in range(len(fs_pitches)):
            note = fs_pitches[i]
            print(key[note], end = " ")
        print("")
        print("")

    again = input("Generate another? 1 for yes and 2 to quit.\n")

    while (again.isdigit() == False or int(again) > 2 or int(again) < 1):
        again = input("Please enter a valid input. ")
        print("")

    again = int(again)

    #reset variables for a new cantus
    if (again == 1):
        pitches = []
        current_pitch = 0
        jump = 0
        done = 0
        max = 0
        max_num = 0
        leap_direction = -1
        leap = 0
        last_leap = 0

        fs_pitches = []
        perfect_consonance = 0
        last_rand_pitch = -20
        pitch_repeats = 0
        tritone_detector = 0
        print("")

    #quit
    if (again == 2):
        run = 1
