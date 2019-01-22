card_list = []

# 欢迎界面
def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

# 新建名片
def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入详细信息
    name_str = input("请输入姓名：")
    phone = input("请输入电话号码：")
    qq = input("请输入qq号码：")
    email = input("请输入邮箱号码：")
    # 2.使用用户输入的数据建立字典
    card_dict = {"name": name_str, "phone": phone, "qq": qq, "email": email}
    # 3. 将名片字典添加到字典中
    card_list.append(card_dict)
    # 4. 提示用户添加成功
    print("添加%s的名片成功！" % name_str)

# 显示名片
def show_all():
    """显示全部名片"""
    print("-" * 50)
    print("显示全部名片")
    if len(card_list) == 0:
        print("当前名片夹为空，请添加名片！")
        # return 关键字，不执行后续代码呵返回函数值
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    # 制表后换行
    print("")
    # 打印分割线
    print("=" * 50)
    #遍历名片列表依次输出
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" %
              (card_dict["name"], card_dict["phone"], card_dict["qq"],
               card_dict["email"]))
    print("=" * 50)

# 搜索名片
def search_card():
    """名片查找"""
    print("-" * 50)
    print("名片查找")
    # 1.提示用户要查找的信息
    find_name = input("请输入要搜索的信息：")
    # 2.遍历所有名片列表
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            # 制表后换行
            print("")
            # 打印分割线
            print("=" * 50)
            #遍历名片列表依次输出
            for card_dict in card_list:
                print("%s\t\t%s\t\t%s\t\t%s\t\t" %
                      (card_dict["name"], card_dict["phone"], card_dict["qq"],
                       card_dict["email"]))
            print("=" * 50)
            # 找到列表后的后续操作
            deal_dict(card_dict)
            break
    else:
        print("抱歉！没有找到！")

    # 3.
    # 4.


# 函数调用处理列表的后续操作
def deal_dict(find_dict):
    """名片处理"""
    action_str = input("请输入要执行的操作[1].修改/[2].删除/[0].返回上级菜单：")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "email：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("名片已成功删除！")


# 名片处理优化
def input_card_info(dict_value, tips):
    """输入名片信息"""
    # 1.提示输入信息
    result_str = input(tips)
    # 2.判断用户输入，输入内容直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果没用输入，返回原字典中的值
    else:
        return dict_value
