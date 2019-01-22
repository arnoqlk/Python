import card_tools
while True:
    # 显示欢迎界面
    card_tools.show_menu()
    # 用户交互
    action = input("请选择希望执行的操作：")
    print("你希望执行的操作是【%s】" % action)

    # 针对1，2，3执行的操作
    if action in ["1", "2", "3"]:
        # 新增名片
        if action == "1":
            card_tools.new_card()
        # 显示全部
        elif action == "2":
            card_tools.show_all()
        # 查询名片
        elif action == "3":
            card_tools.search_card()
    # 针对0的操作
    elif action == "0":
        print("欢迎下次使用!")
        break

    #错误输入
    else:
        print("错误输入，请重新输入！")