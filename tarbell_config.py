# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "hooks30"

# Descriptive title of project
TITLE = "asd"

# Google spreadsheet key
SPREADSHEET_KEY = "0Ak3IIavLYTovdDN2OU1sUUVRTmRUS0pYSFZDSTNuMFE"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "apps.chicagotribune.com/hooks30",
    "staging": "apps.beta.tribapps.com/hooks30",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'hooks30',
    'title': 'asd'
}