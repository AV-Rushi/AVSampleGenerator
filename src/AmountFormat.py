def formatAmount(amtType, amount, lst1, lst2, lst3, ccy, ccy1,txnNo,batchNo):
    formatted_amount1 = 0
    formatted_amount2 = 0
    if amtType == 1:
        if ccy1 is None:
            if ccy in [item for sublist in lst1 for item in sublist]:
                formatted_amount1 = "{:.3f}".format(amount)
            elif ccy in [item for sublist in lst2 for item in sublist]:
                formatted_amount1 = "{:.2f}".format(amount)
            elif ccy in [item for sublist in lst3 for item in sublist]:
                formatted_amount1 = int(amount)
            return formatted_amount1

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
            return formatted_amount1, formatted_amount2

    elif amtType == 2:
        if ccy1 is None:
            if ccy in [item for sublist in lst1 for item in sublist]:
                formatted_amount1 = "{:.3f}".format(amount / (txnNo * batchNo))
            elif ccy in [item for sublist in lst2 for item in sublist]:
                formatted_amount1 = "{:.2f}".format(amount / (txnNo * batchNo))
            elif ccy in [item for sublist in lst3 for item in sublist]:
                formatted_amount1 = int((amount / (txnNo * batchNo)))
            return formatted_amount1
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
            return formatted_amount1, formatted_amount2