#!/usr/bin/env python
# coding: utf-8

# In[2]:


class ExaminationResult:
    def __init__(self):
        self.students = []
        self.subjects = []
        self.passing_threshold = 35  # Example threshold for passing marks

    def set_subjects(self):
        subjects = input("Enter the subjects to be entered (comma separated, e.g., maths, science, english): ")
        self.subjects = [subject.strip().lower() for subject in subjects.split(',')]

    def student_details(self):
        for i in range(3):  # Loop to get details for 3 students
            print(f"Enter details for student {i+1}:")
            name = input("Enter your name: ")
            reg_no = int(input("Enter reg_no: "))
            
            marks = {}
            for subject in self.subjects:
                try:
                    mark = int(input(f"{subject.capitalize()} mark (or press Enter if not applicable): ") or None)
                except ValueError:
                    mark = None
                marks[subject] = mark
            
            self.students.append({
                'name': name,
                'reg_no': reg_no,
                **marks
            })

    def print_subject_marks_and_percentage(self, subject):
        if subject not in self.subjects:
            print("Invalid subject name")
            return
        
        print(f"{subject.capitalize()} marks and percentages of all students:")
        for student in self.students:
            mark = student.get(subject)
            if mark is not None:
                percentage = (mark / 100) * 100  # Assuming the maximum mark is 100
                status = "Pass" if mark >= self.passing_threshold else "Fail"
                print(f"Name: {student['name']}, {subject.capitalize()} mark: {mark}, {subject.capitalize()} percentage: {percentage}%, Status: {status}")
            else:
                print(f"Name: {student['name']}, {subject.capitalize()} mark: Not Applicable")

# Create an instance of the class and call the methods
aa = ExaminationResult()
aa.set_subjects()
aa.student_details()

# Ask the user which subject marks to print
subject = input("Enter the subject to print marks, percentages, and pass/fail status: ").lower()
aa.print_subject_marks_and_percentage(subject)


# In[ ]:




