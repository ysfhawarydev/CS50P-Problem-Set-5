def main() :

    Plate = input("Plate: ")
    
    if is_valid(Plate) :
        print("Valid")

    else :
        print("Invalid")

def is_valid(P) :
    
    if 2 > len(P) > 6 :
        return False
    
    if not P[0].isalpha() or not P[1].isalpha() :
        return False
    
    if not P.isalnum() :
        return False
    
    number_started = False

    for i in P :
        
        if i.isdigit() :
            
            if not number_started :

                if i == "0" :
                    return False
                number_started = True
                
        else :
                    
            if number_started :
                return False

    return False

if __name__ == '__main__' :
    main(  )