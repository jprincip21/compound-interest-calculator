# Calculates compound interest and returns it in a list by amount by year
def compoundInterest(present_value, interest_rate, period, years=10):
    
    interest_rate = float(interest_rate)/100
    present_value = float(present_value)
    years = int(years)

    # Check value for period
    match period:
        case "Annually":
            period = 1
            
        case "Semi-Annually":
            period = 2
            
        case "Quarterly": 
            period = 4
            
        case "Monthly": 
            period = 12
            
        case "Daily": 
            period = 365

    # Generate a list of compounded values
    compounded = [present_value*(1+(interest_rate/period))**(period*year) for year in range(years+1)]

    return compounded
