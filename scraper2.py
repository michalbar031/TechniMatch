
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
from tqdm import tqdm

# Replace these numbers with the actual start and end of your course range.
start_course_number = 94101
end_course_number = 97980
course_ids = [
    "094411", "094202", "094219", "094224", "094312", "094424", "094564",
    "094594", "094139", "094314", "094820", "095605", "097800", "094345",
    "094704", "094210", "094241", "095295", "096570", "097414", "096327",
    "096212", "094101", "094700", "094412", "094290", "094295", "094395",
    "094396", "095140", "096210", "096250", "097209", "096625", "094816",
    "096266", "096600", "096606", "096617", "096620", "096690", "096692",
    "096693", "097325"
]


def find_course_numbers(text):
    # Define the regular expression pattern
    pattern = r'09\d{4}'

    # Find all occurrences of the pattern
    course_numbers = re.findall(pattern, text)

    return course_numbers

str_all="094101 - Intro.to Industrial Eng. and Management Data and Decision Sciences Undergraduate Studies No 094139 - Manage. Logist. System. Data and Decision Sciences Undergraduate Studies Yes 094142 - Operation of Production Service Systems Data and Decision Sciences Undergraduate Studies No 094170 - Industrial Engineering Methods Data and Decision Sciences Undergraduate Studies No 094179 - Industrial Engineering in The Field Data and Decision Sciences Undergraduate Studies Yes 094189 - Design Project Proposal Data and Decision Sciences Undergraduate Studies No 094195 - Design Project 1 Data and Decision Sciences Undergraduate Studies Yes 094198 - Case Studies in Industrial Engineering Data and Decision Sciences Undergraduate Studies Yes 094202 - Introduction to Data Analysis in Python Data and Decision Sciences Undergraduate Studies Yes 094210 - Computer Architecture and Operating Sys. 094219 - Software Engineering Data and Decision Sciences Undergraduate Studies Yes 094222 - Model-based Systems Engineering Data and Decision Sciences Undergraduate Studies No 094224 - Data Structures and Algorithms Data and Decision Sciences Undergraduate Studies No 094241 - Database Management Data and Decision Sciences Undergraduate Studies Yes 094288 - Ethical Issues in Data Responsibility Data and Decision Sciences Undergraduate Studies Yes 094290 - Data Gathering and Management Lab Data and Decision Sciences Undergraduate Studies No 094295 - Data Analysis and Visualization Data and Decision Sciences Undergraduate Studies Yes 094312 - Deterministic Mod.in Operations Research Data and Decision Sciences Undergraduate Studies No 094313 - Deterministic Models in Oper.research Data and Decision Sciences Undergraduate Studies No 094314 - Stochastic Models in Oper.research 094333 - Dynamic Models in Operations Research Data and Decision Sciences Undergraduate Studies No 094345 - Discrete Mathematics (for I.e) Data and Decision Sciences Undergraduate Studies Yes 094395 - Design Project Proposal Data and Decision Sciences Undergraduate Studies No 094396 - Design Project 1 Data and Decision Sciences Undergraduate Studies Yes 094411 - Probability (ie) Data and Decision Sciences Undergraduate Studies Yes 094412 - Probability (advanced) Data and Decision Sciences Undergraduate Studies Yes 094423 - Introduction to Statistics Data and Decision Sciences Undergraduate Studies Yes 094424 - Statistics 1 Data and Decision Sciences Undergraduate Studies Yes 094481 - Int.to Probability and Statistics Data and Decision Sciences Undergraduate Studies Yes 094503 - Microeconomics 1 094504 - Microeconomics 2 Data and Decision Sciences Undergraduate Studies No 094513 - Macroeconomics Data and Decision Sciences Undergraduate Studies No 094564 - Introduction to Financial Management Data and Decision Sciences Undergraduate Studies No 094569 - Capital Markets and Investments Data and Decision Sciences Undergraduate Studies No 094591 - Introductory Economics Data and Decision Sciences Undergraduate Studies Yes 094594 - Principles of Economics For Engineers Data and Decision Sciences Undergraduate Studies Yes 094600 - Seminar in Cognitive Science Data and Decision Sciences Undergraduate Studies Yes 094700 - Introduction to Data Science and Engin. Data and Decision Sciences Undergraduate Studies Yes 094701 - Research Project 1 Data and Decision Sciences Undergraduate Studies Yes 094702 - Research Project 2 094703 - Research Project 3 Data and Decision Sciences Undergraduate Studies Yes 094704 - C Programming Workshop Data and Decision Sciences Undergraduate Studies No 094820 - Introduction to Accounting Data and Decision Sciences Undergraduate Studies Yes 095111 - Manufacturing Systems Design Data and Decision Sciences Undergraduate Studies No 095113 - Quality Data and Decision Sciences Undergraduate Studies Yes 095140 - Project Planning and Management Data and Decision Sciences Undergraduate Studies No 095219 - Writing Software For Machine Learning Data and Decision Sciences Undergraduate Studies Yes 095280 - Project in Machine Learning Data and Decision Sciences Undergraduate Studies Yes 095296 - Algebric Methods For Data Science Data and Decision Sciences Undergraduate Studies No 095334 - Simulation - Modeling and Analysis 095605 - Introduction to Psychology Data and Decision Sciences Undergraduate Studies Yes 095622 - Int. to Cognitive Neuroscience Data and Decision Sciences Undergraduate Studies Yes 096120 - Quality Engineering Data and Decision Sciences Undergraduate Studies Graduate Studies No 096122 - Analytics of Healthcare Networks Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096200 - Mathematical Tools For Data Science Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096208 - Automatic Planning Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096210 - Foundations and Applications of Artifici Data and Decision Sciences Undergraduate Studies Graduate Studies No 096211 - Electronic Commerce Models Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096212 - Probabilistic Graphical Models Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096215 - Seminar in Information Systems 096222 - Language Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096224 - Distributed Data Management Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096226 - Computation Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096231 - Math Models in Advanced Info.retrieval Data and Decision Sciences Undergraduate Studies Graduate Studies No 096235 - Intelligent Interactive Systems Data and Decision Sciences Undergraduate Studies Graduate Studies No 096244 - Research in Language Processing Data and Decision Sciences Undergraduate Studies Graduate Studies No 096250 - Distributed Information Systems Data and Decision Sciences Undergraduate Studies Graduate Studies No 096262 - Information Retrieval Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096265 - Algorithms in Logic Data and Decision Sciences Undergraduate Studies Graduate Studies No 096266 - User Experience in Interactive Systems 096275 - The Human Factor in Data Collection Data and Decision Sciences Undergraduate Studies Graduate Studies No 096291 - Algorithmic and High-frequency Trading Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096292 - Predictive Analytics in Fintec Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096311 - Theory and Algorithms For Optimization Data and Decision Sciences Undergraduate Studies Graduate Studies No 096324 - Service Engineering Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096327 - Nonlinear Models in Operations Research Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096336 - Optimization Methods in Machine Learning Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096351 - Polyhedral Methods For Integer Prog Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096411 - Machine Learning 1 Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096412 - Business Process Management and Mining 096414 - Industrial Statistics Data and Decision Sciences Undergraduate Studies Graduate Studies No 096425 - Time Series and Forecasting Data and Decision Sciences Undergraduate Studies Graduate Studies No 096450 - Multiple Comparisons Data and Decision Sciences Undergraduate Studies Graduate Studies No 096475 - Design and Analysis of Experiments Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096501 - Economics For Systems Engineers Data and Decision Sciences Undergraduate Studies Graduate Studies No 096553 - Environmental Economics Data and Decision Sciences Undergraduate Studies Graduate Studies No 096556 - Options Markets Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096570 - Game Theory and Economic Behavior Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096576 - Learning and Complexity in Game Theory Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096578 - Social Choice and Preference Aggregation 096582 - Advanced Topics in Economic Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096589 - Advanced Econometrics Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096600 - Organizational Behavior Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096606 - Behavioral Econ. in Technological Env. Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096609 - Quan. Models in Behavioral Sciences Data and Decision Sciences Undergraduate Studies Graduate Studies No 096617 - Cognition and Decision Making Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096620 - Introduction to Human Factors Eng Data and Decision Sciences Undergraduate Studies Graduate Studies No 096622 - Identity and Group Processes Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096625 - Cognition in Information Visualization Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096644 - Environmental Psychology 096690 - Behavioral Economics Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096693 - Psychological and Cognitive Networks Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096694 - Metacognition Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 096807 - Social Ventures Data and Decision Sciences Undergraduate Studies Graduate Studies No 096820 - Customer Relationship Management Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097135 - Multidisciplinary Research in Service Data and Decision Sciences Undergraduate Studies Graduate Studies No 097139 - Advanced Supply Chain Management Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097140 - Advanced Project Management Techniques Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097209 - Machine Learning 2 Data and Decision Sciences Undergraduate Studies Graduate Studies No 097215 - Methods in Natural Language Processing 097217 - Seminar in Natural Language Processing Data and Decision Sciences Undergraduate Studies Graduate Studies No 097222 - Computer Vision ¸ Surgical Applications Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097225 - Perturbation Methods in Machine Learning Data and Decision Sciences Undergraduate Studies Graduate Studies No 097244 - Cognitive Robotics Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097246 - Social Computing Models Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097247 - Internet of Things: Technology and Data Data and Decision Sciences Undergraduate Studies Graduate Studies No 097248 - Machine Learning te Studies Yes 097280 - n Sciences 097317 - Cooperative Game Theory Data and Decision Sciences Undergraduate Studies Graduate Studies No 097400 - 097414 - Statistics 2 Data and Decision Sciences Undergraduate Studies Graduate Studies No 097447 - Intro. to Computability and Complexity Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097449 - Nonparametric Statistics Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097510 - Continuous Time Models in Finance Data and Decision Sciences Undergraduate Studies Graduate Studies No 097622 - Introduction to Cognitive Science Data and Decision Sciences Undergraduate Studies Graduate Studies No 097644 - Cultural Psychology Data and Decision Sciences Undergraduate Studies Graduate Studies Yes 097800 -es Undera No 097920 - Yes 097921 - 097922 -  097950 - No 097980 "
course_numbers=find_course_numbers(str_all)
available_courses = []
unavailable_courses = []
print(course_numbers)
print(len(course_numbers))
available_urls = []

