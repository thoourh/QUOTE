import CPU_List,GPU_List,mainboard_List,power_List,RAM_List,ssd_List,DataHandle
import tkinter
import os
class test():
    # 생성자
    cL = CPU_List.CPU_List()
    gL = GPU_List.GPU_List()
    mL = mainboard_List.mainboard_List()
    pL = power_List.power_List()
    rL = RAM_List.RAM_List()
    sL = ssd_List.ssd_List()
    if os.path.exists("C:/Users/User/Desktop/Quote comparison/QUOTE.txt"):
        with open("C:/Users/User/Desktop/Quote comparison/QUOTE.txt", 'r') as file:
            # 파일 내용을 줄 단위로 읽어옵니다.
            lines = file.readlines()
            
            for line in lines:
                parts = []
                line = line.strip().replace(", ", ":")
                parts = line.strip().split(':',)

                if "001" == parts[1].strip():
                    number = parts[0].strip()
                    value1 = parts[1].strip()
                    name = parts[2].strip()
                    value2 = parts[3].strip()
                    price = parts[4].strip()
                    value3 = parts[5].strip()
                    score = parts[6].strip()
                    value4 = parts[7].strip()
                    CPU_List.CPU_List.PartList.append({number: value1, name: value2, price: value3, score: value4 })
                    print(CPU_List.CPU_List.PartList)
                if "002" == parts[1].strip():
                    number = parts[0].strip()
                    value1 = parts[1].strip()
                    name = parts[2].strip()
                    value2 = parts[3].strip()
                    price = parts[4].strip()
                    value3 = parts[5].strip()
                    score = parts[6].strip()
                    value4 = parts[7].strip()
                    GPU_List.GPU_List.PartList.append({number: value1, name: value2, price: value3, score: value4 })
                if "003" == parts[1].strip():
                    number = parts[0].strip()
                    value1 = parts[1].strip()
                    name = parts[2].strip()
                    value2 = parts[3].strip()
                    price = parts[4].strip()
                    value3 = parts[5].strip()
                    score = parts[6].strip()
                    value4 = parts[7].strip()
                    mainboard_List.mainboard_List.PartList.append({number: value1, name: value2, price: value3, score: value4 })
                if "004" == parts[1].strip():
                    number = parts[0].strip()
                    value1 = parts[1].strip()
                    name = parts[2].strip()
                    value2 = parts[3].strip()
                    price = parts[4].strip()
                    value3 = parts[5].strip()
                    score = parts[6].strip()
                    value4 = parts[7].strip()
                    power_List.power_List.PartList.append({number: value1, name: value2, price: value3, score: value4 })
                if "005" == parts[1].strip():
                    number = parts[0].strip()
                    value1 = parts[1].strip()
                    name = parts[2].strip()
                    value2 = parts[3].strip()
                    price = parts[4].strip()
                    value3 = parts[5].strip()
                    score = parts[6].strip()
                    value4 = parts[7].strip()
                    RAM_List.RAM_List.PartList.append({number: value1, name: value2, price: value3, score: value4 })
                if "006" == parts[1].strip():
                    number = parts[0].strip()
                    value1 = parts[1].strip()
                    name = parts[2].strip()
                    value2 = parts[3].strip()
                    price = parts[4].strip()
                    value3 = parts[5].strip()
                    score = parts[6].strip()
                    value4 = parts[7].strip()
                    ssd_List.ssd_List.PartList.append({number: value1, name: value2, price: value3, score: value4 })
            


    #데이터 추가
    def inputData():
        window=tkinter.Tk()
        window.title("추가할 데이터를 입력하시오")
        window.geometry("640x400+100+100")
        window.resizable(False, False)
        def transfor():
            a = entry.get()
            b = a.split()
            if b[0] == "001":
                CPU_List.CPU_List.inputData(self=CPU_List.CPU_List,ddt = a)
            elif b[0] == "002":
                GPU_List.GPU_List.inputData(self=GPU_List.GPU_List,ddt= a)
            elif b[0] == "003":
                mainboard_List.mainboard_List.inputData(self=mainboard_List.mainboard_List,ddt=a)
            elif b[0] == "004":
                power_List.power_List.inputData(self=power_List.power_List,ddt=a)
            elif b[0] == "005":
                RAM_List.RAM_List.inputData(self=RAM_List.RAM_List,ddt=a)
            elif b[0] == "006":
                ssd_List.ssd_List.inputData(self=ssd_List.ssd_List,ddt=a)
            text=tkinter.Label(text= b[1]+"데이터가 추가되었습니다.")
            text.pack()
            
            
        
        
        label=tkinter.Label(window,text="제품의 분류번호,이름,가격,점수를 입력하세요\n001:CPU 002:GPU 003:mainboard 004:power 005:RAM 006:ssd\n")
        label.place(x=170,y=130)

        entry=tkinter.Entry(window)
        entry.place(x=240,y=160)
        check = tkinter.Button(window,text="입력", overrelief="solid", width=15, command=transfor, repeatdelay=1000, repeatinterval=100)
        check.place(x=240,y=190)
        window.mainloop()
        
        return 0

    #데이터 편집
    def setData():
        
        window=tkinter.Tk()
        window.title("수정할 데이터의 분류코드와 이름을 입력하시오")
        window.geometry("640x400+100+100")
        window.resizable(False, False)
        
        def transfor():
            a = entry.get()
            b = a.split()
            if b[0] == "001":
                CPU_List.CPU_List.setData(self=CPU_List.CPU_List,ddt = a)
            elif b[0] == "002":
                GPU_List.GPU_List.setData(self=GPU_List.GPU_List,ddt= a)
            elif b[0] == "003":
                mainboard_List.mainboard_List.setData(self=mainboard_List.mainboard_List,ddt=a)
            elif b[0] == "004":
                power_List.power_List.setData(self=power_List.power_List,ddt=a)
            elif b[0] == "005":
                RAM_List.RAM_List.setData(self=RAM_List.RAM_List,ddt=a)
            elif b[0] == "006":
                ssd_List.ssd_List.setData(self=ssd_List.ssd_List,ddt=a)
            text=tkinter.Label(text= b[1]+"의 "+ b[2]+"(이)가 "+b[3]+"으로 변경되었습니다.")
            text.pack()
        label=tkinter.Label(window,text="정보를 수정할 제품의 분류코드,이름,수정요소,수정값을 입력하세요\n001:CPU 002:GPU 003:mainboard 004:power 005:RAM 006:ssd\n")
        label.place(x=190,y=130)

        entry=tkinter.Entry(window)
        entry.place(x=240,y=160)
        check = tkinter.Button(window,text="입력", overrelief="solid", width=15, command=transfor , repeatdelay=1000, repeatinterval=100)
        check.place(x=240,y=190)
        window.mainloop()
    #데이터 삭제
    def deleteData():
        
        window=tkinter.Tk()
        window.title("삭제할 데이터의 분류코드와 이름을 입력하시오")
        window.geometry("640x400+100+100")
        window.resizable(False, False)
        def transfor():
            f = open("C:/Users/User/Desktop/Quote comparison/QUOTE.txt", 'r')
            a = entry.get()
            b = a.split()
            if b[0] == "001":
                CPU_List.CPU_List.deleteData(self=CPU_List.CPU_List,ddt = a)
            elif b[0] == "002":
                GPU_List.GPU_List.deleteData(self=GPU_List.GPU_List,ddt= a)
            elif b[0] == "003":
                mainboard_List.mainboard_List.deleteData(self=mainboard_List,ddt=a)
            elif b[0] == "004":
                power_List.power_List.deleteData(self=power_List.power_List,ddt=a)
            elif b[0] == "005":
                RAM_List.RAM_List.deleteData(self=RAM_List.RAM_List,ddt=a)
            elif b[0] == "006":
                ssd_List.ssd_List.deleteData(self=ssd_List.ssd_List,ddt=a)
            text=tkinter.Label(text=b[1]+"데이터가 삭제되었습니다.")
            text.pack()



        label=tkinter.Label(window,text="삭제할 데이터의 분류코드와 이름을 입력하세요\n001:CPU 002:GPU 003:mainboard 004:power 005:RAM 006:ssd\n")
        label.place(x=190,y=130)
        entry=tkinter.Entry(window)
        entry.place(x=240,y=160)
        check = tkinter.Button(window,text="입력", overrelief="solid", width=15, command=transfor , repeatdelay=1000, repeatinterval=100)
        check.place(x=240,y=190)
        window.mainloop()
    #데이터 조회
    def searchData():
        
        window=tkinter.Tk()
        window.title("데이터 조회")
        window.geometry("640x400+100+100")
        window.resizable(False, False)
        c=CPU_List.CPU_List.searchData(self=CPU_List.CPU_List)
        label_text = ""
        for item in c:
            label_text += f"   name: {item['name']}, price: {item['price']}, score: {item['score']}\n"
        label=tkinter.Label(window,text='CPU: '+ label_text + "\n\n")
        label.pack()

        c=GPU_List.GPU_List.searchData(self=GPU_List.GPU_List)
        label_text=""
        for item in c:
            label_text += f"   name: {item['name']}, price: {item['price']}, score: {item['score']}\n"
        label=tkinter.Label(window,text='GPU: '+ label_text + "\n\n")
        label.pack()

        c=mainboard_List.mainboard_List.searchData(self=mainboard_List.mainboard_List)
        label_text=""
        for item in c:
            label_text += f"   name: {item['name']}, price: {item['price']}, score: {item['score']}\n"
        label=tkinter.Label(window,text="mainboard: "+label_text + "\n\n")
        label.pack()

        c=power_List.power_List.searchData(self=power_List.power_List)
        label_text=""
        for item in c:
            label_text += f"   name: {item['name']}, price: {item['price']}, score: {item['score']}\n"
        label=tkinter.Label(window,text='power: '+label_text+"\n\n")
        label.pack()

        c=RAM_List.RAM_List.searchData(self=RAM_List.RAM_List)
        label_text=""
        for item in c:
            label_text += f"   name: {item['name']}, price: {item['price']}, score: {item['score']}\n"
        label=tkinter.Label(window,text='RAM: '+label_text+"\n\n")
        label.pack()

        c=ssd_List.ssd_List.searchData(self=ssd_List.ssd_List)
        label_text=""
        for item in c:
            label_text += f"   name: {item['name']}, price: {item['price']}, score: {item['score']}\n"
        label=tkinter.Label(window,text='ssd: '+label_text+"\n\n")
        label.pack()

        window.mainloop()

    

    # GUI만들기
    window=tkinter.Tk()
    window.title("견적비교프로그램")
    window.geometry("640x400+100+100")
    window.resizable(False, False)

    label=tkinter.Label(window, text="견적비교프로그램입니다")
    label.pack()
    
    
    inputD = tkinter.Button(window, text="데이터 추가", overrelief="solid", width=15, command=inputData, repeatdelay=1000, repeatinterval=100)
    inputD.place(x=0,y=120)

    setD = tkinter.Button(window, text="데이터 편집", overrelief="solid", width=15, command=setData, repeatdelay=1000, repeatinterval=100)
    setD.place(x=0,y=150)                           

    delD = tkinter.Button(window, text="데이터 삭제", overrelief="solid", width=15, command=deleteData, repeatdelay=1000, repeatinterval=100)
    delD.place(x=0,y=180)

    searchD = tkinter.Button(window, text="데이터 조회", overrelief="solid", width=15, command=searchData, repeatdelay=1000, repeatinterval=100)
    searchD.place(x=0,y=210)
    
    window.mainloop()





