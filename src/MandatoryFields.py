import datetime
import uuid

def mandatoryFieldsValue(ns, root,batchNo,txnNo,mandatoryData,valueDate):
    for i, (key, path) in enumerate(mandatoryData):
        now = datetime.datetime.now()
        key = key.strip(" ")
        sp = path.strip(" ")
        pathValue = sp.strip("/")
        try:
            if key == "BatchId":
                # btchId = 'BTCH' + c_date + uid  # BtchId
                for btchId1 in root.findall(f".//{pathValue}", ns):
                    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                    btchId = 'BTCH' + c_date + uid
                    btchId1.text = str(btchId)

            elif key == "NumberOfBatch":
                for NoOfBtch1 in root.findall(f".//{pathValue}", ns):
                    NoOfBtch1.text = str(batchNo)

            elif key == "BusinessMessageId":
                for bizMsgIdr1 in root.findall(f".//{pathValue}", ns):
                    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                    bizMsgIdr = 'BZMSG' + c_date + uid  # BizMsgIdr
                    bizMsgIdr1.text = str(bizMsgIdr)

            elif key == "MessageId":
                for msgId1 in root.findall(f".//{pathValue}", ns):
                    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                    msgId = 'MSG' + c_date + '' + uid  # MsgId
                    msgId1.text = str(msgId)

            elif key == "BtchHdr_NumberOfTxn":
                for NbOfTxn1 in root.findall(f".//{pathValue}", ns):
                    NbOfTxn1.text = str(txnNo)

            elif key == "InstructionId":
                for InstrId1 in root.findall(f".//{pathValue}", ns):
                    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                    InstrId = 'INST' + c_date + '' + uid  # InstrId
                    InstrId1.text = str(InstrId)

            elif key == "EndToEndId":
                for EndToEndId1 in root.findall(f".//{pathValue}", ns):
                    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                    EndToEndId = 'E2E' + c_date + '' + uid  # EndToEndId
                    EndToEndId1.text = str(EndToEndId)

            elif key == "TransactionId":
                for TxID1 in root.findall(f".//{pathValue}", ns):
                    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                    TxID = 'TXID' + c_date + uid  # TXID
                    TxID1.text = str(TxID)

            elif key == "ClearingSystemRef":
                for ClrSysRef1 in root.findall(f".//{pathValue}", ns):
                    c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
                    uid = uuid.uuid4().hex[:15].upper()  # Generate UUID
                    ClrSysRef = 'CLRREF' + c_date + uid  # ClrSysRef
                    ClrSysRef1.text = str(ClrSysRef)

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
