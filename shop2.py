a = []
r = 0
while True :
    b = input ('ร้านทีมค้าเกือกยินดีต้อนรับฮ้าฟฟฟไอ้พวกต้าวอ้วงงง\n เลือกเกิบคีบ [q]\n เลือกเกิบสุบ [w]\n เลือกเกิบฮ่าง [s]\n แสดงรายการ [z]\n ออก [x]\n')
    b = b.lower()
    if b=='q' :
        print("**********KerbKeeb**********\n [1] StarTiam 120 บาท\n [2] MhaDaw 100 บาท\n [3] KrataiiDaw 80 บาท\n")
        c = input('ป้อนหมายเลขรุ่นตามต้องการ --->')
        if c == '1' :
            a.append('StarTiam : 120:20%:96')
            r+=96
        elif c == '2' :
            a.append('MhaDaw : 100:20%:80')
            r+=80
        elif c == '3' :
            a.append('KrataiiDaw : 80:20%:64')
            r+=64
        print('\n$$$$$$_ข้อมูลได้เข้าระบบแล้วจ้าาา_$$$$$$\n')    
    elif b=='w' :
        print("**********KerbSub**********\n [1] Adidose 190 บาท\n [2] Niker 189 บาท\n [3] Laanghongnaam 79 บาท\n")
        c = input('ป้อนหมายเลขรุ่นตามต้องการ --->')
        if c == '1' :
            a.append('Adidose : 190:30%:133')
            r+=133
        elif c == '2' :
            a.append('Niker : 189:30%:132')
            r+=132
        elif c == '3' :
            a.append('Laanghongnaam : 79:30%:55') 
            r+=55
        print('\n$$$$$$_ข้อมูลได้เข้าระบบแล้วจ้าาา_$$$$$$\n') 
    elif b=='s' :
        print("**********KerbHaang**********\n [1] Kerbkingnueang 50 บาท\n [2] Kerbbormeehuu 39 บาท\n [3] Kerbsord 35 บาท\n")
        c = input('ป้อนหมายเลขรุ่นตามต้องการ --->')
        if c == '1' :
            a.append('Kerbkingnueang : 50:70%:15')
            r+=15
        elif c == '2' :
            a.append('Kerbbormeehuu : 39:70%:11')
            r+=11
        elif c == '3' :
            a.append('Kerbsord : 35:70%:10')
            r+=10
        print('\n$$$$$$_ข้อมูลได้เข้าระบบแล้วจ้าาา_$$$$$$\n')
    elif b=='z' :
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<10}'.format(""))
        print('{0:<22}{1:<10}{2:<10}{3:<15}'.format('รุ่น','ราคา','ส่วนลด','จ่าย'))
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<10}'.format(""))
        count = 0
        for d in a :
            e=d.split(":")
            count += 1
            print(count,end=". ")
            print('{0[0]:<20}{0[1]:<10}{0[2]:<10}{0[3]:<10}'.format(e))
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<10}'.format(""))
        print('รวมเป็นเงิน                                 ',r)
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<10}'.format(""))
    elif b=='x' :
        print('ขอบคุณที่ให้ความสนใจร้านทีมค้าเกือกจ้า')
        break