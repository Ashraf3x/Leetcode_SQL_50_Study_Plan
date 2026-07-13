select patient_id, patient_name, conditions
from patients
where conditions like 'diab1%' or conditions like '% diab1%'