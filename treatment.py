
def determinescore(Confusion,Respiratory,Systolic,Diastolic,bun,age):

    score=0
    if Confusion == "yes":
       score=score+1
    if Respiratory>30:
       score=score+1
    if Systolic<90 and Diastolic<60:
       score=score+1
    if bun>=19 :
      score=score+1
    if age>=65:
       score=score+1
    return score

def determinetreatment(score,type,chronic_diseases):
    if type == 0:
        if (score == 0 or score==1) and chronic_diseases != "notspesific":
            treatment = """For fear  ofsecondarybacterial  infection, give:   
                                    Levox tab,voloxal tab,tavanic ,Megaxin tab,moxiflox"""
        elif score == 0 or score==1 :
            treatment = 'Acamul,Trophen,Vitamin C,zinc,Liquids'
        elif score == 2 :
            treatment = 'Acamul,Trophen,Vitamin C,zinc,Liquids'

        else:
            treatment = 'Intensive Care'
    else:
        if (score == 0 or score==1) and chronic_diseases != "notspesific":
            treatment = " Levox tab,voloxal tab,tavanic ,Megaxin tab,moxiflox"
        elif  score == 0 or score==1:
            treatment = 'Azemix 500 mg,Levo,Doxal '
        elif score == 2 :
            treatment = 'Rocephen,Ogmin,Tazocin '
        elif score==3:
            treatment = 'Intensive Care'
    return treatment



