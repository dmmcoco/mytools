#Usage:
#python3 mysnippingtool
#python3 mysnippingtool -ua
#python3 mysnippingtool -co
#如果删除了~/githubpic目录下的图片,则要运行python3 mysnippingtool -ua表示手动更新address.txt中的列表
#这种情况使用在人工测试mysnippintool脚本是否有错的时候会偶尔用到

#-co表示打印出需要组合图片时候要访问的网站
import sys
import os
from exp10it import getHomePath

tmp=0
all_file_name_list=[]
def get_all_file_name(folder):
    global tmp
    global root_dir
    global all_file_name_list
    tmp+=1
    if tmp==1:
        if folder[-1]=='/':
            root_dir=folder[:-1]
        else:
            root_dir=folder

    allfile=os.listdir(folder)
    for each in allfile:
        each_abspath=os.path.join(folder,each)
        if os.path.isdir(each_abspath):
            get_all_file_name(each_abspath)
        else:
            #print each_abspath
            if len(each_abspath)>len(root_dir)+1+len(os.path.basename(each)):
                filename=each_abspath[len(root_dir)+1:]
                #print filename
                all_file_name_list.append(filename)
            else:
                #print each
                all_file_name_list.append(each)

    return all_file_name_list


def main():
    import sys
    homePath=getHomePath()
    githubpicPath=homePath+"/githubpic"

    if os.path.exists(githubpicPath) is False:
        print("this is the first time you use me,or you have deleted ~/githubpic,I will mkdir ~/githubpic and git pull the github's pic.git,please put pngs to ~/githubpic when needed,and don't delet any png file in this folder")
        os.system("mkdir ~/githubpic && cd ~/githubpic && git init && git pull https://github.com/3xp10it/pic.git && git remote add origin https://github.com/3xp10it/pic.git && git status")
        return

    addressPath=githubpicPath+"/address.txt"

    if len(sys.argv)==2 and sys.argv[1]=="-ua":
        all_png_list=get_all_file_name(githubpicPath)

        os.system("rm %s" % addressPath)
        with open(addressPath,"a+") as f:
            for each in all_png_list:
                each="https://raw.githubusercontent.com/3xp10it/pic/master/%s" % each
                f.write(each+"\r\n")
        return

    if len(sys.argv)==2 and sys.argv[1]=="-co":
        onLineAddr1="http://www.fotor.com/app.html#!module/collage/tool/PhotoStitching"
        onLineAddr2="http://xiuxiu.web.meitu.com/puzzle/"
        print(onLineAddr1)
        print(onLineAddr2)
        print("tips:macOS下自己截图保存组合后的图片质量更高")
        os.system("firefox %s" % onLineAddr)
        return

    os.system("cd ~/githubpic && git add . && git status && git commit -a -m 'update' && git push -u origin master")

    all_png_list=get_all_file_name(githubpicPath)
    #print(all_png_list)


    for each in all_png_list:
        try:
            with open(addressPath,"a+") as f:
                f.seek(0)
                all=f.readlines()
                each_addr="https://raw.githubusercontent.com/3xp10it/pic/master/%s" % each
                #下面发现从ubuntu到macOS下居然会将\r\n变成\n,于是要写成下面这样
                if each_addr+'\r\n' not in all and each_addr not in all and each_addr+"\n" not in all:
                    if "/.git/objects/" not in each_addr:
                        #非/.git/objects/的文件
                        print(each_addr)
                        f.write(each_addr+'\r\n')
                        f.close()
        except:
            print("open ~/githubpic/address.txt wrong")

if __name__=='__main__':
    main()


'''
print os.path.abspath(each) is not good function,

it will get ~/桌面/spider_wooyun when I put this py script file in ~/桌面,and run:
(cd 桌面)
python mysnippingtool.py
it will get "~/桌面/spider_wooyun" as a result,but the true result should be "~/githubpic/spider_wooyun"
so I use:
current_file_abspath=os.path.isdir("~/githubpic/"+each):
to get the current file's abspath
'''




