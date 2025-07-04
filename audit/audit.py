passwd_filtered = []
#Opens the file in read mode
with open("/etc/passwd", "r") as passwd_file:
    for line in passwd_file:
        #Splits rows into chunks/fields
        passwd_fields = line.strip().split(":")
        #Does not count users who cannot login
        if "nologin" in passwd_fields[6]:
            continue
        #Does not count system users with UID sub-1000
        elif 1000 > int(passwd_fields[2]):
            continue
        passwd_filtered.append(line.strip())

group_filtered = []
with open("/etc/group", "r") as group_file:
    for line in group_file:
        #Splits rows into chunks/fields
        group_fields = line.strip().split(":")
        #Creates variable to check if groups have members
        members = group_fields[3]
        #If NO members, skip that row
        if not members:
            continue
        group_filtered.append(line.strip())

#Takes contents of filtered /etc/passwd list and reformats for human reading
print("*************LIST OF USERS*************")
for line in passwd_filtered:
    fields = line.strip().split(":")
    username = fields[0]
    uid = fields[2]
    home = fields[5]
    print(f"User: {username}\nUID: {uid} \nHome directory: {home}\n_____________________________")

#Takes contents of filtered /etc/group file and reformats for human reading
print("*************LIST OF GROUPS*************")
for line in group_filtered:
    fields = line.strip().split(":")
    group_name = fields[0]
    gid = fields[2]
    members = fields[3]
    print(f"Group: {group_name}\nGID: {gid}\nMembers: {members}\n_____________________________")
