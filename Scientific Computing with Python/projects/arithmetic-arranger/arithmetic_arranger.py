def arithmetic_arranger(problems: list, result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for idx, problem in enumerate(problems):
        first, op, second = problem.split()

        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not first.isdecimal() or not second.isdecimal():
            return "Error: Numbers must only contain digits."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        num_length = len(max([first, second], key=len))

        line1 += first.rjust(num_length + 2)
        line2 += op + second.rjust(num_length + 1)
        line3 += "-" * (num_length + 2)

        if result:
            res = int(first) + int(second) if op == "+" else int(first) - int(second)
            line4 += str(res).rjust(num_length + 2)

        if idx < len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    final_str = line1 + "\n" + line2 + "\n" + line3

    if result:
        final_str += "\n" + line4

    return final_str

