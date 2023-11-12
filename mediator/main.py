from user import Student, Teacher
from chat import ChatMediator


if __name__ == "__main__":
    # Создаем чаты
    teacher_chat = ChatMediator("Teacher's Chat")
    student_chat = ChatMediator("Student's Chat")
    general_chat = ChatMediator("General Chat")

    # Создаем учителей и студентов с использованием общего класса User
    teacher1 = Teacher("Teacher 1")
    teacher2 = Teacher("Teacher 2")

    student1 = Student("Student 1")
    student2 = Student("Student 2")
    student3 = Student("Student 3")
    student4 = Student("Student 4")

    # Учителя и студенты присоединяются к чатам
    teacher1.join_chat(teacher_chat)
    teacher2.join_chat(teacher_chat)

    student1.join_chat(student_chat)
    student2.join_chat(student_chat)
    student3.join_chat(student_chat)
    student4.join_chat(student_chat)

    teacher1.join_chat(general_chat)
    teacher2.join_chat(general_chat)
    student1.join_chat(general_chat)
    student2.join_chat(general_chat)
    student3.join_chat(general_chat)
    student4.join_chat(general_chat)

    # Учителя и студенты могут отправлять сообщения в свои чаты
    teacher1.send("Welcome to the teacher's chat!", teacher_chat)
    print()
    student1.send("Hi everyone in the student's chat!", student_chat)
    print()
    student2.send("Hello in the general chat!", general_chat)
