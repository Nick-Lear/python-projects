#This program will require superuser privileges to function.
#It will parse (READ-ONLY) the contents of the below files on a Linux system
#and output relevant information in human-readable format.
#
#Files:
#   /etc/passwd
#   /etc/group

def uid_duplicate_check():
    uid_filtered = []
    with open("/etc/passwd", "r") as passwd_file:
        #Creates list of UIDs in /etc/passwd
        for line in passwd_file:
            passwd_field = line.strip().split(":")
            uid_filtered.append(passwd_field[2])
        #Checks UIDs in /etc/passwd for duplicates
        #If any of the UIDs matches another UID, output that UID
        for x, uid in enumerate(uid_filtered):
            for y, duplicate in enumerate(uid_filtered):
                if x != y and uid == duplicate:
                    print(f"Multiple users have UID of {x}")

def get_users():
    passwd_filtered = []
    with open("/etc/passwd", "r") as passwd_file:
        for line in passwd_file:
            #Splits rows into chunks/fields
            passwd_fields = line.strip().split(":")
            #Does not count users who cannot log in
            if "nologin" in passwd_fields[6]:
                continue
            #Does not count system users with UID sub-1000, EXCEPT root
            elif 1000 > int(passwd_fields[2]) > 1:
                continue
            passwd_filtered.append(line.strip())
    # Takes contents of filtered /etc/passwd list and reformats for human reading
    print("*************LIST OF USERS*************")
    for line in passwd_filtered:
        fields = line.strip().split(":")
        username = fields[0]
        uid = fields[2]
        home = fields[5]
        # Checks for users with elevated/root permissions, adds advisory warning
        if 0 == int(uid):
            print(f"***WARNING***\nUser: {username} has root permissions with UID: {uid}!\n***WARNING***")
        print(f"User: {username}\nUID: {uid} \nHome directory: {home}\n_____________________________")

def get_groups():
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
    #Takes contents of filtered /etc/group file and reformats for human reading
    print("*************LIST OF GROUPS*************")
    for line in group_filtered:
        fields = line.strip().split(":")
        group_name = fields[0]
        gid = fields[2]
        members = fields[3]
        print(f"Group: {group_name}\nGID: {gid}\nMembers: {members}\n_____________________________")

uid_duplicate_check()
get_users()
get_groups()

#TODO:
#   - Detect duplicate GUIDs
#   - Parse /etc/shadow for expired/locked accounts
#   - Detect Home folders that do not have matching users
#   - Detect users who have not logged in for 90 days
#   - Ability to export to a file via argparse