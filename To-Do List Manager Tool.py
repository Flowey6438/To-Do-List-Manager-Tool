import os

TODO_FILE = "todo_list.txt"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for todo in todos:
            file.write(todo + "\n")

def add_todo(todo):
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)
    print(f"待办事项“{todo}”已成功添加！")

def view_todos():
    todos = load_todos()
    if todos:
        print("\n当前待办事项列表：")
        for idx, todo in enumerate(todos, 1):
            print(f"{idx}. {todo}")
    else:
        print("没有待办事项。")

def mark_done(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        todo = todos.pop(index - 1)
        save_todos(todos)
        print(f"待办事项“{todo}”已标记为完成并移除！")
    else:
        print("无效的待办事项编号。")

if __name__ == "__main__":
    print("欢迎使用待办事项管理工具！")

    while True:
        print("\n请选择一个操作：")
        print("1. 添加待办事项")
        print("2. 查看待办事项")
        print("3. 标记完成")
        print("4. 退出")

        choice = input("请输入选项（1/2/3/4）：")

        if choice == "1":
            todo = input("请输入待办事项内容：")
            add_todo(todo)
        elif choice == "2":
            view_todos()
        elif choice == "3":
            try:
                index = int(input("请输入已完成的待办事项编号："))
                mark_done(index)
            except ValueError:
                print("请输入有效的编号。")
        elif choice == "4":
            print("感谢使用待办事项管理工具，再见！")
            break
        else:
            print("无效选项，请重新选择。")
