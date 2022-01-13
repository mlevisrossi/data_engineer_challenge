select
    neighborhood_district,
    count(incident_number) as total_incidents
from {{ source('postgres', 'incidents') }}
group by neighborhood_district