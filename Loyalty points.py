purchases = [220]

def earn_points(price):
    """' 
    Convert a purchase amount  into a whole-dollar points.
    Each dollar =3 pts.Fraction of a dollar are ignored """
    
    whole_dollar = int(price)
    return whole_dollar * 3
    
def tier_label(points):
    """ Return the loyalty tier name based on total points""" 
    if points >= 500:
        return "Gold"
    elif points >=100:
        return "Silver"
    else:
        return "Bronze"
        
                
                        
total_spent = 0.0
total_points = 0 

for amount in purchases:
    total_spent += amount
    total_points += earn_points(amount)
    
final_tier = tier_label(total_points)

print("==== Loyalty Summary ====")
print(f"Total spent: ${total_spent: 2f}")
print(f"Total points: ${total_points}")
print(f"Tier achieved: ${final_tier}")
            
     
    