def zoopark_kassa(yosh):
    if yosh <= 4 or yosh >= 65:
        return "Chipta narxi bepul"
    elif 5 <= yosh <= 12:
        return "15000 so'm"
    elif 13 <= yosh <= 65:
        return "20000 so'm"
    else:
        return "Noto'g'ri yosh"

user_input_yosh = int(input("Yoshingizni kiriting: "))
print(zoopark_kassa(user_input_yosh))

def haroratni_tekshirish(harorat):
    if harorat < 0:
        return "Juda sovuq!"
    elif harorat > 30:
        return "Juda issiq!"
    else:
        return "Havo harorati qulay."

user_input_harorat = float(input("Havo haroratini kiriting: "))
print(haroratni_tekshirish(user_input_harorat))

def baholarni_baholash(baho):
    if 90 < baho <= 100:
        return "A'lo"
    elif 80 <= baho <= 90:
        return "Yaxshi"
    elif 70 <= baho < 80:
        return "Qoniqarli"
    elif 0 <= baho < 70:
        return "Yomon"
    else:
        return "Noto'g'ri baho"

user_input_baho = float(input("O'quvchining bahosini kiriting (0-100): "))
print(baholarni_baholash(user_input_baho))
