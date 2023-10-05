
MALE = "M"
FEMALE = "F"
NON_BINARY = "N"
GENDER_CHOICES = [
    (MALE, "Male"),
    (FEMALE, "Female"),
    (NON_BINARY, "Non Binary"),
]

DRAFT = 0
REQUIREMENTS_GATHERING = 1
DESIGNING = 2
PROTOTYPE_READY = 3
PENDING_DEVELOPMENT = 4
DEVELOPMENT = 5
DEVELOPMENT_REVIEW = 6
DEVELOPMENT_COMPLETED = 7
TESTING = 8
DEPLOYED = 9
COMPLETED = 10

PROJECT_STATUS = [
    (DRAFT, "Draft"),
    (REQUIREMENTS_GATHERING, "Requirements Gathering"),
    (DESIGNING, "Designing"),
    (PROTOTYPE_READY, "Prototype Prepared"),
    (PENDING_DEVELOPMENT, "Pending Development"),
    (DEVELOPMENT, "Under Development"),
    (DEVELOPMENT_REVIEW, "Code review"),
    (DEVELOPMENT_COMPLETED, "Development work Completed"),
    (TESTING, "Testing"),
    (DEPLOYED, "Deployed to Production"),
    (COMPLETED, "Project Completed"),
]
