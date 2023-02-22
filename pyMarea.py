from datetime import datetime,timedelta
import mareaRequest
class pyMarea:
    dinnie = ""
    dend = ""
    mareas = {}
    
    def __init__(self, i, f):
        self.dinnie = datetime.strptime(i, "%Y/%m/%d")
        self.dend = datetime.strptime(f,"%Y/%m/%d")
    def delta(self):
        delta = self.dend - self.dinnie
        return delta.days
    def process(self):
        for i in range (0,self.delta()+1):
            day = self.dinnie.day
            if(day < 10):
                day = str('0' + str(day))
            month = self.dinnie.month
            if(month < 10):
                month = str('0' + str(month))
            year = str(self.dinnie.year)
            req = mareaRequest.mareaRequest("https://ideihm.covam.es/api-ihm/getmarea?request=gettide&id=57&format=json&date="+str(year)+str(month)+str(day),self.dinnie)
            self.mareas [str(day) + "/" + month + "/" + year] = req.request()
            self.dinnie = self.dinnie+timedelta(days=1)