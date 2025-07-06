#This program will require superuser privileges to function.
#It will parse (READ-ONLY) the contents of the below files on a Linux system
#and output relevant information in human-readable format.
#
#Files:
#   /etc/passwd
#   /etc/group
#   /etc/shadow

import os

def sudo_check():
    userid = os.geteuid()
    if userid != 0:
        print("You must be a superuser to perform this action.")
        exit(1)

def read_file(file_path):
    with open(file_path, "r") as file_open:
        file_contents = file_open.readlines()
    return file_contents

def uid_duplicate_check(passwd_file_contents):
    uid_filtered = []
    #Creates list of UIDs in /etc/passwd
    for line in passwd_file_contents:
        passwd_field = line.strip().split(":")
        uid_filtered.append(passwd_field[2])
    #Checks UIDs in /etc/passwd for duplicates
    #If any of the UIDs matches another UID, output that UID
    for x, uid in enumerate(uid_filtered):
        for y, duplicate in enumerate(uid_filtered):
            if x != y and uid == duplicate:
                print(f"Multiple users have UID of {uid}")

def get_users(passwd_file_contents):
    passwd_filtered = []
    for line in passwd_file_contents:
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

def guid_duplicate_check(group_file_contents):
    guid_filtered = []
    #Creates list of GUIDs in /etc/group
    for line in group_file_contents:
        passwd_field = line.strip().split(":")
        guid_filtered.append(passwd_field[2])
    #Checks GUIDs in /etc/group for duplicates
    #If any of the GUIDs matches another GUID, output that GUID
    for x, guid in enumerate(guid_filtered):
        for y, duplicate in enumerate(guid_filtered):
            if x != y and guid == duplicate:
                print(f"Multiple groups have GUID of {guid}")

def get_groups(group_file_contents):
    group_filtered = []
    for line in group_file_contents:
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

def expired_check(shadow_file_contents):
    print("*************LIST OF LOCKED/EXPIRED ACCOUNTS*************")
    for line in shadow_file_contents:
        shadow_fields = line.strip().split(":")
        user = shadow_fields[0]
        password = shadow_fields [1]

        # Checks to make sure that shadow_fields[2] and shadow_fields[4] are present and valid
        last_changed_string = shadow_fields[2]
        if not last_changed_string.isdigit():
            continue
        last_changed = int(last_changed_string)

        max_age_string = shadow_fields[4]
        if not max_age_string.isdigit():
            continue
        max_age = int(max_age_string)

        #Checks for locked users
        if password in ["!", "*"]:
            print(f"{user}'s account is locked.")

        #Checks for soon to expire, expired users
        expire_days = max_age - last_changed

        if 0 < expire_days <= 14:
            print(f"{user}'s account will expire in {expire_days} days.")
        elif expire_days <= 0:
            print(f"{user}'s account expired {-expire_days} ago. They are unable to login.")

#Checks that user is UID == 0
sudo_check()

#If located in nonstandard locations for some reason, can be changed here
passwd_file = "/etc/passwd"
group_file = "/etc/group"
shadow_file = "/etc/shadow"

#Reads the opened files and stores the contents for use
passwd_file_read = read_file(passwd_file)
group_file_read = read_file(group_file)
shadow_file_read = read_file(shadow_file)

#Checks /etc/passwd for duplicate UIDs
uid_duplicate_check(passwd_file_read)

#Checks /etc/passwd for users UID = 0 or >1000
get_users(passwd_file_read)

#Checks /etc/shadow file for locked users, expired passwords
expired_check(shadow_file_read)

#Checks /etc/group for duplicate GUIDs
guid_duplicate_check(group_file_read)

#Checks /etc/group for groups that have members
get_groups(group_file_read)

#TODO:
#   - Detect Home folders that do not have matching users
#   - Detect users who have not logged in for 90 days
#   - Ability to export to a file via argparse