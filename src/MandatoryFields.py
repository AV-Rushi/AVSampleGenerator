import datetime
import uuid

def mandatoryFieldsValue(ns, root,batchNo,txnNo,mandatoryData,valueDate):
    for i, (key, path) in enumerate(mandatoryData):
        now = datetime.datetime.now()
        c_date = (now.strftime("%y%m%d%H%M%S"))  # Current Date and Time
        uid = uuid.uuid4().hex[:15].upper()  # Generate UUID

        key = key.strip(" ")
        sp = path.strip(" ")
        pathValue = sp.strip("/")
        try:
            if key == "BatchId":
                btchId = 'BTCH' + c_date + uid  # BtchId
                for btchId1 in root.findall(f".//{pathValue}", ns):
                    btchId1.text = str(btchId)

            elif key == "NumberOfBatch":
                for NoOfBtch1 in root.findall(f".//{pathValue}", ns):
                    NoOfBtch1.text = str(batchNo)

            elif key == "BusinessMessageId":
                bizMsgIdr = 'BZMSG' + c_date + uid  # BizMsgIdr
                for bizMsgIdr1 in root.findall(f".//{pathValue}", ns):
                    bizMsgIdr1.text = str(bizMsgIdr)

            elif key == "MessageId":
                msgId = 'MSG' + c_date + '' + uid  # MsgId
                for msgId1 in root.findall(f".//{pathValue}", ns):
                    msgId1.text = str(msgId)

            elif key == "BtchHdr_NumberOfTxn":
                for NbOfTxn1 in root.findall(f".//{pathValue}", ns):
                    NbOfTxn1.text = str(txnNo)

            elif key == "InstructionId":
                InstrId = 'INST' + c_date + '' + uid  # InstrId
                for InstrId1 in root.findall(f".//{pathValue}", ns):
                    InstrId1.text = str(InstrId)

            elif key == "EndToEndId":
                EndToEndId = 'E2E' + c_date + '' + uid  # EndToEndId
                for EndToEndId1 in root.findall(f".//{pathValue}", ns):
                    EndToEndId1.text = str(EndToEndId)

            elif key == "TransactionId":
                TxID = 'TXID' + c_date + uid  # TXID
                for TxID1 in root.findall(f".//{pathValue}", ns):
                    TxID1.text = str(TxID)

            elif key == "ClearingSystemRef":
                ClrSysRef = 'CLRREF' + c_date + uid  # ClrSysRef
                for ClrSysRef1 in root.findall(f".//{pathValue}", ns):
                    ClrSysRef1.text = str(ClrSysRef)

            elif key == "ValueDate":
                for valueDate1 in root.findall(f".//{pathValue}", ns):
                    valueDate1.text = str(valueDate)

            elif key == "CreditDateTime":
                CdtDtTm = (now.strftime("%Y-%m-%dT%H:%M:%S"))  # CdtDtTm
                for cdtDtTm1 in root.findall(f".//{pathValue}", ns):
                    cdtDtTm1.text = str(CdtDtTm)

            elif key == "CreditorDateTime":
                CreDtTm = (now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3])
                for creDtTm1 in root.findall(f".//{pathValue}", ns):
                    creDtTm1.text = str(CreDtTm)
            else:
                continue
        except Exception as e:
            print(f"Error: {e} for {key}")
