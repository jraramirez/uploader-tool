## Setting Up ```settings.py```

File location: ```uploader-tool\uploader\uploader\settings.py```

If there are changes needed on **server or database schema details**, adjust the ```settings.py``` file accordingly. The list below are examples of changes and the corresponding recommended actions.

### Deploying from DEV to PRO Server

If there is a need to deploy new features from DEV to PRO server and there are changes in ```settings.py```, use the values under ```PRO SERVER```.

```python
# DEV SERVER
# server_ip_address = '16.179.110.132'
# server_domain_name = 'a4pgbizopsdev.svcs.entsvcs.net'

# PRO SERVER
server_ip_address = 'a4pgbizops'
server_domain_name = 'a4pgbizops.svcs.entsvcs.net'
```

**DO NOT COPY-PASTE-REPLACE** the settings.py from DEV folder to PRO folder

### Server IP Address or Domain Name Changes

If there are changes in server ip address or domain names, modify the expected ip addresses and domain names variables

```python
# DEV SERVER
server_ip_address = 'NEW DEV IP ADDRESS'
server_domain_name = 'NEW DEV DOMAIN NAME'

# PRO SERVER
server_ip_address = 'a4pgbizops'
server_domain_name = 'NEW PRO DOMAIN NAME'
```

### Additional Schemas

If there is a need to add new databases/schemas, make the system recognize them by adding them to ```DATABASES``` list in ```settings.py```.

```python
DATABASES = {
    # Current DEV Databases
    'default': {
        'NAME': 'FPD',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
    'PG_BIZOPS_DEV': {
        'NAME': 'PG_BIZOPS_DEV',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
    'PG_PROJECTS_DEV': {
        'NAME': 'PG_PROJECTS_DEV',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
    'FPD': {
        'NAME': 'FPD',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
    # Example New Schema
    'NEW_SCHEMA': {
        'NAME': 'NEW_SCHEMA',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
```

```python
DATABASES = {
    # Current PRO Databases
    'default': {
        'NAME': 'PG_BIZOPS',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
    'PG_BIZOPS': {
        'NAME': 'PG_BIZOPS',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
    'PG_PROJECTS': {
        'NAME': 'PG_PROJECTS',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': server_ip_address,
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    },
```