select
    incident_date,
    count(*) as total_incidents
from {{ source('postgres', 'incidents') }}
group by incident_date