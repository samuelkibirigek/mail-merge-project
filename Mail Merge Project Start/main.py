#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
input_path = "/Users/Sam/Desktop/100 days of code/Mail Merge Project/Mail Merge Project Start/Input"
output_path = "/Users/Sam/Desktop/100 days of code/Mail Merge Project/Mail Merge Project Start/Output"
with open(f"{input_path}/Names/invited_names.txt") as invite_list:
    name_list = invite_list.readlines()

for name in name_list:
    guest = name.strip("\n")
    with open(f"{input_path}/Letters/starting_letter.txt") as letter_draft:
        draft = letter_draft.read()
        invite = draft.replace("[name]", f"{guest}")

    with open(f"{output_path}/ReadyToSend/{guest}.txt", "w") as invite_letter:
        invite_letter.write(f"{invite}")
