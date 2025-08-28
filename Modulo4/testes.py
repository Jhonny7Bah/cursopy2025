# def estado():
#     print('inicio')
#     yield 1
#     print('meio')
#     yield 2
#     print('fim')
#     yield 3

# g = estado()

# n1, n2, n3 = g.__next__(), g.__next__(), g.__next__()

# print(n1)
# import asyncio

# async def tarefa1():
#     print("Tarefa 1 começou")
#     await asyncio.sleep(2)  # pausa 2 segundos
#     print("Tarefa 1 terminou")

# async def tarefa2():
#     print("Tarefa 2 começou")
#     await asyncio.sleep(1)  # pausa 1 segundo
#     print("Tarefa 2 terminou")

# async def main():
#     # roda as duas tarefas ao mesmo tempo
#     await asyncio.gather(tarefa1(), tarefa2())

# asyncio.run(main())

students = [
    # nome      idade nota
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],
]

for i, students_row in enumerate(students):
    # print(i, '\n',students_row)
    for j, students_col in enumerate(students_row):
        print(j, '\n',students_col)
        