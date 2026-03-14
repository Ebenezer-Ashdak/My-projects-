revoked_badges = {"A112", "5o7" ,  "Zeke"}

approved = []
denied = []

while True:
    name = input("Enter your name(or type 'done' to finish):    ")
    if name.lower() == "done":
        break
    
    badge =input("Enter badge number:    ").strip().upper()
    
    if badge in revoked_badges:
        denied.append(name)
        print(f"[ACCESS DENIED] {name} - Revoked bedge")
    else:
        approved.append(name)
        print(f"[ACCESS GRANTED]  {name} ")
        
                        
print("===== Access Summary ====")
                                                   
print(" Approved Visitors: ")
for person in sorted(approved) :
    print(f" - {person}")
    
print(" Denied  Visitors: ")
for person in sorted(denied) :
    print(f" - {person}")
    
    
print(f"Total  Approved: {len(approved)}")    
print(f"Total  Denied: {len(denied)}")    
print("Done!")                                                                                                                                                                                                                                                                                                                                 