
notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
def major(first_note = "A"):
    # MAJOR ---> T+T+Y+T+T+T+Y
    first_index = notes.index(first_note)
    print(notes[first_index],end= " ")
    second_index = first_index + 2
    try:
        print(notes[second_index],end=" ")
    except IndexError:
        print(notes[second_index-12],end=" ")
    third_index = second_index + 2
    try:
        print(notes[third_index],end=" ")
    except IndexError:
        print(notes[third_index-12],end=" ")
    fourth_index = third_index + 1
    try:
        print(notes[fourth_index],end=" ")
    except IndexError:
        print(notes[fourth_index-12],end=" ")
    fifth_index = fourth_index + 2
    try:
        print(notes[fifth_index],end=" ")
    except IndexError:
        print(notes[fifth_index-12],end=" ")
    sixth_index = fifth_index + 2
    try:
        print(notes[sixth_index],end=" ")
    except IndexError:
        print(notes[sixth_index-12],end=" ")
    seventh_index = sixth_index + 2
    try:
        print(notes[seventh_index],end=" ")
    except IndexError:
        print(notes[seventh_index-12],end=" ")
    print("------>>>>",end=" ")
    try:
        print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index], end=" ")
    except IndexError:
        try:
            print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index-12], end=" ")
        except IndexError:
            try:
                print(notes[first_index], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
            except IndexError:
                print(notes[first_index-12], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
    print("------>>>>", end=" ")
    print(first_note,end= " ")
    print("Major dizisi")

### NEW SERIE
    for i in range(6):
        placeholder = first_index
        first_index = second_index
        second_index = third_index
        third_index = fourth_index
        fourth_index = fifth_index
        fifth_index = sixth_index
        sixth_index = seventh_index
        seventh_index = placeholder
        try :
            print(notes[first_index], end=" ")
        except IndexError:
            print(notes[first_index-12], end=" ")
        try:
            print(notes[second_index], end=" ")
        except IndexError:
            print(notes[second_index-12], end=" ")
        try:
            print(notes[third_index], end=" ")
        except IndexError:
            print(notes[third_index-12], end=" ")
        try:
            print(notes[fourth_index], end=" ")
        except IndexError:
            print(notes[fourth_index-12], end=" ")
        try:
            print(notes[fifth_index], end=" ")
        except IndexError:
            print(notes[fifth_index-12], end=" ")
        try:
            print(notes[sixth_index], end=" ")
        except IndexError:
            print(notes[sixth_index-12], end=" ")
        try:
            print(notes[seventh_index], end=" ")
        except IndexError:
            print(notes[seventh_index-12], end=" ")

        print("------>>>>", end=" ")
        try:
            print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index], end=" ")
        except IndexError:
            try:
                print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index - 12], end=" ")
            except IndexError:
                try:
                    print(notes[first_index], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
                except IndexError:
                    print(notes[first_index-12], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
        print("------>>>>", end=" ")
        print("{}.Derece".format(i+2))
    print("-------------------------------------------------------------------------------")

def minor(first_note = "A"):
# MINOR ---> T+Y+T+T+Y+T+T
    first_index = notes.index(first_note)
    print(notes[first_index], end=" ")
    second_index = first_index + 2
    try:
        print(notes[second_index], end=" ")
    except IndexError:
        print(notes[second_index - 12], end=" ")
    third_index = second_index + 1
    try:
        print(notes[third_index], end=" ")
    except IndexError:
        print(notes[third_index - 12], end=" ")
    fourth_index = third_index + 2
    try:
        print(notes[fourth_index], end=" ")
    except IndexError:
        print(notes[fourth_index - 12], end=" ")
    fifth_index = fourth_index + 2
    try:
        print(notes[fifth_index], end=" ")
    except IndexError:
        print(notes[fifth_index - 12], end=" ")
    sixth_index = fifth_index + 1
    try:
        print(notes[sixth_index], end=" ")
    except IndexError:
        print(notes[sixth_index - 12], end=" ")
    seventh_index = sixth_index + 2
    try:
        print(notes[seventh_index], end=" ")
    except IndexError:
        print(notes[seventh_index - 12], end=" ")
    print("------>>>>", end=" ")
    try:
        print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index], end=" ")
    except IndexError:
        try:
            print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index-12], end=" ")
        except IndexError:
            try:
                print(notes[first_index], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
            except IndexError:
                print(notes[first_index-12], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
    print("------>>>>", end=" ")
    print(first_note, end=" ")
    print("Minor dizisi")

    ### NEW SERIE
    for i in range(6):
        placeholder = first_index
        first_index = second_index
        second_index = third_index
        third_index = fourth_index
        fourth_index = fifth_index
        fifth_index = sixth_index
        sixth_index = seventh_index
        seventh_index = placeholder
        try:
            print(notes[first_index], end=" ")
        except IndexError:
            print(notes[first_index - 12], end=" ")
        try:
            print(notes[second_index], end=" ")
        except IndexError:
            print(notes[second_index - 12], end=" ")
        try:
            print(notes[third_index], end=" ")
        except IndexError:
            print(notes[third_index - 12], end=" ")
        try:
            print(notes[fourth_index], end=" ")
        except IndexError:
            print(notes[fourth_index - 12], end=" ")
        try:
            print(notes[fifth_index], end=" ")
        except IndexError:
            print(notes[fifth_index-12], end=" ")
        try:
            print(notes[sixth_index], end=" ")
        except IndexError:
            print(notes[sixth_index - 12], end=" ")
        try:
            print(notes[seventh_index], end=" ")
        except IndexError:
            print(notes[seventh_index - 12], end=" ")

        print("------>>>>", end=" ")
        try:
            print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index], end=" ")
        except IndexError:
            try:
                print(notes[first_index], " ", notes[third_index], " ", notes[fifth_index - 12], end=" ")
            except IndexError:
                try:
                    print(notes[first_index], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
                except IndexError:
                    print(notes[first_index-12], " ", notes[third_index - 12], " ", notes[fifth_index - 12], end=" ")
        print("------>>>>", end=" ")
        print("{}.Derece".format(i + 2))
    print("-------------------------------------------------------------------------------")

def main():
    while True:
        note = input("Bir Nota Giriniz (A,B...):")
        print("""
        1.Major
        2.Minor
        """)
        mm = input("Seciminizi Giriniz (1,2):")
        if mm == "1":
            major(note)
        elif mm == "2":
            minor(note)
        else:
            print("Lutfen Dogru Secimi Yaziniz!")
        hervatten = input("Devam etmek istiyor musun (Y/n):").lower()
        if hervatten != "y":
            break



main()

