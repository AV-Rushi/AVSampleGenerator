import sqlite3
import time
import xml.etree.ElementTree as ET
import pandas as pd
from faker import Faker
import uuid
import datetime


def formatCcy():
    pass


def readFile(file,batchNo,txnNo,amtType,amount,ccy,ccy1):
    file1 = (f"Input\Sample_Template\{file}.xml")
    tree = ET.parse(file1)

    ns = dict([node for (_, node) in ET.iterparse(file1, events=['start-ns'])])
    nskeys = list(ns.keys())
    for i in nskeys:
        ET.register_namespace(i, ns[i])
    root = tree.getroot()
    conn = sqlite3.connect('DataBase/SampleGenerator.db')  # Connect to the database

    cur = conn.cursor()  # Create a cursor object

    cur.execute('SELECT distinct CountryCode FROM currency where Decimals=3')
    lst1 = cur.fetchall()
    cur.execute('SELECT distinct CountryCode FROM currency where Decimals=2')
    lst2 = cur.fetchall()
    cur.execute('SELECT distinct CountryCode FROM currency where Decimals=0')
    lst3 = cur.fetchall()


    fileElement = root.find(".//fps:FpsPylds", ns)  # File Level Element
    fiToFiElement = root.find(".//doc:FIToFICstmrCdtTrf", ns)
    # NbOfMsgs
    NbOfMsgs = root.find(".//fps:NbOfMsgs", ns)
    NbOfMsgs.text = str(batchNo)

    for i in range(batchNo - 1):
        btchElement = root.find(".//fps:BizData", ns)  # Batch Level Element
        fileElement.append(btchElement)
    for j in range(txnNo - 1):
        txnElement = root.find(".//doc:CdtTrfTxInf", ns)  # CdtTrfTxInf Level Element
        fiToFiElement.append(txnElement)

    if amtType == 1:
        if ccy1 is None:
            if ccy in [item for sublist in lst1 for item in sublist]:
                formatted_amount1 = "{:.3f}".format(amount)
            elif ccy in [item for sublist in lst2 for item in sublist]:
                formatted_amount1 = "{:.2f}".format(amount)
            elif ccy in [item for sublist in lst3 for item in sublist]:
                formatted_amount1 = int(amount)

            for txn in root.findall('.//doc:CdtTrfTxInf', ns):
                txn.find('.//doc:IntrBkSttlmAmt', ns).text = str(formatted_amount1)
                txn.find('.//doc:InstdAmt', ns).text = str(formatted_amount1)
        else:
            if ccy in [item for sublist in lst1 for item in sublist]:
                formatted_amount1 = "{:.3f}".format(amount)
            elif ccy in [item for sublist in lst2 for item in sublist]:
                formatted_amount1 = "{:.2f}".format(amount)
            elif ccy in [item for sublist in lst3 for item in sublist]:
                formatted_amount1 = int(amount)

            if ccy1 in [item for sublist in lst1 for item in sublist]:
                formatted_amount2 = "{:.3f}".format(amount)
            elif ccy1 in [item for sublist in lst2 for item in sublist]:
                formatted_amount2 = "{:.2f}".format(amount)
            elif ccy1 in [item for sublist in lst3 for item in sublist]:
                formatted_amount2 = int(amount)

            for txn in root.findall('.//doc:CdtTrfTxInf', ns):
                txn.find('.//doc:IntrBkSttlmAmt', ns).text = str(formatted_amount1)
                txn.find('.//doc:InstdAmt', ns).text = str(formatted_amount2)

    elif amtType == 2:
        if ccy1 is None:
            if ccy in [item for sublist in lst1 for item in sublist]:
                formatted_amount1 = "{:.3f}".format(amount / (txnNo * batchNo))
            elif ccy in [item for sublist in lst2 for item in sublist]:
                formatted_amount1 = "{:.2f}".format(amount / (txnNo * batchNo))
            elif ccy in [item for sublist in lst3 for item in sublist]:
                formatted_amount1 = int((amount / (txnNo * batchNo)))

            for txn in root.findall('.//doc:CdtTrfTxInf', ns):
                    txn.find('.//doc:IntrBkSttlmAmt', ns).text = str(formatted_amount1)
                    txn.find('.//doc:InstdAmt', ns).text = str(formatted_amount1)

        else:
            if ccy in [item for sublist in lst1 for item in sublist]:
                formatted_amount1 = "{:.3f}".format(amount / (txnNo * batchNo))
            elif ccy in [item for sublist in lst2 for item in sublist]:
                formatted_amount1 = "{:.2f}".format(amount / (txnNo * batchNo))
            elif ccy in [item for sublist in lst3 for item in sublist]:
                formatted_amount1 = int((amount / (txnNo * batchNo)))

            if ccy1 in [item for sublist in lst1 for item in sublist]:
                formatted_amount2 = "{:.3f}".format(amount / (txnNo * batchNo))
            elif ccy1 in [item for sublist in lst2 for item in sublist]:
                formatted_amount2 = "{:.2f}".format(amount / (txnNo * batchNo))
            elif ccy1 in [item for sublist in lst3 for item in sublist]:
                formatted_amount2 = int((amount / (txnNo * batchNo)))

            for txn in root.findall('.//doc:CdtTrfTxInf', ns):
                txn.find('.//doc:IntrBkSttlmAmt', ns).text = str(formatted_amount1)
                txn.find('.//doc:InstdAmt', ns).text = str(formatted_amount2)

    else:
        raise ValueError("Invalid Input")

    # NbOfTxs
    NbOfTxs = root.find(".//doc:NbOfTxs", ns)
    NbOfTxs.text = str(txnNo)

    tree.write("Input\Temp\SampleFile1.xml", xml_declaration=True, encoding='utf-8')
    time.sleep(5)
    print("File 1 generated sucessfully..")


