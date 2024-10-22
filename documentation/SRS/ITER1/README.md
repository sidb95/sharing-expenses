# SRS: Iteration 1

1. User Management:
    1. A user should have email, name and a phone number,
    2. API endpoints: 
        - user-management/api/create-user,
        - user-management/api/get-details
            1. Assumption: 
            retrievation of details of the user can be done
            using only his phone number (assuming that phone
            number of every user is distinct).
