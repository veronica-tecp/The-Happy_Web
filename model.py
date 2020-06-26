import random
def get_quote(emotion):
    if emotion == "sadness":
        return ["Smile and shine, for God’s got your back!", "BirthdayWishes.expert"]
    elif emotion == "anger":
        return ["Calm mind brings inner strength and self-confidence, so that’s very important for good health.", "Dalai Lama"]
    elif emotion == "nervous-anxious":
        return ["Smile, breath and go slowly.", "Thich Nhat Hanh"]
    elif emotion == "frustration":
        return ["Success loses its delicious taste if it’s achieved with little or no effort.", "BirthdayWishes.expert"]
    elif emotion == "jealousy":
        return ["Jealousy, that dragon which slays love under the pretence of keeping it alive.","Havelock Ellis"]
    elif emotion == "boredom":
        return ["When I’m bored no one texts me and as soon as I’m busy BAM! No one texts me still", "CanYouRelate.org"]
    elif emotion == "doubt":
        return ["Doubt makes you weak. Believing in yourself makes you strong. The choice is yours.", "GYMQUOTES.CO"]
    elif emotion == "irritated":
        return ["Some people just need a high five...... in the face...... with a chair.", "Wondermom Wannabe"]

def get_image(emotion):
    if emotion == "sadness":
        sList = ["https://im.indiatimes.in/content/itimes/photo/2016/Aug/26/1472233327-pug-drunk-on-happiness.jpg?w=1400&h=930&cc=1", "https://media.giphy.com/media/XbxZ41fWLeRECPsGIJ/giphy.gif"]
        sRandomNum = random.randint(0,len(sList)-1)
        return sList[sRandomNum]
    elif emotion == "anger":
        aList = ["https://havingtime.com/wp-content/uploads/2017/07/Four-Choices-CALM-People-Never-Make.jpeg", "https://media.giphy.com/media/USbYNzaNRPcMbMwgCz/giphy.gif"]
        aRandomNum = random.randint(0,len(aList)-1)
        return aList[aRandomNum]
    elif emotion == "nervous-anxious":
        naList = ["https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS9EV2YqyI5FXp9j-qqX2KqDzzde-qlM0L73g&usqp=CAU", "https://media.giphy.com/media/VEgYlCul08RTgHacHV/giphy.gif"]
        naRandomNum = random.randint(0,len(naList)-1)
        return naList[naRandomNum]
    elif emotion == "frustration":
        fList = ["https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSs61DbVImL8iub5R9xYB7clDJeq7Pg0i2PxQ&usqp=CAU", "https://media.giphy.com/media/3kHz1oN8NfxJJgVgvL/giphy.gif"]
        fRandomNum = random.randint(0,len(fList)-1)
        return fList[fRandomNum]
    elif emotion == "jealousy":
        jList = ["https://thumbs.dreamstime.com/b/jealousy-destruction-health-life-symbolized-word-hammer-to-show-negative-aspect-d-illustration-173694750.jpg", "https://media.giphy.com/media/YPVb19Oxbuc13KurWU/giphy.gif"]
        jRandomNum = random.randint(0,len(jList)-1)
        return jList[jRandomNum]
    elif emotion == "boredom":
        bList = ["https://www.askideas.com/media/37/Funny-Animal-Laughing-Sea-Lion-Picture.jpg", "https://media.giphy.com/media/fA7GBW5Vai9nsZK94y/giphy.gif"]
        bRandomNum = random.randint(0, len(bList)-1)
        return bList[bRandomNum]
    elif emotion == "doubt":
        dList = ["https://d2sslp958cft0.cloudfront.net/wp-content/uploads/2017/02/04182310/Self-doubt.png", "https://media.giphy.com/media/l1J9PdkDJ2r8sg4ZG/giphy.gif"]
        dRandomNum = random.randint(0, len(dList)-1)
        return dList[dRandomNum]
    elif emotion == "irritated":
        iList = ["https://ewscripps.brightspotcdn.com/dims4/default/ef175e6/2147483647/strip/true/crop/2125x1195+0+108/resize/1280x720!/quality/90/?url=https%3A%2F%2Fmediaassets.wtvr.com%2Ftribune-network%2Ftribwtvr-files-wordpress%2F2016%2F07%2Fthinkstockphotos-151332978.jpg", "https://media.giphy.com/media/l396DXiUPaIfExvZC/giphy.gif"]
        iRandomNum = random.randint(0, len(iList)-1)
        return iList[iRandomNum]