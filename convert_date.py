def convert_date(x):
    date_elements = x.split(" ")
    for item in date_elements:
        match item.lower():
            case "stycznia":
                return x.replace("stycznia", "1")
            case "lutego":
                return x.replace("lutego", "2")
            case "marca":
                return x.replace("marca", "3")
            case "kwietnia":
                return x.replace("kwietnia", "4")
            case "maja":
                return x.replace("maja", "5")
            case "czerwca":
                return x.replace("czerwca", "6")
            case "lipca":
                return x.replace("lipca", "7")
            case "sierpnia":
                return x.replace("sierpnia", "8")
            case "września":
                return x.replace("września", "9")
            case "pazdziernika":
                return x.replace("pazdziernika", "10")
            case "listopada":
                return x.replace("listopada", "11")
            case "grudnia":
                return x.replace("grudnia", "12")

