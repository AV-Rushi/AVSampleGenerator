import sqlite3

conn = sqlite3.connect('../DataBase/SampleGenerator.db')  # Connect to the database
cur = conn.cursor()  # Create a cursor object

cur.execute('SELECT Bic FROM bank_details')
BicData = cur.fetchall()
BicData1 = [temp[0] for temp in BicData]

cur.execute('SELECT ClearingSysId_Cd FROM bank_details')
ClrSysId_CdData = cur.fetchall()
ClrSysId_CdData1 = [temp[0] for temp in ClrSysId_CdData]

cur.execute('SELECT ClearingSysId_Prtry FROM bank_details')
ClrSysId_PrtryData = cur.fetchall()
ClrSysId_PrtryData1 = [temp[0] for temp in ClrSysId_PrtryData]

cur.execute('SELECT RoutingNo FROM bank_details')
RoutingNoData = cur.fetchall()
RoutingNoData1 = [temp[0] for temp in RoutingNoData]

cur.execute('SELECT OtherId FROM bank_details')
OtherIdData = cur.fetchall()
OtherIdData1 = [temp[0] for temp in OtherIdData]

def AgentBic(AgtCount,AgtBic1):
    for Bic1 in AgtBic1:
        if (AgtCount < len(BicData1)):
            Bic1.text = str(BicData1[AgtCount])
            AgtCount = AgtCount + 1

        else:
            AgtCount = 0
            Bic1.text = str(BicData1[AgtCount])
            AgtCount = AgtCount + 1

def AgentMmbId(AgtCount,AgtMmbId1):
    for MmbId1 in AgtMmbId1:
        if (AgtCount < len(RoutingNoData1)):
            MmbId1.text = str(RoutingNoData1[AgtCount])
            AgtCount = AgtCount + 1

        else:
            AgtCount = 0
            MmbId1.text = str(RoutingNoData1[AgtCount])
            AgtCount = AgtCount + 1


def AgentOthrId(AgtCount,AgtOthrId1):
    for OtherId1 in AgtOthrId1:
        if (AgtCount < len(OtherIdData1)):
            OtherId1.text = str(OtherIdData1[AgtCount])
            AgtCount = AgtCount + 1

        else:
            AgtCount = 0
            OtherId1.text = str(OtherIdData1[AgtCount])
            AgtCount = AgtCount + 1

def AgentClrSysId_Cd(AgtCount,AgtClrSysId_Cd1):
    for ClrSysId_Cd1 in AgtClrSysId_Cd1:
        if (AgtCount < len(ClrSysId_CdData1)):
            ClrSysId_Cd1.text = str(ClrSysId_CdData1[AgtCount])
            AgtCount = AgtCount + 1

        else:
            AgtCount = 0
            ClrSysId_Cd1.text = str(ClrSysId_CdData1[AgtCount])
            AgtCount = AgtCount + 1

def AgentClrSysId_Prtry(AgtCount,AgtClrSysId_Prtry1):
    for ClrSysId_Prtry1 in AgtClrSysId_Prtry1:
        if (AgtCount < len(ClrSysId_PrtryData1)):
            ClrSysId_Prtry1.text = str(ClrSysId_PrtryData1[AgtCount])
            AgtCount = AgtCount + 1

        else:
            AgtCount = 0
            ClrSysId_Prtry1.text = str(ClrSysId_PrtryData1[AgtCount])
            AgtCount = AgtCount + 1