def writeFile(ccy,ccy1,valueDate,ccyCheck,cdtrDataChoice,dbtrDataChoice,cdtrAccountLength,dbtrAccountLength,chkCdtrBic,cdtrBic,chkCdtrClrSysId,radioCdtrCdPrtry,cdtrCd,cdtrPrtry,chkCdtrMmbId,cdtrMmbId,chkCdtrOtherId,cdtrOtherId,chkDbtrBic,dbtrBic,chkDbtrClrSysId,radioDbtrCdPrtry,dbtrCd,dbtrPrtry,chkDbtrMmbId,dbtrMmbId,chkDbtrOtherId,dbtrOtherId,cdtrAgtDataChoice,dbtrAgtDataChoice):
    tree = ET.parse("Input\Temp\SampleFile1.xml")
    ns = dict([node for (_, node) in ET.iterparse("Input\Temp\SampleFile1.xml", events=['start-ns'])])
    nskeys_1 = list(ns.keys())
    for j in nskeys_1:
        ET.register_namespace(j, ns[j])

    root = tree.getroot()
    df = pd.read_csv("Input\Data\Account.csv")
    Acc_no = df['ACC_NO']
    Acc_name = df['ACCOUNTNAME']
    fake = Faker()

    conn = sqlite3.connect('SampleDB/SampleGenerator.db')  # Connect to the database
    cur = conn.cursor()  # Create a cursor object

    now = datetime.datetime.now()
    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID

    for element in root.findall('.//fps:BtchId', ns):
        btchId = 'BTCH' + c_date + uid  # BtchId
        element.text = str(btchId)

    for element in root.findall('.//fps:BizData', ns):
        bizMsgIdr = 'BZMSG' + c_date + uid  # BizMsgIdr
        element.find(".//ah:BizMsgIdr", ns).text = str(bizMsgIdr)

        c_date = (now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z') #Date and Time
        c_date_1 = (now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3])

        element.find(".//ah:CreDt", ns).text = c_date
        element.find(".//doc:CreDtTm", ns).text = c_date_1

    for element in root.findall('.//doc:GrpHdr', ns):
        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID

        msgId = 'MSG' + c_date + '' + uid  # MsgId
        element.find(".//doc:MsgId", ns).text = str(msgId)

    cdtrCount = 0
    dbtrCount = 0
    cdtrAgtCountBic = 0
    dbtrAgtCountBic = 0
    cdtrAgtCountCd = 0
    dbtrAgtCountCd = 0
    cdtrAgtCountMmb = 0
    dbtrAgtCountMmb = 0
    cdtrAgtCountOthr = 0
    dbtrAgtCountOthr = 0
    for element in root.findall('.//doc:CdtTrfTxInf', ns):
        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID

        endToEndId = 'E2E' + c_date + '' + uid  # EndToEndId
        element.find(".//doc:EndToEndId", ns).text = str(endToEndId)

        txID = 'TXID' + c_date + uid  # TXID
        element.find('.//doc:TxId', ns).text = str(txID)

        clrSysRef = 'CLRREF' + c_date + uid  # ClrSysRef
        element.find('.//doc:ClrSysRef', ns).text = str(clrSysRef)

        c_date_2 = (now.strftime("%Y-%m-%dT%H:%M:%S")) #CdtDtTm
        element.find(".//doc:CdtDtTm", ns).text = c_date_2

        vDate = element.find(".//doc:IntrBkSttlmDt", ns) #valueDate
        vDate.text = str(valueDate)

        currency1 = element.find(".//doc:IntrBkSttlmAmt", ns)  # Currency
        currency2 = element.find(".//doc:InstdAmt", ns)
        if (ccyCheck == 'on'):
            currency1.set('Ccy', ccy)
            currency2.set('Ccy', ccy)

        else:
            currency1.set('Ccy', ccy)
            currency2.set('Ccy', ccy1)

        # Id and Name from CSV File for CdtrAcct
        cdtrAcct = element.find(".//doc:CdtrAcct/doc:Id/doc:Othr/doc:Id", ns)
        cdtrNm = element.find(".//doc:Cdtr/doc:Nm", ns)
        if cdtrDataChoice == 1:
            if (cdtrCount < len(df)):
                cdtrAcct.text = str(Acc_no[cdtrCount])
                cdtrNm.text = str(Acc_name[cdtrCount])
                cdtrCount = cdtrCount + 1

            else:
                df = df.reset_index(drop=True)
                cdtrCount = 0
                cdtrAcct.text = str(Acc_no[cdtrCount])
                cdtrNm.text = str(Acc_name[cdtrCount])
                cdtrCount = cdtrCount + 1
        elif cdtrDataChoice == 2:
            name = fake.name()
            account_no = fake.random_number(digits=cdtrAccountLength)
            cdtrAcct.text = str(account_no)
            cdtrNm.text = str(name)


        # Id and Name from CSV File for DbtrAcct
        Id1 = element.find(".//doc:DbtrAcct/doc:Id/doc:Othr/doc:Id", ns)
        Nm1 = element.find(".//doc:Dbtr/doc:Nm", ns)
        if dbtrDataChoice == 1:
            if (dbtrCount < len(df)):
                Id1.text = str(Acc_no[dbtrCount])
                Nm1.text = str(Acc_name[dbtrCount])
                dbtrCount = dbtrCount + 1

            else:
                df = df.reset_index(drop=True)
                dbtrCount = 0
                Id1.text = str(Acc_no[dbtrCount])
                Nm1.text = str(Acc_name[dbtrCount])
                dbtrCount = dbtrCount + 1

        elif dbtrDataChoice == 2:
            name = fake.name()
            account_no = fake.random_number(digits=dbtrAccountLength)
            Id1.text = str(account_no)
            Nm1.text = str(name)

        if cdtrAgtDataChoice == 1:
            cur.execute('SELECT Bic FROM bank_details')
            BicData = cur.fetchall()
            BicData1 = [temp[0] for temp in BicData]
            cur.execute('SELECT ClearingCode FROM bank_details')
            ClearingCodeData = cur.fetchall()
            ClearingCodeData1 = [temp[0] for temp in ClearingCodeData]
            cur.execute('SELECT RoutingNo FROM bank_details')
            RoutingNoData = cur.fetchall()
            RoutingNoData1 = [temp[0] for temp in RoutingNoData]
            cur.execute('SELECT OtherId FROM bank_details')
            OtherIdData = cur.fetchall()
            OtherIdData1 = [temp[0] for temp in OtherIdData]
            if (chkCdtrBic == 'on'):
                cdtrBic1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:BICFI', ns)
                if (cdtrAgtCountBic < len(BicData1)):
                    cdtrBic1.text = str(BicData1[cdtrAgtCountBic])
                    cdtrAgtCountBic = cdtrAgtCountBic + 1

                else:
                    cdtrAgtCountBic = 0
                    cdtrBic1.text = str(BicData1[cdtrAgtCountBic])
                    cdtrAgtCountBic = cdtrAgtCountBic + 1

            if (chkCdtrClrSysId == 'on'):
                if radioCdtrCdPrtry == 1:
                    cdtrCd1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Cd', ns)
                    if (cdtrAgtCountCd < len(ClearingCodeData1)):
                        cdtrCd1.text = str(ClearingCodeData1[cdtrAgtCountCd])
                        cdtrAgtCountCd = cdtrAgtCountCd + 1

                    else:
                        cdtrAgtCountCd = 0
                        cdtrCd1.text = str(ClearingCodeData1[cdtrAgtCountCd])
                        cdtrAgtCountCd = cdtrAgtCountCd + 1

                if radioCdtrCdPrtry == 2:
                    cdtrPrtry1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Prtry', ns)
                    cdtrPrtry1.text = "Prtry12345"

            if (chkCdtrMmbId == 'on'):
                cdtrMmbId1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:MmbId', ns)
                if (cdtrAgtCountMmb < len(RoutingNoData1)):
                    cdtrMmbId1.text = str(RoutingNoData1[cdtrAgtCountMmb])
                    cdtrAgtCountMmb = cdtrAgtCountMmb + 1

                else:
                    cdtrAgtCountMmb = 0
                    cdtrMmbId1.text = str(RoutingNoData1[cdtrAgtCountMmb])
                    cdtrAgtCountMmb = cdtrAgtCountMmb + 1

            if (chkCdtrOtherId == 'on'):
                cdtrOtherId1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:Othr/doc:Id', ns)
                if (cdtrAgtCountOthr < len(OtherIdData1)):
                    cdtrOtherId1.text = str(OtherIdData1[cdtrAgtCountOthr])
                    cdtrAgtCountOthr = cdtrAgtCountOthr + 1

                else:
                    cdtrAgtCountOthr = 0
                    cdtrOtherId1.text = str(OtherIdData1[cdtrAgtCountOthr])
                    cdtrAgtCountOthr = cdtrAgtCountOthr + 1

        elif cdtrAgtDataChoice == 2:
            if (chkCdtrBic == 'on'):
                cdtrBic1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:BICFI', ns)
                cdtrBic1.text = cdtrBic

            else:
                cdtrBic1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:BICFI', ns)
                for elem in root.findall(".//*"):
                    if cdtrBic1 in elem:
                        elem.remove(cdtrBic1)

            if (chkCdtrClrSysId == 'on'):
                if radioCdtrCdPrtry == 1:
                    cdtrCd1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Cd', ns)
                    cdtrCd1.text = cdtrCd

                else:
                    cdtrCd1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Cd', ns)
                    for elem in root.findall(".//*"):
                        if cdtrCd1 in elem:
                            elem.remove(cdtrCd1)

                if radioCdtrCdPrtry == 2:
                    cdtrPrtry1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Prtry', ns)
                    cdtrPrtry1.text = cdtrPrtry

                else:
                    cdtrPrtry1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Prtry', ns)
                    for elem in root.findall(".//*"):
                        if cdtrPrtry1 in elem:
                            elem.remove(cdtrPrtry1)

            else:
                ClrSysId = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId', ns)
                for elem in root.findall(".//*"):
                    if ClrSysId in elem:
                        elem.remove(ClrSysId)

            if (chkCdtrMmbId == 'on'):
                cdtrMmbId1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:MmbId', ns)
                cdtrMmbId1.text = cdtrMmbId

            else:
                cdtrMmbId1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:MmbId', ns)
                for elem in root.findall(".//*"):
                    if cdtrMmbId1 in elem:
                        elem.remove(cdtrMmbId1)

            if (chkCdtrOtherId == 'on'):
                cdtrOtherId1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:Othr/doc:Id', ns)
                cdtrOtherId1.text = cdtrOtherId

            else:
                cdtrOtherId1 = element.find('.//doc:CdtrAgt/doc:FinInstnId/doc:Othr', ns)
                for elem in root.findall(".//*"):
                    if cdtrOtherId1 in elem:
                        elem.remove(cdtrOtherId1)

        if dbtrAgtDataChoice == 1:
            cur.execute('SELECT Bic FROM bank_details')
            BicData = cur.fetchall()
            BicData1 = [temp[0] for temp in BicData]
            cur.execute('SELECT ClearingCode FROM bank_details')
            ClearingCodeData = cur.fetchall()
            ClearingCodeData1 = [temp[0] for temp in ClearingCodeData]
            cur.execute('SELECT RoutingNo FROM bank_details')
            RoutingNoData = cur.fetchall()
            RoutingNoData1 = [temp[0] for temp in RoutingNoData]
            cur.execute('SELECT OtherId FROM bank_details')
            OtherIdData = cur.fetchall()
            OtherIdData1 = [temp[0] for temp in OtherIdData]
            if (chkDbtrBic == 'on'):
                dbtrBic1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:BICFI', ns)
                if (dbtrAgtCountBic < len(BicData1)):
                    dbtrBic1.text = str(BicData1[dbtrAgtCountBic])
                    dbtrAgtCountBic = dbtrAgtCountBic + 1

                else:
                    dbtrAgtCountBic = 0
                    dbtrBic1.text = str(BicData1[dbtrAgtCountBic])
                    dbtrAgtCountBic = dbtrAgtCountBic + 1

            if (chkDbtrClrSysId == 'on'):
                if radioDbtrCdPrtry == 1:
                    dbtrCd1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Cd', ns)
                    if (dbtrAgtCountCd < len(ClearingCodeData1)):
                        dbtrCd1.text = str(ClearingCodeData1[dbtrAgtCountCd])
                        dbtrAgtCountCd = dbtrAgtCountCd + 1

                    else:
                        dbtrAgtCountCd = 0
                        dbtrCd1.text = str(ClearingCodeData1[dbtrAgtCountCd])
                        dbtrAgtCountCd = dbtrAgtCountCd + 1

            if radioDbtrCdPrtry == 2:
                dbtrPrtry1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Prtry',
                                          ns)
                dbtrPrtry1.text = "Prtry12345"

            if (chkDbtrMmbId == 'on'):
                dbtrMmbId1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:MmbId', ns)
                if (dbtrAgtCountMmb < len(RoutingNoData1)):
                    dbtrMmbId1.text = str(RoutingNoData1[dbtrAgtCountMmb])
                    dbtrAgtCountMmb = dbtrAgtCountMmb + 1

                else:
                    dbtrAgtCountMmb = 0
                    dbtrMmbId1.text = str(RoutingNoData1[dbtrAgtCountMmb])
                    dbtrAgtCountMmb = dbtrAgtCountMmb + 1

            if (chkDbtrOtherId == 'on'):
                dbtrOtherId1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:Othr/doc:Id', ns)
                if (dbtrAgtCountOthr < len(OtherIdData1)):
                    dbtrOtherId1.text = str(OtherIdData1[dbtrAgtCountOthr])
                    dbtrAgtCountOthr = dbtrAgtCountOthr + 1

                else:
                    dbtrAgtCountOthr = 0
                    dbtrOtherId1.text = str(OtherIdData1[dbtrAgtCountOthr])
                    dbtrAgtCountOthr = dbtrAgtCountOthr + 1

        elif dbtrAgtDataChoice ==2:
            if (chkDbtrBic == 'on'):
                dbtrBic1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:BICFI', ns)
                dbtrBic1.text = dbtrBic

            else:
                dbtrBic1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:BICFI', ns)
                for elem in root.findall(".//*"):
                    if dbtrBic1 in elem:
                        elem.remove(dbtrBic1)

            if (chkDbtrClrSysId == 'on'):
                if radioDbtrCdPrtry == 1:
                    dbtrCd1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Cd', ns)
                    dbtrCd1.text = dbtrCd

                else:
                    dbtrCd1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Cd', ns)
                    for elem in root.findall(".//*"):
                        if dbtrCd1 in elem:
                            elem.remove(dbtrCd1)

                if radioDbtrCdPrtry == 2:
                    dbtrPrtry1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Prtry',
                                              ns)
                    dbtrPrtry1.text = dbtrPrtry

                else:
                    dbtrPrtry1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId/doc:Prtry',
                                              ns)
                    for elem in root.findall(".//*"):
                        if dbtrPrtry1 in elem:
                            elem.remove(dbtrPrtry1)

            else:
                ClrSysId = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:ClrSysId', ns)
                for elem in root.findall(".//*"):
                    if ClrSysId in elem:
                        elem.remove(ClrSysId)

            if (chkDbtrMmbId == 'on'):
                dbtrMmbId1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:MmbId', ns)
                dbtrMmbId1.text = dbtrMmbId

            else:
                dbtrMmbId1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId/doc:MmbId', ns)
                for elem in root.findall(".//*"):
                    if dbtrMmbId1 in elem:
                        elem.remove(dbtrMmbId1)

            if (chkDbtrOtherId == 'on'):
                dbtrOtherId1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:Othr/doc:Id', ns)
                dbtrOtherId1.text = dbtrOtherId

            else:
                dbtrOtherId1 = element.find('.//doc:DbtrAgt/doc:FinInstnId/doc:Othr', ns)
                for elem in root.findall(".//*"):
                    if dbtrOtherId1 in elem:
                        elem.remove(dbtrOtherId1)

            # ChrgBr = root.find(".//doc:Document/doc:FIToFICstmrCdtTrf/doc:CdtTrfTxInf/doc:ChrgBr", ns)
            # for elem in root.findall(".//*"):
            # if ChrgBr in elem:
            # elem.remove(ChrgBr)

            # Ustrd = root.find(".//doc:Document/doc:FIToFICstmrCdtTrf/doc:CdtTrfTxInf/doc:RmtInf/doc:Ustrd", ns)
            # for elem in root.findall(".//*"):
            # if Ustrd in elem:
            # elem.remove(Ustrd)

            # ClrSysRef = root.find(".//doc:Document/doc:FIToFICstmrCdtTrf/doc:CdtTrfTxInf/doc:PmtId/doc:ClrSysRef", ns)
            # for elem in root.findall(".//*"):
            # if ClrSysRef in elem:
            # elem.remove(ClrSysRef)

            # UETR = root.find(".//doc:Document/doc:FIToFICstmrCdtTrf/doc:CdtTrfTxInf/doc:PmtId/doc:UETR", ns)
            # for elem in root.findall(".//*"):
            # if UETR in elem:
            # elem.remove(UETR)

    tree.write("Output\SampleFileMain.xml", xml_declaration=True, encoding='utf-8')
    print("File 2 generated sucessfully..")


