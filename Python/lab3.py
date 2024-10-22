from datetime import datetime

def pensioner (male, date):
    res = datetime.now() - datetime.strptime(date, "%b %d %Y %I:%M%p")

    if male == "man" and int(res.days) >= 20075:
        return "Пенсионер"
    elif male == "woman" and int(res.days) >= 19000:
        return "Пенсионерка" 
    else:
        return ""  

print(pensioner("man", "Jun 1 1950 1:33PM"))