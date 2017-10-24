import simpleaudio as sa
import time



def welcome():
    print("      _______________________       ")
    print("    /                         \     ")
    print("   /  Made by Martin Haasdijk  \    ")
    print("  /            /  \             \   ")
    print("  \           /    \            /   ")
    print("   \          \    /           /    ")
    print("    \          \  /           /     ")
    print("      ----------------------        ")
    print("Welcome to this awesome beatmaker")

    while True:
        startUp=input("What would you like to do?   (makebeat/quit)  --> ")
        if startUp=="makebeat":
            print("opening beatmaker")
            break
        if startUp=="quit":
            print("Closing beatmaker")
            quit()
        else:
            print("Invalid option")
            continue

welcome()


#input questions
    #time signiture
while True:
    try:
        timesig = input("What time signiture would you like to hear? --> ")
        timesig = timesig.strip().split("/") #timesig is now a list with [beats, count]

        beatsPerMeasure = int(timesig[0])
        if beatsPerMeasure < 2 or  beatsPerMeasure > 12:    #Check Beats per meassure
            print("Invalid beats per measure. The amount of beats per measure should be between 2 and 12.")
            continue

        beatUnit = int(timesig[1])
        if beatUnit == 2 or beatUnit == 4 or beatUnit == 8 or beatUnit == 16: #Check Beat Unit
            break
        else:
            print("Invalid beat unit. The beat unit has to be 2, 4, 8 or 16. Please enter one of the valid options.")
            continue
    except ValueError:
        print("Invalid option. Please enter a valid timesigniture. For example: 7/8")
        continue


    #bpm
while True:
    bpm = input("What is your desired BPM? --> ")
    if bpm.isdigit() and int(bpm) >= 40 and int(bpm) <= 300:
        bpm = int(bpm)
        beatInterval = (240/beatUnit)/(bpm) #bpm conversion, interval for quarter notes
        sixteenInterval = 15/(bpm) #interval of a sixteenth note
        measureInterval = beatsPerMeasure  * beatInterval #interval of a measure
        break
    else:
        print("Invalid response. Please enter a value between 40 and 300.")

    #drumkit TODO: Choose and download sample kits
while True:
    print("1. 909")     #jazz kit
    drumkit = input("what kit would you like to play the beat on? --> ")
    if drumkit.isdigit() and int(drumkit) >= 1 and int(drumkit) <= 4:
        drumtkit = int(drumkit)
        break
    else:
        print("Invalid response. Please enter a value between 1 and 4")
        continue
if drumkit == 1:
    samples = [ sa.WaveObject.from_wave_file("kick.wav"),
                sa.WaveObject.from_wave_file("hihatt.wav"),
                sa.WaveObject.from_wave_file("snare.wav"),    ]
else:
    if drumkit == 2:
        samples = [ sa.WaveObject.from_wave_file("kick.wav"),
                    sa.WaveObject.from_wave_file("hihatt.wav"),
                    sa.WaveObject.from_wave_file("snare.wav"),    ]
    else:
        if drumkit == 3:
            samples = [ sa.WaveObject.from_wave_file("kick.wav"),
                        sa.WaveObject.from_wave_file("hihatt.wav"),
                        sa.WaveObject.from_wave_file("snare.wav"),    ]
        else:
            samples = [ sa.WaveObject.from_wave_file("kick.wav"),
                        sa.WaveObject.from_wave_file("hihatt.wav"),
                        sa.WaveObject.from_wave_file("snare.wav"),    ]


events = []

#TODO: Random beat generating
Kick_seq =  [0, 4, 8, 11]      #Kick, snare and tom matrix
Snare_seq = [2, 6, 12]      # 1 = play, 0 = silence
Tom_seq =   [13, 14, 15, 16]

#transform the sixteenthNoteSequece to an eventlist with time values
for sixteenIndex in Kick_seq:
  events.append([sixteenIndex * sixteenInterval, 0])

for sixteenIndex in Snare_seq:
  events.append([sixteenIndex * sixteenInterval, 1])

for sixteenIndex in Tom_seq:
  events.append([sixteenIndex * sixteenInterval, 2])

events.sort() #sort events list so everything is in line to play at the right time
copyEvents = list(events) #events copy for repeating
event =events.pop(0)
t0 = time.time()    #save starting time for refrence

while True:
    currentTime = time.time()
    if currentTime - t0 >= event[0]: #Check if it's time to play a sample
        samples[event[1]].play()

        if events:  #if there are events left in the events list
            event = events.pop(0)
        else:   #list is empty, refill
            events = list(copyEvents)
            event = events.pop(0)
            t0 = time.time()

    else:
        time.sleep(0.01)
        stop=input("Stop the beat? --> (y/n)")
        if stop=="y":
            print("Beat stopped")
            break
        if stop=="n":
            print("Continue")
            continue


def saveMidi():
    while True:
        save=input("Do you wish to save? --> (y/n)")
        if save=="y":
            print("Saving file")
            break
        if save=="n":
            print("File was not saved")
            break
        else:
            continue
    welcome()

saveMidi()
