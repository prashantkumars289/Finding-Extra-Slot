print('Input current running fractal (e.g: "2"):', end=" ")
fractal = input()  # extra slot for which fractal
print('Input course code for which extra class is required(e.g: "CS301 (16)"):', end=" ")
cr = input()
extra_slot = {}

# input starts
time_table = {
    "Monday": {
        "slot1": ["CS301 (16)", "IC100 (16)"],
        "slot2": ["EE251 (14)", "MA202 (34)"],
        "slot3": ["EE252 (56)", "LA317 (36)"],
    },
    "Tuesday": {
        "slot1": ["EE251 (14)", "IC250 (34)"],
        "slot2": ["IC100 (16)", "MA202 (34)"],
        "slot3": ["IC100 (16)", "EE251 (14)"],
    },
}
prof = {"nikhil": ["EE251 (14)", "IC100 (16)"], "Arzad": [
    "CS301 (16)", "CY201 (34)"]}
allocated_room = {"IC100 (16)": "107", "EE251 (14)": "104"}
rooms = ["102", "103", "104", "107", "207"]
stu = {
    "CS301 (16)": ["CS17", "EE17"],
    "IC100 (16)": ["CS19", "EE19", "ME19"],
    "CY201 (34)": ["CS18", "CS17"],
    "MA202 (34)": ["ME18", "ME17"],
    "ME201 (34)": ["ME18", "ME17"],
    "EE251 (14)": ["CS18", "ME18", "EE18"],
}
# input end


slt = {}  # particular courses in a slot
week = ["Monday", "Tuesday"]
slots = ["slot1", "slot2", "slot3"]

new_table = {}
for day in week:
    new_table[day] = {}
    for slot in slots:
        new_table[day][slot] = []
        for course in time_table[day][slot]:
            if fractal <= course[8] and fractal >= course[7]:
                new_table[day][slot].append(course)
for day in week:
    slt[day] = {}
    for slot in slots:
        slt[day][slot] = set()
        for course in new_table[day][slot]:
            for i in stu[course]:
                slt[day][slot].add(i)
for i in stu[cr]:
    for day in week:
        extra_slot[day] = []
        for slot in slots:
            if i not in slt[day][slot]:
                extra_slot[day].append(slot)


prof_slot = {}  # slots in which professors are busy
for professor in prof:
    prof_slot[professor] = {}
    for day in week:
        prof_slot[professor][day] = {}
        for slot in slots:
            prof_slot[professor][day][slot] = 0
for professor in prof:
    for course in prof[professor]:
        for day in week:
            for slot in slots:
                if course in new_table[day][slot]:
                    prof_slot[professor][day][slot] = 1

professor = "Rishi"
for key, value in prof.items():
    for course in value:
        if course == cr:
            professor = key
for day, slots in extra_slot.items():
    i = 0
    while i < len(slots):
        if prof_slot[professor][day][slots[i]] == 1:
            extra_slot[day].remove(slots[i])
            i = i - 1
        i = i + 1


booked_slot = {}
# print(extra_slot)
# print(new_table)
for day, slots in extra_slot.items():
    booked_slot[day] = {}
    for slot in slots:
        booked_slot[day][slot] = []
        for course in new_table[day][slot]:
            booked_slot[day][slot].append(allocated_room[course])
# print(booked_slot)
unbooked_room = {}
for day, slots in extra_slot.items():
    unbooked_room[day] = {}
    for slot in slots:
        unbooked_room[day][slot] = []
        unbooked_room[day][slot] = list(
            set(rooms) - set(booked_slot[day][slot]))
# print(extra_slot)
print("\nFollowing are all the day, slot and available room for the extra class:")
print(unbooked_room)
# print(extra_slot)
