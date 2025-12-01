#!/usr/bin/env python3
from ofxparse import OfxParser
import csv
import sys

with open(sys.argv[1], encoding='iso-8859-1') as f:
    ofx = OfxParser.parse(f)

with open('saida.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Data', 'Descrição', 'Valor'])
    
    for trans in ofx.account.statement.transactions:
        writer.writerow([trans.date, trans.payee, trans.amount])