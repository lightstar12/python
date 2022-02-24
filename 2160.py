class Solution:
    def minimumSum(self, num: int) -> int:
        str_num = str(num)
        num_list = []
        for i in range(len(str_num)):
            num_list.append(str_num[i])
        new1 = ''
        new2 = ''
        for i in range(2):
            new1 = new1 + min(num_list)
            num_list.remove(min(num_list))
            new2 = new2 + min(num_list)
            num_list.remove(min(num_list))
        new1 = int(new1)
        new2 = int(new2)
        return new1 + new2
