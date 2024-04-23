import fitz,csv
with open(f'static/purchase_details_.csv', 'w') as csv_:
    doc = fitz.open(f'static/purchase_details.pdf')
    writer = csv.writer(csv_)
    writer.writerow(i.replace('\n', ' ').strip() for i in doc[0].find_tables()[0].extract()[0])
    for page in doc:
        writer.writerows(i for i in page.find_tables()[0].extract()[1:])
        print(page)
with open(f'static/redemption_details_.csv', 'w') as csv_:
    doc = fitz.open(f'static/redemption_details.pdf')
    writer = csv.writer(csv_)
    writer.writerow(i.replace('\n', ' ').strip() for i in doc[0].find_tables()[0].extract()[0])
    for page in doc:
        writer.writerows(i for i in page.find_tables()[0].extract()[1:])
        print(page)