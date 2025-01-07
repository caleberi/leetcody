"""
Sample Input
    {
        "business_of_interest_id": 10,
        "positive_reviews": [
            PositiveReview(
                 1,
                 10
            ),
            PositiveReview(
                 2,
                 10
            ),
            PositiveReview(
                 1,
                 11
            ),
            PositiveReview(
                 2,
                 11
            ),
            PositiveReview(
                 1,
                 12
            ),
            PositiveReview(
                 2,
                 12
            ),
            PositiveReview(
                 3,
                 12
            )
        ]
    }
Sample Output
    11
Business Similarity Score against business 10:
    11: 2 / (2 + 2 - 2) = 1.0
    12: 2 / (2 + 3 - 2) = 0.667
"""


class PositiveReview:
    def __init__(self, id, business_id) -> None:
        self.user_id = id
        self.business_id = business_id


def find_most_similar_business(business_of_interest_id, positive_reviews):
    hmap = {}
    for i in range(len(positive_reviews)):
        review = positive_reviews[i]
        id = review.user_id
        business_id = review.business_id
        if business_id not in hmap:
            hmap[business_id] = set()
            hmap[business_id].add(id)
        else:
            hmap[business_id].add(id)
    x = len(hmap[business_of_interest_id])
    xkey = hmap[business_of_interest_id]

    del hmap[business_of_interest_id]

    best = 0
    for k, v in hmap.items():
        if k == business_of_interest_id:
            continue
        else:
            y = len(xkey.intersection(hmap[k]))
            cal = y / ((x + len(hmap[k])- x))
            best = max(best, cal)
    return format(best, ".2f")


print(
    find_most_similar_business(
        10,
        [
            PositiveReview(1, 10),
            PositiveReview(2, 10),
            PositiveReview(1, 11),
            PositiveReview(2, 11),
            PositiveReview(1, 12),
            PositiveReview(2, 12),
            PositiveReview(3, 12),
        ],
    )
)


