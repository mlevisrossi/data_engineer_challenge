select
    incident_date,
    count(incident_number) as total_incidents
from {{ source('postgres', 'incidents') }}
group by incident_date