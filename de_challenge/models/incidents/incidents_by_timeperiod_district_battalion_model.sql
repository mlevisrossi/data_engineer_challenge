select
    incident_date as incident_date,
    battalion,
    neighborhood_district,
    count(incident_number) as total_incidents
from {{ source('postgres', 'incidents') }}
group by incident_date, battalion, neighborhood_district