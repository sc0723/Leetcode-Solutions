recent_submission_id = """
query recentAcSubmissions($username: String!) {
    recentAcSubmissionList(username: $username, limit: 1) {
        id
        title
    }
}
"""

recent_submission_code = """
query submissionDetails($submissionId: Int!) {
    submissionDetails(submissionID: $submissionId) {
        code
    }
}
"""
