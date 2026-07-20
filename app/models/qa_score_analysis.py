class QAScoreResult:

    def __init__(self):

        # Scores parciales

        self.image_score = 0

        self.link_score = 0

        self.accessibility_score = 0

        # Score final

        self.total_score = 0

        # Calificación

        self.grade = ""

        # Mensaje

        self.summary = ""

        # Futuro

        self.recommendations = []