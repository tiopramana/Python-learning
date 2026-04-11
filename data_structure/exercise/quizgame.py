# Test quiz games

question = ((
    "Siapa president indonesia ke 7: ",
    "Dimana kah ijasah dari president ke 7 indonesia: ",
    "Dimana kah tinggal nya presiden indonesia ke 7: ",
    "Siapakah presiden yang menjabat 2 periode dan dimintain ijasah: ",
    "Siapa rival dari presiden ke 7: "
))

options = (("A. Anies","B. Jokowi","C. Putin","D. Trump"),
          ("A. Goa","B. Tembok Ratapan Solo","C. Jimbaran","D. Diasingkan"),
          ("A. Bali","B. Jawa","C. Yogyakarta","D. Solo"),
          ("A. Pria Solo","B. Prabowo","C. Anies","D. Ganjar"),
          ("A. Anies","B. Mahfud Md","C. Prawit","D. Trump"),
          )

answer = ["B", "B", "D", "A", "C"]
guesses = []
score = 0
question_num = 0
input_answer = ["A", "B", "C", "D"]

for task in question:
    print(task)
    for option in options[question_num]:
        print(option)

    the_answer = input("Masukan jawaban: (A, B, C ,D): ").upper()

    if the_answer == input_answer:
        print("Masukan jawaban yang benar seusai dengan", input_answer)

    guesses.append(the_answer)

    if the_answer == answer[question_num]:
        score += 5
        print("Jawaban benar")
    else:
        print("Salah Tetot")

    question_num += 1

print(f"Score {score}")

   