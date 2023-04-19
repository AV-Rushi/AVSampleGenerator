import sqlite3
import time
import xml.etree.ElementTree as ET
from faker import Faker
import uuid
import datetime
import AmountFormat
import Cdtr_DbtrAgtExistingData
import Cdtr_DbtrData
import MandatoryFields
import RemoveCode


def writeFile(file,batchNo,txnNo,amtType,amount, ccy, ccy1, valueDate,ccyCheck,cdtrDataChoice,dbtrDataChoice,cdtrAccountLength,dbtrAccountLength,chkCdtrBic,cdtrBic,chkCdtrClrSysId,radioCdtrCdPrtry,cdtrCd,cdtrPrtry,chkCdtrMmbId,cdtrMmbId,chkCdtrOtherId,cdtrOtherId,chkDbtrBic,dbtrBic,chkDbtrClrSysId,radioDbtrCdPrtry,dbtrCd,dbtrPrtry,chkDbtrMmbId,dbtrMmbId,chkDbtrOtherId,dbtrOtherId,cdtrAgtDataChoice,dbtrAgtDataChoice,cdtrCountry,dbtrCountry):
    tree = ET.parse("Input\Temp\SampleFileDaynamic.xml")
    ns = dict([node for (_, node) in ET.iterparse("Input\Temp\SampleFileDaynamic.xml", events=['start-ns'])])
    nskeys_1 = list(ns.keys())
    for j in nskeys_1:
        ET.register_namespace(j, ns[j])

    root = tree.getroot()
    fake = Faker()

    conn = sqlite3.connect('DataBase/SampleGenerator.db')  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute('SELECT Key,Path FROM template_config where TemplateName=?', (file,))
    ConfigData = cur.fetchall()
    ConfigFieldList = [x[0] for x in ConfigData]
    # print(ConfigFieldList)
    ConfigPathList = [x[1] for x in ConfigData]
    # print(ConfigPathList)
    # print(ConfigData)
    cur.execute('SELECT Key,Path FROM template_config where TemplateName==?', (file,))
    mandataryData = cur.fetchall()
    MandatoryFields.mandatoryFieldsValue(ns,root,batchNo,txnNo,mandataryData,valueDate)

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
                    formatted_amount1 = AmountFormat.formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for intrBkSttlmAmt1 in root.findall(f".//{pathValue}", ns):
                        intrBkSttlmAmt1.text = str(formatted_amount1)
                        intrBkSttlmAmt1.set('Ccy', ccy)

                else:
                    formatted_amount1, formatted_amount2 = AmountFormat.formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for intrBkSttlmAmt1 in root.findall(f".//{pathValue}", ns):
                        intrBkSttlmAmt1.text = str(formatted_amount1)
                        intrBkSttlmAmt1.set('Ccy', ccy)

            elif key == "InstructedAmount":
                if ccy1 is None:
                    formatted_amount1 = AmountFormat.formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for instdAmt1 in root.findall(f".//{pathValue}", ns):
                        instdAmt1.text = str(formatted_amount1)
                        instdAmt1.set('Ccy', ccy)
                else:
                    formatted_amount1, formatted_amount2 = AmountFormat.formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo)
                    for instdAmt1 in root.findall(f".//{pathValue}", ns):
                        instdAmt1.text = str(formatted_amount2)
                        instdAmt1.set('Ccy', ccy1)

            elif key == "CreditorAgentBic":
                cdtrAgtBic1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrBic == 'on'):
                        Cdtr_DbtrAgtExistingData.AgentBic(AgtCount,cdtrAgtBic1)
                    else:
                        delElement = root.find(f".//{pathValue}", ns)
                        RemoveCode.removeTag(root,delElement)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrBic == 'on'):
                        for Bic1 in cdtrAgtBic1:
                            Bic1.text = str(cdtrBic)
                    else:
                        delElement = root.find(f".//{pathValue}", ns)
                        RemoveCode.removeTag(root, delElement)

            elif key == "DebtorAgentBic":
                dbtrAgtBic1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                        if (chkDbtrBic == 'on'):
                            # Cdtr_DbtrAgtExistingData.DbtrAgentBic(dbtrAgtCountBic,dbtrAgtBic1)
                            Cdtr_DbtrAgtExistingData.AgentBic(AgtCount, dbtrAgtBic1)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)


                elif dbtrAgtDataChoice == 2:
                        if (chkDbtrBic == 'on'):
                            for Bic1 in dbtrAgtBic1:
                                Bic1.text = str(dbtrBic)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)

            elif key == "CreditorAgentMemberId":
                cdtrAgtMmbId1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                        if (chkCdtrMmbId == 'on'):
                            Cdtr_DbtrAgtExistingData.AgentMmbId(AgtCount,cdtrAgtMmbId1)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)

                elif cdtrAgtDataChoice == 2:
                        if (chkCdtrMmbId == 'on'):
                            for MmbId1 in cdtrAgtMmbId1:
                                MmbId1.text = str(cdtrMmbId)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)


            elif key == "DebtorAgentMemberId":
                dbtrAgtMmbId1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                        if (chkDbtrMmbId == 'on'):
                            Cdtr_DbtrAgtExistingData.AgentMmbId(AgtCount,dbtrAgtMmbId1)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)
                elif dbtrAgtDataChoice == 2:
                        if (chkDbtrMmbId == 'on'):
                            for MmbId1 in dbtrAgtMmbId1:
                                MmbId1.text = str(dbtrMmbId)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)

            elif key == "CreditorAgentOtherId":
                cdtrAgtOthrId1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrOtherId == 'on'):
                        Cdtr_DbtrAgtExistingData.AgentOthrId(AgtCount,cdtrAgtOthrId1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrOtherId == 'on'):
                        for OthrId1 in cdtrAgtOthrId1:
                            OthrId1.text = str(cdtrOtherId)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

            elif key == "DebtorAgentOtherId":
                dbtrAgtOthrId1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                    if(chkDbtrOtherId == 'on'):
                        Cdtr_DbtrAgtExistingData.AgentOthrId(AgtCount,dbtrAgtOthrId1)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

                elif dbtrAgtDataChoice == 2:
                    if (chkDbtrOtherId == 'on'):
                        for OthrId1 in dbtrAgtOthrId1:
                            OthrId1.text = str(dbtrOtherId)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

            elif key == "CreditorClrSysId_Cd":
                cdtrCd1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 1:
                            Cdtr_DbtrAgtExistingData.AgentClrSysId_Cd(AgtCount,cdtrCd1)

                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)


                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 1:
                            for cdtr_Cd in cdtrCd1:
                                cdtr_Cd.text = str(cdtrCd)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

            elif key == "CreditorClrSysId_Prtry":
                cdtrPrtry1 = root.findall(f".//{pathValue}", ns)
                if cdtrAgtDataChoice == 1:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 2:
                            Cdtr_DbtrAgtExistingData.AgentClrSysId_Prtry(AgtCount,cdtrPrtry1)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

                elif cdtrAgtDataChoice == 2:
                    if (chkCdtrClrSysId == 'on'):
                        if radioCdtrCdPrtry == 2:
                            for cdtr_Prtry in cdtrPrtry1:
                                cdtr_Prtry.text = str(cdtrPrtry)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

            elif key == "DebtorClrSysId_Cd":
                dbtrCd1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                    if (chkCdtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 1:
                            Cdtr_DbtrAgtExistingData.AgentClrSysId_Cd(AgtCount,dbtrCd1)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)

                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

                elif dbtrAgtDataChoice == 2:
                    if (chkCdtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 1:
                            for dbtr_Cd in dbtrCd1:
                                dbtr_Cd.text = str(dbtrCd)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)

                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

            elif key == "DebtorClrSysId_Prtry":
                dbtrPrtry1 = root.findall(f".//{pathValue}", ns)
                if dbtrAgtDataChoice == 1:
                    if (chkCdtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 2:
                            Cdtr_DbtrAgtExistingData.AgentClrSysId_Prtry(AgtCount,dbtrPrtry1)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)


                elif dbtrAgtDataChoice == 2:
                    if (chkCdtrClrSysId == 'on'):
                        if radioDbtrCdPrtry == 2:
                            for dbtr_Prtry in dbtrPrtry1:
                                dbtr_Prtry.text = str(dbtrPrtry)
                        else:
                            delElement = root.find(f".//{pathValue}", ns)
                            RemoveCode.removeTag(root, delElement)
                    else:
                        pathValue1 = "/".join(pathValue.split("/")[:-1])
                        delElement = root.find(f".//{pathValue1}", ns)
                        RemoveCode.removeTag(root, delElement)

            if (chkDbtrClrSysId != 'on') and (chkDbtrMmbId != 'on'):
                ClrSysId2 = root.find(f'.//doc:DbtrAgt/doc:FinInstnId/doc:ClrSysMmbId', ns)
                for elem in root.findall(".//*"):
                    if ClrSysId2 in elem:
                        elem.remove(ClrSysId2)

            if (chkCdtrClrSysId != 'on') and (chkCdtrMmbId != 'on'):
                ClrSysId2 = root.find(f'.//doc:CdtrAgt/doc:FinInstnId/doc:ClrSysMmbId', ns)
                for elem in root.findall(".//*"):
                    if ClrSysId2 in elem:
                        elem.remove(ClrSysId2)

            elif key == "CreditorAccountNo":
                cdtrAccNo1 = root.findall(f".//{pathValue}", ns)
                if cdtrDataChoice == 1:
                    Cdtr_DbtrData.existingAccountNo(Count,cdtrAccNo1)

                elif cdtrDataChoice == 2:

                    Cdtr_DbtrData.DummyAccountNo(cdtrAccountLength,cdtrAccNo1)

            elif key == "CreditorName":
                cdtrNm1 = root.findall(f".//{pathValue}", ns)
                if cdtrDataChoice == 1:
                    Cdtr_DbtrData.existingAccountName(Count,cdtrNm1)

                elif cdtrDataChoice == 2:
                    cdtrCountry = 'IN'
                    Cdtr_DbtrData.DummyAccountNm(cdtrCountry,cdtrNm1)

            elif key == "DebtorAccountNo":
                dbtrAccNo1 = root.findall(f".//{pathValue}", ns)
                if dbtrDataChoice == 1:
                    Cdtr_DbtrData.existingAccountNo(Count, dbtrAccNo1)

                elif dbtrDataChoice == 2:
                    Cdtr_DbtrData.DummyAccountNo(dbtrAccountLength, dbtrAccNo1)

            elif key == "DebtorName":
                dbtrNm1 = root.findall(f".//{pathValue}", ns)
                if dbtrDataChoice == 1:
                    Cdtr_DbtrData.existingAccountName(Count, dbtrNm1)

                elif dbtrDataChoice == 2:
                    dbtrCountry = 'AU'
                    Cdtr_DbtrData.DummyAccountNm(dbtrCountry, dbtrNm1)

            else:
                continue

        except Exception as e:
                print(f"Error: {e} for {key}")

    now = datetime.datetime.now()
    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID

    f_date = (now.strftime("%y%m%d%H%M%S"))
    tree.write(f"Output\Output_{f_date}.xml", xml_declaration=True, encoding='utf-8')
    # tree.write(f"Output\{file}_{f_date}.xml", xml_declaration=True, encoding='utf-8')
    # print("File 2 generated sucessfully..")

# writeFile(3, 5, 'BHD', None, 'off', 2, 56748, '2023-07-05',1,'on',2,'on','on','on','on','on','on',2,1,2,2)
