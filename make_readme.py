import os


if __name__ =='__main__':

    file_list = os.listdir("./yongwoo-cho")

    file_dict = {}

    for file in file_list:
        prob_num = file.split(".")[0]
        prob_name = file.split(".")[1]
        file_dict[int(prob_num)] = prob_name


    sorted_list = sorted(file_dict.items(),key=lambda x : x[0])

    with open("./README.MD","w") as f:
        f.write("# Leetcode\n")
        f.write("problems and link\n")
        f.write("solved problems : {} \n".format(len(sorted_list)))
        for i in sorted_list:
            link = "https://leetcode.com/problems/" + i[1][1:].lower().replace(" ","-")
            f.write("- [" + str(i[0])+"."+i[1]+ "]" +"(" + link +")\n")


