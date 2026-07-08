import { useState, useEffect } from "react"

function CareGap() {

    // state: data this component owns
    const [careGaps, setCareGaps] = useState([]);

    // effects: fetch data or sync with outside systems
    useEffect(() => {
        // ask: what outside thing does this component need to sync with?
        // do: fetch data, subscribe, start a timer, or update something outside React
        // cleanup: return a function if the effect creates something that must be stopped
        // dependencies: list the values that should cause this effect to run again
        const fetchCareGaps = async () => {
            const response = await fetch('/api/patients/view_care_gaps/');
            const data = await response.json();

            console.log(data)
            setCareGaps(data)
        }

        fetchCareGaps()
    }, [])

    // handlers: user actions like clicks, submits, or changes
    // derived values: filtered, sorted, or formatted data for display
    // return jsx
    return (
        <>
            <h1>Care Gaps</h1>
            <ul>
                {careGaps.map((careGap) => (
                    <li key={careGap.id}>
                        {careGap.patient_name} - {careGap.care_gap_type} - {careGap.priority} - {careGap.notes}
                    </li>
                ))}
            </ul>
        </>
    )
}

export default CareGap
