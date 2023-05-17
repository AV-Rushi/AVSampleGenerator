import sqlite3
import time
import xml.etree.ElementTree as ET
from faker import Faker
import uuid
import datetime
from AmountFormat import formatAmount
from Cdtr_DbtrAgtExistingData import AgentBic,AgentOthrId,AgentMmbId,AgentClrSysId_Cd,AgentClrSysId_Prtry
from Cdtr_DbtrData import existingAccountNo,existingAccountName,DummyAccountNo,DummyAccountNm
from MandatoryFields import mandatoryFieldsValue
from RemoveCode import removeTag1
import os

# def writeFile():
def writeFile(file,batchNo,txnNo,amtType,amount, ccy, ccy1, valueDate,ccyCheck,cdtrDataChoice,dbtrDataChoice,cdtrAccountLength,dbtrAccountLength,chkCdtrBic,cdtrBic,chkCdtrClrSysId,radioCdtrCdPrtry,cdtrCd,cdtrPrtry,chkCdtrMmbId,cdtrMmbId,chkCdtrOtherId,cdtrOtherId,chkDbtrBic,dbtrBic,chkDbtrClrSysId,radioDbtrCdPrtry,dbtrCd,dbtrPrtry,chkDbtrMmbId,dbtrMmbId,chkDbtrOtherId,dbtrOtherId,cdtrAgtDataChoice,dbtrAgtDataChoice,cdtrCountry,dbtrCountry):
#     print(os.getcwd())
#     os.chdir(f'..')
    # print(os.getcwd())
    file1 = (f"..\Input\Temp\SampleFileDaynamic.xml")
    tree = ET.parse(file1)
    ns = dict([node for (_, node) in ET.iterparse(file1, events=['start-ns'])])
    nskeys_1 = list(ns.keys())
    for j in nskeys_1:
        ET.register_namespace(j, ns[j])

    root = tree.getroot()
    fake = Faker()

    conn = sqlite3.connect('../DataBase/SampleGenerator.db')  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute('SELECT Key,Path FROM template_config where TemplateName=?', (file,))
    ConfigData = cur.fetchall()
    cur.execute('SELECT Key,Path,RegEx_Pattern FROM template_config where TemplateName==?', (file,))
    mandataryData = cur.fetchall()
    mandatoryFieldsValue(ns,root,batchNo,txnNo,mandataryData,valueDate)

    cur.execute('SELECT distinct CountryCode FROM currency where Decimals=3')
    lst1 = cur.fetchall()
    cur.execute('SELECT distinct CountryCode FROM currency where Decimals=2')
    lst2 = cur.fetchall()
    cur.execute('SELECT distinct CountryCode FROM currency where Decimals=0')
    lst3 = cur.fetchall()

    AgtCount = 0
    Count = 0
    for i, (key, path) in enumerate(ConfigData):
        now = datetime.datetime.now()
        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID

        key = key.strip(" ")
        sp = path.strip(" ")
        pathValue = sp.strip("/")
        try:
            if key == "InterbankSttlmAmtCcy":
                for currency1 in root.findall(f".//{pathValue}", ns):
                    if (ccyCheck == 'on'):
                        currency1.set('Ccy', ccy)
                    else:
                        currency1.set('Ccy', ccy)

            elif key == "InstructedAmtCcy":
                for currency2 in root.findall(f".//{pathValue}", ns):
                    if (ccyCheck == 'on'):
                        currency2.set('Ccy', ccy)
                    else:
                        currency2.set('Ccy', ccy1)

            elif key == "InterbankSettlementAmt":
                if ccy1 is None:
                    formatted_amount1 = formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for intrBkSttlmAmt1 in root.findall(f".//{pathValue}", ns):
                        intrBkSttlmAmt1.text = str(formatted_amount1)
                        intrBkSttlmAmt1.set('Ccy', ccy)

                else:
                    formatted_amount1, formatted_amount2 = formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for intrBkSttlmAmt1 in root.findall(f".//{pathValue}", ns):
                        intrBkSttlmAmt1.text = str(formatted_amount1)
                        intrBkSttlmAmt1.set('Ccy', ccy)

            elif key == "InstructedAmount":
                if ccy1 is None:
                    formatted_amount1 = formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for instdAmt1 in root.findall(f".//{pathValue}", ns):
                        instdAmt1.text = str(formatted_amount1)
                        instdAmt1.set('Ccy', ccy)
                else:
                    formatted_amount1, formatted_amount2 = formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for instdAmt1 in root.findall(f".//{pathValue}", ns):
                        instdAmt1.text = str(formatted_amount2)
                        instdAmt1.set('Ccy', ccy1)

            elif key == "CreditorAgentBic":
                cdtrAgtBic1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrBic == 'on'):
                        AgentBic(AgtCount,cdtrAgtBic1)
                    else:
                        removeTag1(root,cdtrAgtBic1)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrBic == 'on'):
                        for Bic1 in cdtrAgtBic1:
                            Bic1.text = str(cdtrBic)
                    else:
                        removeTag1(root, cdtrAgtBic1)

            elif key == "DebtorAgentBic":
                dbtrAgtBic1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                        if (chkDbtrBic == 'on'):
                            # Cdtr_DbtrAgtExistingData.DbtrAgentBic(dbtrAgtCountBic,dbtrAgtBic1)
                            AgentBic(AgtCount, dbtrAgtBic1)
                        else:
                            removeTag1(root,dbtrAgtBic1)


                elif dbtrAgtDataChoice == 2:
                        if (chkDbtrBic == 'on'):
                            for Bic1 in dbtrAgtBic1:
                                Bic1.text = str(dbtrBic)
                        else:
                            removeTag1(root,dbtrAgtBic1)

            elif key == "CreditorAgentMemberId":
                cdtrAgtMmbId1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                        if (chkCdtrMmbId == 'on'):
                            AgentMmbId(AgtCount,cdtrAgtMmbId1)
                        else:
                            removeTag1(root,cdtrAgtMmbId1)

                elif cdtrAgtDataChoice == 2:
                        if (chkCdtrMmbId == 'on'):
                            for MmbId1 in cdtrAgtMmbId1:
                                MmbId1.text = str(cdtrMmbId)
                        else:
                            removeTag1(root,cdtrAgtMmbId1)


            elif key == "DebtorAgentMemberId":
                dbtrAgtMmbId1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                        if (chkDbtrMmbId == 'on'):
                            AgentMmbId(AgtCount,dbtrAgtMmbId1)
                        else:
                            removeTag1(root,dbtrAgtMmbId1)

                elif dbtrAgtDataChoice == 2:
                        if (chkDbtrMmbId == 'on'):
                            for MmbId1 in dbtrAgtMmbId1:
                                MmbId1.text = str(dbtrMmbId)
                        else:
                            removeTag1(root,dbtrAgtMmbId1)

            elif key == "CreditorAgentOtherId":
                cdtrAgtOthrId1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrOtherId == 'on'):
                        AgentOthrId(AgtCount,cdtrAgtOthrId1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrOtherId == 'on'):
                        for OthrId1 in cdtrAgtOthrId1:
                            OthrId1.text = str(cdtrOtherId)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

            elif key == "DebtorAgentOtherId":
                dbtrAgtOthrId1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                    if(chkDbtrOtherId == 'on'):
                        AgentOthrId(AgtCount,dbtrAgtOthrId1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

                elif dbtrAgtDataChoice == 2:
                    if (chkDbtrOtherId == 'on'):
                        for OthrId1 in dbtrAgtOthrId1:
                            OthrId1.text = str(dbtrOtherId)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

            elif key == "CreditorClrSysId_Cd":
                cdtrCd1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 1:
                            AgentClrSysId_Cd(AgtCount,cdtrCd1)

                        else:
                            removeTag1(root, cdtrCd1)


                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 1:
                            for cdtr_Cd in cdtrCd1:
                                cdtr_Cd.text = str(cdtrCd)
                        else:
                            removeTag1(root, cdtrCd1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

            elif key == "CreditorClrSysId_Prtry":
                cdtrPrtry1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 2:
                            AgentClrSysId_Prtry(AgtCount,cdtrPrtry1)
                        else:
                            removeTag1(root, cdtrPrtry1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 2:
                            for cdtr_Prtry in cdtrPrtry1:
                                cdtr_Prtry.text = str(cdtrPrtry)
                        else:
                            removeTag1(root, cdtrPrtry1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

            elif key == "DebtorClrSysId_Cd":
                dbtrCd1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                    if (chkDbtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 1:
                            AgentClrSysId_Cd(AgtCount,dbtrCd1)

                        else:
                            removeTag1(root, dbtrCd1)

                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

                elif dbtrAgtDataChoice == 2:
                    if (chkDbtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 1:
                            for dbtr_Cd in dbtrCd1:
                                dbtr_Cd.text = str(dbtrCd)
                        else:
                            removeTag1(root, dbtrCd1)

                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

            elif key == "DebtorClrSysId_Prtry":
                dbtrPrtry1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                    if (chkDbtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 2:
                            AgentClrSysId_Prtry(AgtCount,dbtrPrtry1)

                        else:
                            removeTag1(root, dbtrPrtry1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

                elif dbtrAgtDataChoice == 2:
                    if (chkDbtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 2:
                            for dbtr_Prtry in dbtrPrtry1:
                                dbtr_Prtry.text = str(dbtrPrtry)
                        else:
                            removeTag1(root, dbtrPrtry1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.findall(f".//{pathValue1}", ns)
                        removeTag1(root, delElement)

            if (chkDbtrClrSysId != 'on') and (chkDbtrMmbId != 'on'):
                ClrSysId2 = root.find('.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId', ns)
                for elem in root.findall(".//*"):
                    if ClrSysId2 in elem:
                        elem.remove(ClrSysId2)

            if (chkCdtrClrSysId != 'on') and (chkCdtrMmbId != 'on'):
                ClrSysId2 = root.find('.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId', ns)
                for elem in root.findall(".//*"):
                    if ClrSysId2 in elem:
                        elem.remove(ClrSysId2)
            if (chkCdtrBic != 'on') and (chkCdtrClrSysId != 'on') and (chkCdtrMmbId != 'on') and (chkCdtrOtherId != 'on'):
                cdtrSection = root.find('.//doc:CdtrAgt', ns)
                for elem in root.findall(".//*"):
                    if cdtrSection in elem:
                        elem.remove(cdtrSection)

            if (chkDbtrBic != 'on') and (chkDbtrClrSysId != 'on') and (chkDbtrMmbId != 'on') and (
                    chkDbtrOtherId != 'on'):
                dbtrSection = root.find('.//doc:DbtrAgt', ns)
                for elem in root.findall(".//*"):
                    if dbtrSection in elem:
                        elem.remove(dbtrSection)


            elif key == "CreditorAccountNo":
                cdtrAccNo1 = root.findall(f".//{pathValue}", ns)
                if cdtrDataChoice == 1:
                    existingAccountNo(Count,cdtrAccNo1)

                elif cdtrDataChoice == 2:
                    DummyAccountNo(cdtrAccountLength,cdtrAccNo1)

            elif key == "CreditorName":
                cdtrNm1 = root.findall(f".//{pathValue}", ns)
                if cdtrDataChoice == 1:
                    existingAccountName(Count,cdtrNm1)

                elif cdtrDataChoice == 2:
                    DummyAccountNm(cdtrCountry,cdtrNm1)

            elif key == "DebtorAccountNo":
                dbtrAccNo1 = root.findall(f".//{pathValue}", ns)
                if dbtrDataChoice == 1:
                    existingAccountNo(Count, dbtrAccNo1)

                elif dbtrDataChoice == 2:
                    DummyAccountNo(dbtrAccountLength, dbtrAccNo1)

            elif key == "DebtorName":
                dbtrNm1 = root.findall(f".//{pathValue}", ns)
                if dbtrDataChoice == 1:
                    existingAccountName(Count, dbtrNm1)

                elif dbtrDataChoice == 2:
                    DummyAccountNm(dbtrCountry, dbtrNm1)

            else:
                continue

        except Exception as e:
                print(f"Error: {e} for {key}")

    now = datetime.datetime.now()
    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID

    f_date = (now.strftime("%y%m%d%H%M%S"))
    s1 = (f"{file}_{f_date}.xml")
    tree.write(f"..\Output\{file}_{f_date}.xml", xml_declaration=True, encoding='utf-8')
   # tree.write(f"C:/Users/User/AV/AVSampleGenerator1/Output/{s1}", xml_declaration=True, encoding='utf-8')
    return s1