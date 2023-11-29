## Jira Audit Log CSV

Python script that generates an audit log CSV file for a Jira Issue. The CSV file will contain detailed information about the changes made to the issue, including the author, author account ID, change date, field ID, field type, and changes.

### Prerequisites

    Python 3.x installed on your system
    Jira API credentials with the necessary permissions to access the changelog of the desired Jira issue.


### Usage

Open the **config.py** file and provide the necessary configuration parameters:

    user_email: Your Jira email.
    api_key: Your Jira API Token.
    base_url: Base url of your instance.
    issue_key: The key of the Jira issue for which you want to generate the audit log.

Run the **main.py** file

The script will connect to the Jira REST API, retrieve the audit log for the specified issue, and generate a CSV file with the provided configuration. 

> The CSV file will be saved as **auditlog_{issue_key}.csv**

### CSV

The generated CSV file will have the following columns:

    Author: The name of the user who made the change.
    Author Account ID: The unique account ID of the author.
    Change Date: The date and time when the change occurred.
    Field ID: The ID of the field that was modified.
    Field Type: The type of the modified field.
    From String: The previous value of the field.
    To String: The new value of the field.


### Notes

> This script is intended for administrative use.

### License

This script is created by Ana Vitória Selista.

*Please exercise caution while using this script and always double-check your configuration settings before executing it. If you encounter any issues or need further assistance, feel free to reach out to the script's author or refer to the Jira REST API documentation for more information.*
