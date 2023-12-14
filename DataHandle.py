import tkinter
import os

class DataHandle:
    PartList = []
    def read_data_from_file(file_path):
        # 파일을 읽어 딕셔너리로 변환하여 저장할 리스트를 초기화합니다.
        data_list = []

        try:
            with open(file_path, 'r') as file:
                # 파일 내용을 줄 단위로 읽어옵니다.
                lines = file.readlines()

                # 각 줄을 딕셔너리로 변환하여 리스트에 추가합니다.
                for line in lines:
                    # 예제: 각 줄이 "key: value" 형식일 때를 가정합니다.
                    parts = line.strip().split(':')
                    if len(parts) == 8:
                        number = parts[0].strip()
                        value1 = parts[1].strip()
                        name = parts[2].strip()
                        value2 = parts[3].strip()
                        price = parts[4].strip()
                        value3 = parts[5].strip()
                        score = parts[6].strip()
                        value4 = parts[7].strip()
                        data_list.append({number: value1, name: value2, price: value3, score: value4 })
                    # 만약 다른 형식이라면 그에 맞게 수정이 필요합니다.

        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_path}")

        return data_list
    

    def setData(self,ddt):
        a = []
        a = ddt.split()
        for i in self.PartList:
            if i["name"]==a[1]:
                i[a[2]] = a[3]
                print(i)
                break
        print(self.PartList)


    def inputData(self,ddt):
        f = open("C:/Users/User/Desktop/Quote comparison/QUOTE.txt", 'a')
        a = []
        a = ddt.split()
        Part = {"number":0 ,"name":"" ,"price":0 ,"score":0}
        Part["number"] = a[0]
        Part["name"] = a[1]
        Part["price"] = a[2]
        Part["score"] = a[3]
        self.PartList.append(Part)
        print(self.PartList)
        label_text = ""
        label_text += f"number: {a[0]}, name: {a[1]}, price: {a[2]}, score: {a[3]}\n"
        f.write(label_text)
        f.close()

    def deleteData(self, ddt):
        a = ddt.split()
        # 파일 경로를 저장합니다.
        f = "C:/Users/User/Desktop/Quote comparison/QUOTE.txt"

        # 데이터의 이름을 받아와서 해당 데이터를 파일에서 찾고 삭제합니다.
        with open(f, 'r') as 파일:
            lines = 파일.readlines()

        with open(f, 'w') as 파일:
            for line in lines:
                # 데이터의 이름이 포함된 줄은 건너뛰고 쓰지 않습니다.
                if a[1] in line:
                    continue
                파일.write(line)

        # PartList에서도 해당 데이터를 삭제합니다.
        for i in self.PartList:
            if i["name"] == a[1]:
                self.PartList.remove(i)
                break

        # 수정된 PartList를 출력합니다.

    # def deleteData(self,ddt):
    #     f = "C:/Users/User/Desktop/Quote comparison/QUOTE.txt"
    #     a = ddt.split()
    #     for i in self.PartList:
    #         if i["name"]==a[1]:
    #             self.PartList.remove(i)
    #             break
    #     print(self.PartList)


    def searchData(self):
        a = self.PartList
        return a
    
    

    