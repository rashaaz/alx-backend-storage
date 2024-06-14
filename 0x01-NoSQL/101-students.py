#!/usr/bin/env python3
""" top_students.py """


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """ Finds top students from MongoDB """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