write_mode = False

if write_mode:
    for course_number in tqdm(course_numbers):
        url = f"https://students.technion.ac.il/local/technionsearch/course/{course_number}/202302?lang=en"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                available_courses.append(course_number)
                available_urls.append(url)
            else:
                unavailable_courses.append(course_number)
        except requests.exceptions.RequestException as e:
            # In case of a connection error, you might want to log the exception
            print(f"Request for course number {course_number} failed with exception: {e}")
    write_path = 'available_courses_urls.txt'

    with open(write_path, 'w') as file:
        for url in available_urls:
            file.write(f"{url}\n")
    with open('available_courses.txt', 'w') as file:
        for course_number in available_courses:
            file.write(f"{course_number}\n")

if not write_mode:
    with open('available_courses_urls.txt', 'r') as file:
        available_urls = file.read().splitlines()
    with open('available_courses.txt', 'r') as file:
        available_courses = file.read().splitlines()

# Initialize DataFrame to store course data
df = pd.DataFrame(columns=['course_name', 'course_id', 'course_basic_information',
                           'pre_required_courses', 'semesterial_data', 'time'])

# Base URL (replace with the actual base URL of course pages)
# base_url = "https://students.technion.ac.il/local/technionsearch/course/"

# Replace 'your_tag_or_class' with the actual tag or class used in the HTML of the webpage
# These are placeholder values and should be replaced with the actual identifiers
tag_for_course_name = 'your_tag_or_class'
tag_for_course_id = 'your_tag_or_class'
tag_for_basic_info = 'your_tag_or_class'
tag_for_pre_reqs = 'your_tag_or_class'
tag_for_credit_points = 'your_tag_or_class'
tag_for_time = 'your_tag_or_class'

