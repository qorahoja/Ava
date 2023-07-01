import datetime
import winsound

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))

    altime = altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mineral = altime[3:5]
    Mineral = int(Mineral)
    print(f"Done, alarm is set for {Timing}") 

    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mineral == datetime.datetime.now().minute:
                print("alarm running")
                winsound.PlaySound("abc", winsound.SND_LOOP)
            elif Mineral<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm("10:36 AM")