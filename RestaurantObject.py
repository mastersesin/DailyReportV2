class resObj():
    def __init__(self,sqlReturn):
        #Sales Data of current day
        self.sqlReturn = sqlReturn
        self.resName = ""
        self.wineRevenue = 0.0
        self.drinkAndFruitRevenue = 0.0
        self.totalCustomer = 0
        self.totalRevenue = 0.0
        self.transactionAverage = 0.0
        #Month to date declaration
        self.monthToDateWine = 0.0
        self.monthToDateDrinkAndFruit = 0.0
        self.monthToDateRevenue = 0.0
        self.monthToDateCustomer = 0.0
        self.monthToDateTargetTransactionAverage = 0.0
        #Target declaration
        self.monthTargetWine = 0.0
        self.monthTargetDrinkAndFruit = 0.0
        self.monthTargetRevenue = 0.0
        #ID declaration
        self.codeName = ""
        self.hashcode = ""
print("hello")