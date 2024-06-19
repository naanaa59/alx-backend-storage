#!/usr/bin/env python3
""" returns all students sorted by average score"""


def top_students(mongo_collection):
    """ returns all students sorted by average score"""
    all_students = mongo_collection.find()
    total = 0

    for student in all_students:
        total = 0
        for topic in student["topics"]:
            total += topic["score"]
        av_score = total / len(student["topics"]) if topic["score"] else 0
        mongo_collection.update_one({
            "name": student["name"]}, {'$set': {"averageScore": av_score}})

    all_students = mongo_collection.find()
    return sorted(
            list(all_students), key=lambda x: x['averageScore'], reverse=True)
