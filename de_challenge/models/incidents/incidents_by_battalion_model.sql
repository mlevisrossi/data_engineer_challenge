select
    battalion,
    count(incident_number) as total_incidents
from {{ source('postgres', 'incidents') }}
group by battalion