select
    neighborhood_district,
    count(*) as total_incidents
from {{ source('postgres', 'incidents') }}
group by neighborhood_district