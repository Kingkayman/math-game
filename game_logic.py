import random


def multiplication_question(table):

    random_number = random.randint(1, 10)

    return {
        "question": f"{random_number} × {table}",
        "answer": random_number * table
    }


def addition_question(max_num):

    random_number1 = random.randint(1, max_num)
    random_number2 = random.randint(1, max_num)

    return {
        "question": f"{random_number1} + {random_number2}",
        "answer": random_number1 + random_number2
    }


def subtraction_question(max_num):

    random_number1 = random.randint(1, max_num)
    random_number2 = random.randint(1, max_num)

    if random_number1 < random_number2:
        random_number1, random_number2 = random_number2, random_number1

    return {
        "question": f"{random_number1} - {random_number2}",
        "answer": random_number1 - random_number2
    }


def division_question(table):

    quotient = random.randint(1, 10)

    dividend = quotient * table

    return {
        "question": f"{dividend} / {table}",
        "answer": quotient
    }