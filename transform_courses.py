import pandas as pd
from datetime import datetime
# Data Science Program Course IDs
ds_course_ids = [
    "104031",
    "104166",
    "234117",
    "094345",
    "324033",
    "104032",
    "094412",
    "094700",
    "094210",
    "094219",
    "114051",
    "094424",
    "096570",
    "096411",
    "094314",
    "095295",
    "094224",
    "094241",
    "096327",
    "096211",
    "097447",
    "096224",
    "097414",
    "096275",
    "097209",
    "096210",
    "096250",
    "094290",
    "094295"
]

# Industrial Engineering Program Course IDs
ie_course_ids = [
    "234221",
    "104016",
    "094345",
    "104042",
    "094101",
    "094219",
    "094202",
    "104044",
    "094411",
    "324033",
    "094312",
    "094224",
    "094424",
    "094594",
    "094564",
    "114051",
    "094139",
    "094314",
    "095605",
    "097800",
    "094820",
    "095140",
    "094142",
    "094334",
    "094170",
    "096324",
    "094189",
    "094195"
]

# Software Engineering Program Course IDs
se_course_ids = [
    "104016",
    "104042",
    "234221",
    "094704",
    "094345",
    "324033",
    "104044",
    "094411",
    "094202",
    "094219",
    "094210",
    "094312",
    "094594",
    "094424",
    "094564",
    "094314",
    "096211",
    "096570",
    "095605",
    "094224",
    "094241",
    "096411",
    "097447",
    "095140",
    "114051",
    "096250",
    "096210",
    "094395",
    "094396"
]


ds_course_ids = [int(id) for id in ds_course_ids]
ie_course_ids = [int(id) for id in ie_course_ids]
se_course_ids = [int(id) for id in se_course_ids]

cols=["course_name","course_id","course_basic_information","pre_required_courses","semesterial_data","time"]
path="courses_data.csv"
df = pd.read_csv(path)
df["is_manadatory_ds"]=df["course_id"].apply(lambda x: x in ds_course_ids)
df["is_manadatory_ie"]=df["course_id"].apply(lambda x: x in ie_course_ids)
df["is_manadatory_se"]=df["course_id"].apply(lambda x: x in se_course_ids)


def get_time_category(time_str):
    try:
        # Try to convert the string to a datetime object
        hour = datetime.strptime(time_str, '%H:%M:%S').time().hour
    except ValueError:
        # If there is a ValueError, then it is not in the correct format
        # You can decide how to handle it, for now, we'll return 'Invalid'
        hour = 0

    # Return the time category based on the hour
    return "M" if hour < 12 else "N" if hour < 16 else "E"

df["time_category"] = df["time"].apply(get_time_category)

# df["time_category"]=df["time"].apply(lambda x: "M" if x<12 else "N" if x<16 else "E")
df.to_csv("'transformed_'"+path,index=False)


