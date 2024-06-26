import pandas as pd
import numpy as np


# Define columns
columns = ['name', 'number', 'syllabus', 'spring', 'winter', 'pre_courses', 'lecturers', 'means']

# Create an empty DataFrame with these columns
df = pd.DataFrame(columns=columns)


data2 = [
    ["Introduction to Python", "CS101", "Python basics, control structures, functions, and modules.", True, False, [], ["Dr. Smith"], [85]],
    ["Advanced Python", "CS102", "Advanced topics in Python, including OOP, data structures, and algorithms.", False, True, ["CS101"], ["Dr. Johnson"], [88]]
]


data = [
    ["Introduction to Python", "CS101", "Python basics, control structures, functions, and modules.", True, False, [], ["Dr. Smith"], [85]],
    ["Advanced Python", "CS102", "Advanced topics in Python, including OOP, data structures, and algorithms.", False, True, ["CS101"], ["Dr. Johnson"], [88]],
    ["Data Structures", "CS103", "Introduction to data structures: stacks, queues, linked lists, and more.", True, False, ["CS101"], ["Dr. Allen"], [90]],
    ["Algorithms", "CS104", "Algorithm design, analysis, and complexity. Sorting, searching, and graph algorithms.", False, True, ["CS103"], ["Dr. Beech"], [92]],
    ["Web Development", "CS105", "Web development essentials, including HTML, CSS, and JavaScript.", True, False, [], ["Dr. Carter"], [87]],
    ["Database Systems", "CS106", "Fundamentals of database systems, SQL, and schema design.", False, True, [], ["Dr. Davis"], [89]],
    ["Operating Systems", "CS107", "Concepts in operating systems including processes, threading, and file systems.", True, False, ["CS103"], ["Dr. Evans"], [91]],
    ["Computer Networks", "CS108", "Introduction to computer networks, protocols, and network programming.", False, True, [], ["Dr. Foster"], [85]],
    ["Machine Learning", "CS109", "Fundamentals of machine learning, supervised and unsupervised learning.", True, False, ["CS102", "CS103"], ["Dr. Green"], [94]],
    ["Artificial Intelligence", "CS110", "Study of AI principles, algorithms for intelligence, applications.", False, True, ["CS109"], ["Dr. Hill"], [93]],
    ["Software Engineering", "CS111", "Software development life cycle, methodologies, and project management.", True, False, ["CS101"], ["Dr. Iris"], [88]],
    ["Cybersecurity", "CS112", "Principles of cybersecurity, cryptography, and network security.", False, True, [], ["Dr. Jones"], [86]],
    ["Human-Computer Interaction", "CS113", "Design and evaluation of user interfaces, usability, and user experience.", True, False, [], ["Dr. Klein"], [89]],
    ["Cloud Computing", "CS114", "Cloud services, virtualization, scalability, and cloud application development.", False, True, ["CS103"], ["Dr. Lee"], [90]],
    ["Game Development", "CS115", "Game design principles, development engines, and interactive media creation.", True, False, ["CS105"], ["Dr. Moore"], [87]],
    ["Mobile App Development", "CS116", "Developing applications for mobile devices using various frameworks.", False, True, ["CS105"], ["Dr. Nelson"], [85]],
    ["Data Mining", "CS117", "Techniques and tools for data mining, pattern recognition, and data analysis.", True, False, ["CS109"], ["Dr. O'Neil"], [92]],
    ["Natural Language Processing", "CS118", "Processing and understanding human language using computational techniques.", False, True, ["CS109"], ["Dr. Patel"], [93]],
    ["Parallel Computing", "CS119", "Concepts in parallel architecture, algorithms, and program optimization.", True, False, ["CS104"], ["Dr. Quinn"], [91]],
    ["Blockchain Technology", "CS120", "Introduction to blockchain, cryptocurrencies, and decentralized applications.", False, True, [], ["Dr. Rivera"], [88]]
]


# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=columns)
df.to_csv('courses.csv', index=False)
#
# # Assuming you have a list of distinct course numbers:
# distinct_course_numbers = ['CS101', 'CS102', 'CS103', 'CS104', 'CS105']
#
# # Number of students
# num_students = 50
#
# rankings_df = pd.DataFrame(columns=distinct_course_numbers)
#
# # Generating rankings for 50 students
# num_students = 50
# student_types=[[0.2, 0.3, 0.3, 0.1, 0.1], [0.1, 0.2, 0.3, 0.3, 0.1], [0.1, 0.1, 0.1, 0.4, 0.3]]
# for _ in range(num_students):
#     # Randomly select a student type for demonstration purposes
#     # In a real scenario, you might assign types based on specific criteria
#     student_type = np.random.choice([0, 1, 2])
#     distribution = student_types[student_type]
#
#     rankings = [np.random.choice([1, 2, 3, 4, 5, np.nan], p=distribution) for _ in distinct_course_numbers]
#     rankings_df = rankings_df.append(pd.Series(rankings, index=distinct_course_numbers), ignore_index=True)
#
# # Display the first few rows of the DataFrame
# print(rankings_df.head())
