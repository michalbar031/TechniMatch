import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# The URL to the course search form
form_url = 'https://students.technion.ac.il/local/technionsearch/search?lang=en'
# Data that needs to be sent in the form
form_data = {
    'semester': 'Spring 2023/24',
    # Add other form fields here
}
form_data_string = r"""mform_isexpanded_id_advance_filters=1&sesskey=0auGtVuncG&_qf__local_technionsearch_form_search_advance=1&course_name=&semesterscheckboxgroup%5B202302%5D=0&semesterscheckboxgroup%5B202302%5D=1&semesterscheckboxgroup%5B202301%5D=0&semesterscheckboxgroup%5B202301%5D=1&semesterscheckboxgroup%5B202203%5D=0&semesterscheckboxgroup%5B202202%5D=0&no_semester_filter=0&faculties=_qf__force_multiselect_submission&faculties%5B%5D=9&lecturer_name=_qf__force_multiselect_submission&daycheckboxgroup%5Bsunday%5D=0&daycheckboxgroup%5Bsunday%5D=1&daycheckboxgroup%5Bmonday%5D=0&daycheckboxgroup%5Bmonday%5D=1&daycheckboxgroup%5Btuesday%5D=0&daycheckboxgroup%5Btuesday%5D=1&daycheckboxgroup%5Bwednesday%5D=0&daycheckboxgroup%5Bwednesday%5D=1&daycheckboxgroup%5Bthursday%5D=0&daycheckboxgroup%5Bthursday%5D=1&daycheckboxgroup%5Bfriday%5D=0&daycheckboxgroup%5Bfriday%5D=1&hours_group_filter%5Bfromtime%5D=7.00&hours_group_filter%5Btotime%5D=23.30&credit_group_filter%5Bmin_points%5D=0.0&credit_group_filter%5Bmax_points%5D=20.0&academic_level_group%5B1%5D=0&academic_level_group%5B1%5D=1&academic_level_group%5B2%5D=0&academic_level_group%5B2%5D=1&academic_level_group%5B3%5D=0&academic_level_group%5B3%5D=1&has_english_lessons=0&submitbutton=Search"""

from urllib.parse import parse_qs
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,nl;q=0.6',
    # 'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Origin': 'https://students.technion.ac.il',
    # 'Referer': 'https://students.technion.ac.il/local/technionsearch/search?lang=en',
    # "Cookie": '_ga_NRMSNN9DYD=GS1.1.1711487231.2.0.1711487236.0.0.0; _ga=GA1.1.1484800049.1710426181; _ga_WRR46JN9W2=GS1.1.1711563355.2.1.1711564166.60.0.0; _ga_S96KCZV4RR=GS1.1.1711564551.8.0.1711564551.0.0.0; _fbp=fb.2.1711809141906.1638871245; _ga_NX0XNVRZ28=GS1.1.1711809141.1.1.1711810075.0.0.0; _ga_096QT9J0HM=GS1.1.1711820553.1.0.1711820555.0.0.0; MoodleSessionstudentsprod=eda0ieh18d2k4l6i514jeibtni; _ga_VWN9CP1D7R=GS1.1.1711885193.5.1.1711887075.0.0.0'
}
#
# form_data_dict = parse_qs(form_data_string)
# form_data = {k: v[0] if len(v) == 1 else v for k, v in form_data_dict.items()}
# form_data = r"mform_isexpanded_id_advance_filters=1&sesskey=frnsMaG4W8&_qf__local_technionsearch_form_search_advance=1&course_name=&semesterscheckboxgroup%5B202302%5D=0&semesterscheckboxgroup%5B202302%5D=1&semesterscheckboxgroup%5B202301%5D=0&semesterscheckboxgroup%5B202301%5D=1&semesterscheckboxgroup%5B202203%5D=0&semesterscheckboxgroup%5B202202%5D=0&no_semester_filter=0&faculties=_qf__force_multiselect_submission&faculties%5B%5D=9&lecturer_name=_qf__force_multiselect_submission&daycheckboxgroup%5Bsunday%5D=0&daycheckboxgroup%5Bsunday%5D=1&daycheckboxgroup%5Bmonday%5D=0&daycheckboxgroup%5Bmonday%5D=1&daycheckboxgroup%5Btuesday%5D=0&daycheckboxgroup%5Btuesday%5D=1&daycheckboxgroup%5Bwednesday%5D=0&daycheckboxgroup%5Bwednesday%5D=1&daycheckboxgroup%5Bthursday%5D=0&daycheckboxgroup%5Bthursday%5D=1&daycheckboxgroup%5Bfriday%5D=0&daycheckboxgroup%5Bfriday%5D=1&hours_group_filter%5Bfromtime%5D=7.00&hours_group_filter%5Btotime%5D=23.30&credit_group_filter%5Bmin_points%5D=0.0&credit_group_filter%5Bmax_points%5D=20.0&academic_level_group%5B1%5D=0&academic_level_group%5B1%5D=1&academic_level_group%5B2%5D=0&academic_level_group%5B2%5D=1&academic_level_group%5B3%5D=0&academic_level_group%5B3%5D=1&has_english_lessons=0&submitbutton=Search"
# driver = webdriver.Chrome()
# driver.get(form_url)
# Initialize an empty list to store the course data
courses_data = []

# Start a session to keep cookies
with requests.Session() as session:
    print('Session started')
    # Send a POST request with the form data
    initial_page = session.get(form_url, headers=headers)
    response = session.post(form_url, data=form_data_string, headers=headers)
    print("response.status_code")
    print(response.status_code)
    print(response.text)
    with open("response.html", "w") as file:
        file.write(response.text)
    print('Response received:', response.status_code)
    # Check if response is ok (200)
    if response.ok:
        # print('Session cookies:', session.cookies)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())
        # Check if courses are in the response
        # print('Response HTML:', soup.prettify()[:1000])  # Print the beginning of the HTML
        courses = soup.find_all('td', class_='cell c1')
        print('Courses found:', len(courses))

        for course in courses:
            # Extract course details like name, ID, link to syllabus, etc.
            # ... (Adjust these next lines with the correct data extraction)
            course_name = course.find('div', class_='course-name').text.strip()
            course_id = course.find('span', class_='course-id').text.strip()
            general_info = course.find('a', class_='syllabus-link')['href']
            # ... Add other data extractions here

            # Get the URL for the course's detail page
            detail_page_url = course.find('a', class_='detail-link')['href']
            # Make a GET request to the detail page
            detail_response = session.get(detail_page_url)
            detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
            # Extract detailed information from the course's detail page
            # ... (Adjust these next lines with the correct data extraction)
            lecturer = detail_soup.find('div', class_='lecturer').text.strip()
            lecture_time = detail_soup.find('time', class_='lecture-time').text.strip()
            prerequired_courses = detail_soup.find('div', class_='prerequisites').text.strip()
            has_test = 'Yes' if detail_soup.find('div', class_='test-info') else 'No'
            credit_points = detail_soup.find('span', class_='credits').text.strip()

            # Create a dictionary for the course with the required information
            course_info = {
                'name': course_name,
                'id': course_id,
                'general_info': general_info,
                'lecturer': lecturer,
                'lecture_time': lecture_time,
                'prerequired_courses': prerequired_courses,
                'has_test': has_test,
                'credit_points': credit_points
            }
            print(course_info)
            # Append the course_info dictionary to the courses_data list
            courses_data.append(course_info)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(courses_data)
print("saving to csv")

# Define the CSV file name
csv_file_name = 'courses_data_scraped.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_name, index=False, encoding='utf-8-sig')