# Add course ids to the DataFrame
# df['course_id'] = course_ids
# Progress bar
for course_id in tqdm(available_courses):
    course_basic_information = ""
    url = f"https://students.technion.ac.il/local/technionsearch/course/{course_id}/202302?lang=en"
    # url = f"{base_url}{course_id}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # course_name = soup.find('div', class_='course-name-class').text.strip()
        # course_name = soup.find('li', class_='breadcrumb-item active').text.strip()
        course_link = soup.select_one('a[aria-current="page"]')
        if course_link:
            course_name = course_link.get_text(strip=True)
        else:
            course_name = "Not found"
        print("course_name")
        print(course_name)
        card_texts = soup.find_all('p', class_='card-text')
        semesterial_data = [i.text.strip() for i in card_texts[1:]]
        print("-------semesterial_data-----------")
        print(semesterial_data)

        course_basic_information=card_texts[0].text.strip()
        # Assuming the first 'card-text' class is the course basic information
        # if len(card_texts) > 0:
        #     course_basic_information = card_texts[0].text.strip()
        print("-------course_basic_information-----------")
        print(course_basic_information)

        # if len(card_texts) > 1:
        #     credit_points = card_texts[-1].text.strip()


        # And the second 'card-text' class is the credit points
        # if len(card_texts) > 2:
        #     try:
        #         credit_points = card_texts[2].text.strip()
        #     except:
        #         credit_points = card_texts[1].text.strip()
            # print("credit_points")
            # print(credit_points)

        # course_basic_information = soup.find('p', {'class': 'card-text'}).text.strip()
        # print("course_basic_information")
        # print(course_basic_information)
        pre_req_title = soup.find('h5', string='Pre-required courses')
        pre_req_container = pre_req_title.find_next_sibling('p') if pre_req_title else None
        pre_required_courses = []
        if pre_req_container:
            pre_required_courses = [a.get_text(strip=True) for a in pre_req_container.find_all('a')]
        else:
            pre_required_courses = []

        # pre_required_courses = [li.text.strip() for li in soup.select('#pre-reqs-id li')]
        print("-----------pre_required_courses-----------")
        print(pre_required_courses)
        # credit_points = soup.find('p', {'class': 'card-text'}).text.strip()
        # print("-----------credit_points-----------")
        # print(credit_points)
        # time = soup.find('div', class_='time-class').text.strip()
        print("-----------time-----------")
        table_body = soup.find(lambda tag: tag.name == "tbody" and "Lecture" in tag.text)

        # Initialize a list to hold the starting times
        starting_times = []
        average_start_time = 0
        # Find all the rows in the table body
        rows = table_body.find_all('tr') if table_body else []

        # Iterate through rows to get starting times
        for row in rows:
            # Find all cells in the row
            cells = row.find_all('td')
            # The time is typically in one of the cells, you need to identify which one
            for cell in cells:
                time_text = cell.get_text().strip()
                # Use regular expression to match time patterns, assuming they're in the format 'HH:MM'
                match = re.match(r'(\d{1,2}:\d{2})', time_text)
                if match:
                    # Convert time to a datetime object and append to list
                    starting_time = datetime.strptime(match.group(), '%H:%M').time()
                    starting_times.append(starting_time)

        # Now calculate the average start time
        # Convert all times to minutes past midnight, take the average, then convert back to a time object
        if starting_times:
            average_minutes = sum(time.hour * 60 + time.minute for time in starting_times) / len(starting_times)
            average_hour, average_minute = divmod(int(average_minutes), 60)
            average_start_time = datetime.strptime(f"{average_hour}:{average_minute}", "%H:%M").time()
            print("Average start time:", average_start_time)
        else:
            print("No starting times found")
        # Update the DataFrame
        # df.loc[df['course_id'] == course_id, 'course_name'] = course_name
        # df.loc[df['course_id'] == course_id, 'course_basic_information'] = course_basic_information
        # df.loc[df['course_id'] == course_id, 'pre_required_courses'] = pre_required_courses
        # df.loc[df['course_id'] == course_id, 'credit_points'] = credit_points
        # df.loc[df['course_id'] == course_id, 'time'] = average_start_time
        new_data = {
            'course_name': course_name,
            'course_id': course_id,
            'course_basic_information': course_basic_information,
            'pre_required_courses': pre_required_courses,
            'semesterial_data': semesterial_data,
            'time': average_start_time  # assuming average_start_time is a datetime.time or string
        }
        # Adding the new row to the DataFrame
        new_row_df = pd.DataFrame([new_data])
        df = pd.concat([df, new_row_df], ignore_index=True)
        csv_file_path = 'courses_data.csv'
        df.to_csv(csv_file_path, index=False)
        print(df.count())


    else:
        print(f"Failed to retrieve {course_id}")

print(df)
# Save the DataFrame to a CSV file
csv_file_path = 'courses_data.csv'
df.to_csv(csv_file_path, index=False)

# df.head(), csv_file_path  # Show the first few rows of the DataFrame and the path to the CSV file
