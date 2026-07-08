import { useEffect, useState } from 'react'

function Patients() {
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        const fetchPatients = async () => {
            const response = await fetch('/api/patients/view_patient/');
            const data = await response.json();
            setPatients(data)
        }

        fetchPatients()
    }, [])

    return (
        <>
            <h1>Patients</h1>
            <ul>
                {patients.map((patient) => (
                    <li key={patient.id}>
                        {patient.first_name} {patient.last_name} - {patient.age} - {patient.language}
                    </li>
                ))}
            </ul>
        </>
    )
}

export default Patients