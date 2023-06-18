import requests
import csv
import time
import random


def fetch_udemy_courses():
    base_url = "https://www.udemy.com/api-2.0/discovery-units/all_courses/"
    all_courses = []
    field_names = ['title', 'id', 'avg_rating', 'num_reviews', 'num_subscribers', 'is_paid', 'course_length',
                   'num_published_lectures', 'created', 'published_time', 'last_update', 'instructional_level',
                   'instructor', 'url']

    for page_number in range(1, 20):
        # Randomize the sleep duration between 2 and 5 seconds
        sleep_duration = random.uniform(2, 5)
        time.sleep(sleep_duration)

        query_params = {
            "p": page_number,
            "page_size": "60",
            "category_id": "294",
            "source_page": "category_page",
            "locale": "en_US",
            "currency": "usd",
            "navigation_locale": "en_US",
            "sos": "pc",
            "fl": "cat"
        }

        response = requests.get(base_url, params=query_params)
        print(f"Page {page_number} - Response status code: {response.status_code}")

        json_data = response.json()
        courses = json_data["unit"]["items"]

        for course in courses:
            course_data = {
                "title": course["title"],
                "id": course["id"],
                "avg_rating": course["avg_rating"],
                "num_reviews": course["num_reviews"],
                "num_subscribers": course["num_subscribers"],
                "is_paid": course["is_paid"],
                "course_length": course["content_info_short"],
                "num_published_lectures": course["num_published_lectures"],
                "created": course["created"],
                "published_time": course["published_time"],
                "last_update": course["last_update_date"],
                "instructional_level": course["instructional_level_simple"],
                "instructor": course["visible_instructors"][0]["display_name"],
                "url": "www.udemy.com" + course["url"],
            }
            all_courses.append(course_data)

    with open("udemy_courses.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(all_courses)


if __name__ == "__main__":
    fetch_udemy_courses()
