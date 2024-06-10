# retrieve text form web elements
def prepare_reviews(data):
    reviews = []
    for review in data:
        reviews.append(review.text)
    return reviews