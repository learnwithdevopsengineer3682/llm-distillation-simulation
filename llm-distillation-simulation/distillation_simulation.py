
from teacher_model import teacher_response
from student_model import student_response

prompt = "What is kubernetes?"

print("\n--- STUDENT BEFORE ---")
print(student_response(prompt))

teacher_output = teacher_response(prompt)

print("\n--- TEACHER OUTPUT ---")
print(teacher_output)

print("\n--- STUDENT AFTER (Guided Simulation) ---")
guided_prompt = f"Use this structured guidance:\n{teacher_output}\nNow answer the question again."
print(student_response(guided_prompt))

print("\nNote: This is a simulation of knowledge distillation.")
print("Real training requires compute, backpropagation, and GPU resources.")
