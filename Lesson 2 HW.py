#--------------------------in chuoi so nguyen to

def in_so_nguyen_to(n: int):
    list_nguyen_to = []
    list_ko_nguyen_to = []
    for i in range(1, n+1):
        for k in range(1, round(i/2)): #chỉ cần kiểm tra i chia cho các số từ 1 đến 1/2 i là đủ
            #Kiểm tra số i có chia hết cho số nào khác ngoài 1 và chính nó ko.
            #Nếu có thì i không phải là số nguyên tố
            if i%k==0 and k!=1:
                list_ko_nguyen_to.append(i)
                break
        if i not in list_ko_nguyen_to:
            list_nguyen_to.append(i)
    return list_nguyen_to

print(in_so_nguyen_to(20))

#kiem tra thoi gian
import timeit
setup = """
def in_so_nguyen_to(n: int):
    list_nguyen_to = []
    list_ko_nguyen_to = []
    for i in range(1, n+1):
        for k in range(1, round(i/2)): #chỉ cần kiểm tra i chia cho các số từ 1 đến 1/2 i là đủ
            #Kiểm tra số i có chia hết cho số nào khác ngoài 1 và chính nó ko.
            #Nếu có thì i không phải là số nguyên tố
            if i%k==0 and k!=1:
                list_ko_nguyen_to.append(i)
                break
        if i not in list_ko_nguyen_to:
            list_nguyen_to.append(i)
    return list_nguyen_to
"""
code = """
in_so_nguyen_to(20)
"""
t = timeit.timeit(setup=setup, stmt=code, number=10000)
print(f"{t*1000000:6.2f} micro seconds")

#------------------------------------
#bài tập luyện khả năng xử lý vấn đề: cho 2 mảng số tự nhiên đã sắp xếp từ thấp đến cao, có số phần tử khác nhau.
#Hãy nhập 2 mảng này thành một mảng mới làm sao tốc độ thực hiện nhanh nhất.
#mảng mới cũng phải được sắp xếp  thấp lên cao
'''
B1: gộp 2 mảng thành 1 m
B2: chạy vòng lặp qua từng phần tử của mảng mới, kiểm tra với từng phần tử còn lại
nếu thấy lớn hơn bất kỳ phần từ còn lại nào thì swap vị trí
'''

list1 = [1, 4, 9, 3, 2, 6, 10, 10, 99, 40, 23, 29, 33]
list2 = [102, 4, 77, 3, 9, 6, 82, 103, 96, 49]

def group_and_sort_arrays(list1: tuple, list2: tuple) -> tuple:
    #group 2 arrays into 1
    list_new = list1 + list2

    #sort new array ASC
    i = 0
    while i <= len(list_new) - 2:
        for k in range(i+1, len(list_new)-1+1): #k chay tu sau so i den so cuoi cua day list_new
            if list_new[i] > list_new[k]:
                list_new[i], list_new[k] = list_new[k], list_new[i]
        i += 1
    return list_new

print(group_and_sort_arrays(list1, list2))

#-----------------------------đảo chuỗi:

list = 'abcd'
list_reverse = list[::-1]
print(list_reverse)

#-----------------------------Nhập vào 2 chuỗi, kiểm tra chúng có phải là anagram, cùng chứa số
#ký tự bằng nhau. ‘Hello’ và ‘eHlol’ là anagram

list1 = 'abcdefg'
list2 = 'gdbefca'

def check_anagram(list1, list2):
    if sorted(list1) == sorted(list2):
        msg = 'anagram'
    else:
        msg = 'not anagram'
    return msg

print(check_anagram(list1, list2))

#---------------------------Truyền vào list các số nguyên, hãy tìm ra số nào xuất hiện nhiều nhất. Cơ chế vote.

int_list = [1,5,5,5,6,8,2,3,8,8,5,8]

def check_highest_frequency(list):
    frequency_list = [] #chứa giá trị tần suất xuất hiện của các số trong list ban đầu
    numbers_appear_the_most = [] #chứa kết quả các số xuất hiện nhiều nhất
    highest_frequency = []
    for i in range(0, len(list)):
        #so sánh từng số với tất cả các số trong list, bao nhieu lần = nhau thi chính là tần suất
        count = 0
        for k in range(0, len(list)):
            if list[i] == list[k]:
                count += 1
        frequency_list.append(count)
    #tìm vị trí của frequency lớn nhất trong frequency_list, đó chính là vị trí của số có tần suất lớn nhất trong chuỗi list ban đầu
    max_num = max(frequency_list)
    for i in range(0, len(frequency_list)):
        if frequency_list[i] == max_num and list[i] not in numbers_appear_the_most: #lệnh not in để đảm bảo lấy distinct giá trị
            numbers_appear_the_most.append(list[i])
            highest_frequency.append(frequency_list[i])
    return  'Most appear numbers are '+str(numbers_appear_the_most), 'which appear '+str(highest_frequency)+' times respectively'


print(check_highest_frequency(int_list))

#-------------------------Truyền vào một chuỗi, hãy kiểm tra chuỗi có phải là palindrome hay khong

list = 'madame'

#dung reverse slicing de kiem tra chuoi co phai palindrome ko:
reverse_list = list[::-1]
if reverse_list == list:
    print('palindrome')
else:
    print('not palindrome')