import datetime
import sqlite3
import uuid
from IDGenerationRegEx import regex_pattern

def mandatoryFieldsValue(ns, root,batchNo,txnNo,mandatoryData,valueDate):
    for i, (key, path,regex_pattern1) in enumerate(mandatoryData):
        now = datetime.datetime.now()
        key = key.strip(" ")
        sp = path.strip(" ")
        pathValue = sp.strip("/")
        try:
            if key == "BatchId":
                btchId1  = root.findall(f".//{pathValue}", ns)
                if regex_pattern1 is not None:
                    regex_pattern(btchId1,regex_pattern1)

                else:
                    for btch_Id in btchId1:
                        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                        btchId = 'BTCH' + c_date + uid
                        btch_Id.text = str(btchId)

            elif key == "NumberOfBatch":
                for NoOfBtch1 in root.findall(f".//{pathValue}", ns):
                    NoOfBtch1.text = str(batchNo)

            elif key == "BusinessMessageId":
                bizMsgIdr1 = root.findall(f".//{pathValue}", ns)
                if regex_pattern1 is not None:
                    regex_pattern(bizMsgIdr1, regex_pattern1)

                else:
                    for bizMsgId in bizMsgIdr1:
                        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                        bizMsgIdr = 'BZMSG' + c_date + uid  # BizMsgIdr
                        bizMsgId.text = str(bizMsgIdr)

            elif key == "MessageId":
                msgId1 = root.findall(f".//{pathValue}", ns)
                if regex_pattern1 is not None:
                    regex_pattern(msgId1, regex_pattern1)

                else:
                    for msg_Id in msgId1:
                        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                        msgId = 'MSG' + c_date + '' + uid  # MsgId
                        msg_Id.text = str(msgId)

            elif key == "BtchHdr_NumberOfTxn":
                for NbOfTxn1 in root.findall(f".//{pathValue}", ns):
                    NbOfTxn1.text = str(txnNo)

            elif key == "InstructionId":
                InstrId1 = root.findall(f".//{pathValue}", ns)
                if regex_pattern1 is not None:
                    regex_pattern(InstrId1, regex_pattern1)

                else:
                    for Instr_Id in InstrId1:
                        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                        InstrId = 'INST' + c_date + '' + uid  # InstrId
                        Instr_Id.text = str(InstrId)

            elif key == "EndToEndId":
                EndToEndId1 = root.findall(f".//{pathValue}", ns)
                if regex_pattern1 is not None:
                    regex_pattern(EndToEndId1, regex_pattern1)
                else:
                    for EndToEnd in EndToEndId1:
                        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                        EndToEndId = 'E2E' + c_date + '' + uid  # EndToEndId
                        EndToEnd.text = str(EndToEndId)

            elif key == "TransactionId":
                TxID1 = root.findall(f".//{pathValue}", ns)
                if regex_pattern1 is not None:
                    regex_pattern(TxID1, regex_pattern1)
                else:
                    for txId in TxID1:
                        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                        TxID = 'TXID' + c_date + uid  # TXID
                        txId.text = str(TxID)

            elif key == "ClearingSystemRef":
                ClrSysRef1 = root.findall(f".//{pathValue}", ns)
                if regex_pattern1 is not None:
                    regex_pattern(ClrSysRef1, regex_pattern1)
                else:
                    for clrSysRef in ClrSysRef1:
                        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                        ClrSysRef = 'CLRREF' + c_date + uid  # ClrSysRef
                        clrSysRef.text = str(ClrSysRef)

            elif key == "ValueDate":
                for valueDate1 in root.findall(f".//{pathValue}", ns):
                    valueDate1.text = str(valueDate)

            elif key == "CreditDateTime":
                for cdtDtTm1 in root.findall(f".//{pathValue}", ns):
                    CdtDtTm = (now.strftime("%Y-%m-%dT%H:%M:%S"))  # CdtDtTm
                    cdtDtTm1.text = str(CdtDtTm)

            elif key == "CreditorDateTime":
                for creDtTm1 in root.findall(f".//{pathValue}", ns):
                    CreDtTm = (now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3])
                    creDtTm1.text = str(CreDtTm)
            else:
                continue
        except Exception as e:
            print(f"Error: {e} for {key}")
