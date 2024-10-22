# Commands

For running the server, type:
```bash
python3 manage.py runserver
```

### Iteration 1

current working directory: sharing-expenses
``` bash
python3 -m django startproject app
cd app
python3 -m django startapp user_management
```
- After creating model ```Person```

``` bash
1. python3 manage.py migrate
```
- Iteration 1 complete

### Iteration 2

current working directory: app
``` bash
python3 -m django startapp expense_management
```

- After creating model ```Expense```
``` bash
python3 manage.py migrate
```

- Iteration 2 complete
