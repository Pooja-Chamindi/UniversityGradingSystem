# Author - Pooja Malagala

progress_count = 0
progress_list = []
trailer_count = 0
trailer_list = []
m_retriever_count = 0
m_retriever_list = []
exclude_count = 0
exclude_list = []
rerun_count = 0
pass_credit = 0
defer_credit = 0
fail_credit = 0
dict = {}
student_id = ""


def generateOutcome():
    global pass_credit, defer_credit, fail_credit, progress_list, progress_count, trailer_list, trailer_count, m_retriever_list, m_retriever_count, exclude_list, exclude_count, rerun_count, dict, student_id
    if pass_credit + defer_credit + fail_credit != 120:
        print("Total incorrect")
        return
    elif pass_credit == 120:
        print("Progress")
        progress_list.append([pass_credit, defer_credit, fail_credit])
        progress_count = progress_count + 1
        dict[student_id] = "progress -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit == 100:
        print("Progress(module trailer)")
        trailer_list.append([pass_credit, defer_credit, fail_credit])
        trailer_count = trailer_count + 1
        dict[student_id] = "progress(module trailer) -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit == 80:
        print("Do not progress - module retriever")
        m_retriever_list.append([pass_credit, defer_credit, fail_credit])
        m_retriever_count = m_retriever_count + 1
        dict[student_id] = "Do not progress - module retriever -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit == 60:
        print("Do not progress - module retriever")
        m_retriever_list.append([pass_credit, defer_credit, fail_credit])
        m_retriever_count = m_retriever_count + 1
        dict[student_id] = "Do not progress - module retriever -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit + defer_credit == 40:
        print("Exclude")
        exclude_list.append([pass_credit, defer_credit, fail_credit])
        exclude_count = exclude_count + 1
        dict[student_id] = "Exclude -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit == 40:
        print("Do not progress - module retriever")
        m_retriever_list.append([pass_credit, defer_credit, fail_credit])
        m_retriever_count = m_retriever_count + 1
        dict[student_id] = "Do not progress - module retriever -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit + defer_credit == 20:
        print("Exclude")
        exclude_list.append([pass_credit, defer_credit, fail_credit])
        exclude_count = exclude_count + 1
        dict[student_id] = "Exclude -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit == 20:
        print("Do not progress - module retriever")
        m_retriever_list.append([pass_credit, defer_credit, fail_credit])
        m_retriever_count = m_retriever_count + 1
        dict[student_id] = "Do not progress - module retriever -", [pass_credit, defer_credit, fail_credit]
    elif pass_credit + defer_credit == 0:
        print("Exclude")
        exclude_list.append([pass_credit, defer_credit, fail_credit])
        exclude_count = exclude_count + 1
        dict[student_id] = "Exclude -", [pass_credit, defer_credit, fail_credit]
    else:
        print("Do not progress - module retriever")
        m_retriever_list.append([pass_credit, defer_credit, fail_credit])
        m_retriever_count = m_retriever_count + 1
        dict[student_id] = "Do not progress - module retriever -", [pass_credit, defer_credit, fail_credit]
    rerun_count = rerun_count + 1


while True:
    try:
        student_id = input("Enter your student ID: ")
        while True:
            pass_credit = int(input("Enter your total PASS credits: "))
            if pass_credit not in range(0, 140, 20):
                print("Out of range")
            else:
                break
        while True:
            defer_credit = int(input("Enter your total DEFER credits: "))
            if defer_credit not in range(0, 140, 20):
                print("Out of range")
            else:
                break
        while True:
            fail_credit = int(input("Enter your total FAIL credits: "))
            if fail_credit not in range(0, 140, 20):
                print("Out of range")
            else:
                break
    except ValueError:
        print("Integer required")
        continue

    generateOutcome()

    print("\nWould you like to enter another set of data?")
    rerun = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print("\n")
    if rerun == 'y':
        continue
    if rerun == 'q':
        print("Histogram")
        print("progress ", progress_count, "  :", end=" ")
        for i in range(0, progress_count):
            print("*", end=" ")
        print("")
        print("Trailer ", trailer_count, "   :", end=" ")
        for i in range(0, trailer_count):
            print("*", end=" ")
        print("")
        print("Retriever ", m_retriever_count, " :", end=" ")
        for i in range(0, m_retriever_count):
            print("*", end=" ")
        print("")
        print("Excluded ", exclude_count, "  :", end=" ")
        for i in range(0, exclude_count):
            print("*", end=" ")
        print("")
        print("")
        print(rerun_count, " outcomes in total")
        print("\nPart 2:")
        for i in range(0, len(progress_list)):
            print("Progress - ", end="")
            print(progress_list[i][0], end=", ")
            print(progress_list[i][1], end=", ")
            print(progress_list[i][2])

        for i in range(0, len(trailer_list)):
            print("Progress (module trailer) - ", end="")
            print(trailer_list[i][0], end=", ")
            print(trailer_list[i][1], end=", ")
            print(trailer_list[i][2])

        for i in range(0, len(m_retriever_list)):
            print("Module retriever - ", end="")
            print(m_retriever_list[i][0], end=", ")
            print(m_retriever_list[i][1], end=", ")
            print(m_retriever_list[i][2])

        for i in range(0, len(exclude_list)):
            print("Exclude - ", end="")
            print(exclude_list[i][0], end=", ")
            print(exclude_list[i][1], end=", ")
            print(exclude_list[i][2])

        # Part 3
        print("\nPart 3")
        f = open('data.txt', 'w')

        for i in range(0, len(progress_list)):
            f.write(f"Progress - {progress_list[i][0]}, {progress_list[i][1]}, {progress_list[i][2]}\n")

        for i in range(0, len(trailer_list)):
            f.write(f"Progress (module trailer) - {trailer_list[i][0]}, {trailer_list[i][1]}, {trailer_list[i][2]}\n")

        for i in range(0, len(m_retriever_list)):
            f.write(
                f"Module retriever - {m_retriever_list[i][0]}, {m_retriever_list[i][1]}, {m_retriever_list[i][2]}\n")

        for i in range(0, len(exclude_list)):
            f.write(f"Exclude - {exclude_list[i][0]}, {exclude_list[i][1]}, {exclude_list[i][2]}\n")

        f.close()

        f = open('data.txt', 'r')

        for l in f:
            print(l, end="")

        #part 4

        print("\nPart 4")
        print(dict)
        break

