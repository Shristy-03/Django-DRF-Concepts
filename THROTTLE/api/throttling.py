from rest_framework.throttling import UserRateThrottle

class jackThrottle(UserRateThrottle):
    scope='jack'
    